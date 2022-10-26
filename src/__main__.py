print("____-menu_____")
print("Enter directory")
  
dir = str(input())
# dir = "data/test_1dirctory"
  
if dir != None: 
    from builder import get_treaties_from_dir
    try:
        out = get_treaties_from_dir(dir)
        print(out)
    except:
        print('unable to get treaties')