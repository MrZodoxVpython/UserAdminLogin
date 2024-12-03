userData = {
    "user1": "password1"
}
def loginUser():
    username = input("Masukkan username: ")
    if username in userData:
        password = input("Masukkan password: ")
        if password in userData:
            print("Login berhasil")
        else:
            print("Password salah")
    else:
        ("User tidak ada di database")
def userDashboard():
    pass