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
            return True
        else:
            print("Password salah")
            return False
    else:
        print("User tidak ada di database")
def userDashboard():
    print("Welcome to user dashboard")