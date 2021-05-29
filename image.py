import turtle
import time

ask = input("bruh")

if ask == "n":  
  wn = turtle.Screen()
  wn.title("Animation Demo")
  wn.bgcolor("black")


player = turtle.Turtle()
player.shape("square")
player.color("orange")

nugget = True
while nugget == True:
  player.shape("square")
  time.sleep(0.5)
  player.shape("circle")
  time.sleep(0.5)
  player.shape("square")
  

wn.mainloop()