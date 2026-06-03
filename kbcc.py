def kbc_game():
    questions = [
        ["What is the fastest way to lose motivation?",
         "Watching reels 📱", "Reading books", "Sleeping", "Walking", "A"],

        ["What happens when teacher says 'Any doubts?'",
         "Students ask questions", "Class becomes silent 🤐", "Everyone leaves", "Debate starts", "B"],

        ["What is the most difficult decision?",
         "Study or Sleep 🤔", "Eat or Study", "Play or Study", "Watch series or Study", "A"],

        ["What is the real meaning of 'I will study tonight'?",
         "Full study", "Half study", "Sleep early 😴", "Party time 🎉", "C"],

        ["What do students check first after waking up?",
         "Books", "News", "Phone 📱", "Exercise", "C"],

        ["What is the biggest enemy of productivity?",
         "Hard work", "Discipline", "Mobile phone 😅", "Focus", "C"]
    ]

    money = 0

    for i in range(len(questions)):
        q = questions[i]
        print("\nQuestion", i + 1, "for Rs.", (i + 1) * 1000)
        print(q[0])
        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q[5]:
            print("✅ Correct Answer!")
            money += (i + 1) * 1000
        else:
            print("❌ Wrong Answer!")
            print("Correct answer was:", q[5])
            break

    print("\n💰 You won Rs.", money)


# Run the game
kbc_game()
