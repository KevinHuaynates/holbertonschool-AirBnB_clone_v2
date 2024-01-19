#!/usr/bin/python3
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    def close(self):
        """Calls remove() method on the private
        session attribute (self.__session)"""
        self.__session.close()
