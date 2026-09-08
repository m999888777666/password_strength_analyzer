from entropy import calculate_entropy, get_pool_size
from dictionary_checker import load_password_list, is_dictionary_password
from leetspeak import check_advanced_password
from crack_time import format_crack_time,calculate_crack_time_seconds
wordlist = load_password_list("data/common_passwords.txt")
def analyze_password(password):
    if check_advanced_password(password,wordlist):
        return "very weak"
    elif calculate_entropy(password)<40:
        return "weak"
    elif calculate_entropy(password)>=40 and calculate_entropy(password)<60:
        return "medium"
    elif calculate_entropy(password)>=60:
        return "strong"

def final_analyze(password):
    entropy=calculate_entropy(password)
    sec=calculate_crack_time_seconds(entropy,10**10)
    rating=analyze_password(password)
    return {
    "password": password,
    "is_dictionary": check_advanced_password(password,wordlist),
    "pool_size": get_pool_size(password),
    "entropy": calculate_entropy(password),
    "crack_seconds": sec,
    "crack_time_readable": format_crack_time(sec),
    "rating":rating
}
