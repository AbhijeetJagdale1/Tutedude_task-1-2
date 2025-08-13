# Task 2: Personalized Greeting

def main():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    full_name = f"{first_name} {last_name}"

    print(f"Hello, {full_name}! It's great to have you here. Let's start coding now !!")

if __name__ == "__main__":
    main()