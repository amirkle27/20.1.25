
from datetime import datetime,timedelta
from errors import *

class User:
    def __init__(self, name:str, email:str, password:str, birthday:datetime, created_at: datetime = None):
        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.created_at = created_at if created_at else datetime.now()



    def __str__(self):
        return f"name: {self.name}\nemail: {self.email}\npassword: {self.password}\nbirthday: {self.birthday}\ncreated_at: {self.created_at}"

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
            birthday = datetime.strptime(birthday, '%d/%m/%Y')
        if not birthday <= datetime.now():
            raise IllegalBirthdayError ("Birthday cannot be in the future!")
        if not (datetime.now()-birthday).days // 365 >= 20:
            raise UserTooYoungError ("User's age must be above 20!")
        self.__birthday = birthday

    @property
    def age(self):
        age = (datetime.now()-self.birthday).days // 365
        return age

    # @property
    # def created_at(self):
    #      return self.__created_at

    # @created_at.setter
    # def created_at(self):
    #     created_at = datetime.now()
    #     self.__created_at = created_at
try:

    user = User('Arnon', 'arnon@gmail.com', '1@Asasdsd23', datetime(1990, 1, 1), datetime.now())
except IllegalPasswordFormatError as e:
    print(f"Password Error: {e}")
except IllegalEmailFormatError as e:
    print(f"Email Error: {e}")
except UserNameTooShortError as e:
    print(f"Name Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    user1 = User('Berta', 'berta12@gmailcom', 'IamBerta!', datetime(1983, 4, 24), datetime.now())
except IllegalPasswordFormatError as e:
    print(f"Password Error: {e}")
except IllegalEmailFormatError as e:
    print(f"Email Error: {e}")
except UserNameTooShortError as e:
    print(f"Name Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    user2 = User('Shosh', 'shoshinka@walla.co.il', 'Shosh$$$15', datetime(2022, 14, 8), datetime.now())
except IllegalPasswordFormatError as e:
    print(f"Password Error: {e}")
except IllegalEmailFormatError as e:
    print(f"Email Error: {e}")
except UserNameTooShortError as e:
    print(f"Name Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    user3 = User('Gabi', 'ggmail.com', 'IamBerta!', datetime(2083, 10, 6), datetime.now())
except IllegalPasswordFormatError as e:
    print(f"Password Error: {e}")
except IllegalEmailFormatError as e:
    print(f"Email Error: {e}")
except UserNameTooShortError as e:
    print(f"Name Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



print(user)
print(user._User__name)
# print(user1.email)
# print(user1.password)

# print(user1.birthday)
# print(user1.created_at)

print(user)
# print(user1)
# print(user2)
# print(user3)
# print(user.birthday)
