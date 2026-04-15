# ╔═══════════════════════════════════════════════════════════╗
# ║                                                           ║
# ║   ███╗   ██╗ ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗   ║
# ║   ████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝   ║
# ║   ██╔██╗ ██║██║   ██║██████╔╝██║   ██║██║  ██║ ╚████╔╝    ║
# ║   ██║╚██╗██║██║   ██║██╔══██╗██║   ██║██║  ██║  ╚██╔╝     ║
# ║   ██║ ╚████║╚██████╔╝██████╔╝╚██████╔╝██████╔╝   ██║      ║
# ║   ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝      ║
# ║                                                           ║
# ║            [Data Sorter - Clean the mess up!]             ║
# ║                                                           ║
# ╚═══════════════════════════════════════════════════════════╝
# Nobody's Data Sorter (NobodyDS) 
# A comprehensive utility tool to organize and sort files in a specified directory or drive based on their types.


import os
import shutil
import time


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def cleaner():
    def print_banner():
        print(f"""{Colors.BOLD}{Colors.MAGENTA}
    ╔════════════════════════════════════════════╗
    ║   Nobody's Data Sorter (NobodyDS)          ║
    ║   v1.0 - Data Sorter - Clean the mess up!  ║
    ╚════════════════════════════════════════════╝
    {Colors.RESET}""")

    def help():
        print(f"""{Colors.RESET}
Here is a list of commands you can use:
        1. open - opens the directory you want to sort
        2. check - checks the directory path you entered
        3. sort - sorts the files into folders
        4. clear - clears the terminal
        5. help - command explanation and help

usage:

    open    before using 'sort', you need to use 'open' to specify the directory you want to sort
    check   checks the directory path you entered, make sure it's correct before sorting
    sort    sorts the files in the directory into folders based on their types
    clear   clears the terminal and shows the menu again
    help    shows this help message

attention:

    Follow the commands chronologically!
    check does create new folders or use your folder if you have them:
    Images, Documents, Videos, Audio, 3D, Zip, ISO, exe, Txt, Coding
    If you have files with the same name as the ones being sorted, they will be skipped

Supported file types and their corresponding folders:

    Images:    .jpg, .png, .gif, .webp, .bmp, .svg, .tiff, .ico
    Documents: .doc, .docx, .pdf
    Videos:    .mp4, .avi, .mkv
    Audio:     .mp3, .wav, .flac
    3D:        .obj, .fbx, .blend, .stl, .stp, .igs, .3mf
    Zip:       .zip, .rar, .7z, .gz, .tar, .bz2
    ISO:       .iso, .img
    exe:       .exe, .msi, .bat, .sh
    Txt:       .txt, .csv, .log, .md, .json, .xml
    Coding:    .py, .js, .html, .css, .java, .cpp, .c, .cs, .rb, .php, .go, .rs, .swift, .kt, .ts, .tsx, .jsx, .jar, .dll, .so, .dylib

    Found a bug? Have a suggestion? Want to contribute? Visit the GitHub repository:
    https://github.com/Nobody-OS/Data-sorter/
""")

    def menu():
        print_banner()
        print(f"""{Colors.CYAN}Here is a list of commands you can use:
            1. open - opens the directory you want to sort
            2. check - checks the directory path you entered
            3. sort - sorts the files into folders
            4. clear - clears the terminal
            5. help - command explanation and help{Colors.RESET}""")

    directory = None
    sorting = False

    menu()

    while True:
        try:
            command = input(f"\n{Colors.BLUE}Enter a command:{Colors.RESET} ").lower()
        except KeyboardInterrupt:
            if sorting:
                print(f"\n{Colors.YELLOW}Sorting in progress. Please wait...{Colors.RESET}")
                time.sleep(1)
                continue
            else:
                print(f"\n{Colors.RED}CTRL + C pressed. Interrupted by user{Colors.RESET}")
                time.sleep(1)
                break

        if command == "open":
            directory = input("Enter the directory you want to sort: ")

            if os.path.exists(directory):
                print(f"Directory {Colors.GREEN}{directory}{Colors.RESET} opened successfully")
            else:
                print(f"Directory {Colors.RED}{directory}{Colors.RESET} does not exist")
                directory = None

        elif command == "clear":
            clear()
            menu()

        elif command == "help":
            help()

        elif command == "check":
            if directory is None:
                print("You need to use 'open' first")
            elif os.path.exists(directory):
                print("Directory path is valid")
                print(f"Current directory: {Colors.GREEN}{directory}{Colors.RESET}")
            else:
                print(f"Directory {Colors.RED}{directory}{Colors.RESET} path is invalid")

        elif command == "sort":
            moved = 0

            if directory is None:
                print("You need to use 'open' first")
                continue

            sorting = True

            FOLDERS = ["Images", "Documents", "Videos", "Audio", "3D", "Zip", "ISO", "exe", "Txt", "Coding"]

            for folder in FOLDERS:
                path = os.path.join(directory, folder)
                if not os.path.exists(path):
                    os.makedirs(path)

            for filename in os.listdir(directory):
                if filename in FOLDERS:
                    continue

                old_path = os.path.join(directory, filename)

                if not os.path.isfile(old_path):
                    continue

                name = filename.lower()

                if name.endswith((".jpg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff", ".ico")):
                    new_path = os.path.join(directory, "Images", filename)

                elif name.endswith((".doc", ".docx", ".pdf")):
                    new_path = os.path.join(directory, "Documents", filename)

                elif name.endswith((".mp4", ".avi", ".mkv")):
                    new_path = os.path.join(directory, "Videos", filename)

                elif name.endswith((".mp3", ".wav", ".flac")):
                    new_path = os.path.join(directory, "Audio", filename)

                elif name.endswith((".obj", ".fbx", ".blend", ".stl", ".stp", ".igs", ".3mf")):
                    new_path = os.path.join(directory, "3D", filename)

                elif name.endswith((".zip", ".rar", ".7z", ".gz", ".tar", ".bz2")):
                    new_path = os.path.join(directory, "Zip", filename)

                elif name.endswith((".iso", ".img")):
                    new_path = os.path.join(directory, "ISO", filename)

                elif name.endswith((".exe", ".msi", ".bat", ".sh")):
                    new_path = os.path.join(directory, "exe", filename)

                elif name.endswith((".txt", ".csv", ".log", ".md", ".json", ".xml")):
                    new_path = os.path.join(directory, "Txt", filename)

                elif name.endswith((".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".cs", ".rb", ".php", ".go", ".rs", ".swift", ".kt", ".ts", ".tsx", ".jsx", ".jar", ".dll", ".so", ".dylib")):
                    new_path = os.path.join(directory, "Coding", filename)

                else:
                    continue

                if os.path.exists(new_path):
                    print(f"Skipped (already exists): {filename}")
                else:
                    shutil.move(old_path, new_path)
                    moved += 1
                    print(f"Moved: {filename}")

            print("Sorting complete")
            print(f"Total files moved: {moved}")

            sorting = False

            time.sleep(2)
            clear()
            menu()

        else:
            print(f"{Colors.RED}Invalid command{Colors.RESET}")


if __name__ == "__main__":
    cleaner()