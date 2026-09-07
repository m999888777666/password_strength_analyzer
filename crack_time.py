from entropy import calculate_entropy
import math
#alttaki fonksiyonda saniye başına denenecek password sayısı 10 üzeri 10 olarak alındı.
def calculate_crack_time_seconds(entropy, guesses_per_second=10**10):
    if entropy<=0:
        return 0
    else:
        sec=2**(entropy-1)
        sec=sec/guesses_per_second
        return float(sec)
def format_crack_time(sec):
    if sec<1:
        return "instantly"
    elif sec<60:
        return f"{round(sec, 2)} seconds"
    elif sec<3600:
        return f"{round(sec / 60, 2)} minutes"
    elif sec<86400:
        return f"{round(sec / 3600, 2)} hours"
    elif sec<31536000:
        return f"{round(sec / 86400, 2)} days"
    elif sec>=31536000:
        return f"{round(sec / 31536000, 2)} years"

