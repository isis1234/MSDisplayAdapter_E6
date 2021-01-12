import subprocess, sys
import keyboard

print("Start MSDiaplayAdapter_E6_script.bat ...")

print('%windir%\explorer.exe ms-settings-connectabledevices:devicediscovery')
subprocess.call('%windir%\explorer.exe ms-settings-connectabledevices:devicediscovery', shell=True)

subprocess.call('@ping 127.0.0.1 -n 2 -w 5000 > nul', shell=True)

keyboard.press_and_release('tab')
keyboard.press_and_release('shift+tab')
keyboard.press_and_release('enter')

subprocess.call('@ping 127.0.0.1 -n 2 -w 1000 > nul', shell=True)

keyboard.write('MSDisplayAdapter_E6')
subprocess.call('@ping 127.0.0.1 -n 2 -w 1000 > nul', shell=True)

keyboard.press_and_release('tab')
keyboard.press_and_release('enter')
print("END MSDiaplayAdapter_E6_script.bat ...")
