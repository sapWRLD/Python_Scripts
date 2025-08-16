import os
import subprocess
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_path):
    if script_path.endswith(".py"):
        subprocess.run([sys.executable, script_path])
    else:
        print(f"Unsupported script type: {script_path}")

def main():
    python_scripts = [
        ("Run Color Picker", "Color_clicker/autoclicker.py"),
        ("Run RGB Finder", "RGB_finder/Rgb_Finder.py"),
        ("Run Type Spammer", "Type_spammer/spammer.py"),
        ("Run Speech to Text", "Speech_to_text/Speech_to_text.py")
    ]

    while True:
        clear_screen()
        print("=" * 30)
        print("       Script Menu")
        print("=" * 30)

        for i, (name, _) in enumerate(python_scripts, start=1):
            print(f"{i}. {name}")
        print(f"{len(python_scripts) + 1}. Exit")

        choice = input("Choose an option: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(python_scripts):
                _, path = python_scripts[choice - 1]
                run_script(path)
                input("\nPress Enter to return to the menu...")
            elif choice == len(python_scripts) + 1:
                break
            else:
                input("Invalid choice! Press Enter to try again...")
        else:
            input("Invalid choice! Press Enter to try again...")

if __name__ == "__main__":
    main()
 