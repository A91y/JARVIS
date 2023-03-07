# https://geekflare.com/password-generator-python-code/
# necessary imports
import secrets
import string


def newpassword(pwd_length=12):

    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # generate a password string
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd
