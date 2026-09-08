from analyzer import final_analyze
import time
BANNER=r"""
  ▄▄▄      ▄         ▄        ▄     ░▄           ▄▄       ▄▄        ▄         
▀▒█▀░█▄  ▄░▓▀▒░▄  ▄░▓ ▀█░▀ ▄░▓ ▀█░▀ ░░▓   ▓▄  ▄░▒▀▀██▄ ▀▀▓▀▓█▄  ▀▓▀▀▀▒█▄      
 ▄▒  ▓░▀ ▓▓█  ▓█░ ▀▓█▄ ▀   ▀▓█▄ ▀   ▒▓█   ▒█▒ ░▒▓  ▓█▒ ▄░▓  ▓░▀   ▄░  ▓█▌     
▒▓█░▀▀   ▒██▀░▓█░   ▄ ▀▒▄    ▄ ▀▒▄  ▓██ ░▄▓▒▓ ▓▓█  ▒█░ ▒▓█▄▀▒▄   ▀░▓  ▒▓█     
░█▒      ▓██  ░▀  ▄░▓▄ ▓░▀ ▄░▓▄ ▓░▀ ██▓▀  ▀░░ ▀░█▄▄█░▀ ▓██▀ ▓█░  ▐▒▓ ▄▓▒▀     
 ▀░      █▀        ▀ ▀▀▀    ▀ ▀▀▀   ░▀      ▀    ▀▀    ▀░█  █▀    ░▒▀▀        
                                                         ▀  ▀                 
   ▄              ▄▄       ▄▄█▄     ▄   ▄▓   ▄░▀▄▄▄▄              ▄     
▄░▓ ▀█░▀ ▀░▓█▀ ▀▀▓▀▓█▄   ▄░▀ ▓▒░▀ ▄░▓▄ ░▓█ ▄░▓  ▓░▀  ▀░▓█▀  ▄▓  ▄▒▓     
▀▓█▄ ▀    ▒█▒  ▄░▓  ▓░▀ ▀░▓▄ ░▀   ░▓█▀░▒█▓ ▒▓█  ▀     ▒█▒  ▒▓█  ▒▓█     
  ▄ ▀▒▄   ▓█░  ▒▓█▄▀▒▄  ▐▓█  ▄    ░██  ▓▒▓ ▓██ ▀▒▓█▀  ▓█░  ▓██▒░▓██     
▄░▓▄ ▓░▀  █░▀  ▓██▀ ▓█░  ▀█▄▀▓░▀   ▀░  ░░▒ ▀▒█▄░▓█▀   █░▀  ██░  ░██     
 ▀ ▀▀▀    ▀    ▀░█  █▀       ▀          ▀░      ░▀    ▀    ░▀    ▀░     
                 ▀  ▀                                                   
  ▄        ▄   ▄▓   ▄      ▒▄         ▄▒    ▄             ▄▄█▄      ▄▄   
▄░▓▀▒░▄  ▄░▓▄ ░▓█ ▄░▓▀▒░▄  ░▒▓       ░▒▓  ▄░▓ ▀░▓▀▀▓▒▄  ▄░▀ ▓▒░▀ ▀▀▓▀▓█▄ 
▓▓█  ▓█░ ░▓█▀░▒█▓ ▓▓█  ▓█░ ▒▓█  ▄     ▀▀▀▄▒▓▒   ▀ ▄▓▀  ▀░▓▄ ░▀   ▄░▓  ▓░▀
▒██▀░▓█░ ░██  ▓▒▓ ▒██▀░▓█░ ▓██  ▒█▄    ▄  ▓█░  ▄▄▀ ▄   ▐▓█  ▄    ▒▓█▄▀▒▄ 
▓██  ░▀   ▀░  ░░▒ ▓██  ░▀  ▀███▄▀██▄ ▄░▓ ▄▒░▀ ░▒▓ ▄▒░▄  ▀█▄▀▓░▀  ▓██▀ ▓█░
█▀             ▀░ █▀          ▀▀▀▀    ▀▀▀▀     ▀▀▀ ▀▀       ▀    ▀░█  █▀ 
                                                                   ▀  ▀  
"""

while True:
    print("\n\n")
    print(BANNER)
    user_input=input("Enter password, if you want to exit, enter q: ").strip()
    if user_input=='q' or user_input=='Q':
        break
    if not user_input:
        print("Password cannot be empty. Please enter valid password.")
        continue
    result=final_analyze(user_input)
    print("------------------------   REPORT   ------------------------")
    print("password:                         {password}".format(**result))
    print("rating:                           {rating}".format(**result))
    print("entropy:                          {entropy}".format(**result))
    print("character pool size:              {pool_size}".format(**result))
    print("crack time:                       {crack_time_readable}".format(**result))
    print("-------------------   END OF THE REPORT   -------------------")
    print("\nnow lets search if the password {} is in dictionary...".format(user_input))
    time.sleep(3)
    if result["is_dictionary"]:
        print("\nFOUND IN DICTIONARY...OR..detected as a l337speak variant ;)")
        time.sleep(3)
    else:
        print("\nno worries")
        time.sleep(3)
