import re

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    # 2. Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A-Z)")

    # 3. Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # 4. Numbers check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # 5. Special characters check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&* etc.)")

    # Strength result
    print("\n--- Password Analysis ---")
    print(f"Password Length: {len(password)}")
    
    if score == 5:
        strength = "VERY STRONG ✅"
    elif score == 4:
        strength = "STRONG ✅"
    elif score == 3:
        strength = "MODERATE ⚠️"
    elif score == 2:
        strength = "WEAK ❌"
    else:
        strength = "VERY WEAK ❌"

    print(f"Score: {score}/5")
    print(f"Strength: {strength}")

    if feedback:
        print("\nFeedback to improve:")
        for msg in feedback:
            print(f"  {msg}")
    else:
        print("\nGreat! Your password meets all complexity criteria.")

def main():
    print("--- Password Complexity Checker ---")
    while True:
        password = input("\nEnter password to check (or type 'exit'): ").strip()
        if password.lower() == 'exit':
            break
        if not password:
            continue
        check_password_strength(password)

if __name__ == "__main__":
    main()