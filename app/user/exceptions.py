from uuid import UUID

class UserNotFoundError(Exception):
    def __init__(self, email:str):
        self.email = email
        super().__init__(f"No user found with email: {email}")

class UserNotFoundByIdError(Exception):
    def __init__(self, id:UUID):
        self.id = id
        super().__init__(f"No user found with id: {id}")