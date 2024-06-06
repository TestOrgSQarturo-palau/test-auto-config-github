def add_numbers(a,b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def main():
    """
    Entry point of the script.
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = add_numbers(num1, num2)
    print("The sum is: {}".format(result))

if __name__ == "__main__":
    main()