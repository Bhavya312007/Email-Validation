# Email Validation
import re
import dns.resolver

def is_valid_format(email): # Check if the email is in the correct format
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.(com|org|net|edu|gov|io|co|in|uk|au)$'
    return re.match(pattern, email, re.IGNORECASE) is not None

def check_domain(email):
    domain=email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return True
    except dns.resolver.Nxdomain:
        print("Domain does not exist")  # Check if the domain exists
        return False

    except Exception:
        print("Could not validate the domain. Please check your internet connection")
        return False

def check(email):

    special_characters = r'[!#\$%\^&\*\(\)=\+\{\}\[\]\|;:\'",<>\?/\\]'
    
    if email == "":  # Check if the email is empty
        print("Email cannot be empty")
    elif " " in email:  # Check if there is a space in the email
        print("Invalid email: Email should not contain spaces.")
    elif email.count("@") > 1:  # Check if there is more than one @ in the email
        print("Invalid email: Email should contain only one '@' symbol.")
    elif email.isupper():  # Check if the email is in uppercase
        print("Email must be in lowercase")
    elif len(email) < 5:  # Check if the email is less than 5 characters
        print("Length of email cannot be less than 5 characters")
    elif email[0].isdigit():  # Check if the first character is a digit
        print("First character cannot be a digit")
    elif email[-1].isdigit():  # Check if the last character is a digit
        print("Last character cannot be a digit")
    elif len(email) > 320:  # Check if the email is more than 320 characters
        print("Length of email cannot be more than 320 characters")
    elif "@" not in email or email.find(".", email.find("@")) == -1: # Check if there is a '.' after '@'
        print("Invalid email: There should be a '.' after '@'.")
    elif len(email.split('@')[0]) > 64:  # Check if the local part is more than 64 characters
        print("Length of local part cannot be more than 64 characters")
    elif len(email.split('@')[0]) < 2:  # Check if the local part is less than 2 characters
        print("Length of local part cannot be less than 2 characters")
    elif len(email.split("@")[-1].split(".")[0]) < 2:
        print("Length of domain part cannot be less than 2 characters")
    elif len(email.split(".")[-1]) < 2:
        print("Invalid email: There should be at least 2 characters after the last '.'.")
    elif len(email.split("@")[-1].split(".")[0]) < 2:
        print("Invalid email: There should be at least 2 characters before the '.'.")
    elif re.search(special_characters, email):
        print("Invalid email: No special characters are allowed.")
    elif re.search(special_characters, email.split("@")[-1]):
        print("Invalid email: No special characters are allowed after '@'.")
    elif not is_valid_format(email):
        print("Invalid email: Email format is incorrect. Make sure it follows 'username@domain.com'.")
    elif not check_domain(email):
        print("Invalid email: Domain does not exist.")
    else:
        return True
    return False

# Main loop
attempt = 0
while True:
    print("Email Validation Program")
    print("-----------------------------------------------")
    print(f"Attempt {attempt + 1}")
    print("-----------------------------------------------")
    email = input("Enter your email (or type exit to quit) : ")
    if email.lower() == "exit":
        break
    if check(email):
        print("Email provided is valid")
        break
    attempt += 1
    if attempt == 3:
        print("You have exceeded the number of attempts. Exiting program.")
        print("Ensure your email looks like 'example@domain.com'.")
        print("-----------------------------------------------")
        break
    with open("invalid_emails.log", "a") as log_file:
        log_file.write(f"{email}\n")
        print()
        print("Email provided is invalid. Check the log file for more details.")
        print()
        print("Ensure your email looks like 'example@domain.com'.")
