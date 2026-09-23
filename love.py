import time
import os

heart = [
"  **   ***  ",
" ****** ****** ",
" ************* ",
"  ***********  ",
"    *********   ",
"      *****      ",
"        ***       ",
"         *        "
]

for i in range(5):
    os.system("cls" if os.name == "nt" else "clear")
    for line in heart:
        print(line)
    time.sleep(0.5)

print("\nWill you be the reason my heart beats? ❤️")
