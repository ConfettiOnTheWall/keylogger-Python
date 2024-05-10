import os
import time
import signal

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
    opt = int(input("Choose a option for your PyLogger: \n"))
    
    match opt:
        case 1:
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
            
        case 2:
            print("[2] Activate Keylogger [selected]")
            print("")
            pathK = int(input("Path of the Keylogger \n[1] Use common path\n[2] Inform the path where the keylogger is located\n>>> "))
            match pathK:
                case 1:
                    print("")
                    print("Using normal path")
                    print("USE CTRL + C to kill the keylogger")
                    os.popen("python clientbuild.py")
                case 2:
                    print("")
                    print("Please insert the path: ")
                    pathV = str(input("Paste here -> "))
                    Crun = "python " + pathV + "/clientbuild.py"
                    os.popen(Crun)
                    input("Use CTRL + C to kill keylogger")
                    
        case 3:
            print("[3] DELETE ALL LOGS [selected]")
        case _:
            print("!! Sorry this is not a Option !!")
            time.sleep(2)
            os.system('cls')