userData = {
    "user1": "password1"
}
def loginUser():
    username = input("Masukkan username: ")
    if username in userData:
        password = input("Masukkan password: ")
        p = len(userData[username])
        if password in userData[username] and len(password) == p:
            print("Login berhasil")
        else:
            print("Password salah")
    else:
        print("User tidak ada di database")
def userDashboard():
    pass