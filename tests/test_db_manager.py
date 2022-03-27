# test aql hanling module
import pytest
from modules.db_manager import *

test_userID = "U20testtest"

def test_check_user_id():
    assert check_user_id("test")