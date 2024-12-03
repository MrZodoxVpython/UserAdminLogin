adminData = {
    "admin1": "password1"
}
def loginAdmin():
    username = input("Masukkan username: ")
    if username in adminData:
        password = input("Masukkan password: ")
        p = len(adminData[username])
        if password in adminData[username] and len(password) == p:
            print("Login berhasil")
            return True
        else:
            print("Password salah")
            return False
    else:
        print("Username tidak ada di database")
def adminDashboard():
    print("Welcome to admin dashboard")