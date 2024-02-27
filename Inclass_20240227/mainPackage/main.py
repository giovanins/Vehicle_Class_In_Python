#main py
#add an import statment for vehicle class

from vehiclePackage.vehicleClass import *


if __name__ == "__main__":
    myCorvette = Vehicle("Car", 120)
    myCorvette.printType()
    myCorvette_maxspeed = myCorvette.getSpeed()
    print(myCorvette_maxspeed)
    
    mySpark = Vehicle("Car")
    
    myNio = Vehicle("Car", 140)
    myMaryCeleste = Vehicle("Sail boat",20)
    myEdenZero = Vehicle("Spaceship", 3000)
    mylist = []
    mylist = [myNio,myMaryCeleste,myEdenZero]
    for row in mylist:
        row.printType()
        print(row.getSpeed())