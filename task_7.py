from validate_email import validate_email
from password_validator import PasswordValidator


def check_mail(mail, dict_white_black, consent):
    if validate_email(mail):
        if mail in dict_white_black['white']:
            print("Your mail in white list.")
            if consent == 'white':
                return False
        elif mail in dict_white_black['black']:
            print("Your mail in black list.")
            if consent == 'yes' or consent == 'black':
                return False
        else:
            print("Your mail matches pattern.")
        return True
    else:
        print("Your mail doesn't match pattern.")
        return False


vault = {'white': ['good@good.good', 'notbad@notbad.notbad'],
         'black': ['penis@penis.penis', 'bad@bad.bad']}
vault_user = {}
schema = PasswordValidator()
schema\
    .min(8)\
    .has().digits()\
    .has().letters()\
    .has().symbols()\
    .has().no().spaces()
while True:
    answer_user = input("Use white and black lists? (yes/no/debug/exit)\n")
    if answer_user == 'exit':
        break
    elif answer_user == 'debug':
        while True:
            answer_user_2 = input("Debug white or black list? (white/black/exit)\n")
            if answer_user_2 == 'exit':
                break
            elif answer_user_2 != 'white' and answer_user_2 != 'black':
                continue
            mail_user_2 = input("Please enter added mail: ")
            if check_mail(mail_user_2, vault, answer_user_2):
                vault[answer_user_2] = mail_user_2
                print("The mail is added.")
        continue
    elif answer_user != 'yes' and answer_user != 'no':
        continue
    mail_user = input("Please enter your mail: ")
    if mail_user in vault_user.keys():
        print("This mail is already registered.")
        password_user = input("Please enter your password: ")
        if password_user == vault_user[mail_user]:
            print("Your password is correct.")
        else:
            print("Your password is not correct.")
        continue
    if check_mail(mail_user, vault, answer_user):
        while True:
            password_user = input("Please enter your password: ")
            if schema.validate(password_user):
                vault_user[mail_user] = password_user
                print("Your mail is registered.")
                break
            else:
                print("Your password doesn't match pattern.")
