def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("Your color must be a string")
    if type(text) is not str:
        raise TypeError("Your text must be a string")
    if color not in colors:
        raise ValueError("that is not a color")
    print(f"printed {text} in a {color}")

print(colorize("green", "yellow")) 
print(colorize("purple", "red"))

