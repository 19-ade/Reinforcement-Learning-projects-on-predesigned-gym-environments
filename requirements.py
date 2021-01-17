import os
import subprocess
import sys


def install(package):
    os.system("pip install " + str(package))
    reqs = subprocess.check_output([sys.executable, "-m", "pip", "show", str(package)])

    print(str(reqs) + "\n")
    print("Installed " + package.upper() + "\n")


install("requests")
install("beautifulsoup4")
install("cryptography")
install("selenium")
install("webdriver_manager")
install("telegram")
install("chatterbot")
install("chatterbot-corpus")