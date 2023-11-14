import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_valid_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Invalid length. Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        length = get_valid_password_length()
        password = generate_random_password(length)
        print("Generated password: " + password)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
