import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
        feedback.append("Consider using at least 12 characters.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Use at least one special character (e.g., !, @, #, etc.).")

    # Evaluate final strength
    if strength >= 6:
        result = "Very Strong"
    elif strength >= 5:
        result = "Strong"
    elif strength >= 3:
        result = "Moderate"
    else:
        result = "Weak"

    return result, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter your password to check strength: ")
    result, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {result}")
    if feedback:
        print("Feedback:")
        for tip in feedback:
            print(f"- {tip}")
