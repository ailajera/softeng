# START HERE
def get_grade(score):
    
    if score < 60:
        return("F")
    elif score < 70:
        return("D")
    elif score < 80:
        return("C")
    elif score < 90:
        return("B")
    else:
        return("A")

#
if __name__ == "__main__":
    score = int(input("Enter score: "))
    print(f"Grade: {get_grade(score)}")
