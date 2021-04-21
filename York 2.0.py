# 2021 04 09 Friday.
# York city wall.
# Defence ability model.
# Iuha Von Orius Latest model.


# First----Mass of the wall.

# Define other values we need:

# Density of the first section of the wall:
density1 = 0
# Width should be the same for all sections, and through out the model for convinience:
width = 0
# First height is the same for the Nanjing city wall:
height1 = 0
# First section, top length of the trapezoidal.
# For York, this is zero becuase York has this secction as a triangle not trapezium.
first_length1 = 0
# First section, base (bottom length) of the trapezoidal:
first_length2 = 0
# Mass of the first section:
mass1 = 0


# Density of the second section:
density2 = 0
# Second height:
height2 = 0
# Second section, top length of the trapezoidal:
second_length1 = 0
# Second section, bottom length of the trapezoidal:
second_length2 = 0
# Mass of the second section:
mass2 = 0


# Density of the third section:
density3 = 0
# third height:
height3 = 0
# Third section, top length of the trapezoidal:
# For York, this is zero becuase York has this secction as a triangle not trapezium.
third_length1 = 0
# Third section, bottom length of the trapezoidal:
third_length2 = 0
# Mass of the third section:
mass3 = 0


#Let the Mass be the total mass of the wall.
Mass = 0

print("\n")
print("Hello, this model will help you to calculate the change in GPE of the York city wall.")
print("York walls are made of three sections, please enter the values for the following sections:")
print("(answer all questions in digits)\n")


width = float(input("Enter the width of the wall please\n"))
height1 = float(input("1st height please\n"))
density1 = float(input("1st Density please\n"))
#first_length1 = float(input("1st Top length please\n"))
first_length2 = float(input("1st bottom length please\n"))
volume1 = (first_length1 + first_length2)*(height1)*(0.5)*width
print("1st volume is", volume1)
mass1 = density1 * volume1
print("1st mass is", mass1)




density2 = float(input("2nd Density please\n"))
height2 = float(input("2nd height please\n"))
second_length1 = float(input("2nd Top length please\n"))
second_length2 = float(input("2nd bottom length please\n"))
volume2 = (second_length1 + second_length2)*(height2)*(0.5)*width
print("2nd volume is",volume2)
mass2 = density2 * volume2
print("2nd mass is", mass2)
    
density3 = float(input("3rd Density please\n"))
height3 = float(input("3rd height please\n"))
#third_length1 = float(input("3rd Top length please\n"))
third_length2 = float(input("3rd bottom length please\n"))
volume3 = (third_length1 + third_length2)*(height3)*(0.5)*width
print("3rd volume is", volume3)
mass3 = density3 * volume3
print("3rd mass is", mass3)


Mass = mass1 + mass2 + mass3

print("Thank you! The mass is" ,Mass,"\n")



# Secondly------Height(of the initial centre of mass).

# Initial height of the centre of mass--" imY (initial mean Y)"
imY = 0

# Height of the centre of mass of each sections:
# e.g.section 1 is "imy_1".
imy_1 = 0
imy_2 = 0
imy_3 = 0

imy_1 = (height1 / 3) * ((2*first_length1 + first_length2)/(first_length1 + first_length2))
print("Height of the Centre of Mass of the 1st section is", imy_1)

imy_2 = (height2 / 3) * ((2*second_length1 + second_length2)/(second_length1 + second_length2))
print("Height of the Centre of Mass of the 2nd section is", imy_2)

imy_3 = (height3 / 3) * ((2*third_length1 + third_length2)/(third_length1 + third_length2))
print("Height of the Centre of Mass of the 3rd section is", imy_3,"\n")

imY = (mass1*imy_1 + mass2*imy_2 + mass3*imy_3)/Mass
print("The initial height of the overall Centre of Mass is",imY)

# iGPE = initial Gravitational Potential Energy:
iGPE = 0

iGPE = Mass * imY * 9.81

print("The initial GPE is", iGPE, "\n")



# Thirdly, the height of the final centre of mass (disfunctioned wall):



# A(Area) is the cross-sectional area of the wall(trapezium):
A = 0
# area 1,2&3 are the area of three sections of the wall,we use them to find the total area (A).
area1 = 0
area2 = 0
area3 = 0

area1 = (first_length1 + first_length2)*(height1)*(0.5)
area2 = (second_length1 + second_length2) * (height2) * (0.5)
area3 = (third_length1 + third_length2) * (height3) * (0.5)

# A(Area) of the cross-sectional area of the wall:
A = area1 + area2 + area3
print("Total cross-sectional area of the wall is", A,"\n")

# B is the area of the back triangle.
B = 0
# R is the area of the front trapezium. R = A - B
R = 0
# L is the base of the area of the back triangle.
L = 0
# angle of the slope inclined with the ground of the back triangle.
theta = 0
# J that has height height2.(J_height_z)
J_h2 = 0
# J that has height height3.(J_height_x)
J_h3 = 0
# Final height of the centre of mass--"fmY(final mean Y)"
fmY = 0

# Check if L is needed.
# Obtaine L, if necessary.

answer_L = 0
print("For cross-secctional area of the wall, is the middle section a rectangle? ")
print("type either yes or no please.")
print("If no, the model still works, you need to insert the value of L, thanks.")
answer_L = input()


if answer_L == "yes":
    L = third_length2

elif answer_L == "no":
    print("Enter the value of L please")
    L = float(input())
    
else:
    print("Sorry, only yes or no are accepted.")


# Obtain R:
B = (L*height3)/2
R = A - B

# import math for trigonometry:
import math

# calculate the cross-sectional area(triangles)---J_h2 and J_h3:
J_h2 = (height2**2)/(2*math.tan(math.pi/4))
J_h3 = (height3**2)/(2*math.tan(math.pi/4))

# area 1,2 and 3 are different to area a,b and c.
#The former are the initial area of section 1,2 and 3 of the cross-sectional area of the wall,
#they are used to find the total cross-sectional area---A;
#The later are more flexible, their values are different according to different cases of collapse,
#and they are used for finding the height og centre of mass of the disfunctioned wall.
area_a = 0
area_b = 0
area_c = 0

# Final height of the centre of mass of each section
fmy_a = 0
fmy_b = 0
fmy_c = 0


if R >= J_h2:
    #case1
    print("It is case 1.")
    area_a = (height2**2)/2*math.tan(math.pi/4)
    area_b = R - area_a
    area_c = B

    fmy_a = height2/3
    fmy_b = height2/2
    fmy_c = height3/3

    fmY = ( area_a*(fmy_a)+area_b*(fmy_b)+area_c*(fmy_c) )/A



elif J_h2 >= R > J_h3:
    #case2
    print("It is case 2.")
    area_a = R
    area_b = 0
    area_c = B

    fmy_a = (math.sqrt(2*R*math.tan(math.pi/4)))/3
    fmy_b = 0
    fmy_c = height3/3

    fmY = ( area_a*(fmy_a)+area_b*(fmy_b)+area_c*(fmy_c) )/A
    print("Height of the final Centre of Mass is", fmY)


elif R <= J_h3:
    #case3
    print("It is case 3.")
    theta = math.atan(height3/L)
    fmY = math.sqrt( 2*A /(1/math.tan(math.pi/4) + 1/math.tan(theta)) )/3
    print("The back of the wall does change.\n")


else:
    print("Sorry! something has gone wrong! please try again.")


# final Gravitational Potential Energy:
fGPE = 0
# change in GPE:
Change_GPE = 0

# Work out the final GPE:
fGPE = Mass * fmY * 9.81
print("The final GPE is", fGPE)

# Change in GPE (Initial vs Final):
Change_GPE = iGPE - fGPE

print("The change in GPE is",Change_GPE,"\n")

# Efficiency:
Efficiency = 0
Efficiency = ( Change_GPE / iGPE ) * 100
print("The defence efficiency is", Efficiency, "%\n")

print("Thanks!")







