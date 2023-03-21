import os

required_modules = ["pystyle", "colorama", "urllib.request", "sys", "bs4", "requests"]
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} not found. Installing now...")
        os.system(f"pip install {module}")
        __import__(module)

import requests, sys, datetime, urllib.request, platform, re
from colorama import Style, Fore, Back, init
from bs4 import BeautifulSoup

GB, YB, WB, IB = Back.GREEN, Back.YELLOW, Back.RED, Back.BLACK
g, c, y, r, b, w = Style.BRIGHT+Fore.GREEN, Style.BRIGHT+Fore.CYAN, Style.BRIGHT+Fore.YELLOW, Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.BLUE, Style.BRIGHT+Fore.LIGHTWHITE_EX

def cls():
    os.system('cls || clear')

def space():
    print("")

now = datetime.datetime.now()
dattt = now.strftime("%Y/%m/%d %H:%M:%S\n")
cls()
banner = f"""
{w}<{y}/{w}> {GB}{r}• Proxy Scrapper{Back.RESET}
{w}<{y}/{w}> {WB}{b}• Author : SIDDHU123M (GIT){Back.RESET}
{w}<{y}/{w}> {YB}{c}• Date and Time : {Back.RESET} {dattt}"""

def run_script(script_name):
    os.system(f"python {script_name}.py")

print("Select a script to run:")
print(f"{c}1. Scraper")
print(f"{c}2. Checker")
user_choice = input(f"{g}Enter your choice (1/2): ")

if user_choice == "1":
    run_script("scraper")
elif user_choice == "2":
    run_script("checker")
else:
    print("Invalid choice. Please enter 1 or 2.")
