import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from ..utils import *
from ..logic import *
from .components import HoverButton
import random
import datetime

class NewGameFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['BG_MAIN'])
        self.controller = controller
        
        tk.Label(self, text=get_msg('NEW_GAME_TITLE'), font=FONTS['HEADER'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=20)
        
        # Name
        tk.Label(self, text=get_msg('LBL_NAME'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.entry_name = tk.Entry(self, font=FONTS['BODY'], relief='flat')
        self.entry_name.pack(pady=5)
        
        # Lang
        tk.Label(self, text=get_msg('LBL_LANG'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.lang_var = tk.StringVar(value="ES")
        tk.Radiobutton(self, text="Español", variable=self.lang_var, value="ES", bg=COLORS['BG_MAIN'], fg=COLORS['TEXT'], font=FONTS['BODY'], command=self.update_lang, highlightthickness=0).pack()
        tk.Radiobutton(self, text="English", variable=self.lang_var, value="EN", bg=COLORS['BG_MAIN'], fg=COLORS['TEXT'], font=FONTS['BODY'], command=self.update_lang, highlightthickness=0).pack()
        
        # Mode
        tk.Label(self, text=get_msg('LBL_MODE'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.mode_var = tk.StringVar(value=get_msg('MODE_BEG'))
        self.combo_mode = ttk.Combobox(self, textvariable=self.mode_var, state="readonly", font=FONTS['BODY'])
        self.combo_mode['values'] = (get_msg('MODE_BEG'), get_msg('MODE_ADV'))
        self.combo_mode.pack(pady=5)
        
        tk.BooleanVar(self) # Need instance var for timer?
        self.timer_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, text=get_msg('CHK_TIMER'), variable=self.timer_var,
                       bg=COLORS['BG_MAIN'], fg=COLORS['TEXT'], font=FONTS['BODY'],
                       selectcolor=COLORS['BG_MAIN'], activebackground=COLORS['BG_MAIN']).pack(pady=5)
        
        # Hardcore Mode
        self.hardcore_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, text="🔥 Hardcore (3 Lives, 2x Pts)", variable=self.hardcore_var,
                       bg=COLORS['BG_MAIN'], fg=COLORS['ERROR'], font=FONTS['BODY_BOLD'],
                       selectcolor=COLORS['BG_MAIN'], activebackground=COLORS['BG_MAIN']).pack(pady=5)
        
        tk.Button(self, text=get_msg('BTN_PLAY'), command=self.start_game, width=30, height=2,
                  bg=COLORS['BTN_PRIMARY'], fg='white', font=FONTS['BODY_BOLD'], relief='flat').pack(pady=20)
                  
        tk.Button(self, text=get_msg('BACK_BTN'), command=lambda: controller.show_frame("MainMenu"),
                  bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'], font=FONTS['BODY'], relief='flat', width=30, height=2).pack()

    # ... (rest of NewGameFrame omitted, jumping to GameFrame.draw_hangman)

    def draw_hangman(self):
        self.canvas.delete("all")
        # Gallows in Highlight (Cyan)
        self.canvas.create_line(50, 250, 250, 250, width=4, fill=COLORS['HIGHLIGHT'])
        self.canvas.create_line(150, 250, 150, 50, width=4, fill=COLORS['HIGHLIGHT'])
        self.canvas.create_line(150, 50, 200, 50, width=4, fill=COLORS['HIGHLIGHT'])
        self.canvas.create_line(200, 50, 200, 80, width=4, fill=COLORS['HIGHLIGHT'])
        
        # Body in Text/Error (White/Red)
        if self.wrong > 0: self.canvas.create_oval(180, 80, 220, 120, width=4, outline=COLORS['TEXT']) # Head
        if self.wrong > 1: self.canvas.create_line(200, 120, 200, 190, width=4, fill=COLORS['TEXT']) # Body
        if self.wrong > 2: self.canvas.create_line(200, 140, 170, 170, width=4, fill=COLORS['TEXT']) # Left Arm
        if self.wrong > 3: self.canvas.create_line(200, 140, 230, 170, width=4, fill=COLORS['TEXT']) # Right Arm
        if self.wrong > 4: self.canvas.create_line(200, 190, 170, 220, width=4, fill=COLORS['TEXT']) # Left Leg
        if self.wrong > 5: self.canvas.create_line(200, 190, 230, 220, width=4, fill=COLORS['ERROR']) # Right Leg (Death)

    def update_lang(self):
        # Guard against premature triggering during initialization
        if "NewGameFrame" not in self.controller.frames:
            return
            
        new_lang = self.lang_var.get()
        set_lang(new_lang)
        self.controller.refresh_all()
        self.combo_mode['values'] = (get_msg('MODE_BEG'), get_msg('MODE_ADV'))
        self.mode_var.set(get_msg('MODE_BEG'))

    def start_game(self):
        name = my_strip(self.entry_name.get())
        if my_len(name) == 0:
            messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_EMPTY'))
            return
            
        mode_str = self.mode_var.get()
        is_beg = (mode_str == get_msg('MODE_BEG'))
        use_timer = self.timer_var.get()
        is_hardcore = self.hardcore_var.get()
        
        filepath = FILES['PALABRAS'] if is_beg else FILES['FRASES']
        lines = read_file_lines(filepath)
        if not lines:
            messagebox.showerror(get_msg('MSG_ERROR'), "No words available")
            return
            
        line = random.choice(lines)
        parts = my_split(line, ',')
        target = my_strip(parts[1]).upper()
        
        game_frame = self.controller.frames["GameFrame"]
        game_frame.setup_game(name, mode_str, target, use_timer, is_hardcore)
        self.controller.show_frame("GameFrame")

class PvPSetupFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['BG_MAIN'])
        self.controller = controller
        
        tk.Label(self, text=get_msg('PVP_TITLE'), font=FONTS['HEADER'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=20)
        
        # Secret Word
        tk.Label(self, text=get_msg('LBL_SECRET'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.entry_secret = tk.Entry(self, font=FONTS['BODY'], show="*", relief='flat')
        self.entry_secret.pack(pady=5)
        
        # Challenger
        tk.Label(self, text=get_msg('LBL_CHALLENGER'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.entry_challenger = tk.Entry(self, font=FONTS['BODY'], relief='flat')
        self.entry_challenger.pack(pady=5)
        
        # Guesser
        tk.Label(self, text=get_msg('LBL_NAME'), font=FONTS['BODY_BOLD'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack()
        self.entry_guesser = tk.Entry(self, font=FONTS['BODY'], relief='flat')
        self.entry_guesser.pack(pady=5)
        
        tk.Button(self, text=get_msg('BTN_PLAY'), command=self.start_pvp, width=20, height=2,
                  bg=COLORS['BTN_PRIMARY'], fg='white', font=FONTS['BODY_BOLD'], relief='flat').pack(pady=20)
        tk.Button(self, text=get_msg('BACK_BTN'), command=lambda: controller.show_frame("MainMenu"),
                  bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'], font=FONTS['BODY'], relief='flat').pack()
                  
    def start_pvp(self):
        secret = my_strip(self.entry_secret.get()).upper()
        challenger = my_strip(self.entry_challenger.get())
        guesser = my_strip(self.entry_guesser.get())
        
        if my_len(secret) == 0:
             messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_SECRET_EMPTY'))
             return
             
        # Validate secret: only letters and spaces
        valid = True
        for c in secret:
            if not ('A' <= c <= 'Z' or c == 'Ñ' or c == ' '):
                valid = False
                break
        if not valid:
             messagebox.showerror(get_msg('MSG_ERROR'), "Invalid characters in secret word")
             return

        game_frame = self.controller.frames["GameFrame"]
        game_frame.setup_game(guesser, "PvP", secret, False) # No timer for pvp default
        self.controller.show_frame("GameFrame")

class GameFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['BG_GAME'])
        self.controller = controller
        
        # Enable focus for keyboard events
        self.bind("<Key>", self.handle_keypress)
        
        self.canvas = tk.Canvas(self, width=300, height=300, bg=COLORS['BG_GAME'], highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, padx=30, pady=30)
        
        right_panel = tk.Frame(self, bg=COLORS['BG_GAME'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Timer Label
        self.lbl_timer = tk.Label(right_panel, text="", font=FONTS['HEADER'], bg=COLORS['BG_GAME'], fg=COLORS['ERROR'])
        self.lbl_timer.pack(pady=5)
        
        self.lbl_word = tk.Label(right_panel, text="", font=FONTS['MONO'], bg=COLORS['BG_GAME'], fg=COLORS['TEXT'])
        self.lbl_word.pack(pady=20)

        # ... (rest of init)
        
        self.lbl_info = tk.Label(right_panel, text="", font=FONTS['BODY'], bg=COLORS['BG_GAME'], fg=COLORS['TEXT_LIGHT'])
        self.lbl_info.pack(pady=10)
        
        self.btn_hint = HoverButton(right_panel, text="", command=self.use_hint, 
                                  bg=COLORS['ACCENT'], fg=COLORS['TEXT'], font=FONTS['BODY_BOLD'], relief='flat')
        self.btn_hint.pack(pady=5)
        
        self.kb_frame = tk.Frame(right_panel, bg=COLORS['BG_GAME'])
        self.kb_frame.pack(pady=20)
        
        self.buttons = {}
        row = 0
        col = 0
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for char in alphabet:
            b = HoverButton(self.kb_frame, text=char, width=4, height=2, 
                          command=lambda c=char: self.guess(c),
                          bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'], font=('Arial', 10, 'bold'), relief='flat')
            b.grid(row=row, column=col, padx=4, pady=4)
            self.buttons[char] = b
            col += 1
            if col > 6:
                col = 0
                row += 1
                
        HoverButton(right_panel, text=get_msg('BACK_BTN'), command=self.quit_game,
                  bg=COLORS['ERROR'], fg='white', font=FONTS['BODY'], relief='flat').pack(pady=10)
        
    def handle_keypress(self, event):
        max_wrong = 3 if self.is_hardcore else 6
        if self.wrong >= max_wrong: return # Game over
        char = event.char.upper()
        if 'A' <= char <= 'Z' or char == 'Ñ':
            # Check if button enabled (not guessed yet)
            if char in self.buttons and self.buttons[char]['state'] == tk.NORMAL:
                self.guess(char)

    def setup_game(self, player, mode, target, use_timer=False, is_hardcore=False):
        self.player = player
        self.mode = mode
        self.target = target
        self.use_timer = use_timer
        self.is_hardcore = is_hardcore
        self.guessed = []
        self.wrong = 0
        self.hints = 0
        self.start_time = datetime.datetime.now()
        self.timer_val = 60 
        self.timer_running = False
        
        self.lbl_timer.config(text="")
        if self.is_hardcore:
             self.lbl_timer.config(text="🔥 HARDCORE MODE 🔥", fg=COLORS['ERROR'])
        
        self.btn_hint.config(text=get_msg('HINT_BTN'), state=tk.NORMAL)
        
        for b in self.buttons.values():
            b.config(state=tk.NORMAL, bg=COLORS['BTN_BG'])
            
        self.update_ui()
        self.focus_set()
        
        if self.use_timer:
            self.timer_running = True
            self.update_timer()
            
    def update_timer(self):
        if not self.timer_running: return
        
        self.lbl_timer.config(text=f"{get_msg('TIME_LBL')} {self.timer_val}s")
        if self.timer_val <= 0:
            self.timer_running = False
            self.end_game("time_out")
        else:
            self.timer_val -= 1
            self.after(1000, self.update_timer)

    def draw_hangman(self):
        self.canvas.delete("all")
        self.canvas.create_line(50, 250, 250, 250, width=4)
        self.canvas.create_line(150, 250, 150, 50, width=4)
        self.canvas.create_line(150, 50, 200, 50, width=4)
        self.canvas.create_line(200, 50, 200, 80, width=4)
        
        if self.wrong > 0: self.canvas.create_oval(180, 80, 220, 120, width=4)
        if self.wrong > 1: self.canvas.create_line(200, 120, 200, 190, width=4)
        if self.wrong > 2: self.canvas.create_line(200, 140, 170, 170, width=4)
        if self.wrong > 3: self.canvas.create_line(200, 140, 230, 170, width=4)
        if self.wrong > 4: self.canvas.create_line(200, 190, 170, 220, width=4)
        if self.wrong > 5: self.canvas.create_line(200, 190, 230, 220, width=4)

    def update_ui(self):
        self.draw_hangman()
        
        display = ""
        done = True
        missing_chars = []
        for char in self.target:
            if char == ' ':
                display += "  "
            elif my_in(char, self.guessed):
                display += char + " "
            else:
                display += "_ "
                done = False
                if my_not_in(char, missing_chars):
                    missing_chars = my_append(missing_chars, char)
        
        self.lbl_word.config(text=display)
        
        max_wrong = 3 if self.is_hardcore else 6
        multiplier = 2 if self.is_hardcore else 1
        
        score_calc = (((6 - self.wrong) * 100) + (my_len(self.target) * 10) - (self.hints * 50)) * multiplier
        if score_calc < 0: score_calc = 0
        
        lives = max_wrong - self.wrong
        lbl_text = f"{self.player} | "
        if self.is_hardcore:
             lbl_text += f"Lives: {lives} | "
        else:
             lbl_text += f"{get_msg('ATTEMPTS_LBL')} {lives} | "
             
        lbl_text += f"{get_msg('SCORE_LBL')} {score_calc}"
        self.lbl_info.config(text=lbl_text)
        
        if done:
            self.end_game("ganador")
        elif self.wrong >= max_wrong:
            self.end_game("perdedor")
            
    def guess(self, char):
        if my_in(char, self.guessed): return
        
        play_sound('click')
        self.guessed = my_append(self.guessed, char)
        self.buttons[char].config(state=tk.DISABLED)
        
        if my_in(char, self.target):
            self.buttons[char].config(bg=COLORS['SUCCESS'])
        else:
            play_sound('error')
            self.buttons[char].config(bg=COLORS['ERROR'])
            self.wrong += 1
            
        self.update_ui()
        
    def use_hint(self):
        play_sound('click')
        missing = []
        for c in self.target:
             if c != ' ' and my_not_in(c, self.guessed):
                 if my_not_in(c, missing):
                     missing = my_append(missing, c)
                     
        if my_len(missing) > 0:
            hint = random.choice(missing)
            self.hints += 1
            self.guess(hint)
        else:
            self.btn_hint.config(state=tk.DISABLED)

    def animate_win(self, particles):
        if not particles: return
        self.canvas.delete("confetti")
        new_particles = []
        for p in particles:
            # p = [x, y, vx, vy, color]
            p[0] += p[2]
            p[1] += p[3]
            p[3] += 0.5 # gravity
            if p[1] < 400: # Below canvas height
                self.canvas.create_oval(p[0], p[1], p[0]+5, p[1]+5, fill=p[4], tags="confetti")
                new_particles = my_append(new_particles, p)
        
        if my_len(new_particles) > 0:
             # Keep reference to after to cancel if needed? For now just run
             self.after(50, lambda: self.animate_win(new_particles))

    def trigger_win_effect(self):
        play_sound('win')
        colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
        particles = []
        for i in range(50):
            x = 150
            y = 50 # Start from head? or 150 center
            vx = random.uniform(-5, 5)
            vy = random.uniform(-10, -5)
            c = random.choice(colors)
            particles = my_append(particles, [x, y, vx, vy, c])
        self.animate_win(particles)
        self.after(3000, lambda: self.finish_win_sequence())

    def finish_win_sequence(self):
         messagebox.showinfo("Game Over", get_msg('GAME_WIN'))
         self.controller.show_frame("MainMenu")

    def end_game(self, result):
        self.timer_running = False # Stop timer
        end_time = datetime.datetime.now()
        save_finished_game(self.player, self.mode, self.target, self.wrong, self.guessed, result, self.start_time, end_time)
        
        if result == "ganador":
            self.trigger_win_effect()
        else:
            play_sound('lose')
            msg = get_msg('GAME_LOSE')
            if result == "time_out": msg = get_msg('GAME_TIMEOUT')
            msg += f"\nTarget: {self.target}"
            messagebox.showinfo("Game Over", msg)
            self.controller.show_frame("MainMenu")
        
    def quit_game(self):
        if messagebox.askyesno("Quit", "Are you sure? Progress will be lost."):
            self.controller.show_frame("MainMenu")
