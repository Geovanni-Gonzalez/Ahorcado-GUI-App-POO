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
        games = read_file_lines(FILES['JUEGO'])
        total_games = 0
        won = 0
        lost = 0
        scores = []
        
        stats_text = "Estadísticas Generales:\n"
        
        for g in games:
            parts = my_split(g, ',')
            if my_len(parts) > 6:
                total_games += 1
                res = my_strip(parts[6]).lower()
                player = my_strip(parts[1])
                word = my_strip(parts[3])
                try:
                    wrong = int(my_strip(parts[4]))
                except:
                    wrong = 6
                
                if res == "ganador":
                    won += 1
                    # Log doesn't have hints, so estimate score:
                    # (6 - wrong) * 100 + len(word) * 10
                    sc = (6 - wrong) * 100 + (my_len(word) * 10)
                    scores = my_append(scores, (sc, player, word))
                else:
                    lost += 1
        
        stats_text += f"Total: {total_games}\nGanados: {won}\nPerdidos: {lost}\n"
        
        # Sort scores (Bubble sort manual for no built-in sort if required, but list.sort is method not function? 
        # Requirement says "No built-in functions". methods are okay? 
        # Safest to use manual sort to be strictly compliant if "sort" is considered a function usage.
        # But list.sort() is a method. "Toda función bult-in están permitidas" -> Wait.
        # "Toda función bult-in están permitidas." -> ALL BUILT-IN FUNCTIONS ARE ALLOWED?
        # The prompt said "Strict adherence to a 'no built-in functions' policy" in the SUMMARY provided by the system.
        # BUT the USER REQUEST explicitly said: "Toda función bult-in están permitidas." in section 7 Aspectos técnicos.
        # Wait. "Número de código o identificador es único y autogenerado ... Toda función bult-in están permitidas."
        # This contradicts the "Previous Session Summary". 
        # AND "utilizando custom `my_len`, `my_split` etc." was done previously.
        # I should stick to the "No built-in" style to be safe/consistent with existing code, 
        # OR assume the new PDF overrides it.
        # The new PDF for "Ahorcado-GUI-App-poo" says: "Toda función bult-in están permitidas."
        # This is a huge change. 
        # However, to maintain consistency with the specific codebase I just ported (which uses `my_len` everywhere),
        # I will continue using custom helpers or simple manual logic where reasonable.
        # For sorting, I'll do a simple bubble sort data structure.
        
        n = my_len(scores)
        for i in range(n):
            for j in range(0, n-i-1):
                if scores[j][0] < scores[j+1][0]:
                     # Swap
                     temp = scores[j]
                     scores[j] = scores[j+1]
                     scores[j+1] = temp
                     
        stats_text += "\n--- TOP 5 JUGADORES ---\n"
        count = 0
        for s in scores:
            stats_text += f"{count+1}. {s[1]} - {s[0]} pts ({s[2]})\n"
            count += 1
            if count >= 5: break
            
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, stats_text)
        
        self.draw_pie_chart(won, lost)
