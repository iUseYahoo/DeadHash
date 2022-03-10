import hashlib
import os
from columnar import columnar
from time import sleep

def clear():
    os.system("cls")

class hashing:
    def md5hashing(rawhash):
        md5hash = hashlib.md5(rawhash.encode("utf-8"))
        print(md5hash.hexdigest())

    def sha1hashing(rawhash):
        sha1hash = hashlib.sha1(rawhash.encode("utf-8"))
        print(sha1hash.hexdigest())

    def sha512hashing(rawhash):
        sha512hash = hashlib.sha512(rawhash.encode("utf-8"))
        print(sha512hash.hexdigest())

    def sha256hashing(rawhash):
        sha256hash = hashlib.sha256(rawhash.encode("utf-8"))
        print(sha256hash.hexdigest())

def main():
    while True:
        title = ["Number", "Algorithm"]
        data = [
            ["1", "MD5"],
            ["2", "SHA1"],
            ["3", "SHA512"],
            ["4", "SHA256"],
        ]
        table = columnar(data, title, no_borders=True)
        print(table + "\n")

        hashnum = int(input("Pick an Algorithm via its number: "))
        rawhash = input("Enter something to encrypt: ")

        if hashnum == 1:
            hashing.md5hashing(rawhash)
        elif hashnum == 2:
            hashing.sha1hashing(rawhash)
        elif hashnum == 3:
            hashing.sha512hashing(rawhash)
        elif hashnum == 4:
            hashing.sha256hashing(rawhash)
        else:
            print(f"{hashnum} is not a valid option.")
            sleep(3)
            clear()

if __name__ == "__main__":
    clear()
    main()
