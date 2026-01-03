import tkinter as tk
from ..utils import *
from ..logic import *
import math

class StatsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['BG_MAIN'])
        self.controller = controller
        
        tk.Label(self, text=get_msg('BTN_STATS'), font=FONTS['HEADER'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=10)
        
        self.canvas = tk.Canvas(self, width=400, height=300, bg=COLORS['BG_CARD'], highlightthickness=0)
        self.canvas.pack(pady=10)
        
        self.text_area = tk.Text(self, width=60, height=10, font=FONTS['BODY'], bg=COLORS['BG_CARD'], relief='flat')
        self.text_area.pack(pady=10)
        
        tk.Button(self, text=get_msg('BACK_BTN'), command=lambda: controller.show_frame("MainMenu"),
                  bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'], font=FONTS['BODY'], relief='flat').pack(pady=10)
        
    def draw_pie_chart(self, w, l):
        self.canvas.delete("all")
        total = w + l
        if total == 0:
            self.canvas.create_text(200, 150, text="No Data", font=("Arial", 20))
            return
            
        start_angle = 0
        
        # Win Slice
        win_angle = (w / total) * 360
        self.canvas.create_arc(50, 50, 250, 250, start=start_angle, extent=win_angle, fill=COLORS['SUCCESS'])
        if w > 0:
            self.canvas.create_text(280, 100, text=f"Won: {w}", fill='green', anchor="w")
        
        # Lose Slice
        start_angle += win_angle
        lose_angle = (l / total) * 360
        self.canvas.create_arc(50, 50, 250, 250, start=start_angle, extent=lose_angle, fill=COLORS['ERROR'])
        if l > 0:
            self.canvas.create_text(280, 200, text=f"Lost: {l}", fill='red', anchor="w")
            
    def refresh(self):
        # Calculate Logic inline or move to logic.py? Moving some here for simplicity of access
        games = read_file_lines(FILES['JUEGO'])
        total_games = 0
        won = 0
        lost = 0
        
        stats_text = "Estadísticas Generales:\n"
        
        for g in games:
            parts = my_split(g, ',')
            if my_len(parts) > 6:
                total_games += 1
                res = my_strip(parts[6]).lower()
                if res == "ganador":
                    won += 1
                else:
                    lost += 1
        
        stats_text += f"Total: {total_games}\nGanados: {won}\nPerdidos: {lost}\n"
        
        # We can implement top words etc similar to console
        
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, stats_text)
        
        self.draw_pie_chart(won, lost)
