class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", 'Gustavo')
user2 = User("002", 'Juliana')

user1.follow(user2)

print(user1.followers, user1.following)
print(user2.followers, user2.following)
