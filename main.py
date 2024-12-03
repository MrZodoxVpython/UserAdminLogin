from login import loginUserVerification
from login import loginAdminVerification
def dashboard():
    pilihan = input("1.Login User\n2.Login Admin\nMasukkan pilihan: ")
    if pilihan == "1":
        loginUserVerification()
    if pilihan == "2":
        loginAdminVerification()
dashboard() 