from security.authentication_provider.abstract_authentication_provider import Abstract_Authentication_Provider
import sqlalchemy as sqlalchemy
import database.authentication_models as authentication_models
from flask import Flask
import safrs
from dotmap import DotMap  # a dict, but you can say aDict.name instead of aDict['name']... like a row
from sqlalchemy import inspect

# **********************
# sql auth provider
# **********************

db = safrs.DB         # Use the safrs.DB, not db!
session = db.session  # sqlalchemy.orm.scoping.scoped_session

class Authentication_Provider(Abstract_Authentication_Provider):

    @staticmethod
    def get_user(id: str, password: str) -> object:
        """
        Must return a row object with attributes name and role_list
        role_list is a list of row objects with attribute name

        TP: id / pwd or token

        row object is a SQLAlchemy row (could have been a DotMap)

        Row Caution: https://docs.sqlalchemy.org/en/14/errors.html#error-bhk3
        """

        def row_to_dotmap(row, row_class):
            rtn_dotmap = DotMap()
            mapper = inspect(row_class)
            for each_column in mapper.columns:
                rtn_dotmap[each_column.name] = getattr(row, each_column.name)
            return rtn_dotmap


        user = session.query(authentication_models.User).filter(authentication_models.User.id == id).one()
        rtn_user = row_to_dotmap(user, authentication_models.User)
        rtn_user.UserRoleList = []
        user_roles = getattr(user, "UserRoleList")
        for each_row in user_roles:
            each_user_role = row_to_dotmap(each_row, authentication_models.UserRole)
            rtn_user.UserRoleList.append(each_user_role)
        return rtn_user  # returning user fails per caution above
