def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#We use a while loop when we want to repeat an action as long as a condition is true.
number_of_hurdles = 6 
while number_of_hurdles > 0:
    turn_around()
    number_of_hurdles -= 1
    print(number_of_hurdles)