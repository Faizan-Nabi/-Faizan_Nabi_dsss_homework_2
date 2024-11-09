import random

def get_random_integer(min_val, max_val):
    """
    Get a random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)

def get_random_operator():
    """
    Pick a random math operator.
    """
    return random.choice(['+', '-', '*'])

def calculate_answer(n1, n2, operator):
    """
    Calculate the result based on the operator.
    """
    problem = f"{n1} {operator} {n2}"
    
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    
    return problem, answer

def math_quiz():
    """
    Run the quiz and check answers.
    """
    score = 0
    total_questions = 5  # Set how many questions there will be

    print("Welcome to the Math Quiz Game!")

    for _ in range(total_questions):
        # Get random numbers and an operator
        n1 = get_random_integer(1, 10)
        n2 = get_random_integer(1, 5)
        operator = get_random_operator()

        # Get the problem and correct answer
        problem, correct_answer = calculate_answer(n1, n2, operator)

        print(f"\nQuestion: {problem}")

        # Try to get a valid answer from the user
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        # Check if the answer is right or wrong
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
