import re

def remove_non_digit(s:str):
    return int(re.sub("\D","",s))