# START HERE
def list_processor(numbers):
    for number in numbers:
        if number % 2 == 0:
         print(f"{number} is even")
        else: 
         print(f"{number} is odd")   
##

if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5]
    list_processor(sample_numbers)
