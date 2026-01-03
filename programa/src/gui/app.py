import tkinter as tk
from .admin import AdminFrame, MgmtFrame
from .player import NewGameFrame, GameFrame, PvPSetupFrame
from .stats import StatsFrame
from .components import HoverButton
from ..utils import *
from ..logic import login
from tkinter import messagebox, simpledialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(get_msg('APP_TITLE'))
        self.geometry("800x600")
        self.eval('tk::PlaceWindow . center') # Simple Tkinter centering or custom
        self.center_window(800, 600)
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.create_frames()
        self.show_frame("MainMenu")
        
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_frames(self):
        # Helper for styled buttons
        def create_btn(parent, text, cmd):
            return HoverButton(parent, text=text, width=25, height=1, 
                             command=cmd, bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'],
                             font=FONTS['BODY'], relief='flat', activebackground=COLORS['HIGHLIGHT_DARK'])

        # Main Menu Frame
        mm = tk.Frame(self.container, bg=COLORS['BG_MAIN'])
        tk.Label(mm, text=get_msg('MAIN_MENU'), font=FONTS['TITLE'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=40)
        
        create_btn(mm, get_msg('K_ADMIN'), self.req_login).pack(pady=10)
        create_btn(mm, get_msg('K_PLAYER'), lambda: self.show_frame("PlayerMenu")).pack(pady=10)
        
        # Exit button with simpler style or same?
        # Exit button with simpler style or same?
        tk.Button(mm, text=get_msg('K_EXIT'), width=25, height=1, command=self.quit,
                  bg=COLORS['ERROR'], fg='white', font=FONTS['BODY'], relief='flat').pack(pady=10)
        
        # Sound Toggle
        self.btn_sound = tk.Button(mm, text="🔊 Sound: ON", command=self.toggle_app_sound,
                                   bg=COLORS['BG_MAIN'], fg=COLORS['TEXT'], font=FONTS['SMALL'], relief='flat')
        self.btn_sound.place(relx=0.9, rely=0.05, anchor='ne') # Top right corner
                  
        self.frames["MainMenu"] = mm
        mm.grid(row=0, column=0, sticky="nsew")
        
        # Player Menu
        pm = tk.Frame(self.container, bg=COLORS['BG_MAIN'])
        tk.Label(pm, text=get_msg('PLAYER_MENU'), font=FONTS['TITLE'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=40)
        
        create_btn(pm, get_msg('BTN_NEW_GAME'), lambda: self.show_frame("NewGameFrame")).pack(pady=10)
        create_btn(pm, get_msg('BTN_PVP'), lambda: self.show_frame("PvPSetupFrame")).pack(pady=10)
        create_btn(pm, get_msg('BTN_STATS'), lambda: self.show_frame("StatsFrame")).pack(pady=10)
        
        # History (Text View)
        def show_hist():
            top = tk.Toplevel(self)
            top.title(get_msg('BTN_HISTORY'))
            top.config(bg=COLORS['BG_MAIN'])
            txt = tk.Text(top, width=60, height=20, font=FONTS['BODY'], bg=COLORS['BG_CARD'], fg=COLORS['TEXT'], relief='flat')
            txt.pack(padx=20, pady=20)
            lines = read_file_lines(FILES['HISTORIA'])
            for l in lines: txt.insert(tk.END, l + "\n")
        
        create_btn(pm, get_msg('BTN_HISTORY'), show_hist).pack(pady=10)
        
        # Help (Text View)
        def show_help():
            top = tk.Toplevel(self)
            top.title(get_msg('BTN_HELP'))
            top.config(bg=COLORS['BG_MAIN'])
            txt = tk.Text(top, width=60, height=20, font=FONTS['BODY'], bg=COLORS['BG_CARD'], fg=COLORS['TEXT'], relief='flat')
            txt.pack(padx=20, pady=20)
            lines = read_file_lines(FILES['AYUDA'])
            for l in lines: txt.insert(tk.END, l + "\n")
            
        create_btn(pm, get_msg('BTN_HELP'), show_help).pack(pady=10)
        create_btn(pm, get_msg('BACK_BTN'), lambda: self.show_frame("MainMenu")).pack(pady=20)
        
        self.frames["PlayerMenu"] = pm
        pm.grid(row=0, column=0, sticky="nsew")

        # Other Frames
        for F in (AdminFrame, NewGameFrame, GameFrame, StatsFrame, PvPSetupFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mgmt Frames initialized with args? 
        # Easier to handle in show_frame with dynamic creation or just separate classes
        # Let's instantiate MgmtFrames
        wf = MgmtFrame(self.container, self, is_phrase=False)
        self.frames["WordMgmt"] = wf
        wf.grid(row=0, column=0, sticky="nsew")
        
        pf = MgmtFrame(self.container, self, is_phrase=True)
        self.frames["PhraseMgmt"] = pf
        pf.grid(row=0, column=0, sticky="nsew")
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, 'refresh'):
            frame.refresh()
        frame.tkraise()
        
    def refresh_all(self):
        # Destroy and recreate frames to update language?
        # A bit expensive but ensures full update.
        for f in self.frames.values():
            f.destroy()
        self.create_frames()
        self.show_frame("NewGameFrame") # Assume we came from there if changing lang

    def req_login(self):
        pwd = simpledialog.askstring(get_msg('LOGIN_TITLE'), get_msg('LOGIN_LBL'), show='*')
        if pwd:
            if login(pwd):
                self.show_frame("AdminFrame")
            else:
                messagebox.showerror(get_msg('MSG_ERROR'), "Access Denied")

    def toggle_app_sound(self):
        is_on = toggle_sound()
        txt = "🔊 Sound: ON" if is_on else "🔇 Sound: OFF"
        self.btn_sound.config(text=txt)
