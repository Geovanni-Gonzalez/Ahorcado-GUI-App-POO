import tkinter as tk
from ..utils import COLORS, FONTS, play_sound

class HoverButton(tk.Button):
    def __init__(self, master, **kwargs):
        # Extract custom properties if any, else default
        bg_color = kwargs.get('bg', COLORS['BTN_BG'])
        active_color = kwargs.get('activebackground', COLORS['HIGHLIGHT_DARK'])
        
        # Set defaults for style if not provided
        if 'relief' not in kwargs: kwargs['relief'] = 'flat'
        if 'font' not in kwargs: kwargs['font'] = FONTS['BODY']
        if 'cursor' not in kwargs: kwargs['cursor'] = 'hand2' # Hand cursor on hover
        
        super().__init__(master, **kwargs)
        
        self.default_bg = bg_color
        self.hover_bg = self.lighten_color(bg_color)
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def on_enter(self, e):
        if self['state'] == tk.NORMAL:
            self['bg'] = self.hover_bg
            # Optional: play tick sound on hover? Maybe too noisy.
            
    def on_leave(self, e):
        if self['state'] == tk.NORMAL:
            self['bg'] = self.default_bg

    def on_click(self, e):
        if self['state'] == tk.NORMAL:
             play_sound('click')

    def lighten_color(self, hex_color):
        # Simple lightening logic
        # If standard color name, return as is or map? 
        # Assuming we use hex from COLORS
        if not hex_color.startswith('#'): return hex_color
        
        # Parse
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Lighten by 20%
        r = min(255, int(r * 1.2))
        g = min(255, int(g * 1.2))
        b = min(255, int(b * 1.2))
        
        return f"#{r:02x}{g:02x}{b:02x}"
