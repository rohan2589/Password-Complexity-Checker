import re

def assess_password_strength(password):
    score = 0
    suggestions = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Criteria 2: Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter (A-Z).")

    # Criteria 3: Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter (a-z).")

    # Criteria 4: Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    # Criteria 5: Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$, etc).")

    # Determine strength level
    strength_levels = {
        5: " Very Strong",
        4: " Strong",
        3: " Moderate",
        2: " Weak",
        1: " Very Weak",
        0: " Extremely Weak"
    }

    print("\n--- Password Strength Report ---")
    print(f"Password: {password}")
    print(f"Strength: {strength_levels[score]}")

    if suggestions:
        print("\nSuggestions to Improve:")
        for tip in suggestions:
            print(f" - {tip}")
    else:
        print("Great! Your password is strong.")

if __name__ == "__main__":
    user_password = input(" Enter a password to check: ")
    assess_password_strength(user_password)
    input("\nPress Enter to exit...")
