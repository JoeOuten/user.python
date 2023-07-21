class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Reward member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User is a member already")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Not enough points")
        return self


userOne = User("Xavier", "Xang", "Xavier_Xang8@gmail.com", 23, "False", 0)
userTwo = User("Aiden", "Abraham", "Aidien5@gmail.com", 18, "False", 0)
userThree = User("Bob", "Kuzma", "Who'sKuz@gmail.com", 40, "False", 0)
userFour = User("John", "Smith", "JohnS123@gmail.com", 32, "False", 0)
# userOne.display_info().spend_points(50)
# print(userOne.spend_points)
# userTwo.enroll().display_info().enroll().spend_points(80).display_info()
# print(userTwo.display_info)
# User.display_info(userOne), User.display_info(
#     userTwo), User.display_info(userThree), User.display_info(userFour)
