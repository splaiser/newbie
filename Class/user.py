class User():
    def __init__(self,first_name,last_name,age,location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(f"First name : {self.first.title()}")
        print(f"Last name : {self.last.title()}")
        print(f"Age : {self.age}")
        print(f"Location : {self.location.title()}")
    def greet_user(self):
        print(f"Welcome and Hello Dear, {self.first.title()} {self.last.title()}")

user_0 = User('Nikita','Chernyavskiy','29','Rostov-On-Don')
user_1 = User('Svetlana','Chernyavskaya','52','Rostov-On-Don')
user_2 = User('Katerina','Popova','21','Rostov-On-Don')
user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()