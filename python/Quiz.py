
print("Welcome to the Quiz Game")

score = 0
total = 3


print("What is the capital of France?")
print("1. Paris")
print("2. London")
print("3. Berlin")
print("4. Rome")
answer1 = int(input("Your answer : "))
if answer1 == 1:
    print("Correct")
    score += 1
else:
    print("Wrong")

print("Where is semicolon located?")
print("1. Ikeja")
print("2. Sabo Yaba")
print("3. Yaba Sabo")
print("4. Ikotun")
answer2 = int(input("Your answer : "))
if answer2 == 2:
    print("Nice")
    score += 1
else:
    print("Fair")

print("What is the color of Nigeria Flag?")
print("1. Green,white")
print("2. White,Green")
print("3. Green,Green")
print("4. Green,White,Green")
answer3 = int(input("Your answer : "))
if answer3 == 4:
    print("Good")
    score += 1
else:
    print("At this point I can't help you")

print("You scored", score, "out of", total,"")