class User():

    def __init__(self,first_name,last_name,age,location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        print(f"First name : {self.first.title()}")
        print(f"Last name : {self.last.title()}")
        print(f"Age : {self.age}")
        print(f"Location : {self.location.title()}")

    def greet_user(self):
        print(f"Welcome and Hello Dear, {self.first.title()} {self.last.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print (f"Login attempts : {self.login_attempts}")


class Admin(User):

    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["can add user","can delete user", "can ban user"]

    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")

admin_0 = Admin('Nikita','Chernyavskiy','29','Rostov-On-Don')
admin_0.privileges.show_privileges()