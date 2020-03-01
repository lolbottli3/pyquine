from pathlib import Path
import os


def main():
    x = 0
    Path("hacked.txt").touch()
    if os.path.exists("hacked.txt"):
        Path("hacked" + str(x) + ".txt").touch()
        x = x + 1


main()