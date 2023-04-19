import math

def Radius_Height():
    Radius = float(input("Please enter the radius of the cone: "))
    Height = float(input("Please enter the height of the cone: "))
    volume = (1/3) * math.pi * Radius**2 * Height
    return volume

if __name__ == '__main__':
    print(f"The volume is: {Radius_Height()} ")
