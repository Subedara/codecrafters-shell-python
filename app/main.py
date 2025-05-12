import sys

import os

import shutil

def main():

    builtin = ["echo", "exit", "type"]

    while True:

        # Uncomment this block to pass the first stage

        sys.stdout.write("$ ")

        # Wait for user input

        command = input()

        splitCommand = command.split()

        if splitCommand[0] == "exit":

            sys.exit(0)

        elif splitCommand[0] == "echo":

            for i in range(1, len(splitCommand)):

                print(splitCommand[i], end=" ", sep=" ")

            print()

        elif splitCommand[0] == "type":

            if splitCommand[1] in builtin:

                print(f"{splitCommand[1]} is a shell builtin")

            elif path := shutil.which(splitCommand[1]):

                print(f"{splitCommand[1]} is {path}")

            else:

                print(f"{splitCommand[1]}: not found")

        elif shutil.which(splitCommand[0]) != None:

            os.system(f"{splitCommand[0]} {' '.join(splitCommand[1:])}")

        else:

            print(f"{command}: command not found")

if __name__ == "__main__":

    main()