question = ("You are in the Main Menu,\n"
            "what do you want to do?\n"
            "[1] Basic Math\n"
            "[2] Advanced Math\n"
            "[3] Exit\nYour choice: ")

basic_math_question = ("You are in Basic Math,\n"
                       "what do you want to do?\n"
                       "[1] Factorial\n"
                       "[2] Square Root\n"
                       "[3] Go back\nYour choice: ")

advanced_math_question = ("You are in Advanced Math,\n"
                          "what do you want to do?\n"
                          "[1] Quadratic\n"
                          "[2] Go back\nYour choice: ")

invalide_choice = ("Invalid choice.\n"
                   "Please try again.")

factorial_question = "Enter a positive integer: "
square_root_question = "Enter a positive number: "
quadratic_question = "Enter the coefficient 'a': "
quadratic_question2 = "Enter the coefficient 'b': "
quadratic_question3 = "Enter the coefficient 'c': "
precision = 0.0000000001  # You can increase or decrease precision for better results


def check_type(n):
    try:
        n = float(n)
        return "integer" if n == int(n) else "float"
    except ValueError:
        return "other"


def check_set(n):
    return ("zero" if n == 0 else
            "negative" if n < 0 else "positive")


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
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2.0
    return guess


def canonical_form_start(a, b, c):
    while True:
        if all(check_type(x) in ["integer", "float"]
               for x in [a, b, c]):
            a, b, c = float(a), float(b), float(c)
            if a == 0:
                print("Coefficient 'a' cannot be 0\n"
                      "in a quadratic equation.")
                a = input(quadratic_question)
                b = input(quadratic_question2)
                c = input(quadratic_question3)
                continue
            return canonical_form(a, b, c)
        print("Invalid input. Please enter\n"
              "numeric values for 'a', 'b',\nand 'c'.")
        a = input(quadratic_question)
        b = input(quadratic_question2)
        c = input(quadratic_question3)


def canonical_form(a, b, c):
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        root1 = (-b + delta ** 0.5) / (2 * a)
        root2 = (-b - delta ** 0.5) / (2 * a)
        factored_form = str(a) + "(" + str(root1) + ")(" + str(root2) + ")"
        roots = (root1, root2)
    elif delta == 0:
        root = -b / (2 * a)
        factored_form = str(a) + "(" + str(root) + ")^2"
        roots = (root,)
    else:
        factored_form = "No real roots (delta < 0)"
        roots = None

    return {
        "canonical_form": str(a) + "(x - " + str(h) + ")^2 + " + str(k),
        "factored_form": factored_form,
        "roots": roots,
        "discriminant": delta
    }


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
                    print("The factorial of " + str(number) + " is:\n" + str(factorial_start(number)))
                elif basic_math_answer == 2:
                    number = input(square_root_question)
                    print("The square root of " + str(number) + " is:\n" + str(square_root_start(number)))
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
                    print("Canonical form is:\n" +
                          str(canonical_form_start(a, b, c)))
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
    print("See you soon!")
except Exception as e:
    print("An error occurred:", str(e))
    print("Feel free to open an issue on GitHub: "
          "https://github.com/NitroStar654/PyMathLab")
