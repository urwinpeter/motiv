import re

def required(value, message):
    if not value:
        raise ValueError(message)
    return value

def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)
    return value

class Contact():
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    pass_regex = re.compile(r"[a-z]")
    salary_regex = re.compile(r"[0-9]")

    def __init__(self, username='', password='', salary=''):
        self.username = username
        self.password = password
        self.salary = salary
        
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = matches(value, self.email_regex, "Invalid Email Format")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = matches(value, self.pass_regex, "Invalid Password Format")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = matches(value, self.salary_regex, "Invalid salary format")


'''class NewContact():
    def __init__(self, username='', password = '', salary = ''):
        super().__init__(username, password)
        self.salary = salary'''
        

    