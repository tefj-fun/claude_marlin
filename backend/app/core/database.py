from typing import List, Optional
from ..models.user import User, UserCreate

class Database:
    def __init__(self) -> None:
        self.users: List[User] = []
        self._id = 1

    def create_user(self, data: UserCreate) -> User:
        user = User(id=self._id, username=data.username, email=data.email, password=data.password)
        self.users.append(user)
        self._id += 1
        return user

    def get_user(self, username: str) -> Optional[User]:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def list_users(self) -> List[User]:
        return self.users


db = Database()
