import os
import platform

def is_platform_windows():
	return platform.system() == "Windows"
def is_platform_linux():
	return platform.system() == "Linux"

print(is_platform_windows())
print(is_platform_linux())


while True:
	if is_platform_windows():
		os.system("cls")
	elif is_platform_linux():
		os.system("clear")
	else:
		print("您好富...")
	os.system("python data/bot.py")
	
