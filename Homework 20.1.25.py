
from datetime import datetime,timedelta
from errors import *

class User:
    def __init__(self, name:str, email:str, password:str, birthday:datetime, __created_at: datetime = None):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.__created_at = datetime.now()


    def __str__(self):
        return f"name: {self.name}\nemail: {self.email}\npassword: {self.password}\nbirthday: {self.birthday}\ncreated_at: {self.__created_at}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not len(name) >= 4:
            raise UserNameTooShortError ("Username too short, must contain at least 4 characters...")
        if not any(char.isalpha() for char in name):
            raise UserNameNonCharError ("Name must have at least 1 letter")
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not "@" in email or not "." in email:
            raise IllegalEmailFormatError("Illegal email address. Email must contain '@' and '.'")
        self.__email = email

    @property
    def password(self):
         return self.__password

    @password.setter
    def password(self,password):
         if not len(password) >= 8:
             raise IllegalPasswordFormatError("Password must contain at least 8 characters")
         if not any(char.islower() for char in password):
             raise IllegalPasswordFormatError("Password must contain at least one lower-case character")
         if not any(char.isupper() for char in password):
             raise IllegalPasswordFormatError("Password must contain at least one higher-case character")
         if not any(char in "*&^#$%@!~" for char in password):
             raise IllegalPasswordFormatError("Password must contain at least one special character (*, &, ^, #, $, %, @, !, ~)")
         self.__password = password

    @property
    def birthday(self):
         return self.__birthday

    @birthday.setter
    def birthday(self,birthday:datetime):
        if isinstance(birthday, str):
            birthday = datetime.strptime(birthday, '%Y, %m, %d')
        if not birthday <= datetime.now():
            raise IllegalBirthdayError ("Birthday cannot be in the future!")
        if not (datetime.now()-birthday).days // 365 >= 20:
            raise UserTooYoungError ("User's age must be above 20!")
        self.__birthday = birthday

    @property
    def age(self):
        age = (datetime.now()-self.birthday).days // 365
        return age

    @property
    def created_at(self):
         return self.__created_at


users = [('Berta', 'berta12@gmailcom', 'IamBerta!','1983, 4, 24'),
             ('Shosh', 'shoshinka@walla.co.il', 'Shosh$$$15', '2022, 8, 14'),
             ('Gal', 'ggmail.com', 'GalWOW@#!', '2083, 10, 6')
         ]

for name, email, password, birthday in users:
    try:
        user = User(name, email, password, datetime.strptime(birthday, '%Y, %m, %d'), datetime.now())
        print(f"User created successfully: {user}")
    except IllegalPasswordFormatError as e:
        print(f"Password Error: {e}")
    except IllegalEmailFormatError as e:
        print(f"Email Error: {e}")
    except UserNameTooShortError as e:
        print(f"Name Error: {e} ")
    except UserTooYoungError as e:
        print(f"Age Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e} ")

