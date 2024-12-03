adminData = {
    "admin1": "password1"
}
def loginAdmin():
    username = input("Masukkan username: ")
    if username in adminData:
        password = input("Masukkan password: ")
        if password in adminData:
            print("Login berhasil")
        else:
            print("Password salah")
    else:
        print("Username tidak ada di database")
def adminDashboard():
    pass