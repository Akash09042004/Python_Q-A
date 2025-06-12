score = 0

def ask_question(question, answer):
    global score
    user = input(question + " ")
    if user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Ask user's name
name = input("Enter your good name: ")

# Quiz questions
ask_question("What is the capital of France?", "Paris")
ask_question("What is the capital of Germany?", "Berlin")
ask_question("What is the capital of Italy?", "Rome")
ask_question("What is the capital of Spain?", "Madrid")
ask_question("What is the capital of Japan?", "Tokyo")
ask_question("What is the capital of Canada?", "Ottawa")
ask_question("What is the capital of Australia?", "Canberra")
ask_question("What is the capital of India?", "New Delhi")
ask_question("What is the capital of Brazil?", "Brasília")
ask_question("What is the capital of Russia?", "Moscow")

# Grade system
if score >= 7:
    grade = "🌟 Excellent"
elif score >= 4:
    grade = "👍 Good"
else:
    grade = "❌ Fail"

# Show result to user
print("\nThank you!!", name)
print("Your point is", score)
print("Your grade is", grade)

# Save result to a file
with open("quiz_results.txt", "a", encoding="utf-8") as file:
    file.write(f"Name: {name}, Score: {score}/10, Grade: {grade}\n")

print("📝 Your result has been saved to 'quiz_results.txt'")
