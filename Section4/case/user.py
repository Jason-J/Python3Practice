import  hashlib
from cunsomException import UsernameAlreadyExists
from cunsomException import PasswordTooShort
import cunsomException
class User:
    def __init__(self, username, password):
        '''Create a new user object . The password will be
         encrypted before storing'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        '''Encrypt the password with the username and return the sha digest'''
        hash_string = (self.username+password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        '''Return True if the passwod is valid for this user, false otherwise'''
        encrypted = self._encrypt_pw(password)
        return  encrypted == self.password
class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage user logging in and out.'''
        self.users = {}
    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)
    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise  cunsomException.InvalidUsername(username)
        if not user.check_password(password):
            raise cunsomException.InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
