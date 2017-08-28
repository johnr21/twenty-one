# Asks the user for a float input
# Validates input and breaks loop if input is a float



while True:
    try:
        userInput = float(input("Enter a number: "))
        break
    except ValueError:
        print("You lose")
        continue

# Calculates whatever the user inputs to the number 21

if userInput == 21:
    print("You win")
elif userInput > 21:
    twentyOne = float(21)
    answer = float(0)
    difference = userInput - twentyOne
    result = userInput - difference
    print(int(result))
    print("You win")
elif userInput < 21:
    twentyOne = float(21)
    answer = float(0)
    difference = twentyOne - userInput
    result = userInput + difference
    print(int(result))
    print("You win")

# When the number is to big or to small than the answer is 0
    
