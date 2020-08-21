# Import the turtle module - Importa el modulo tortuga
import turtle
# Create a new turtle named ami - Crea a ami
ami = turtle.Turtle()
# Set ami´color - Le pone color a ami
colores = ["purple", "red", "orange", "yellow", "green","blue"]
#Velocidad de ami
ami.speed(2)
# ami mas gorda
ami.width(3)


for sidess in range(6):
    ami.color(colores[sidess])
    for sides in range(5):
        ami.forward(50)
        ami.right(145)
    ami.penup()
    ami.right(60)
    ami.forward(50)
    ami.pendown()
