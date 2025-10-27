import random

print("Welcome to Simple Arithmeti GameApp!")
score = 0

for i in range(1, 11):
	number1 = random.randint(0, 20)
	number2 = random.randint(0, number1) 
	print(f"Question: What is {number1} - {number2} ?")
    
	for i in range(1, 3):
		answer = int(input("Your answer:"))
		if answer == number1 - number2:
			print("Correct!")
			score += 1

			break
		else:
			print("Try again")
			print(f"Game Over! You got {score} out of 10 correct.")

		
		
 
    