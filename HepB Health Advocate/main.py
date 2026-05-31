def main():
    # Step 1: Print a welcome message tailored to your project name
    print("Welcome to the HepB Health Advocate Quiz!")
    print("Today, we are testing your knowledge on Hepatitis B prevention and care.")
    print("Let's see how much you know. Type your answers as A, B, or C.")
    print("-" * 50) # Prints a clean divider line
    print()
    
    # Steps 2 & 3: Our dictionary storing questions, correct answers, and facts
    quiz_data = {
        "What is the primary way Hepatitis B is transmitted?\nA) Airborne droplets\nB) Contaminated food/water\nC) Contact with infectious blood or body fluids\nType A, B, or C: ": 
        ["C", "Hepatitis B is highly infectious and can survive outside the body for at least 7 days and still be capable of causing infection."],
        
        "Which major organ does the Hepatitis B virus primarily attack?\nA) Lungs\nB) Liver\nC) Kidneys\nType A, B, or C: ": 
        ["B", "The virus attacks the liver and can cause both acute and chronic disease, sometimes leading to cirrhosis or liver cancer."],
        
        "Is there a vaccine available to prevent Hepatitis B?\nA) Yes\nB) No\nType A or B: ": 
        ["A", "The Hepatitis B vaccine is highly effective and is considered the first 'anti-cancer' vaccine because it prevents liver cancer caused by the virus."],
        
        "True or False: Everyone infected with Hepatitis B will show immediate, severe symptoms.\nA) True\nB) False\nType A or B: ": 
        ["B", "Many people are asymptomatic when newly infected. This is why testing and awareness campaigns are so critical for early detection."],
        
        "While there is no absolute cure for chronic Hepatitis B, can it be managed with medication?\nA) Yes\nB) No\nType A or B: ": 
        ["A", "Chronic Hepatitis B can be treated with medicines, including oral antiviral agents, which can slow the progression of cirrhosis and reduce incidence of liver cancer."]
    }

    # Step 4: Set up the score tracker
    score = 0
    
    # Step 5: Loop through every question in the dictionary
    for question in quiz_data:
        
        # Ask the user the question and wait for their input
        user_answer = input(question)
        
        # Extract the correct answer and the educational fact from our list
        # [0] is the answer (e.g., "C"), [1] is the fact
        correct_answer = quiz_data[question][0]
        educational_fact = quiz_data[question][1]
        
        # Step 6: Check if they got it right 
        # (We use .upper() so if they type 'a' instead of 'A', it still counts!)
        if user_answer.upper() == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect. The right answer was " + correct_answer + ".")
            
        # Always print the educational fact after they answer
        print("Did you know? " + educational_fact)
        print("-" * 50)
        print()
        
    # Step 7: Print the final score
    print("Quiz Complete!")
    print("Your final score is: " + str(score) + " out of " + str(len(quiz_data)))


# This is the trigger that tells Python to run your code!
if __name__ == '__main__':
    main()