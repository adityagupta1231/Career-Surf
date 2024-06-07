import math

#Return the ceiling of x as a float,
#the largest integer value less than
#or equal to x.
print(math.floor(4.1))
print(math.floor(4.5))
print(math.floor(4.9))

#math.copysign(x,y) : Return x with the sign of y
print("math.copysign(2,-4) =",math.copysign(2,-4))

#math.pow(x,y)

#math.fabs(x) : Return the absolute value of x
print("math.fabs(-5.1) =",math.fabs(-5.1))

#math.factorial(x) :Return x factorial, Raises ValueError
print("math.factorial(5) =",math.factorial(5))

#math.fsum(iterable) : Return an accurate floating point sum
#Avoid loss of precision by tracking
print("math.fsum([.4,.6,.2])=",math.fsum([.4,.6,.2]))

#math.pi :The mathematical constant pi = 3.141592....
print("Constant value of math.pi=",math.pi)

#math.degrees(x) Convert angle x from radians to degrees
print("math.degrees(2.0) =",math.degrees(2.0))

#math.radians(x) : convert angle x from degrees to radian
print("math.radians(114.591559026)=",math.radians(114.591559026))

#math.log(num,base)
print("math.log(1000,10)=", round(math.log(1000,10)))
print("math.log(128,2)=", round(math.log(128,2)))

#math.sqrt(num)
print("math.sqrt(25)=",math.sqrt(25))
print("\n\n")

print("                  Lecture 2\n\n")
import sys
print("sys.version =",sys.version)
print("sys.version_info =",sys.version_info)
print("sys.platform =",sys.platform)
print("sys.path=",sys.path)

import os
print("\nos.name =",os.name)
print("\nos.getenv('PATH')=",os.getenv('PATH'))
print("\nos.getcwd= ",os.getcwd())
#For creating a new folder
#os.mkdir("AkarshanDir")
#print("New folder created successfully in C://Python bin.")

#For deleting a folder 
#os.rmdir('AkarshanDir')
#print("Folder deleted")

#os.chdir("AkarshanDir")
#os.mkdir("Infolder")




