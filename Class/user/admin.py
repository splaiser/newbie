from user import User
class Admin(User):

    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["can add user","can delete user", "can ban user"]

    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")