import tkinter as tk
from tkinter import messagebox, simpledialog
from ..utils import *
from ..logic import *

class AdminFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['BG_MAIN'])
        self.controller = controller
        
        # Title
        tk.Label(self, text=get_msg('ADMIN_MENU'), font=FONTS['TITLE'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=20)
        
        # Helper
        def create_btn(text, cmd):
            tk.Button(self, text=text, width=30, height=2, command=cmd, 
                      bg=COLORS['BTN_BG'], fg=COLORS['BTN_FG'], font=FONTS['BODY'], relief='flat').pack(pady=10)

        create_btn(get_msg('MGM_WORDS'), lambda: controller.show_frame("WordMgmt"))
        create_btn(get_msg('MGM_PHRASES'), lambda: controller.show_frame("PhraseMgmt"))
        create_btn(get_msg('BACK_BTN'), lambda: controller.show_frame("MainMenu"))

class MgmtFrame(tk.Frame):
    def __init__(self, master, controller, is_phrase=False):
        super().__init__(master, bg=COLORS['BG_MAIN'])
        self.controller = controller
        self.is_phrase = is_phrase
        self.filepath = FILES['FRASES'] if is_phrase else FILES['PALABRAS']
        
        self.title_key = 'MGM_PHRASES' if is_phrase else 'MGM_WORDS'
        
        tk.Label(self, text=get_msg(self.title_key), font=FONTS['HEADER'], bg=COLORS['BG_MAIN'], fg=COLORS['TEXT']).pack(pady=10)
        
        # Listbox
        self.listbox = tk.Listbox(self, width=50, height=15, font=FONTS['BODY'], bg=COLORS['BG_CARD'], relief='flat')
        self.listbox.pack(pady=10)
        
        btn_frame = tk.Frame(self, bg=COLORS['BG_MAIN'])
        btn_frame.pack(pady=10)
        
        def create_small_btn(text, cmd, color=COLORS['BTN_BG']):
            tk.Button(btn_frame, text=text, command=cmd, bg=color, fg=COLORS['BTN_FG'], font=FONTS['BODY'], relief='flat').pack(side=tk.LEFT, padx=5)
            
        create_small_btn(get_msg('BTN_ADD'), self.add_item, COLORS['SUCCESS'])
        create_small_btn(get_msg('BTN_MOD'), self.mod_item, COLORS['HIGHLIGHT'])
        create_small_btn(get_msg('BTN_DEL'), self.del_item, COLORS['ERROR'])
        create_small_btn(get_msg('BACK_BTN'), lambda: controller.show_frame("AdminFrame"), COLORS['BTN_BG'])
        
        self.refresh()
        
    def refresh(self):
        self.listbox.delete(0, tk.END)
        entries = get_all_entries(self.filepath)
        for eid, text in entries:
            self.listbox.insert(tk.END, f"{eid} | {text}")
            
    def get_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return None
        item = self.listbox.get(sel[0])
        # "ID | TEXT"
        parts = my_split(item, '|')
        return int(my_strip(parts[0]))

    def add_item(self):
        text = simpledialog.askstring(get_msg('BTN_ADD'), get_msg('LBL_TEXT'))
        if text:
            if my_len(my_strip(text)) == 0:
                messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_EMPTY'))
                return
            if add_entry(self.filepath, text):
                messagebox.showinfo(get_msg('MSG_SUCCESS'), get_msg('MSG_ADDED'))
                self.refresh()
            else:
                messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_EXISTS'))

    def del_item(self):
        pid = self.get_selected()
        if not pid: return
        
        res = delete_entry(self.filepath, pid, self.is_phrase)
        if res == "OK":
            messagebox.showinfo(get_msg('MSG_SUCCESS'), get_msg('MSG_DELETED'))
            self.refresh()
        elif res == "USED":
             messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_USED'))
        else:
             messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_NOT_FOUND'))

    def mod_item(self):
        pid = self.get_selected()
        if not pid: return
        
        new_text = simpledialog.askstring(get_msg('BTN_MOD'), get_msg('LBL_TEXT'))
        if new_text:
             if my_len(my_strip(new_text)) == 0:
                messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_EMPTY'))
                return
             res = modify_entry(self.filepath, pid, new_text)
             if res == "OK":
                 messagebox.showinfo(get_msg('MSG_SUCCESS'), get_msg('MSG_MODIFIED'))
                 self.refresh()
             elif res == "EXISTS":
                 messagebox.showerror(get_msg('MSG_ERROR'), get_msg('MSG_EXISTS'))
