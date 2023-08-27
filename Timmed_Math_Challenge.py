import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 10
TOTAL_PROBLEMS = 5


def generate_problem():
    first_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    second_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    problem = str(first_operand) + " " + operator + " " + str(second_operand)
    answer = eval(problem)
    return problem, answer


wrong_answers = 0
input("Press enter to start: ")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    problem, answer = generate_problem()
    while True:
        user_answer = input("Problem #" + str(i + 1) + ": " + problem + " =")
        if user_answer == str(answer):
            break
        wrong_answers += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("------------------")
print("Nice work, you finished it in ", total_time,  "seconds.")
