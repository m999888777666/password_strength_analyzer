import string
leet_speak={'4':'a','3':'e','@':'a','0':'o','5':'s','1':'i','$':'s','7':'t'}
def decode_leetspeak(password):
    #bu kod fonksiyon içindeki password kelimesini dönüştürüyor.
    new_password=password.lower()
    for e,y in leet_speak.items():
        new_password=new_password.replace(e,y)
    return new_password
def password_list(filepath):
    passwords=set()
    with open(filepath,"r",encoding="utf-8") as dosya:
        for x in dosya:
            passwords.add(x.strip().lower())
    return passwords
def is_dictionary_password(password,password_set):
    lower_password=password.lower()
    if lower_password in password_set:
        return True
    else:
        return False
def check_advanced_password(password,password_set):
    if is_dictionary_password(password,password_set):
        return True
    else:
        new_password=decode_leetspeak(password)
        if is_dictionary_password(new_password,password_set):
            return True
        else:
            return False


