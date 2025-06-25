def fizzbuzz(n):
    """
    Given an integer n, return a list of strings representing numbers from 1 to n.
    For multiples of 3, add "Fizz" instead of the number.
    For multiples of 5, add "Buzz" instead of the number.
    For multiples of both 3 and 5, add "FizzBuzz".
    """
    pass


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = fizzbuzz(number)
    for item in result:
        print(item)
