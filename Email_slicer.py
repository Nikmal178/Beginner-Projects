
# take the email string and separate the username and domain 
def email_slicer(email_add):
    username, domain = email_add.split(sep="@")
    print("Your username is {} & domain is {}".format(username, domain))

# take the email address as input
email_add = input()
email_slicer(email_add)


