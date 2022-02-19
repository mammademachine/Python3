is_male = False
is_tall = True
if is_male and is_tall:
    print("Yes you are man or tall or both")
elif is_male and not(is_tall):
    print("You are short man")
elif not(is_male) and is_tall:
    print("You are Tall non man")    
else:
    print("No you are not nor man nor tall")
