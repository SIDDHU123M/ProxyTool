import os

def run_script(script_name):
    os.system(f"python {script_name}.py")

print("Select a script to run:")
print("1. Scraper")
print("2. Checker")
user_choice = input("Enter your choice (1/2): ")

if user_choice == "1":
    run_script("scraper")
elif user_choice == "2":
    run_script("checker")
else:
    print("Invalid choice. Please enter 1 or 2.")
