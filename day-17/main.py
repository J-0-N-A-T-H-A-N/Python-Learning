class User:
    """User Class"""
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.active = True
        self.followers = 0
        self.following = 0

    def make_inactive(self):
        self.active = False

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("0001", "jonathan")
user_2 = User("0002", "aoife")

user_1.follow(user_2)

print(user_1.userid)
print(user_1.username)
print(user_1.active)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
