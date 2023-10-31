import json
import os
import bcrypt
import time
import getpass
import admin as menuAdmin
import kurir as menuKurir

def hiasan(text:str, centerText:int, accesories:str, centerAccesories:int):
    print(" ")
    print(accesories*centerAccesories)
    print(text.center(centerText))
    print(accesories*centerAccesories)
    print(" ")

def loadingtext(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.5)

def load_account():
    try:
        with open("user.json", "r") as user:
            users = json.load(user)
    except:
        users = {}
    return users

def save_account(data_account):
    with open("user.json", "w") as file:
        json.dump(data_account, file, indent=4)

def register():
    hiasan("CREATE NEW ACCOUNT", 30, "=", 30)
    account = load_account()
    passAcces = "0987654321"
    user_role = ""

    print("DAFTAR SEBAGAI")
    print("1. ADMIN")
    print("2. USERS/KURIR")

    user_choice = input("MASUKKAN PILIHAN ANDA : ")
    if user_choice == "1" :
        acces = input("Masukkan Sandi Acces : ")
        if(acces == passAcces):
            user_role = "Admin"
        else:
            print("Sandi Salah, Anda Tidak dapat mendaftar Sebagai Admin")
            time.sleep(1.5)
            os.system("cls")
            register()
            
    elif user_choice == "2":
        user_role = "users"
    else :
        print("Pilihan Tidak Tersedia")
        time.sleep(1.5)
        os.system("cls")
        print("")
        menuAdmin.ketik("SILAHKAN MASUKKAN KEMBALI DENGAN BENAR")
        print("")
        register()

    username = input("Username : ")
    email = input("Email : ")
    password = input("password : ") 
    if username in account:
        print("Username Ini Telah Terdaftar")
        print("Silahkan Coba Username Yang Lain")
    else:
        encryptPassword = password.encode('utf-8')
        hashed = bcrypt.hashpw(encryptPassword, bcrypt.gensalt(12))
        new_user = {username : {
            "email" : email, 
            "password" : hashed.decode('utf-8'),
            "role" : user_role
            }
        }

        account.update(new_user)
        save_account(account)
        print("ANDA BERHASIL DAFTAR, SILAHKAN LOGIN")
        time.sleep(2)
        login()
        

def login():
    os.system("cls")
    account = load_account()
    hiasan("LOGIN ACCOUNT", 30, "=", 30)
    username = input("Masukkan Username Anda : ")
    password = getpass.getpass("Masukkan Password : ")

    if username not in account:
        print("Username Tidak Di Temukan")
        print("")
        print("SILAHKAN MASUKKAN KEMBALI DENGAN BENAR")
        print("")
        
        while True:
            confirm = input("Apakah Anda Ingin Melanjutkan Login (y/n) :").lower()
            if confirm == "y":
                login()
            elif confirm == "n":
                HomePage()
            else:
                print("Masukkan Input Yang Benar")
                continue

    encodePass = password.encode('utf-8')
    confirmation1 = account[username]["password"].encode('utf-8')


    if username in account and bcrypt.checkpw(encodePass, confirmation1):
        if account[username]["role"] == "Admin":
            print("")
            print("SEDANG MENGALIHKAN KE HALAMAN ADMIN")
            menuAdmin.loading()
            menuAdmin.create_data_file()
            os.system("cls")
            HomePage()
        else :
            print("")
            print("SEDANG MENGALIHKAN KE HALAMAN KURIR")
            menuAdmin.loading()
            menuKurir.menu_kurir()
            HomePage()
            os.system("cls")
    else:
        print("KATA SANDI SALAH")
        print("")
        print("SILAHKAN MASUKKAN KEMBALI DENGAN BENAR")
        time.sleep(2)
        print("")
        login()

def resetPassword():
    os.system("cls")
    hiasan("RESET PASSWORD", 30, "=", 30)
    account = load_account()
    username = input("Masukkan Username Anda : ")
    if username in account:
        email = input("Masukkan Email Verifikasi : ")
        if email == account[username]["email"] :
            newpassword = input("MASUKKAN PASSWORD BARU : ")
            newpassword = newpassword.encode('utf-8')
            hashed = bcrypt.hashpw(newpassword, bcrypt.gensalt(12))
            account[username]["password"] = hashed.decode('utf-8')
            save_account(account)

            print("")
            print("BERHASIL MENGUBAH KATA SANDI")
            loadingtext("MENUJU HALAMAN LOGIN")
            login()

        else:
            print("Alamat Email Tidak Sama")
            loadingtext("MENUJU HALAMAN UTAMA")
        
        HomePage()
    else:
        print("USERNAME TIDAK DI TEMUKAN")
        time.sleep(1.5)
        resetPassword()

def HomePage():
    os.system('cls')
    menuAdmin.ketik("="*29)
    menuAdmin.ketik("||      SELAMAT DATANG     ||")
    menuAdmin.ketik("||      StorageMaster      ||")
    menuAdmin.ketik("||      Solusi Terbaik     ||")
    menuAdmin.ketik("||          untuk          ||")
    menuAdmin.ketik("||  Manajemen Pergudangan  ||")
    menuAdmin.ketik("="*29)

    print("\n","-"*20)
    print("1. Login")
    print("2. Register")
    print("3. Lupa Password")
    print("0. Exit")

    user_choice = input("\nMasukkan Pilihan Anda : ")
    if user_choice == "1":
        os.system("cls")
        login()
    elif user_choice == "2":
        os.system("cls")
        register()
    elif user_choice == "3":
        resetPassword()
    elif user_choice == "0":
        loadingtext("Sedang Logout")
        exit()
    else:
        print("Input Salah")
        HomePage()

HomePage()