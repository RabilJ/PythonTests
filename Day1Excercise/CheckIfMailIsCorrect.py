def check_if_mail_is_correct(emails):
    for mail in emails:
        if "@" in mail and "." in mail:
            print(f"{mail} is correct")
        else:
            print(f"{mail} is incorrect")

list = ['exampleexamplecom', 'example@example.com']


print(check_if_mail_is_correct(list))