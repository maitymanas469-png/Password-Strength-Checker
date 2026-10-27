def check_length(password):
    return len(password) >= 8
def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False
def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def has_special_char(password):
    special_characters = "!@#$%^&*()-_+=[]{}|;:,.<>?/~`"
    for char in password:
        if char in special_characters:
            return True
    return False
def is_common_password(password):
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "password1", "111111", "123123", "letmein", "iloveyou",
        "admin", "welcome", "monkey", "dragon", "football"
    ]
    return password.lower() in common_passwords
def calculate_strength_score(password):
    score = 0
    if check_length(password):
        score += 1
    if has_uppercase(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special_char(password):
        score += 1
    return score
def get_strength_label(score, password):
    if is_common_password(password):
        return "Very Weak (Common Password)"
    elif score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"
def display_feedback(password):
    print("\n----- Detailed Feedback -----")
    print(f"[{'OK' if check_length(password) else 'X'}] At least 8 characters long")
    print(f"[{'OK' if has_uppercase(password) else 'X'}] Contains an uppercase letter (A-Z)")
    print(f"[{'OK' if has_lowercase(password) else 'X'}] Contains a lowercase letter (a-z)")
    print(f"[{'OK' if has_digit(password) else 'X'}] Contains a digit (0-9)")
    print(f"[{'OK' if has_special_char(password) else 'X'}] Contains a special character (!@#$ etc.)")
def main():
    print("=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)
    while True:
        password = input("\nEnter a password to check (or 'exit' to quit): ")
        if password.lower() == "exit":
            print("Thank you for using Password Strength Checker. Goodbye!")
            break
        if password == "":
            print("Password cannot be empty. Please try again.")
            continue
        score = calculate_strength_score(password)
        strength = get_strength_label(score, password)
        print(f"\nPassword Strength: {strength}  (Score: {score}/5)")
        display_feedback(password)
if __name__ == "__main__":
    main()
