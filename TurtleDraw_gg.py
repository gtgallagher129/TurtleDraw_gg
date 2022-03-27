#author: Grant Gallagher
#Project: Turtle Draw
#Email: granttgallagher@lewisu.edu
#liscense: MIT

import turtle


success = False
while success == False:
    try:
        TEXTFILE = input('\n\nEnter Text File name used\n\n')
        draw = open(TEXTFILE, 'r')
        success = True
    except Exception as e:
        print('No file Found With That Name')


turtle.screensize(450,450)
turtle.setup(450,450)
Michelangelo = turtle.Turtle()
Michelangelo.speed(10)
Michelangelo.penup()
line = draw.readline()

distance = []

for line in draw:
	print(line, end='')
	parts = line.split(' ')

	if (len(parts) == 3):
		color = parts[0]
		x = int(parts[1])
		y = int(parts[2])

		Michelangelo.color(color)
		Michelangelo.goto(x,y)
		Michelangelo.pendown()
		distance.append(turtle.distance(x,y))

	else:
		Michelangelo.pu()

line = draw.readline()

draw.close()
TotalDistance = sum(distance)
Michelangelo.pu()
Michelangelo.goto(-10,-200)
Michelangelo.color("orange")
Michelangelo.pd()
Michelangelo.write("Total Drawn Line Distance = %.2f" %TotalDistance, False, 'left',( 'Arial', 10, 'normal'))
print('Total Drawn Distance = %.2f' %TotalDistance)


input=input("\n\nWithin the Terminal Hit Enter Key to Close")
if input == '':
    turtle.bye()
else:
    input


print('\nEnd')