from os import system, name
from time import sleep
from sys import stdout


class Animate:
    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')

        else:
            _ = system('clear')

    @staticmethod
    def buffer():
        done = False
        while done == False:
            stdout.write('\rloading .')
            sleep(0.5)
            stdout.write('\rloading ..')
            sleep(0.5)
            stdout.write('\rloading ...')
            sleep(0.5)
            stdout.write('\rloading ....')
            sleep(0.5)
            done = True
        stdout.write('\r                  \n')
