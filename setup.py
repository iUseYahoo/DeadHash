import os

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print("\n\n-- Installing Columnar --\n\n")
os.system("pip install columnar")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

print("\n\n-- Installed Columnar --\n\n")
