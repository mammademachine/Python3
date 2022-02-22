import random

feet_in_mile = 5280
metars_in_km  = 1000
starcarft_2_chars = ["Nova","Jim Raynor","Zeratul","Tassadar"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1, num)

# use 30-pip-test for actual coding