# test aql hanling module
import pytest
from modules.db_manager import *

test_userID = "U20testtest"

def test_check_user_id():
    assert check_user_id("test")
    assert check_user_id(1111)

def test_check_record():
    assert create_record()

def test_delete_record():
    assert delete_record()

def test_set_artist_data():
    assert set_artist_data()

def test_set_similar_user():
    assert set_similar_user()

def test_get_user_record():
    assert get_user_record()
