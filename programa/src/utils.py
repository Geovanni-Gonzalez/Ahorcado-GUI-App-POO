import os
import winsound

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

FILES = {
    'ACCESO': os.path.join(DATA_DIR, 'Acceso.txt'),
    'PALABRAS': os.path.join(DATA_DIR, 'Palabras.txt'),
    'FRASES': os.path.join(DATA_DIR, 'Frases.txt'),
    'HISTORIA': os.path.join(DATA_DIR, 'Historia.txt'),
    'AYUDA': os.path.join(DATA_DIR, 'Ayuda.txt'),
    'JUEGO': os.path.join(DATA_DIR, 'Juego.txt'),
    'ESTADISTICAS': os.path.join(DATA_DIR, 'Estadísticas.txt')
}

# Global State
CURRENT_LANG = 'ES'
SOUND_ON = True

# Colors
THEMES = {
    'DARK': {
        'BG_MAIN': '#0F172A',       # Deep Slate
        'BG_GAME': '#1E293B',       # Lighter Slate
        'BG_CARD': '#1E293B',       # Surface
        'TEXT': '#F8FAFC',          # Off-white
        'TEXT_LIGHT': '#94A3B8',    # Muted Blue-Grey
        'HIGHLIGHT': '#00E5FF',     # Neon Cyan
        'HIGHLIGHT_DARK': '#00B8D4',
        'ERROR': '#FF1744',         # Bright Red
        'SUCCESS': '#00E676',       # Bright Green
        'ACCENT': '#F50057',        # Neon Pink
        'BTN_BG': '#334155',        # Slate
        'BTN_FG': '#F8FAFC',        # White
        'BTN_PRIMARY': '#00E5FF'    # Cyan
    },
    'LIGHT': {
        'BG_MAIN': '#F0F4F8',       # Soft Cloud
        'BG_GAME': '#FFFFFF',       # White
        'BG_CARD': '#FFFFFF',
        'TEXT': '#102A43',          # Deep Navy
        'TEXT_LIGHT': '#627D98',    # Steel Blue
        'HIGHLIGHT': '#3366FF',     # Vivid Blue
        'HIGHLIGHT_DARK': '#1939B7',
        'ERROR': '#D64545',         # Red
        'SUCCESS': '#007D4F',       # Teal Green
        'ACCENT': '#FF9F43',        # Orange
        'BTN_BG': '#D9E2EC',        # Light Slate
        'BTN_FG': '#102A43',        # Navy
        'BTN_PRIMARY': '#3366FF'    # Blue
    }
}

COLORS = THEMES['DARK'].copy()
CURRENT_THEME = 'DARK'

def get_current_theme():
    return CURRENT_THEME

def set_theme(name):
    global CURRENT_THEME
    if name in THEMES:
        CURRENT_THEME = name
        COLORS.clear()
        COLORS.update(THEMES[name])

def toggle_theme_logic():
    new_theme = 'LIGHT' if CURRENT_THEME == 'DARK' else 'DARK'
    set_theme(new_theme)
    return new_theme

# Fonts
FONTS = {
    'TITLE': ("Segoe UI", 32, "bold"),
    'HEADER': ("Segoe UI", 20, "bold"),
    'BODY': ("Segoe UI", 12),
    'BODY_BOLD': ("Segoe UI", 12, "bold"),
    'MONO': ("Consolas", 28, "bold"), 
    'SMALL': ("Segoe UI", 10)
}

# Strings
STRINGS = {
    'ES': {
        'APP_TITLE': "Juego del Ahorcado",
        'MAIN_MENU': "MENÚ PRINCIPAL",
        'K_ADMIN': "Opciones administrativas",
        'K_PLAYER': "Opciones de jugador",
        'K_EXIT': "Salir",
        'LOGIN_TITLE': "Acceso Administrativo",
        'LOGIN_LBL': "Ingrese Clave:",
        'LOGIN_BTN': "Ingresar",
        'BACK_BTN': "Volver",
        'ADMIN_MENU': "Administración",
        'MGM_WORDS': "Gestión de Palabras",
        'MGM_PHRASES': "Gestión de Frases",
        'BTN_ADD': "Incluir",
        'BTN_MOD': "Modificar",
        'BTN_DEL': "Eliminar",
        'LBL_ID': "ID:",
        'LBL_TEXT': "Texto:",
        'MSG_SUCCESS': "Éxito",
        'MSG_ERROR': "Error",
        'MSG_ADDED': "Agregado correctamente",
        'MSG_MODIFIED': "Modificado correctamente",
        'MSG_DELETED': "Eliminado correctamente",
        'MSG_EXISTS': "Ya existe",
        'MSG_NOT_FOUND': "No encontrado",
        'MSG_USED': "No se puede eliminar: está en uso",
        'MSG_EMPTY': "Campo vacío",
        'PLAYER_MENU': "Menú Jugador",
        'BTN_NEW_GAME': "Nuevo Juego",
        'BTN_HISTORY': "Historia",
        'BTN_STATS': "Estadísticas",
        'BTN_HELP': "Ayuda",
        'NEW_GAME_TITLE': "Configuración Nuevo Juego",
        'LBL_NAME': "Nombre:",
        'LBL_LANG': "Idioma:",
        'LBL_MODE': "Modo:",
        'MODE_BEG': "Principiante",
        'MODE_ADV': "Avanzado",
        'BTN_PLAY': "Jugar",
        'GAME_WIN': "¡GANASTE!",
        'GAME_LOSE': "PERDISTE",
        'HINT_BTN': "Pista (-50 pts)",
        'SCORE_LBL': "Puntaje:",
        'ATTEMPTS_LBL': "Intentos:",
        'TIME_LBL': "Tiempo:",
        'BTN_PVP': "Duelo (2 Jugadores)",
        'PVP_TITLE': "Configurar Duelo",
        'LBL_SECRET': "Palabra Secreta:",
        'LBL_CHALLENGER': "Retador:",
        'MSG_SECRET_EMPTY': "Debe ingresar una palabra secreta",
        'CHK_TIMER': "Modo Contrarreloj (60s)",
        'GAME_TIMEOUT': "¡Se acabó el tiempo!"
    },
    'EN': {
        'APP_TITLE': "Hangman Game",
        'MAIN_MENU': "MAIN MENU",
        'K_ADMIN': "Administrative Options",
        'K_PLAYER': "Player Options",
        'K_EXIT': "Exit",
        'LOGIN_TITLE': "Admin Access",
        'LOGIN_LBL': "Enter Password:",
        'LOGIN_BTN': "Login",
        'BACK_BTN': "Back",
        'ADMIN_MENU': "Administration",
        'MGM_WORDS': "Word Management",
        'MGM_PHRASES': "Phrase Management",
        'BTN_ADD': "Add",
        'BTN_MOD': "Modify",
        'BTN_DEL': "Delete",
        'LBL_ID': "ID:",
        'LBL_TEXT': "Text:",
        'MSG_SUCCESS': "Success",
        'MSG_ERROR': "Error",
        'MSG_ADDED': "Added successfully",
        'MSG_MODIFIED': "Modified successfully",
        'MSG_DELETED': "Deleted successfully",
        'MSG_EXISTS': "Already exists",
        'MSG_NOT_FOUND': "Not found",
        'MSG_USED': "Cannot delete: currently in use",
        'MSG_EMPTY': "Empty field",
        'PLAYER_MENU': "Player Menu",
        'BTN_NEW_GAME': "New Game",
        'BTN_HISTORY': "History",
        'BTN_STATS': "Statistics",
        'BTN_HELP': "Help",
        'NEW_GAME_TITLE': "New Game Setup",
        'LBL_NAME': "Name:",
        'LBL_LANG': "Language:",
        'LBL_MODE': "Mode:",
        'MODE_BEG': "Beginner",
        'MODE_ADV': "Advanced",
        'BTN_PLAY': "Play",
        'GAME_WIN': "YOU WON!",
        'GAME_LOSE': "YOU LOST",
        'HINT_BTN': "Hint (-50 pts)",
        'SCORE_LBL': "Score:",
        'ATTEMPTS_LBL': "Attempts:",
        'TIME_LBL': "Time:",
        'BTN_PVP': "Duel (2 Players)",
        'PVP_TITLE': "Setup Duel",
        'LBL_SECRET': "Secret Word:",
        'LBL_CHALLENGER': "Challenger:",
        'MSG_SECRET_EMPTY': "Must enter a secret word",
        'CHK_TIMER': "Time Attack Mode (60s)",
        'GAME_TIMEOUT': "Time's up!"
    }
}

# Custom Helpers
def toggle_sound():
    global SOUND_ON
    SOUND_ON = not SOUND_ON
    return SOUND_ON

def play_sound(sound_type):
    """
    Plays a system sound based on type.
    Types: 'click', 'correct', 'error', 'win', 'lose'
    """
    if not SOUND_ON: return
    
    try:
        import winsound
        if sound_type == 'click':
            # Low frequency beep
            winsound.Beep(400, 50)
        elif sound_type == 'correct':
            # High pleasant beep
            winsound.Beep(1000, 150)
        elif sound_type == 'error':
            # Low long buzz
            winsound.Beep(200, 400)
        elif sound_type == 'win':
            # Victory Arpeggio
            winsound.Beep(523, 100) # C5
            winsound.Beep(659, 100) # E5
            winsound.Beep(784, 100) # G5
            winsound.Beep(1046, 300)# C6
        elif sound_type == 'lose':
            # Sad descent
            winsound.Beep(500, 200)
            winsound.Beep(400, 200)
            winsound.Beep(300, 400)
    except:
        pass # Fail silently if sound HW issue

def my_len(seq):
    c = 0
    for _ in seq:
        c += 1
    return c

def my_in(item, seq):
    for x in seq:
        if x == item:
            return True
    return False

def my_not_in(item, seq):
    return not my_in(item, seq)

def my_strip(s):
    length = my_len(s)
    if length == 0:
        return ""
    start = 0
    while start < length:
        c = s[start]
        if c != ' ' and c != '\n':
            break
        start += 1
    end = length - 1
    while end >= start:
        c = s[end]
        if c != ' ' and c != '\n':
            break
        end -= 1
    res = ""
    i = start
    while i <= end:
        res += s[i]
        i += 1
    return res

def my_split(s, delim):
    res = []
    curr = ""
    for char in s:
        if char == delim:
            res = res + [curr] 
            curr = ""
        else:
            curr += char
    res = res + [curr]
    return res

def my_append(lst, item):
    return lst + [item]

def my_pop(lst, index=-1):
    """
    Removes item at index and returns (item, new_list).
    Note: Since we can't mutate list in place easily without pop/del,
    we return a new list.
    """
    length = my_len(lst)
    if length == 0:
        return None, lst
    
    if index < 0:
        index = length + index
        
    if index < 0 or index >= length:
        return None, lst
        
    item = lst[index]
    new_lst = []
    for i in range(length):
        if i != index:
            new_lst = new_lst + [lst[i]]
            
    return item, new_lst

def get_msg(key):
    return STRINGS[CURRENT_LANG].get(key, key)

def set_lang(lang):
    global CURRENT_LANG
    if lang == 'ES' or lang == 'EN':
        CURRENT_LANG = lang

def read_file_lines(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            stripped = my_strip(line)
            if my_len(stripped) > 0:
                lines = my_append(lines, stripped)
        return lines

def write_file_lines(filepath, lines):
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(str(line) + "\n")

def append_file_line(filepath, line):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(str(line) + "\n")
