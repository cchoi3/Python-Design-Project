from ChoiFunction import*
bob.speed(0)
turtle.colormode(255)
turtle.bgcolor(0,0,0)
def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

for times in range(50):
  bob.color("red")
  print(times*10+10)

for times in range(50):
    print(times*10+10)

for times in range(50):
    bob.circle(100)
    bob.left(92)
    bob.right(120)

for times in range(100):
  bob.color("white")
  print(times*10+10)

for times in range(100):
  print(times*10+10)

for times in range(50):
  bob.color("blue")
  bob.circle(125)
  bob.right(120)
  bob.left(92)
  print(times*10+10)

for times in range(50):
  bob.color("green")
  bob.circle(150)
  bob.right(145)
  bob.left(92)
  print(times*10+10)

for times in range(50):
  bob.color("yellow")
  bob.circle(175)
  bob.right(145)
  bob.left(92)
  print(times*10+10)

jump(-370,300)
for times in range(200):
  bob.color("white")
  bob.circle(50)
  bob.left(90)
  bob.right(92)

jump(370,-300)
for times in range(200):
  bob.color("white")
  bob.circle(50)
  bob.left(90)
  bob.right(92)

jump(-370,-300)
for times in range(200):
  bob.color("white")
  bob.circle(50)
  bob.left(90)
  bob.right(92)

jump(370,300)
for times in range(200):
  bob.color("white")
  bob.circle(50)
  bob.left(90)
  bob.right(92)

