import time
import random
import colorama
from colorama import init

init(convert=True) #Allows the colors on Anaconda Terminal to work
colors = list(vars(colorama.Fore).values())

while True:
    time.sleep(0.5)
    print(
        " " * random.randint(0, 150)
        + f"{colorama.Style.BRIGHT} {random.choice(colors)}Happy {random.choice(colors)}Mother's {random.choice(colors)}Day!",
        end="",
    )
    print(
        " " * random.randint(0,150)
        + f"{colorama.Style.BRIGHT} {random.choice(colors)}Best {random.choice(colors)}Mom {random.choice(colors)}Ever!",
        end="",
    )

    print(" " * random.randint(0, 150) + f"{colorama.Style.BRIGHT}*", end="")
    print(" " * random.randint(0, 150) + f"{colorama.Style.BRIGHT}*")