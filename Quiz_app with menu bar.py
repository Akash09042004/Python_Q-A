# Initialize score
score = 0

# Function to ask each question
def ask_question(question, answer):
    global score
    user = input(question + " ")
    if user.lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
def take_quiz():
# Ask user's name
    global score
    score =0
    name = input("Enter your good name: ")

# Ask 10 capital questions
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

    # Grading logic
    if score >= 7:
        grade = "🌟 Excellent"
    elif score >= 4:
        grade = "👍 Good"
    else:
        grade = "❌ Fail"

    # Show result
    print("\n📊 Result Summary")
    print("Thank you,", name)
    print("Your score is:", score)
    print("Your grade is:", grade)

    # Save result to CSV file
    with open("quiz_results.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name}, Score: {score}/10, Grade: {grade}\n")

    print("📝 Your result has been saved to 'quiz_results.txt'")

# Function to show leaderboard
def show_leaderBoard():
    try:
        with open("quiz_results.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No results found.")
                return

            print("\n🏆 Leaderboard")
            print("-" * 40)
            scores = []

            for line in lines:
                print(line.strip())
                parts = line.strip().split(",")
                for part in parts:
                    if "Score:" in part:
                        score_str = part.split(":")[1].strip().split("/")[0]
                        try:
                            scores.append(int(score_str))
                        except ValueError:
                            pass

            if scores:
                print("-" * 40)
                print("🥇 Highest Score:", max(scores), "/10")
            else:
                print("No valid scores found.")
    except FileNotFoundError:
        print("File not found. Please ensure 'quiz_results.txt' exists.")

# Show leaderboard at end
show_leaderBoard()

def menu():
    while True:
        print("\n📋 Menu:")
        print("1. Show LeaderBoard")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            show_leaderBoard()
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            print("👋 Bye! Thanks for using the app.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Now call the menu
menu()
  