from project.user import User
from project.library import Library


class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        for u in library.user_records:
            if u.username == user.username:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(self, user: User, library: Library):
        for u in library.user_records:
            if u.user_id == user.user_id:
                library.user_records.remove(u)
                return
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(self, user_id: int, new_username: str, library: Library):
        for u in library.user_records:
            if u.user_id == user_id:
                if u.username == new_username:
                    return ("Please check again the provided username - "
                            "it should be different than the username used so far!")
                u.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"

# In the registration.py, create a class called Registration. Upon initialization, It will not receive anything,
# but we'll have these three methods.
#     • add_user(user: User, library: Library):
#         ◦ Adds the user if we do not have them in the library's user records already
#         ◦ Otherwise, returns the message "User with id = {user_id} already registered in the library!"
#     • remove_user(user: User, library: Library):
#         ◦ Removes the user from the library records if present
#         ◦ Otherwise, returns the message "We could not find such user to remove!"
#     • change_username(user_id: int, new_username: str, library: Library):
#         ◦ If there is a record with the same user id in the library and the username is different than the
#         provided one, change the username with the new one provided and return the message
#         "Username successfully changed to: {new_username} for user id: {user_id}".
#         Changes his username in the rented_books dictionary as well (if present).
#         ◦ If the new username is the same for this id, return the following message
#         "Please check again the provided username - it should be different than the username used so far!".
#         ◦ If there is no record for the provided id return "There is no user with id = {user_id}!"
