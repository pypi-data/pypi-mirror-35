import re

def remove_no_digit(s:str):
    return int(re.sub("\D","",s))