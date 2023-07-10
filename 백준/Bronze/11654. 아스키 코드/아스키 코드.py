import sys
W = input()

if type(W) == str:
    print(ord(W))
elif type(W) == int:
    print(chr(W))