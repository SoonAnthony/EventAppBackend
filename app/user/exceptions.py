

class UserNotFoundError(Exception):
    def __init__(self, email:str):
        self.email = email
        super().__init__("No user found with {email}")