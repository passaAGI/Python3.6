import keyboard
import os

print("***********")
print("**Program**")
print("***********")

A = ["A", ""]
B = ["B", ""]
C = ["C", ""]
selector = '\x1b'

print("|Options|")
print(A[0])
print(B[0])
print(C[0])
while not(keyboard.is_pressed('enter')):
    if keyboard.is_pressed('down') or keyboard.is_pressed('up'):
        os.system('cls')
        A[1] = selector
        print("|Options|")
        print(A[0], selector)
        print(B[0])
        print(C[0])
        while not(keyboard.is_pressed('enter')):
            if keyboard.is_pressed('up') and A[1] == selector:
                os.system('cls')
                A[1] = ""
                C[1] = selector
                print("|Options|")
                print(A[0])
                print(B[0])
                print(C[0], selector)
            elif keyboard.is_pressed('down') and A[1] == selector:
                os.system('cls')
                A[1] = ""
                B[1] = selector
                print("|Options|")
                print(A[0])
                print(B[0], selector)
                print(C[0])
            if keyboard.is_pressed('up') and B[1] == selector:
                os.system('cls')
                B[1] = ""
                A[1] = selector
                print("|Options|")
                print(A[0], selector)
                print(B[0])
                print(C[0])
            elif keyboard.is_pressed('down') and B[1] == selector:
                os.system('cls')
                B[1] = ""
                C[1] = selector
                print("|Options|")
                print(A[0])
                print(B[0])
                print(C[0], selector)
            if keyboard.is_pressed('up') and C[1] == selector:
                os.system('cls')
                C[1] = ""
                B[1] = selector
                print("|Options|")
                print(A[0])
                print(B[0], selector)
                print(C[0])
            elif keyboard.is_pressed('down') and C[1] == selector:
                os.system('cls')
                C[1] = ""
                A[1] = selector
                print("|Options|")
                print(A[0], selector)
                print(B[0])
                print(C[0])
