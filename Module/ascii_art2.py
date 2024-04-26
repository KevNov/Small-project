from pyfiglet import figlet_format
from termcolor import colored

valid_color = ("red", "blue", "green", "yellow", "white", "magenta", "cyan")

msg = input("what kind of text you trying to print?: ")
color = input("what colored did you want to used?: ")

if color not in valid_color:
    color = "white"

ascii_art = figlet_format(msg)
color_ascii = colored(ascii_art, color=color)
print(color_ascii)

