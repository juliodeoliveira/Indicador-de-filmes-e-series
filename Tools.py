
def CreateFile(name):
    try:
        n = open(name, "wt+")
        n.close()
    except:
        print("Something just failed")

    else:
        print(f"File with name: {name} have been created.")


def FileExists(name):
    try:
        n = open(name, "rt")
        
    except FileNotFoundError:
        return False

    else:
        return True

def WriteFile(file_name, write):
    try:
        n = open(file_name, "wt")
    except:
        print("An error occoured.")
    else:
        try:
            n.write(write)
        except:
            print("Error when I try to write in archive")
        

def ReadFile(name):
    try:
        n = open(name, "r")
    except:
        print("A error occoured when I try to open the file.")

    else:
        for line in n:
            #dice = line.split(";")
            #dice[1] = dice[1].replace("\n","")
            return f"{line}"
    finally:
        n.close()
