# START HERE
def translator():
    translate = {
        "hello" : "kamusta",
        "thank you" : "salamat",
        "goodbye" : "paalam"
    }

    phrase = input().lower() 

    translates = translate.get(phrase,"Translation not found")
    print(f"Filipino: {translates}")
##

if __name__ == "__main__":
    translator()
