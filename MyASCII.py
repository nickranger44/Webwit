import random

# All of the scripts possible ASCII art
ascii_header1 = """'|| '||'  '|'         '||                   ||    .   
 '|. '|.  .'    ....   || ...  ... ... ... ...  .||.  
  ||  ||  |   .|...||  ||'  ||  ||  ||  |   ||   ||   
   ||| |||    ||       ||    |   ||| |||    ||   ||   
    |   |      '|...'  '|...'     |   |    .||.  '|.' 
    
Created by: Nick Lueth"""

ascii_header2 = """ _    _  ____  ____  _    _  ____  ____ 
( \/\/ )( ___)(  _ \( \/\/ )(_  _)(_  _)
 )    (  )__)  ) _ < )    (  _)(_   )(  
(__/\__)(____)(____/(__/\__)(____) (__) 

Created by: Nick Lueth"""

ascii_header3 = """ _    _      _             _ _   
| |  | |    | |           (_) |  
| |  | | ___| |____      ___| |_ 
| |/\| |/ _ \ '_ \ \ /\ / / | __|
\  /\  /  __/ |_) \ V  V /| | |_ 
 \/  \/ \___|_.__/ \_/\_/ |_|\__|

Created by: Nick Lueth"""

ascii_header4 = """ __      __      ___.          .__  __   
/  \    /  \ ____\_ |____  _  _|__|/  |_ 
\   \/\/   // __ \| __ \ \/ \/ /  \   __\\
 \        /\  ___/| \_\ \     /|  ||  |  
  \__/\  /  \___  >___  /\/\_/ |__||__|  
       \/       \/    \/                 

Created by: Nick Lueth"""

ascii_header5 = """ _       __     __            _ __ 
| |     / /__  / /_ _      __(_) /_
| | /| / / _ \/ __ \ | /| / / / __/
| |/ |/ /  __/ /_/ / |/ |/ / / /_  
|__/|__/\___/_.___/|__/|__/_/\__/  

Created by: Nick Lueth"""

ascii_header6 = """ ____ ____ ____ ____ ____ ____ 
||W |||e |||b |||w |||i |||t ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|

Created by: Nick Lueth"""

ascii_header7 = """___       __    ______           __________ 
__ |     / /_______  /____      ____(_)_  /_
__ | /| / /_  _ \_  __ \_ | /| / /_  /_  __/
__ |/ |/ / /  __/  /_/ /_ |/ |/ /_  / / /_  
____/|__/  \___//_.___/____/|__/ /_/  \__/  

Created by: Nick Lueth"""

ascii_header8 = """__        __   _             _ _   
\ \      / /__| |____      _(_) |_ 
 \ \ /\ / / _ \ '_ \ \ /\ / / | __|
  \ V  V /  __/ |_) \ V  V /| | |_ 
   \_/\_/ \___|_.__/ \_/\_/ |_|\__|

Created by: Nick Lueth"""

ascii_header9 = """||   / |  / /                                           
||  /  | / /  ___     / __                  ( ) __  ___ 
|| / /||/ / //___) ) //   ) ) //  / /  / / / /   / /    
||/ / |  / //       //   / / //  / /  / / / /   / /     
|  /  | / ((____   ((___/ / ((__( (__/ / / /   / /     

Created by: Nick Lueth"""

# List to manage all ASCII headers and to be able to choose one from random in this list
headers = [ascii_header1, ascii_header2, ascii_header3, ascii_header4, ascii_header5, ascii_header6, ascii_header7,
           ascii_header8, ascii_header9]


def random_ascii():
    """
    This function chooses an ascii art to display randomly.
    :return: (string) header
    """
    # Generate a random number between 0 and the length of the headers list minus one
    index = random.randint(0, len(headers)-1)
    # Return the corresponding ASCII header
    return headers[index]
