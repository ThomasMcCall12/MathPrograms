from time import *
from math import * 
def calc_area():
    print("-----Welcome To The Area Calculator-----")
    r = float(input("Please enter the radius of the circle: "))
    r2 = r*r
    area = pi*r2
    return area

def calc_circum():
    print("-----Welcome To The Circumfrence Calculator-----")
    dknown = str(input("Do you know the diamiter: ")).lower()
    if dknown == 'yes':
        diam = float(input("Great! What is your diameter then!: "))
    else:
        r = float(input("No problem! We will just use the radius, please enter your radius: "))
        diam = r*2
    circum = diam*pi
    return(circum)

def calc_vol_cyl():
    print("Welcome to the volume of a cylinder calculator!")
    r = float(input("Firstly we need the radius of the cylinder: "))
    r2 = r*r
    height = float(input("Could you please provide us with the height aswell: "))
    volume = pi*r2*height
    return volume

def Main_Operation():
    print("Welcome to the wonderful maths system!")
    print("Your functions are as followed -")
    sleep(0.5)
    print("A - Area (of a circle) calculator")
    sleep(0.5)
    print("B - Circumfrence of a Circle Calculator")
    sleep(0.5)
    print("C - Volume of a cylinder calculator")
    sleep(0.5)
    print("D - Exit")
    sleep(0.5)
    doagain ="yes"
    while doagain == "yes":
        opt = str(input("Which would you like to run please enter your option as A,B,C or D: ")).lower()
        while opt !="a" and opt !="b" and opt!="c" and opt!="d":
            print("Sorry that was not an appropriate answer!")
            opt = str(input("Which would you like to run please enter your option as A,B,C or D: ")).lower()
        if opt == "a":
            i = calc_area()
            print("Calculating ...")
            sleep(2)
            print("--------------------")
            print("Your area is ...")
            print(i)
            doagain = str(input("Please enter yes to select another option: "))
        elif opt == "b":
            i = calc_circum()
            print("Calculating the circumfrence ...")
            sleep(2)
            print("--------------------")
            print("Your circumfrence is ...")
            print(i)
            doagain = str(input("Please enter yes to select another option: "))
        elif opt == "c":
            i = calc_vol_cyl()
            print("Calculating the volume... ")
            sleep(2)
            print("--------------------")
            print("Your volume is ...")
            print(i)
            
            doagain = str(input("Please enter yes to select another option: "))
        elif opt =="d":
            quit()
        else:
            doagain = "yes"
        
Main_Operation()       
    
