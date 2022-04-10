# test aql hanling module
import os
import tempfile

import pytest
from club_activity_app.app import create_app
from  modules.models import *

app = create_app()
init_db(app)

def test_User():
    user = User(user_token="#thisistoken", user_name="username", mail_address="user@user.com", pass_word="user", done=False)
    assert user

def test_UserList():
    assert UserList().add_user(user_token="#thisistoken", user_name="username", mail_address="user@user.com", pass_word="user")
