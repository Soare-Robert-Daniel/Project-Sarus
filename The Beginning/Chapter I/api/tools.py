import re

# Check if the email has valids characters
def check_email(email):
    if email and not re.search("[;'&*(){}""!?=+#$|`~]", email):
        print("Email %s is good to go!" % (email))
        return True
    return False

def test():
    test1 = "abd@hehe.com"
    print(test1, check_email(test1))

    test2 = "test{}@hehe.com"
    print(test2, check_email(test2))

    test3 = "test@hehe.com' and 1=1;"
    print(test3, check_email(test3))

    test4 = "abd_memi@hehe.com"
    print(test4, check_email(test4))

