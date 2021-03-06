
class AuthException(Exception):
    def __init__(self, username, user = None):
        super(Exception, self).__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass
class InvalidPassword(AuthException):
    pass

