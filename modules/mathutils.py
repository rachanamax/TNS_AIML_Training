def areaCircle(radius):
    area = 3.14*radius**2
    return area
if __name__== "__main__":
        print("Testing : ", areaCircle(5))


def perimeterCircle(radius):
    perimeter= 2*3.14*radius
    return perimeter
if __name__=="__main__":
        print("Testing : ", perimeterCircle(4))

def areaRectangle(length, breadth):
    area = length*breadth
    return area
if __name__=="__main__":
        print("Testing : ", areaRectangle(3,4))

def perimeterRectangle(length, breadth):
    perimeter = 2*(length+breadth)
    return perimeter
if __name__=="__main__":
        print("Testing: ", perimeterRectangle(3,4))

