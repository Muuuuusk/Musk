import os

def print_banner():
    os.system('clear')  # Clears the terminal screen
    print("\033[1;32m")
    print("""
  
═══════════════════════════════════════════════════║           
║  ███╗░░░███╗██╗░░░██╗░██████╗██╗░░██╗  PREMIUM   ║
║  ████╗░████║██║░░░██║██╔════╝██║░██╔╝  TERMUX    ║
║  ██╔████╔██║██║░░░██║╚█████╗░█████═╝░  TOOL      ║
║  ██║╚██╔╝██║██║░░░██║░╚═══██╗██╔═██╗░  BASED ON. ║
║  ██║░╚═╝░██║╚██████╔╝██████╔╝██║░╚██╗  EDUCATION ║
║  ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░░╚═╝  PURPOSE   ║
║══════════════════════════════❝ V:0.01❞═══❛2024❜══║            
 
║――――――――――――――――――――――――――――――――――――――――――――――――║
║ [•] Developer      <>    MUHAMMAD ABU HURAYRAH ║
║ [•] Tools          <>    BASIC TO ADVANCE  [BD]║ 
║ [•] Type           <>    PREMIUM               ║
║――――――――――――――――――――――――――――――――――――――――――――――――║   
""")
    print("\033[0m")

def basic_setup():
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pkg install nano")

def full_setup():
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pkg install nano")
    os.system("pkg install wget")
    os.system("pkg install curl")

def install_kali():
    os.system("pkg update && pkg upgrade")
    os.system("pkg install wget")
    os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh")
    os.system("bash kali.sh")

def set_username_header():
    username = input("\033[1;32mEnter your desired username: \033[0m")
    os.system(f'echo "\033[1;32mPS1=\'\[\033[1;32m\]{username}\[\033[0m\]:\[\033[1;34m\]\W\[\033[0m\]\$ \[\033[0m\]\'" > ~/.bashrc')

def main():
    print_banner()
    print("\033[1;32m1. Termux Basic Setup")
    print("2. Termux Full Setup")
    print("3. Install Kali Linux")
    print("4. Set Username Header in Termux")
    print("5. Exit")

    choice = input("\033[1;32mEnter your choice: \033[0m")

    if choice == '1':
        basic_setup()
    elif choice == '2':
        full_setup()
    elif choice == '3':
        install_kali()
    elif choice == '4':
        set_username_header()
    elif choice == '5':
        print("\033[1;32mExiting...\033[0m")
    else:
        print("\033[1;31mInvalid choice\033[0m")

if __name__ == "__main__":
    main()