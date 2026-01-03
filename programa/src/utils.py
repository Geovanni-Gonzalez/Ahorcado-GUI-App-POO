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

# Colors (Modern Flat Design)
COLORS = {
    'BG_MAIN': '#F5F7FA',       # Light Blue-Gray for background
    'BG_GAME': '#FFFFFF',       # White for game area/cards
    'BG_CARD': '#FFFFFF',
    'TEXT': '#2C3E50',          # Dark Blue-Gray for main text
    'TEXT_LIGHT': '#7F8C8D',    # Grey for secondary text
    'HIGHLIGHT': '#3498DB',     # Bright Blue (Primary)
    'HIGHLIGHT_DARK': '#2980B9',# Darker blue for active state
    'ERROR': '#E74C3C',         # Red
    'SUCCESS': '#2ECC71',       # Green
    'ACCENT': '#F1C40F',        # Yellow/Orange for hints
    'BTN_BG': '#34495E',        # Dark Grey for secondary buttons
    'BTN_FG': '#ECF0F1',        # White text
    'BTN_PRIMARY': '#3498DB'
}

# Fonts
FONTS = {
    'TITLE': ("Helvetica", 28, "bold"),
    'HEADER': ("Helvetica", 18, "bold"),
    'BODY': ("Helvetica", 12),
    'BODY_BOLD': ("Helvetica", 12, "bold"),
    'MONO': ("Consolas", 24, "bold"), # For the secret word
    'SMALL': ("Helvetica", 10)
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
def play_sound(sound_type):
    """
    Plays a system sound based on type.
    Types: 'click', 'correct', 'error', 'win', 'lose'
    """
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
