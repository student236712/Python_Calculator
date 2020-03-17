import re

print("Our calculator")
print("Type 'quit' to exit\n")

# Previous result
previous = 0
run = True
counter = 0


def perform_math():
    global run
    global previous
    global counter
    equation = ""

    # Check if it is first program iteration - then we don't have previous result to show
    if counter == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    # Check if user typed equation or program closing command
    if equation == 'quit':
        run = False
    else:
        # Trim input equation for only numbers and mathematical operators
        equation = re.sub('[a-zA-z,:()" " ]', '', equation)

        # If it is first program iteration evaluate only equation from input
        # else take previous result with input together, then evaluate
        if counter == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
            # Increment counter because one operation is done correctly
            counter += 1


while run:
    perform_math()
