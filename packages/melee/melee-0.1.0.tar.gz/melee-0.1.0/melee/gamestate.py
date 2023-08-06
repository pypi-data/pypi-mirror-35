from melee import enums, stages
from melee.enums import Action, Character
import csv
from struct import *
import binascii
import os
import socket
import math
import time
from collections import defaultdict

"""Represents the state of a running game of Melee at a given moment in time"""
class GameState:
    frame = 0
    stage = enums.Stage.FINAL_DESTINATION
    menu_state = enums.Menu.CHARACTER_SELECT
    player = dict()
    projectiles = []
    stage_select_cursor_x = 0.0
    stage_select_cursor_y = 0.0
    ready_to_start = False
    distance = 0.0
    sock = None
    processingtime = 0.0
    frametimestamp = 0.0

    def __init__(self, dolphin):
        #Dict with key of address, and value of (name, player)
        self.locations = dict()
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + "/locations.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                self.locations[line["Address"]] = (line["Name"], line["Player"])
        self.player[1] = PlayerState()
        self.player[2] = PlayerState()
        self.player[3] = PlayerState()
        self.player[4] = PlayerState()
        self.player[5] = PlayerState()
        self.player[6] = PlayerState()
        self.player[7] = PlayerState()
        self.player[8] = PlayerState()
        self.newframe = True
        #Helper names to keep track of us and our opponent
        self.ai_state = self.player[dolphin.ai_port]
        self.opponent_state = self.player[dolphin.opponent_port]
        #Read in the action data csv
        with open(path + "/actiondata.csv") as csvfile:
            #A list of dicts containing the frame data
            actiondata = list(csv.DictReader(csvfile))
            #Dict of sets
            self.zero_indices = defaultdict(set)
            for line in actiondata:
                if line["zeroindex"] == "True":
                    self.zero_indices[int(line["character"])].add(int(line["action"]))
        #read the character data csv
        self.characterdata = dict()
        path = os.path.dirname(os.path.realpath(__file__))
        with open(path + "/characterdata.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                del line["Character"]
                #Convert all fields to numbers
                for key, value in line.items():
                    line[key] = float(value)
                self.characterdata[Character(line["CharacterIndex"])] = line
        #Creates the socket if it does not exist, and then opens it.
        path = dolphin.get_memory_watcher_socket_path()
        try:
            os.unlink(path)
        except OSError:
            pass
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.bind(path)

    """Return a list representation of the current gamestate
    Only caring about in-game things, not menus and such"""
    def tolist(self):
        thelist = []
        #I don't think that the frame is really relevant here...
        #thelist.append(self.frame)
        thelist.append(self.distance)
        thelist.append(self.stage.value)
        thelist = thelist + self.ai_state.tolist()
        thelist = thelist + self.opponent_state.tolist()
        #TODO: Figure out the best way to add projectiles to the list
        #thelist = thelist + self.projectiles.tolist()
        return thelist

    def step(self):
        # How long did it take to get here from last time?
        self.processingtime = time.time() - self.frametimestamp
        for mem_update in self:
            if mem_update == None:
                continue
            #If the frame counter has updated, then process it!
            if self.update(mem_update):
                # Start the timer, now that we're done waiting for dolphin updates
                self.frametimestamp = time.time()
                return
    #Melee's indexing of action frames is wildly inconsistent.
    #   Here we adjust all of the frames to be indexed at 1 (so math is easier)
    def fixframeindexing(self):
        for index, player in self.player.items():
            if player.action.value in self.zero_indices[player.character.value]:
                player.action_frame = player.action_frame + 1

    # The IASA flag doesn't set or reset for special attacks.
    #   So let's just set IASA to False for all non-A attacks.
    def fixiasa(self):
        for index, player in self.player.items():
            # Luckily for us, all the A-attacks are in a contiguous place in the enums!
            #   So we don't need to call them out one by one
            if player.action.value < Action.NEUTRAL_ATTACK_1.value or player.action.value > Action.DAIR.value:
                player.iasa = False

    """Process one new memory update
       returns True if the frame is finished processing (no more updates this frame)
       Run this in a loop until it returns returns True, then press your buttons,
       wash, rinse, repeat."""
    def update(self, mem_update):
        label = self.locations[mem_update[0]][0]
        player_int = int(self.locations[mem_update[0]][1])
        if label == "frame":
            self.frame = unpack('<I', mem_update[1])[0]
            self.newframe = True
            #Now that the frame is ready, let's calculate some derived information
            #   These are not stored inside Melee anywhere, but are nonetheless
            #   important pieces of information that we don't want to make the
            #   user have to re-calculate on their own
            for i in self.player:
                # Move current x,y over to prev
                self.player[i].prev_x = self.player[i].x
                self.player[i].prev_y = self.player[i].y
                # Move future x,y over to current
                self.player[i].x = self.player[i].next_x
                self.player[i].y = self.player[i].next_y

                if (abs(self.player[i].x) > stages.edgegroundposition(self.stage) or \
                        self.player[i].y < -6) and not self.player[i].on_ground:
                    self.player[i].off_stage = True
                else:
                    self.player[i].off_stage = False

                # Keep track of a player's invulnerability due to respawn or ledge grab
                self.player[i].invulnerability_left = max(0, self.player[i].invulnerability_left - 1)
                if self.player[i].action == Action.ON_HALO_WAIT:
                    self.player[i].invulnerability_left = 120
                # Don't give invulnerability to the first descent
                if self.player[i].action == Action.ON_HALO_DESCENT and self.frame > 150:
                    self.player[i].invulnerability_left = 120
                if self.player[i].action == Action.EDGE_CATCHING and self.player[i].action_frame == 1:
                    self.player[i].invulnerability_left = 36

                # Which character are we right now?
                if self.player[i].character in [Character.SHEIK, Character.ZELDA]:
                    if self.player[i].transformed == self.player[i].iszelda:
                        self.player[i].character = Character.SHEIK
                    else:
                        self.player[i].character = Character.ZELDA
                # If the player is transformed, then copy over the sub-character attributes
                if self.player[i].transformed:
                    self.player[i].action = self.player[i+4].action
                    self.player[i].action_counter = self.player[i+4].action_counter
                    self.player[i].action_frame = self.player[i+4].action_frame
                    self.player[i].invulnerable = self.player[i+4].invulnerable
                    self.player[i].hitlag_frames_left = self.player[i+4].hitlag_frames_left
                    self.player[i].hitstun_frames_left = self.player[i+4].hitstun_frames_left
                    self.player[i].charging_smash = self.player[i+4].charging_smash
                    self.player[i].jumps_left = self.player[i+4].jumps_left
                    self.player[i].on_ground = self.player[i+4].on_ground
                    self.player[i].speed_air_x_self = self.player[i+4].speed_air_x_self
                    self.player[i].speed_y_self = self.player[i+4].speed_y_self
                    self.player[i].speed_x_attack = self.player[i+4].speed_x_attack
                    self.player[i].speed_y_attack = self.player[i+4].speed_y_attack
                    self.player[i].speed_ground_x_self = self.player[i+4].speed_ground_x_self
                    self.player[i].x = self.player[i+4].x
                    self.player[i].y = self.player[i+4].y
                    self.player[i].percent = self.player[i+4].percent
                    self.player[i].facing = self.player[i+4].facing

                # The pre-warning occurs when we first start a dash dance.
                if self.player[i].action == Action.DASHING and self.player[i].prev_action not in [Action.DASHING, Action.TURNING]:
                    self.player[i].moonwalkwarning = True

                # Take off the warning if the player does an action other than dashing
                if self.player[i].action != Action.DASHING:
                    self.player[i].moonwalkwarning = False

            #TODO: This needs updating in order to support >2 players
            xdist = self.ai_state.x - self.opponent_state.x
            ydist = self.ai_state.y - self.opponent_state.y
            self.distance = math.sqrt( (xdist**2) + (ydist**2) )
            self.fixiasa()
            self.fixframeindexing()
            return True
        if label == "stage":
            self.stage = unpack('<I', mem_update[1])[0]
            self.stage = self.stage >> 16
            self.stage &= 0x000000ff
            try:
                self.stage = enums.Stage(self.stage)
            except ValueError:
                self.stage = enums.Stage.NO_STAGE
            return False
        if label == "menu_state":
            self.menu_state = unpack('<I', mem_update[1])[0]
            self.menu_state &= 0x000000ff
            self.menu_state = enums.Menu(self.menu_state)
            return False
        #Player variables
        if label == "percent":
            if player_int > 4:
                try:
                    self.player[player_int].percent = int(unpack('<f', mem_update[1])[0])
                except ValueError:
                    self.player[player_int].percent = 0
                return False
            self.player[player_int].percent = unpack('<I', mem_update[1])[0]
            self.player[player_int].percent = self.player[player_int].percent >> 16
            return False
        if label == "stock":
            self.player[player_int].stock = unpack('<I', mem_update[1])[0]
            self.player[player_int].stock = self.player[player_int].stock >> 24
            return False
        if label == "facing":
            self.player[player_int].facing = unpack('<I', mem_update[1])[0]
            self.player[player_int].facing = not bool(self.player[player_int].facing >> 31)
            return False
        if label == "x":
            self.player[player_int].next_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "y":
            self.player[player_int].next_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "character":
            temp = unpack('<I', mem_update[1])[0] >> 24
            try:
                self.player[player_int].character = enums.Character(temp)
            except ValueError:
                self.player[player_int].character = enums.Character.UNKNOWN_CHARACTER
            return False
        if label == "cursor_x":
            self.player[player_int].cursor_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "cursor_y":
            self.player[player_int].cursor_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "action":
            temp = unpack('<I', mem_update[1])[0]
            try:
                # Keep track of old action
                self.player[player_int].prev_action = self.player[player_int].action
                self.player[player_int].action = enums.Action(temp)
            except ValueError:
                self.player[player_int].action = enums.Action.UNKNOWN_ANIMATION
            return False
        if label == "action_counter":
            #TODO look if this is backwards
            temp = unpack('I', mem_update[1])[0]
            temp = temp >> 8
            self.player[player_int].action_counter = temp
            return False
        if label == "action_frame":
            temp = unpack('<f', mem_update[1])[0]
            try:
                self.player[player_int].action_frame = int(temp)
            except ValueError:
                pass
            return False
        if label == "invulnerable":
            self.player[player_int].invulnerable = unpack('<I', mem_update[1])[0]
            self.player[player_int].invulnerable = self.player[player_int].invulnerable >> 31
            return False
        if label == "hitlag_frames_left":
            temp = unpack('<f', mem_update[1])[0]
            try:
                self.player[player_int].hitlag_frames_left = int(temp)
            except ValueError:
                pass
            return False
        if label == "hitstun_frames_left":
            temp = unpack('<f', mem_update[1])[0]
            try:
                self.player[player_int].hitstun_frames_left = int(temp)
            except ValueError:
                pass
            return False
        if label == "charging_smash":
            temp = unpack('<I', mem_update[1])[0]
            if temp == 2:
                self.player[player_int].charging_smash = True
            else:
                self.player[player_int].charging_smash = False
            return False
        if label == "jumps_left":
            temp = unpack('<I', mem_update[1])[0]
            temp = temp >> 24
            #This value is actually the number of jumps USED
            #   so we have to do some quick math to turn this into what we want
            try:
                totaljumps = int(self.characterdata[self.player[player_int].character]["Jumps"])
                self.player[player_int].jumps_left = totaljumps - temp + 1
            # Key error will be expected when we first start
            except KeyError:
                self.player[player_int].jumps_left = 1
            return False
        if label == "on_ground":
            temp = unpack('<I', mem_update[1])[0]
            if temp == 0:
                self.player[player_int].on_ground = True
            else:
                self.player[player_int].on_ground = False
            return False
        if label == "speed_air_x_self":
            self.player[player_int].speed_air_x_self = unpack('<f', mem_update[1])[0]
            return False
        if label == "speed_y_self":
            self.player[player_int].speed_y_self = unpack('<f', mem_update[1])[0]
            return False
        if label == "speed_x_attack":
            self.player[player_int].speed_x_attack = unpack('<f', mem_update[1])[0]
            return False
        if label == "speed_y_attack":
            self.player[player_int].speed_y_attack = unpack('<f', mem_update[1])[0]
            return False
        if label == "speed_ground_x_self":
            self.player[player_int].speed_ground_x_self = unpack('<f', mem_update[1])[0]
            return False
        if label == "coin_down":
            temp = unpack('<I', mem_update[1])[0]
            temp = temp & 0x000000ff
            self.player[player_int].coin_down = (temp == 2)
            return False
        if label == "stage_select_cursor_x":
            self.stage_select_cursor_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "stage_select_cursor_y":
            self.stage_select_cursor_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "ready_to_start":
            temp = unpack('>I', mem_update[1])[0]
            temp = temp & 0x000000ff
            self.ready_to_start = not bool(temp)
            return False
        if label == "controller_status":
            temp = unpack('>I', mem_update[1])[0]
            temp = temp & 0x000000ff
            self.player[player_int].controller_status = enums.ControllerStatus(temp)
            return False
        if label == "hitbox_1_size":
            self.player[player_int].hitbox_1_size = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_2_size":
            self.player[player_int].hitbox_2_size = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_3_size":
            self.player[player_int].hitbox_3_size = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_4_size":
            self.player[player_int].hitbox_4_size = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_1_status":
            temp = unpack('<I', mem_update[1])[0]
            status = True
            if temp == 0:
                status = False
            self.player[player_int].hitbox_1_status = status
            return False
        if label == "hitbox_2_status":
            temp = unpack('<I', mem_update[1])[0]
            status = True
            if temp == 0:
                status = False
            self.player[player_int].hitbox_2_status = status
            return False
        if label == "hitbox_3_status":
            temp = unpack('<I', mem_update[1])[0]
            status = True
            if temp == 0:
                status = False
            self.player[player_int].hitbox_3_status = status
            return False
        if label == "hitbox_4_status":
            temp = unpack('<I', mem_update[1])[0]
            status = True
            if temp == 0:
                status = False
            self.player[player_int].hitbox_4_status = status
            return False
        if label == "hitbox_1_x":
            self.player[player_int].hitbox_1_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_1_y":
            self.player[player_int].hitbox_1_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_2_x":
            self.player[player_int].hitbox_2_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_2_y":
            self.player[player_int].hitbox_2_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_3_x":
            self.player[player_int].hitbox_3_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_3_y":
            self.player[player_int].hitbox_3_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_4_x":
            self.player[player_int].hitbox_4_x = unpack('<f', mem_update[1])[0]
            return False
        if label == "hitbox_4_y":
            self.player[player_int].hitbox_4_y = unpack('<f', mem_update[1])[0]
            return False
        if label == "iasa":
            self.player[player_int].iasa = bool(unpack('<I', mem_update[1])[0] >> 31)
            return False
        if label == "transformed":
            temp = unpack('<I', mem_update[1])[0]
            status = False
            if temp == 16777216:
                status = True
            self.player[player_int].transformed = status
            return False
        if label == "iszelda":
            temp = unpack('<I', mem_update[1])[0]
            status = False
            if temp == 18:
                status = True
            self.player[player_int].iszelda = status
            return False
        if label == "projectiles":
            #Only once per new frame that we get a projectile, clear the list out
            if self.newframe:
                self.projectiles.clear()
                self.i = 0
            self.i += 1
            self.newframe = False
            if len(mem_update[1]) < 10:
                self.projectiles.clear()
                return False
            proj = Projectile()
            proj.x = unpack('>f', mem_update[1][0x4c:0x50])[0]
            proj.y = unpack('>f', mem_update[1][0x50:0x54])[0]
            proj.x_speed = unpack('>f', mem_update[1][0x40:0x44])[0]
            proj.y_speed = unpack('>f', mem_update[1][0x44:0x48])[0]
            try:
                proj.subtype = enums.ProjectileSubtype(unpack('>I', mem_update[1][0x10:0x14])[0])
            except ValueError:
                return False
            self.projectiles.append(proj)
        return False

    """Iterate over this class in the usual way to get memory changes."""
    def __iter__(self):
        return self

    """Closes the socket."""
    def __del__(self):
        if self.sock != None:
            self.sock.close()

    """Returns the next (address, value) tuple, or None on timeout.
    address is the string provided by dolphin, set in Locations.txt.
    value is a four-byte string suitable for interpretation with struct.
    """
    def __next__(self):
        try:
            data = self.sock.recvfrom(9096)[0].decode('utf-8').splitlines()
        except socket.timeout:
            return None
        # Strip the null terminator, pad with zeros, then convert to bytes
        try:
            return data[0], binascii.unhexlify(data[1].strip('\x00').zfill(8))
        except binascii.Error:
            print("failed at: ", data)
            return None

"""Represents the state of a single player"""
class PlayerState:
    character = enums.Character.UNKNOWN_CHARACTER
    x = 0
    y = 0
    percent = 0
    stock = 0
    facing = True
    action = enums.Action.UNKNOWN_ANIMATION
    action_counter = 0
    action_frame = 0
    invulnerable = False
    invulnerability_left = 0
    hitlag_frames_left = 0
    hitstun_frames_left = 0
    charging_smash = 0
    jumps_left = 0
    on_ground = True
    speed_air_x_self = 0
    speed_y_self = 0
    speed_x_attack = 0
    speed_y_attack = 0
    speed_ground_x_self = 0
    cursor_x = 0
    cursor_y = 0
    coin_down = False
    controller_status = enums.ControllerStatus.CONTROLLER_UNPLUGGED
    off_stage = False
    transformed = False
    iszelda = False
    iasa = 0
    moonwalkwarning = False
    hitbox_1_size = 0
    hitbox_2_size = 0
    hitbox_3_size = 0
    hitbox_4_size = 0
    hitbox_1_status = False
    hitbox_2_status = False
    hitbox_3_status = False
    hitbox_4_status = False
    hitbox_1_x = 0
    hitbox_1_y = 0
    hitbox_2_x = 0
    hitbox_2_y = 0
    hitbox_3_x = 0
    hitbox_3_y = 0
    hitbox_4_x = 0
    hitbox_4_y = 0
    # For internal use only, ignore these
    next_x = 0
    next_y = 0
    prev_x = 0
    prev_x = 0
    # Start from a standing state
    prev_action = Action.UNKNOWN_ANIMATION

    """Produces a list representation of the player's state"""
    def tolist(self):
        thelist = []
        thelist.append(self.x)
        thelist.append(self.y)
        thelist.append(self.percent)
        thelist.append(self.stock)
        thelist.append(int(self.facing))
        thelist.append(self.action.value)
        #We're... gonna leave this one out for now since it's a bit irrelevant
        #thelist.append(self.action_counter)
        thelist.append(self.action_frame)
        thelist.append(int(self.invulnerable))
        thelist.append(self.hitlag_frames_left)
        thelist.append(self.hitstun_frames_left)
        thelist.append(int(self.charging_smash))
        thelist.append(self.jumps_left)
        thelist.append(int(self.on_ground))
        #We're combining speeds here for simplicity's sake
        thelist.append(self.speed_air_x_self + self.speed_x_attack + self.speed_ground_x_self)
        thelist.append(self.speed_y_self + self.speed_y_attack)
        thelist.append(int(self.off_stage))
        return thelist

"""Represents the state of a projectile (items, lasers, etc...)"""
class Projectile:
    x = 0
    y = 0
    x_speed = 0
    y_speed = 0
    opponent_owned = True
    subtype = enums.ProjectileSubtype.UNKNOWN_PROJECTILE

    """Produces a list representation of the projectile"""
    def tolist(self):
        thelist = []
        thelist.append(self.x)
        thelist.append(self.y)
        thelist.append(self.x_speed)
        thelist.append(self.y_speed)
        thelist.append(int(self.opponent_owned))
        thelist.append(self.subtype.value)
        return thelist
