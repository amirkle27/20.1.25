
class UserNameNonCharError(Exception):
    def __init__(self, error):
        super().__init__(error)

class UserNameTooShortError(Exception):
    def __init__(self, error):
        super().__init__(error)

class IllegalEmailFormatError(Exception):
    def __init__(self, error):
       super().__init__(error)

class IllegalPasswordFormatError(Exception):
    def __init__(self, error):
        super().__init__(error)

class IllegalBirthdayError(Exception):
    def __init__(self, error):
        super().__init__(error)

class UserTooYoungError(Exception):
    def __init__(self, error):
        super().__init__(error)
