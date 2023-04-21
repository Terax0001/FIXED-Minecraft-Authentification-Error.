from colorama import Back, Fore, Style, deinit, init
import shutil
import msvcrt as m
init()

print(Fore.MAGENTA + Style.NORMAL + 'Make Sure You Have The .minecraft Folder In Roaming. Type Enter To Continue')
m.getch()

shutil.move(r'C:\Windows\System32\drivers\etc\hosts.ics', r'C:\Users\pc\AppData\Roaming\.minecraft\hosts.ics')
