class UserNotFoundError(Exception):
    def __init__(self, username):
        super().__init__(f"Użytkownik {username} nie został znaleziony")


class WrongPasswordError(Exception):
    def __init__(self):
        super().__init__("Błędne hasło")


class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(username)
        if self.users[username] != password:
            raise WrongPasswordError()
        print(f"Pomyślne logowanie")


auth = UserAuth({"admin": "1234", "user": "abcd"})
try:
    auth.login("admin", "1234")  # Sukces
    auth.login("unknown", "pass")  # Powinien rzucić UserNotFoundError
except Exception as e:
    print(f"Błąd: {e}")

try:
    auth.login("user", "wrongpass")  # Powinien rzucić WrongPasswordError
except Exception as e:
    print(f"Błąd: {e}")
