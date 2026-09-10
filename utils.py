
def load_keyboard_patterns(filepath):
    passwords=set()
    try:
        with open(filepath,"r",encoding="utf-8") as dosya:
            for satir in dosya:
                passwords.add(satir.strip().lower())
        return passwords         
    except:
        return set() #boş döndürecek.
def has_keyboard_pattern(password, patterns):
    lower_password=password.lower()
    for i in patterns:
        if password in patterns:
            return True
    return False
    
