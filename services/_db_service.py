from sqlalchemy.orm import Session


class DbService:
    def __init__(self, db: Session):
        """Base class used for all services to connect to db"""
        self.db = db
