from termcolor import colored

text = colored("hello world", color = "magenta", on_color="on_blue", attrs=["blink"])
print(text)