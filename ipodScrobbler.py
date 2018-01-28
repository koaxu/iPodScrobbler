import os
import sys
import string
import shutil
import subprocess
import signal
from constants import *


def main():
    # Kill any audio programs currently running
    print("Please close any media player programs before continuing - e.g. iTunes, MusicBee, foobar2000.")
    while True:
        bool1 = input("Are all media players closed? y/n: ")
        if bool1 == "y" or bool1 == "Y":
            break
        else:
            continue

    if os.path.ismount(iDrive) == False:
        print("iPod is not mounted")
        print("Exiting")
        sys.exit(1)

    if os.path.exists(pcDest) == True:
        print("Play Counts exists!")
    else:
        print("Play counts file doesn't exist")
        print("Exiting")
        sys.exit(2)

    if os.path.exists("{}\\Play Counts".format(copyDest)) == True:
        print("File already exists at destination: {}!".format(copyDest))
        boolPC = input("Delete existing file? y/n: ")
        if boolPC == "y" or boolPC == "Y":
            os.remove("{}\\Play Counts".format(copyDest))
            print("Play Counts file deleted!")
        else:
            print("Exiting")
            sys.exit(3)

    print("Moving Play Counts file to {}.....".format(copyDest))
    shutil.copy2(pcDest,copyDest)

    # Open qtScrob Program
    scrobOpen = subprocess.Popen(scrobDest)

    # Ask if scrobbling has completed
    while True:
        bool2 = input("Have you submitted the scrobbles in QTScrobler? y/n: ")
        if bool2 == "y" or bool1 == "Y":
            break
        else:
            continue
    scrobOpen.terminate()

    print("Moving Play Counts back to iPod......")

    shutil.move(copyDest + "\\Play Counts", pcDest.replace("Play Counts", ""))
    print("Moved!")

    # Ask user if iTunes should be opened
    while True:
        iBool = input("Do you wish for iTunes to be opened? y/n: ")
        if iBool == "Y" or iBool == "y":
            subprocess.Popen(iPath)
            break
        else:
            break

if __name__ == '__main__':
    main()
