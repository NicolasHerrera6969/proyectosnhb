import turtle

# Configuración de la ventana
screen = turtle.Screen()
screen.bgcolor("white")

# Configuración de la tortuga
hexagon = turtle.Turtle()
hexagon.shape("turtle")
hexagon.color("purple")
hexagon.speed(4)

# Dibujar un hexágono
for _ in range(6):
    hexagon.forward(100)
    hexagon.left(60)  # Ángulo interno de un hexágono regular

# Finaliza el dibujo al hacer clic en la ventana
screen.exitonclick()
