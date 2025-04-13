suspicious_keywords = [
    "urgent", "verify", "update", "login", "click here", "reset password",
    "security alert", "account suspended", "payment required", "confirm"
]

def check_for_phishing(text):
    found = [word for word in suspicious_keywords if word.lower() in text.lower()]
    if found:
        print("⚠️ Warning! Possible phishing keywords found:")
        for word in found:
            print(f" - {word}")
    else:
        print("✅ No common phishing keywords found.")

# Example usage
message = input("Paste the email or message text here:\n")
check_for_phishing(message)
