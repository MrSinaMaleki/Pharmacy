from os import system as terminal, name as os_name


def clear():
    terminal("cls" if os_name == "nt" else "clear")


def banner(title: str):
    clear()
    print("_" * 40, f"\u001b[38;5;4m{title.title().center(40)}\u001b[0m", "=" * 40, sep="\n")
