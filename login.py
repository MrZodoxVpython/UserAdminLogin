from user import loginUser, userDashboard
from admin import loginAdmin, adminDashboard
def loginUserVerification():
    if loginUser():
        userDashboard()
    else:
        print("Login gagal")
def loginAdminVerification():
    if loginAdmin():
        adminDashboard()