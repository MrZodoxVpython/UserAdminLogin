from user import loginUser, userDashboard
from admin import loginAdmin, adminDashboard
def loginUserVerification():
    if loginUser():
        userDashboard()
def loginAdminVerification():
    if loginAdmin():
        adminDashboard()