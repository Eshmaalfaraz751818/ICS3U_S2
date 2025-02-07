import math
length = input("Please input a length: ")
length = float(length)
area = math.pow(length, 2)
print("The area of a square of side length", length, "is:", area)
#The code stopped executing for the lenght untill I entered a lenght, once I entered the lenght the code found the area by raising it to the exponent of 2. 
import math
r= 2
n=math.pi
areaS= math.pow(r, 2)*4
areaCS= math.pow(r,2)*n*0.5
AreaT=math.pow(r,2)*n*0.5 + math.pow(r, 2)*4
print("The result is:", AreaT)
# I calculated the area of the semi circle and square then added them together. in the formula for the square it has to be multiplied by 2 because r is not 1 but half of x the side lenght. 
