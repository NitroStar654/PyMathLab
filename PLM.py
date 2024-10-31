question = ("You are in the Main Menu,\n"
            "what do you want to do?\n"
            "[1] Basic Math\n"
            "[2] Advanced Math\n"
            "[3] Exit\n"
            "Your choice: ")

basic_math_question = ("You are in Basic Math,\n"
                       "what do you want to do?\n"
                       "[1] Factorial\n"
                       "[2] Square Root\n"
                       "[3] Go back\n"
                       "Your choice: ")

advanced_math_question = ("You are in Advanced Math,\n"
                          "what do you want to do?\n"
                          "[1] Quadratic\n"
                          "[2] Go back\n"
                          "Your choice: ")

invalide_choice = ("Invalid choice.\n"
                   "Please try again.")

factorial_question = "Enter a positive integer: "
square_root_question = "Enter a positive number: "
quadratic_question = "Enter the coefficient 'a': "
quadratic_question2 = "Enter the coefficient 'b': "
quadratic_question3 = "Enter the coefficient 'c': "
precision = 7  # Précision par défaut à 7 chiffres


def check_type(n):
    try:
        n = float(n)
        return "integer" if n == int(n) else "float"
    except ValueError:
        return "other"


def check_set(n):
    return ("zero" if n == 0 else
            "negative" if n < 0 else "positive")


def round_to_precision(value, precision_value):
    return round(value, precision_value)


def format_number(value):
    if value == int(value):
        return str(int(value))
    return str(value)


def factorial_start(n):
    while True:
        if check_type(n) == "integer":
            n = int(float(n))
            if check_set(n) in ["positive", "zero"]:
                return factorial(n)
            print("Factorial is not defined for\nnegative numbers.")
        else:
            print("Invalid input.")
        n = input(factorial_question)


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def square_root_start(n):
    while True:
        if check_type(n) in ["integer", "float"]:
            n = float(n)
            if check_set(n) in ["positive", "zero"]:
                return square_root(n)
            print("Square root is not defined for\nnegative numbers.")
        else:
            print("Invalid input.")
        n = input(square_root_question)


def square_root(n):
    guess = n / 2.0
    while abs(guess * guess - n) > 0.000000000001:
        guess = (guess + n / guess) / 2.0
    return round_to_precision(guess, precision)


def canonical_form_start(a, b, c):
    while True:
        if all(check_type(x) in ["integer", "float"] for x in [a, b, c]):
            a, b, c = float(a), float(b), float(c)
            if a == 0:
                print("Coefficient 'a' cannot be 0\nin a quadratic equation.")
                a = input(quadratic_question)
                b = input(quadratic_question2)
                c = input(quadratic_question3)
                continue
            return canonical_form(a, b, c)
        print("Invalid input. Please enter\nnumeric values for 'a', 'b',\nand 'c'.")
        a = input(quadratic_question)
        b = input(quadratic_question2)
        c = input(quadratic_question3)


def canonical_form(a, b, c):
    h = round_to_precision(-b / (2 * a), precision)
    k = round_to_precision(c - (b ** 2) / (4 * a), precision)
    delta = round_to_precision(b ** 2 - 4 * a * c, precision)

    if delta > 0:
        root1 = round_to_precision(square_root(delta), precision)
        root1 = round_to_precision((-b + root1) / (2 * a), precision)
        root2 = round_to_precision((-b - delta ** 0.5) / (2 * a), precision)
        factored_form = str(format_number(a)) + "(x - " + format_number(root1) + ")(x - " + format_number(root2) + ")"
        roots = (root1, root2)
    elif delta == 0:
        root = round_to_precision(-b / (2 * a), precision)
        factored_form = str(format_number(a)) + "(" + format_number(root) + ")^2"
        roots = (root,)
    else:
        factored_form = None
        roots = "No real roots (delta < 0)"

    return ("Canonical Form:\n" + str(format_number(a)) + "(x - " + format_number(h) + ")^2 + " + format_number(k) +
            "\nDiscriminant: " + str(format_number(delta)) +
            "\nRoots: " + str(roots) +
            "\nFactored Form:\n" + str(factored_form))


def main():
    print("Welcome to PyMathLab!")
    while True:
        answer = input(question)
        while True:
            try:
                answer = int(answer)
                break
            except ValueError:
                print(invalide_choice)
                answer = input(question)

        if answer == 1:
            while True:
                basic_math_answer = input(basic_math_question)
                try:
                    basic_math_answer = int(basic_math_answer)
                except ValueError:
                    print(invalide_choice)
                    continue

                if basic_math_answer == 1:
                    number = input(factorial_question)
                    factorial_result = factorial_start(number)
                    print("The factorial of " + str(number) + " is:\n" + format_number(factorial_result))
                elif basic_math_answer == 2:
                    number = input(square_root_question)
                    square_root_result = square_root_start(number)
                    print("The square root of " + str(number) + " is:\n" + format_number(square_root_result))
                elif basic_math_answer == 3:
                    break
                else:
                    print(invalide_choice)
        elif answer == 2:
            while True:
                advanced_math_answer = input(advanced_math_question)
                try:
                    advanced_math_answer = int(advanced_math_answer)
                except ValueError:
                    print(invalide_choice)
                    continue

                if advanced_math_answer == 1:
                    a = input(quadratic_question)
                    b = input(quadratic_question2)
                    c = input(quadratic_question3)
                    result = canonical_form_start(a, b, c)
                    while True:
                        print("Result for " + a + "x^2 + " + b + "x + " + c + " is:\n" + str(result))
                        input("Press ENTER to continue")
                        break
                elif advanced_math_answer == 2:
                    break
                else:
                    print(invalide_choice)
        elif answer == 3:
            print("See you soon!")
            return
        else:
            print(invalide_choice)


try:
    main()
except KeyboardInterrupt:
    print("\nSee you soon!")
except Exception as e:
    print("An error occurred:", str(e))
    print("Feel free to open an issue on GitHub:\n"
          "https://github.com/NitroStar654/PyMathLab")
