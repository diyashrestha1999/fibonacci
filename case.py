

            

from enum import Enum
class Color(Enum):
    RED= 'red'
    BLUE= 'blue'
    BLACK= 'black'
    PURPLE= 'purple'

color= Color(input("Print your choice of 'red', 'blue', 'black' or 'purple':"))

match color :
    case Color.RED
        print("I see red")
    case Color.BLUE
        print("I see blue")
    case Color.BLACK
        print("I see black")
    case Color.PURPLE
        print("I see purple")