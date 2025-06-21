print("""\n
      ************************************
             Check Password Strength
      ************************************\n""")

import re

def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False 
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%]', password):
        return False
    return True

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    if check_password_strength(pwd):
        print("Password is strong.")
    else:
        print("""Password is weak. 
              Please ensure it must be 
              1) at least 8 characters long
              2) contain uppercase and lowercase letters, 
              3) at least one digit, 
              4) and at least one special character (!, @, #, $, %).""")