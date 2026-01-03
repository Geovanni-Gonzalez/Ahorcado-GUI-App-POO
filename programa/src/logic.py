from .utils import *
import random
import datetime

def login(password):
    lines = read_file_lines(FILES['ACCESO'])
    if my_len(lines) > 0:
        real_pass = my_strip(lines[0])
        return real_pass == password
    # Fallback if file empty/missing for safety, or return False. 
    # Requirement says access code must be in file.
    return False

def get_next_id(lines):
    if not lines:
        return 1
    ids = []
    for line in lines:
        try:
            parts = my_split(line, ',')
            ids = my_append(ids, int(my_strip(parts[0])))
        except ValueError:
            continue
    current_max = 0
    for i in ids:
        if i > current_max:
            current_max = i
    return current_max + 1

def add_entry(filepath, text):
    lines = read_file_lines(filepath)
    text = text.upper()
    # Check dup
    for line in lines:
        parts = my_split(line, ',')
        if my_len(parts) > 1 and my_strip(parts[1]).upper() == text:
            return False # Exists
            
    nid = get_next_id(lines)
    append_file_line(filepath, f"{nid}, {text}")
    return True

def delete_entry(filepath, target_id, is_phrase=False):
    # Check usage
    games = read_file_lines(FILES['JUEGO'])
    
    # Get text first
    lines = read_file_lines(filepath)
    target_text = ""
    found_line = False
    
    for line in lines:
        parts = my_split(line, ',')
        if int(my_strip(parts[0])) == target_id:
            target_text = my_strip(parts[1]).upper()
            found_line = True
            break
            
    if not found_line:
        return "NOT_FOUND" 
        
    for game in games:
        parts = my_split(game, ',')
        if my_len(parts) >= 4:
            if my_strip(parts[3]).upper() == target_text:
                return "USED"
                
    # Delete
    new_lines = []
    for line in lines:
        parts = my_split(line, ',')
        if int(my_strip(parts[0])) != target_id:
            new_lines = my_append(new_lines, line)
            
    write_file_lines(filepath, new_lines)
    return "OK"

def modify_entry(filepath, target_id, new_text):
    lines = read_file_lines(filepath)
    new_text = new_text.upper()
    
    # Check dup
    for line in lines:
        parts = my_split(line, ',')
        if int(my_strip(parts[0])) != target_id:
            if my_len(parts) > 1 and my_strip(parts[1]).upper() == new_text:
                return "EXISTS"
    
    new_lines = []
    found = False
    for line in lines:
        parts = my_split(line, ',')
        pid = int(my_strip(parts[0]))
        if pid == target_id:
            new_lines = my_append(new_lines, f"{pid}, {new_text}")
            found = True
        else:
            new_lines = my_append(new_lines, line)
            
    if not found:
        return "NOT_FOUND"
        
    write_file_lines(filepath, new_lines)
    return "OK"

def get_all_entries(filepath):
    # Return list of (id, text)
    lines = read_file_lines(filepath)
    result = []
    for line in lines:
        parts = my_split(line, ',')
        if my_len(parts) > 1:
            result = my_append(result, (int(my_strip(parts[0])), my_strip(parts[1])))
    return result

def save_finished_game(player, mode, word, attempts, used_letters, result, start_time, end_time):
    # Format: Code, Player, Mode, Word, Attempts, Letters, Result, Date, Time, Duration
    
    duration = end_time - start_time
    # Format duration HH:MM:SS manually roughly
    seconds = int(duration.total_seconds())
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    duration_str = f"{h:02d}:{m:02d}:{s:02d}"
    
    date_str = start_time.strftime("%d/%m/%Y")
    time_str = start_time.strftime("%I:%M %p").lower()
    
    games = read_file_lines(FILES['JUEGO'])
    nid = get_next_id(games)
    
    formatted_letters = "["
    c = 0
    l_len = my_len(used_letters)
    for l in used_letters:
        formatted_letters += '"' + l + '"'
        if c < l_len - 1:
             formatted_letters += ", "
        c += 1
    formatted_letters += "]"
    
    line = f"{nid}, {player}, {mode}, {word}, {attempts}, {formatted_letters}, {result}, {date_str}, {time_str}, {duration_str}"
    append_file_line(FILES['JUEGO'], line)
