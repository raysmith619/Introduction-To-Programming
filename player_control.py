# player_control.py 05Nov2018
"""
Player control window layout

players
Name      Label    Playing  Color    col bg  Voice Help  Pause    
--------- ------   -        -------  ------  ----  -----  -----
computer  co       ()       gray     white   ( )   ( )    1.0
Alex      Ax       (.)      pink     white   (.)   ( )
Decklan   D        ()       blue     white   (.)   ( )
Avery     Av       ()       pink     white   (.)   ( )
Grampy    Gp       (.)      blue     white   (.)   ( )
Grammy    Gm       (.)      pink     white   (.)   ( )

[Add] [Change] [Remove]
"""


from tkinter import *
import random
from select_error import SelectError
from select_trace import SlTrace
from builtins import str
from select_dd_choice import SelectDDChoice
from turtledemo.minimal_hanoi import play
from matplotlib.rcsetup import _prop_validators

class SelectPlayer:
    id = 0          # Unique id
    name = None
    label = None
    playting = False
    color = "gray"
    voice = False
    help_play = False
    pause = 0
    npoints = 0
    
    def __init__(self,
                 id = None,
                 name = None,
                 label = None,
                 move = None,
                 playing = False,
                 color = "gray",
                 color_bg = "white",
                 voice = False,
                 help_play = False,
                 pause = 0.,
                 npoints = 0
                 ):
        """ Player attributes
        :id:   Unique id (count)
            default: generate new id
        :name: playter's name
        :label: square labeling letter/string
                default: Upercase first character of name
        :playing: True - player is playing game
                default: not playing
        :move: move number 1 - first to play
        :color:  color for name, label, message
        :color_bg: background color
                default: white
        :voice:  True - add voice to player responses
        :help_play: Help player
                default: no help
        :pause: Pause number of seconds before player play
                Provides some delay before computer response
        :npoints: Number of points in game
                default: 0
        """
        if id is None:
            SelectPlayer.id += 1
            id = SelectPlayer.id
        self.id = id
        self.name = name
        if label is None:
            if self.name is not None:
                label = self.name[0]
        self.label = label
        self.playing = playing
        if move is None:
            move = self.id
        self.move = move
        self.color = color
        self.color_bg = color_bg
        self.voice = voice
        self.help_play = help_play
        self.pause = pause
        self.ctls = {}          # Dictionary of field control widgets
        self.ctls_vars = {}     # Dictionary of field control widget variables


    def get_prop_key(self, name):
        """ Translate full  control name into full Properties file key
        """
        
        key = PlayerControl.CONTROL_NAME_PREFIX + "." + str(self.id) + "." + name
        return key


    def get_val(self, field_name):
        """ get value in data field, returning value
        :field_name: - field name = use lower case
        """
        field = field_name.lower()
        if hasattr(self, field):
            return getattr(self, field)
        
        raise SelectError("SelectPlayer.get_val(%s) - no entry: %s"
                           % (field_name, field))

    def set_val_from_ctl(self, field_name):
        """ Set player value from field
        Also updates player value properties
        :field_name: field name
        """
        if not hasattr(self, field_name):
            raise SelectError("Player has no attribute %s" % field_name)
        value = self.ctls_vars[field_name].get()
        setattr(self, field_name, value)
        self.set_prop_val(field_name)


    def set_prop_val(self, field_name):
        """ Update properties value for field, so that properties file
        will contain the updated value
        :field_name: field attribute name
        """
        prop_key = self.get_prop_key(field_name)
        field_value = self.get_val(field_name)
        prop_value = str(field_value)
        SlTrace.setProperty(prop_key, prop_value)

    
class PlayerControl(Toplevel):
    CONTROL_NAME_PREFIX = "player_control"
    
    def __init__(self, ctlbase, title=None, display=True):
        """ Display / Control of players
        :ctlbase: base control object
        
        values stored in properties file
        All values stored under "player_control.".<player_id>
        The player_id is constructed by replacing all
        sequences of [^a-zA-Z_0-9]+ by "_" in the player name
        to produce a legal properties file id string
        Value strings:
            id                  value type
            ------------        -------------
            name                string
            label               string
            playing             bool
            mV                  int
            color               string (fill)
            voice               bool
            help_play           bool
            pause               float
        
        
        """
        ###Toplevel.__init__(self, parent)
        self.ctlbase = ctlbase
        """ Setup control names found in properties file
        Updated as new control entries are added
        """
        prop_keys = SlTrace.getPropKeys()
        player_pattern = r'(?:\.(\w+))'
        pattern = self.CONTROL_NAME_PREFIX + player_pattern + player_pattern
        rpat = re.compile(pattern)
        self.players = {}   # Dictionary of SelectPlayer
                            # by name
        self.call_d = []    # Call back routines, if any
        for prop_key in prop_keys:
            rmatch = re.match(rpat, prop_key)
            if rmatch:
                player_match = rmatch[0]
                player_match_1 = rmatch[1]
                player_id = rmatch[1]
                player_field = rmatch[2]
                prop_val = SlTrace.getProperty(prop_key)
                
                if player_id not in self.players:
                    player = SelectPlayer(player_id)
                    self.players[player_id] = player # New entry
                else:
                    player = self.players[player_id]
                player_attr = rmatch[2]
                if not hasattr(player, player_attr):
                    raise SelectError("Unrecognized player attribute %s in %s"
                                      % (player_attr, prop_key))
                else:
                    pat = getattr(player, player_attr)
                    if isinstance(pat, float):
                        player_val = float(prop_val)
                    elif isinstance(pat, bool):
                        pvl = prop_val.lower()
                        if (pvl == "yes"
                                or pvl == "y"
                                or pvl == "1"
                                or pvl == "true"):
                            player_val = True
                        elif (pvl == "no"
                                or pvl == "n"
                                or pvl == "0"
                                or pvl == "false"):
                            player_val = False
                        else:
                            raise SelectError("Unrecognized boolean value (%s =)  %s"
                                              % (player_attr, prop_val))
                    elif isinstance(pat, int):
                        player_val = int(prop_val)
                    else:
                        player_val = prop_val
                    setattr(player, player_attr, player_val)
                    self.players[player_id] = player
        
        if title is None:
            title = "Player Control"
        self.title = title
        
        if display:
            self.control_display()
            
    def control_display(self):
        """ display /redisplay controls to enable
        entry / modification
        """
        win_width =  500
        win_height = 200
        win_x0 = 100
        win_y0 = 100
                    
        self.mw = Toplevel()
        win_setting = "%dx%d+%d+%d" % (win_width, win_height, win_x0, win_y0)

        
        self.mw.geometry(win_setting)
        self.mw.title(self.title)
        top_frame = Frame(self.mw)
        self.mw.protocol("WM_DELETE_WINDOW", self.delete_window)
        top_frame.pack(side="top", fill="x", expand=True)
        self.top_frame = top_frame
        
        controls_frame = Frame(top_frame)
        controls_frame.pack(side="top", fill="x", expand=True)
        self.controls_frame = controls_frame
        players_frame = Frame(controls_frame)
        players_frame.pack(side="top", fill="x", expand=True)
        class ColumnInfo:
            def __init__(self, field_name,
                         hd=None, width=None):
                """ column info
                :field_name: - SelectPlayer field name
                :hd: heading default: field_name.capitalized()
                :width: width in characters
                        default: length of heading + 1
                """
                self.field_name = field_name
                if hd is None:
                    hd = field_name.capitalize()
                self.heading = hd
                if width is None:
                    width = len(self.heading) + 1
                self.width = width
                
                
        """ fields in the order to present """        
        player_fields = ["name", "label",
                         "playing",
                         "move",
                         "color", "color_bg",
                         "voice", "help_play", "pause"]
        col_infos = []
        for field in player_fields:
            heading = self.get_heading(field)
            width = self.get_col_width(field)
            col_info = ColumnInfo(field, hd=heading, width=width)
            col_infos.append(col_info)
            
            
        self.set_field_headings(players_frame, col_infos)
        for pid, player in self.players.items():
            for idx, field in enumerate(player_fields):
                self.set_player_frame(players_frame, player, col_infos, idx)
            players_frame.rowconfigure(pid, weight=1)


        """ Contol buttons """
        control_button_frame = Frame(controls_frame)
        control_button_frame.pack(side="top", fill="x", expand=True)
        set_button = Button(master=control_button_frame, text="Set", command=self.set)
        set_button.pack(side="left", expand=True)
        add_button = Button(master=control_button_frame, text="Add",
                            command=self.add_player)
        add_button.pack(side="left", expand=True)
        delete_button = Button(master=control_button_frame, text="Delete",
                            command=self.delete_player)
        delete_button.pack(side="left", expand=True)


    def set(self):
        """ Set info from form
        """
        self.set_vals()
        
        
    def add_player(self):
        """ Add new player
        """
        SlTrace.lg("add_player not yet implemented")
    
    def delete_player(self):
        """ Delete player
        """
        SlTrace.lg("delete_player not yet implemented")
        
        
        
    def set_field_headings(self, field_headings_frame, col_infos):
        """ Setup player headings, possibly recording widths
        """
        for info_idx, col_info in enumerate(col_infos):
            field_name = col_info.field_name
            heading = col_info.heading
            heading_label = Label(master=field_headings_frame,
                                  text=heading, anchor=CENTER,
                                  justify=CENTER,
                                  width=col_info.width)
            heading_label.grid(row=0, column=info_idx, sticky=NSEW)
            field_headings_frame.columnconfigure(info_idx, weight=1)


    def get_col_width(self, field_name):
        """ Calculate widget text width
        :field_name: field name SelectPlayer attribute
        :returns:  proper column width, given heading and all values for this field
        """
        heading = self.get_heading(field_name)
        width = len(heading)        # Start with heading as width
        for player in self.players.values():
            val = getattr(player, field_name)
            val_len = len(str(val)) + 1
            if val_len > width:
                width = val_len
        return int(width*1.25)

    
    def get_field_name(self, heading):
        """ Convert heading into field name
        :heading:  Heading text
        """
        field = heading.lower()
        if field == "help":
            field = "help_play"
        return field

    
    def get_heading(self, field_name):
        """ Convert heading into field name
        :field_name:  field attribute
        """
        heading = field_name
        if heading == "help_play":
            heading = "help"
        heading = heading.capitalize()
        return heading
    

    def set_player_frame(self, frame, player, col_infos, idx):
        """ Create player info line
        :frame: players frame
        :player: player info
        :col_infos: list of information for each column
        :idx: index into col_infos
        """
        col_info = col_infos[idx]
        field_name = col_info.field_name
        value = player.get_val(field_name)
        width = self.get_col_width(field_name)
        frame = Frame(frame, height=1, width=width)
        frame.grid(row=player.id, column=idx, sticky=NSEW)

        if field_name == "name":
            self.set_player_frame_name(frame, player, value, width=width)
        elif field_name == "label":
            self.set_player_frame_label(frame, player, value, width=width)
        elif field_name == "playing":
            self.set_player_frame_playing(frame, player, value, width=width)
        elif field_name == "move":
            self.set_player_frame_move(frame, player, value, width=width)
        elif field_name == "color":
            self.set_player_frame_color(frame, player, value, width=width)
        elif field_name == "color_bg":
            self.set_player_frame_color_bg(frame, player, value, width=width)
        elif field_name == "voice":
            self.set_player_frame_voice(frame, player, value, width=width)
        elif field_name == "help_play":
            self.set_player_frame_help(frame, player, value, width=width)
        elif field_name == "pause":
            self.set_player_frame_pause(frame, player, value, width=width)
        else:
            raise("Unrecognized player field_name: %s" % field_name)    


    def set_player_frame_name(self, frame, player, value, width=None):
        content = StringVar()
        content.set(value)
        val_entry = Entry(frame, textvariable=content, width=width)
        val_entry.pack(side="left", fill="none", expand=True)
        player.ctls["name"] = val_entry
        player.ctls_vars["name"] = content

    def set_player_frame_label(self, frame, player, value, width=None):
        content = StringVar()
        content.set(value)
        val_entry = Entry(frame, textvariable=content, width=width)
        val_entry.pack(side="left", fill="none", expand=True)
        player.ctls["label"] = val_entry
        player.ctls_vars["label"] = content

    def set_player_frame_playing(self, frame, player, value, width=None):
        content = BooleanVar()
        content.set(value)
        yes_button = Checkbutton(frame, variable=content, width=None)
        yes_button.pack(side="left", fill="none", expand=True)
        player.ctls["playing"] = yes_button
        player.ctls_vars["playing"] = content

    def set_player_frame_move(self, frame, player, value, width=None):
        content = IntVar()
        content.set(value)
        yes_button = Entry(frame, textvariable=content, width=width)
        yes_button.pack(side="left", expand=True)
        player.ctls["move"] = yes_button
        player.ctls_vars["move"] = content

    def set_player_frame_color(self, frame, player, value, width=None):
        content = StringVar()
        content.set(value)
        val_entry = Entry(frame, textvariable=content, width=width)
        val_entry.pack(side="left", fill="none", expand=True)
        player.ctls["color"] = val_entry
        player.ctls_vars["color"] = content

    def set_player_frame_color_bg(self, frame, player, value, width=None):
        content = StringVar()
        content.set(value)
        val_entry = Entry(frame, textvariable=content, width=width)
        val_entry.pack(side="left", fill="none", expand=True)
        player.ctls["color_bg"] = val_entry
        player.ctls_vars["color_bg"] = content

    def set_player_frame_voice(self, frame, player, value, width=None):
        content = BooleanVar()
        content.set(value)
        yes_button =  Checkbutton(frame, variable=content, width=width)
        yes_button.pack(side="left", fill="none", expand=True)
        player.ctls["voice"] = yes_button
        player.ctls_vars["voice"] = content

    def set_player_frame_help(self, frame, player, value, width=None):
        content = BooleanVar()
        content.set(value)
        yes_button = Checkbutton(frame, variable=content, width=width)
        yes_button.pack(side="left", fill="none", expand=True)
        player.ctls["help_play"] = yes_button
        player.ctls_vars["help_play"] = content

    def set_player_frame_pause(self, frame, player, value, width=None):
        content = DoubleVar()
        content.set(value)
        yes_button = Entry(frame, textvariable=content, width=width)
        yes_button.pack(side="left", expand=True)
        player.ctls["pause"] = yes_button
        player.ctls_vars["pause"] = content


    def set_vals(self):
        """ Read form, if displayed, and update internal values
        """
        for player in self.players.values():
            for field in player.ctls_vars:
                player.set_val_from_ctl(field)
                
       
    def delete_window(self):
        """ Process Trace Control window close
        """
        if self.mw is not None:
            self.mw.destroy()
            self.mw = None
    
    
    def add(self):
        if "set" in self.call_d:
            self.call_d["set"]()
    
    def edit(self):
        if "edit" in self.call_d:
            self.call_d["edit"]()
        
    def delete(self):
        if "delete" in self.call_d:
            self.call_d["delete"]()
    

        
if __name__ == '__main__':
        
    root = Tk()

    frame = Frame(root)
    frame.pack()
    SlTrace.setProps()
    SlTrace.setFlags("")
    plc = PlayerControl(frame, title="player_control", display=True)
        
    root.mainloop()