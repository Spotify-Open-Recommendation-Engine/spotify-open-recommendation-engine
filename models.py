"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

# def get_user_email():
#     return auth.current_user.get('email') if auth.current_user else None
#
# def get_user():
#     return db(db.auth_user.email == get_user_email()).select().first().id if auth.current_user else None
#
# db.commit()
