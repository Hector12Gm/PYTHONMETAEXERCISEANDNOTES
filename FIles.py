
try: 
    with open('snewFile.txt',mode="a") as file:
        file.writelines(["\nThis  a new file created","\nLines"])
except FileNotFoundError as e:
    print('ERROR',e)