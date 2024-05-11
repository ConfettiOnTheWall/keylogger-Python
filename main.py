import os
import time
import shutil

while True:
    print("""
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                            
                                                                                                            
    """)
    print("[1] List last Keylogs.txt")
    print("[2] Activate Keylogger")
    print("[3] DELETE ALL LOGS")
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
                opt = str(input("[0] restart program \n[enter] close program\n>> "))
                if opt == "":
                    break
                
            case "2":
                print("[2] Activate Keylogger [selected]")
                print("")
                pathK = str(input("Path of the Keylogger \n[1] Use common path\n[2] Inform the path where the keylogger is located\n>>> "))
                match pathK:
                    case "1":
                        print("")
                        print("Using normal path")
                        os.popen("python clientbuild.py")
                        try:
                            input("Use CTRL + C to kill keylogger")
                        except KeyboardInterrupt:
                            break
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
            case _:
                print("!! Sorry this is not a Option !!")
                time.sleep(2)
                os.system('cls')
    except KeyboardInterrupt:
        print("")
        print("invalid input, closing")
        break