from words import Wordle


def main():
    wordle = Wordle("Apple")
    print("Hello from wordle!")

    while True:
        guess = input("Enter your guess:")
        if guess == wordle.secret:
            print("Your guess is correct")
            break
        print("Your guess is not correct")


if __name__ == "__main__":
    main()
