
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def logged_in_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("Not logged in")
    return wrapper


@logged_in_decorator
def create_blog_post(user):
    print(f"This is a post from {user.name}")


new_user = User("Jonathan")
new_user.is_logged_in = True
create_blog_post(new_user)
