

def load_password_list(filepath):
    passwords=set()
    with open(filepath,"r",encoding="utf-8") as dosya:
        for sat in dosya:
            passwords.add(sat.strip().lower())
    return passwords
def is_dictionary_password(password, password_set):
    lowered_password=password.lower()
    if lowered_password in password_set:
        return True
    else:
        return False

