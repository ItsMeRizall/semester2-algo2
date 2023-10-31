import time
import os
import pandas as pd
from tabulate import tabulate as tb
import numpy as np
import datetime

def loadingtext(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.5)

def clear():
    os.system("cls")

def ketik(kata):
    u = ''
    for i in kata:
        u += i
        print("\r",u,end='')
        time.sleep(0.005)
    print()

def loading():
    for i in range(1,101):
        time.sleep(0.005)
        print(f"\rLoading {i}%",end="") 
    print("\nLoading selesai...\n")

def view_data():
    file = f"{data_base}.csv"
    reader = pd.read_csv(file)
    reader.index = np.arange(1, len(reader) + 1)
    print(tb(reader, headers=["Nama", "Jumlah(kg)", "Harga"], tablefmt="fancy_grid"))

def partisi(array, low, high, indeks):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j][indeks] < pivot[indeks] :
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high, indeks):
    if low < high:
        pivot_index = partisi(array, low, high, indeks)
        quick_sort(array, low, pivot_index - 1, indeks)
        quick_sort(array, pivot_index + 1, high, indeks)

def create_data_file():
    clear()
    print("<<===============>>")
    print("[1] create newdata" )    
    print("[2] load data" )
    print("[3] Logout" )
    print(">>===============<<")
    global data_base
    pilih = input("\nsilahkan memilih : ")
    if pilih == "1":

        data_base = input("masukkan nama file : ")
        with open(f"{data_base}.csv","w",encoding="utf-8") as file_new:
            nama = "Nama"
            Jumlah = "Jumlah(kg)"
            harga = "Harga"
            data_str = f"{nama},{Jumlah},{harga}"
            file_new.write(data_str)
    elif pilih == "2":    
        data_base = input(f"masukkan nama data yang ingin anda load\n==> ")
        if os.path.exists(f"{data_base}.csv") :
            dataBase_Benar()
        else:
            dataBase_Salah()
    elif pilih == "3":
        loadingtext("Terima Kasih telah menggunakan Program ini")
        print("")
        loadingtext("Sedang Logout")
        exit()
    else:
        print("nomor yang anda masukkan tidak valid")
        time.sleep(1.5)
        create_data_file()
        
def hapus_data_gudang():
    clear()
    global data_file
    file = f"{data_base}.csv"
    data_file = pd.read_csv(file)
    view_data()
    print("""\n
    pilih baris pada data tersebut:
    *Note: masukan angka 0 apabila ingin membatalkan""")
    x = int(input("\nData baris keberapa yang mau dihapus: "))
    if x == 0:
        back =input("apakah anda ingin membatalakan penghapusan baris?(y/t)")
        if back == "y":
            loading()
            kembali_admin()
        elif back == "t":
            loading()
            clear()
            hapus_data_gudang()
    elif x in list(range(len(data_file)+1)):
        data_file.drop(index= x-1,inplace=True)
        data_file.index = list(range(len(data_file)))
        data_file.to_csv(file, index= False)
        loading()
        ketik("Item berhasil dihapus")
        ketik("Silahkan anda cek pada menu Lihat Data")
        kembali_admin()
    else:
        print('No baris yang anda inputkan salah')
        input('Tekan Enter untuk memasukkan nomor yang benar pada data')
        loading()
        clear()
        hapus_data_gudang()

def tambah_data_file():
    clear()
    global data_file 
    file = f"{data_base}.csv"
    data_file = pd.read_csv(file)
    view_data()
    print("\n")
    ketik("masukan hasil pertanian apa yang mau ditambah")
    nama = input("Nama \t: ")
    Jumlah = int(input("Jumlah \t: "))
    harga = int(input("Harga \t: "))
    data_file.loc[len(data_file)] = {'Nama':nama,'Jumlah(kg)': Jumlah, 'Harga' : harga}
    data_file.index = list(range(len(data_file)))
    data_file.to_csv(file, index = False)
    loading()
    ketik("Item Berhasil Ditambahkan")
    ketik("Silahkan cek pada menu Lihat Data")
    kembali_admin()
    print()

def edit_data_gudang():
    file = f"{data_base}.csv"
    data_gudang = pd.read_csv(file)
    def edit_satu_baris():
        view_data()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))
        nama = input("Nama Barang : ")
        Jumlah = int(input("Jumlah : "))
        harga = int(input("Harga : "))
        data_kebutuhan = [nama, Jumlah, harga]
        data_gudang.loc[nomer-1] = data_kebutuhan
        data_gudang.to_csv(file, index = False)
        view_data()
        print('data berhasil di edit')

    def edit_barang():
        view_data()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        barang = input("Nama Barang : ")
        data_gudang.loc[nomer-1,'Nama'] = barang
        data_gudang.to_csv(file, index = False)
        view_data()
        print('data berhasil di edit')

    def edit_jumlah():
        view_data()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        jumlah = int(input("Jumlah : "))
        data_gudang.loc[nomer-1,'Jumlah(kg)'] = jumlah
        data_gudang.to_csv(file, index = False)
        view_data()
        print('data berhasil di edit')

    def edit_harga():
        view_data()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        harga = int(input("Harga : "))
        data_gudang.loc[nomer-1,'Harga'] = harga
        data_gudang.to_csv(file, index = False)
        view_data()

    print("\n<==== MENU EDIT ====>")
    print("1) Edit Satu Baris")
    print("2) Edit Nama Barang")
    print("3) Edit Jumlah Barang ")
    print("4) Edit Harga Satuan Barang")
    print("5) Kembali")
    print("<= = = = = = = = = = =>")    
    pilih_edit = input('Pilih Menu > ')
    if pilih_edit == "1":
        edit_satu_baris()
        edit_data_gudang()
    elif pilih_edit == "2":
        edit_barang()
        edit_data_gudang()
    elif pilih_edit == "3":
        edit_jumlah()
        edit_data_gudang()
    elif pilih_edit == "4":
        edit_harga()
        edit_data_gudang()
    elif pilih_edit == "5":
        kembali_admin()
    else:
        print(f'menu {pilih_edit} tidak ada')
        edit_data_gudang()

def cari_data_gudang():
    print("1) cari berdasarkan nama")
    print("2) cari berdasarkan Jumlah")
    print("3) cari berdasarkan harga")
    print("4) kembali")
    opsi = input("masukan opsi: ")
    if opsi == "1":
        view_data()
        cari_nama = input("nama apa yang dicari? : ") 
        linear_search(cari_nama, 0, data_base)
        cari_data_gudang()
    elif opsi == "2":
        cari_jumlah = int(input("jumlah berapa yang dicari? : "))
        linear_search(cari_jumlah, 1, data_base)
        cari_data_gudang()
    elif opsi == "3":
        cari_harga = int(input("harga yang yang dicari? : "))

        linear_search(cari_harga, 2, data_base)
        cari_data_gudang()
    elif opsi == "4":
        lihat_data_file()
    else:
        print("Invalid Input masukan input yang benar")
        cari_data_gudang()

def linear_search(cari,kolom, data_base):
    file = f"{data_base}.csv"
    data_file = pd.read_csv(file)
    data_ditemukan = []

    for index, row in data_file.iterrows():
        if isinstance(row[kolom], str):
            if str(row[kolom]).lower() == cari.lower():
                data_ditemukan.append(row)
        elif row[kolom] == cari:
            data_ditemukan.append(row)
    
    if len(data_ditemukan) > 0:
        if data_base == "jadwal_pengiriman":
            print("\n == Hasil Pencarian ==\n")
            result = []
            for i, data in enumerate(data_ditemukan, start=1):
                result.append([i] + data.tolist())
            print(tb(result, ["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt="fancy_grid"))
        else:
            print("\n == Hasil Pencarian ==\n")
            result = []
            for i, data in enumerate(data_ditemukan, start=1):
                result.append([i] + data.tolist())
            print(tb(result, ["Nama", "Jumlah(kg)", "Harga"], tablefmt="fancy_grid"))
    else:
        print("tidak ditemukan.")
        time.sleep(1.5)

def hapus_data_jadwal():
    clear()
    file_jadwal = "jadwal_pengiriman.csv"
    data_jadwal = pd.read_csv(file_jadwal)
    view_data_jadwal()
    print("""\n
    pilih baris pada data tersebut:
    *Note: masukan angka 0 apabila ingin membatalkan""")
    x = int(input("\nData baris keberapa yang mau dihapus: "))
    if x == 0:
        back =input("apakah anda ingin membatalakan penghapusan baris?(y/t)")
        if back == "y":
            loading()
            kembali_kurir()
        elif back == "t":
            loading()
            clear()
            hapus_data_jadwal()
    elif x in list(range(len(data_jadwal)+1)):
        data_jadwal.drop(index= x-1,inplace=True)
        data_jadwal.index = list(range(len(data_jadwal)))
        data_jadwal.to_csv(file_jadwal, index= False)
        loading()
        ketik("Item berhasil dihapus")
        ketik("Silahkan anda cek pada menu Lihat Data")
        time.sleep(2)
        menu_jadwal()
    else:
        print('No baris yang anda inputkan salah')
        input('Tekan Enter untuk memasukkan nomor yang benar pada data')
        loading()
        clear()
        hapus_data_jadwal()


def edit_data_jadwal():
    file_jadwal = "jadwal_pengiriman.csv"
    data_jadwal = pd.read_csv(file_jadwal)
    def satu_baris():
        view_data_jadwal()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))
        tanggal = input("masukan tanggal(yyyy-mm-dd): ")
        Nama = input("Nama \t: ")
        kota = input("kota tujuan \t: ")
        barang = input("masukan nama barang \t: ")
        Jumlah = int(input("Berat(kg) \t: "))
        status = "Belum Dikirim"
        data_kebutuhan = [tanggal, Nama, kota, barang, Jumlah, status]
        data_jadwal.loc[nomer-1] = data_kebutuhan
        data_jadwal.to_csv(file_jadwal, index = False)
        view_data_jadwal()
        print('data berhasil di edit')

    def edit_tanggal():
        view_data_jadwal()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        tanggal = input("masukan tanggal(yyyy-mm-dd): ")
        data_jadwal.loc[nomer-1,'Tanggal'] = tanggal
        print(data_jadwal)
        data_jadwal.to_csv(file_jadwal, index = False)
        view_data_jadwal()
        print('data berhasil di edit')

    def edit_kota():
        view_data_jadwal()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        kota = input("kota tujuan \t: ")
        data_jadwal.loc[nomer-1,'Kota'] = kota
        data_jadwal.to_csv(file_jadwal, index = False)
        view_data_jadwal()

    def edit_nama_barang():
        view_data_jadwal()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        barang = input("masukan nama barang \t: ")
        data_jadwal.loc[nomer-1,'Barang'] = barang
        data_jadwal.to_csv(file_jadwal, index = False)
        view_data_jadwal()

    def edit_berat_barang():
        view_data_jadwal()
        nomer = int(input('\nMasukkan baris yang ingin diedit : '))        
        Jumlah = int(input("Berat(kg) \t: "))
        data_jadwal.loc[nomer-1,'Berat(kg)'] = Jumlah
        data_jadwal.to_csv(file_jadwal, index = False)
        view_data_jadwal()

    print("\n<==== MENU EDIT ====>")
    print("1) Edit Satu Baris")
    print("2) Edit Tanggal")
    print("3) Edit Kota Tujuan")
    print("4) Edit Nama Barang ")
    print("5) Edit Berat Barang")
    print("6) Kembali")
    print("<= = = = = = = = = = =>")    
    pilih_edit = input('Pilih Menu > ')
    if pilih_edit == "1":
        satu_baris()
        edit_data_jadwal()
    elif pilih_edit == "2":
        edit_tanggal()
        edit_data_jadwal()
    elif pilih_edit == "3":
        edit_kota()
        edit_data_jadwal()
    elif pilih_edit == "4":
        edit_nama_barang()
        edit_data_jadwal()
    elif pilih_edit == "5":
        edit_berat_barang()
        edit_data_jadwal()
    elif pilih_edit == "6":
        kembali_kurir()
    else:
        print(f'menu {pilih_edit} tidak ada')
        edit_data_jadwal()

def lihat_data_jadwal():
    view_data_jadwal()
    print("\n<==== MENU ====>")
    print("1) UrutKan Data")
    print("2) Cari Data")
    print("0) Kembali")
    print("<= = = = = = = = = = =>")  
    chose = input('Pilih Menu > ')
    if chose == "1":
        urutkan_data_jadwal()
    elif chose == "2":
        cari_data_jadwal()
    elif chose == "0":
        kembali_kurir()
    else:
        print("masukkan input yang benar !!!")
        time.sleep(1.5)
        lihat_data_jadwal()

def urutkan_data_jadwal():
    clear()
    df = pd.read_csv("jadwal_pengiriman.csv")
    dataJadwal = df.values.tolist()

    print("--- MENU SORTING ---\n")
    print("1) Urutkan Berdasarkan Tanggal")
    print("2) Tampilkan jadwal Yang Belum Dikirim")
    print("3) Tampilkan Jadwal Yang Telah Dikirim")
    print("4) kembali")
    pilihurut = input("masukan opsi: ")
    if pilihurut ==  "1":
        quick_sort(dataJadwal, 0, len(dataJadwal)-1, 0)
        print("\n ===> Hasil Sorting berdasarkan Nama <===\n")
        print(tb(dataJadwal, headers=["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt= "fancy_grid"))
        print("\n")
        x = input("Tekan ENTER Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "2":
        notCompleted = df.loc[df['Status'] == "Belum Dikirim"].values.tolist()
        print("\n ===> Hasil Sorting berdasarkan Status Belum Dikirim <===\n")
        print(tb(notCompleted, headers=["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt= "fancy_grid"))
        print("\n")
        x = input("Tekan ENTER Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "3":
        Completed = df.loc[df['Status'] == "Sudah Terkirim"].values.tolist()
        print("\n ===> Hasil Sorting berdasarkan Status Sudah Dikirim <===\n")
        print(tb(Completed, headers=["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt= "fancy_grid"))
        print("\n")
        x = input("Tekan ENTER Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "4":
        lihat_data_jadwal()
    else:
        print("masukkan input yang benar")
        time.sleep(1.5)
        urutkan_data_file()

def cari_data_jadwal():
    file_jadwal = "jadwal_pengiriman"
    print("\n\n1) cari berdasarkan Tanggal")
    print("2) cari berdasarkan Nama")
    print("3) cari berdasarkan Kota")
    print("4) cari berdasarkan Barang")
    print("5) cari berdasarkan Berat(kg)")
    print("0) kembali")
    opsi = input("masukan opsi: ")
    if opsi == "1":
        view_data_jadwal()
        settanggal = input("Tanggal berapa yang mau di cari?(yyyy-mm-dd) : ")
        linear_search(settanggal, 0, file_jadwal)
        cari_data_jadwal()
    elif opsi == "2":
        cari_nama = input("Nama apa yang di cari? : ")
        linear_search(cari_nama, 1, file_jadwal)
        cari_data_jadwal()
    elif opsi == "3":
        cari_kota = input("Kota apa yang dicari? : ")
        linear_search(cari_kota, 2, file_jadwal)
        cari_data_jadwal()
    elif opsi == "4":
        cari = input("Barang apa yang dicari? : ")
        linear_search(cari, 3, file_jadwal)
        cari_data_jadwal()
    elif opsi == "5":
        cari_jumlah = int(input("jumlah berapa yang dicari? : "))
        linear_search(cari_jumlah, 4, file_jadwal)
        cari_data_jadwal()
    elif opsi == "0":
        lihat_data_jadwal()
    else:
        print("Invalid Input masukan input yang benar")
        cari_data_jadwal()

def view_data_jadwal():
    file_jadwal = "jadwal_pengiriman.csv"
    reader_jadwal = pd.read_csv(file_jadwal)
    reader_jadwal.index = np.arange(1, len(reader_jadwal) + 1)
    print(tb(reader_jadwal,["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt="fancy_grid"))

def tambah_data_jadwal():
    clear()
    file_jadwal = "jadwal_pengiriman.csv"
    data_jadwal = pd.read_csv(file_jadwal)
    view_data_jadwal()
    print("\n")
    ketik("masukan hasil apa yang mau ditambah")
    tanggal = input("masukan tanggal(yyyy-mm-dd): ")
    nama = input("Nama \t\t\t: ")
    kota = input("kota tujuan \t\t: ")
    barang = input("masuukan nama barang \t: ")
    Jumlah = int(input("Berat(kg) \t\t: "))
    data_jadwal.loc[len(data_jadwal)] = {'Tanggal':tanggal, 'Nama':nama, 'Kota':kota, 'Barang': barang, 'Berat(kg)': Jumlah, 'Status' : "Belum Dikirm"}
    data_jadwal.index = list(range(len(data_jadwal)))
    data_jadwal.to_csv(file_jadwal, index = False)
    loading()
    ketik("Item Berhasil Ditambahkan")
    ketik("Silahkan cek pada menu Lihat Data")
    time.sleep(2)
    menu_jadwal()

def dataBase_Benar():
    file = f"{data_base}.csv"
    data_file = pd.read_csv(file)
    ketik("data sedang diproses")
    loading()
    time.sleep(1.5) 
    menu_admin()

def dataBase_Salah():
    print("nama data tersebut tidak ada")
    konfirmasi = input("apakah anda ingin menambahakan data yang baru dengan menggunakn nama file tersebut??(y/n)")
    if konfirmasi == "y":
        with open(f"{data_base}.csv","w",encoding="utf-8") as file_new:
            nama = "Nama"
            Jumlah = "Jumlah(kg)"
            harga = "Harga"
            data_str = f"{nama},{Jumlah},{harga}"
            file_new.write(data_str)
        menu_admin()
    elif konfirmasi == "n":
        create_data_file()
    else:
        print("masukan jawaban yang valid !!!")
        time.sleep(1.5)
        dataBase_Salah()

def menu_admin():
    clear()
    print('='*36)
    print("<<<<<<< Pilih Opsi Pada Menu >>>>>>>")
    print('='*36)
    print("[1] Data Gudang")
    print("[2] Data Jadwal")
    print("[3] Keluar")
    pilih = input("Pilih Opsi: ")
    if pilih == "1":
        menu_gudang_admin()
    elif pilih == "2":
        menu_jadwal()
    elif pilih == "3":
        create_data_file()


def menu_gudang_admin():
    clear()
    print('='*36)
    print("<<<<<<< Pilih Opsi Pada Menu >>>>>>>")
    print('='*36)
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Hapus Data")
    print("[4] Edit Data")
    print("[0] Back")
    print("<= = = = = = = = = = = = = = = = = =>")
    pilih_menu_admin = input("Pilih Opsi: ")
    if pilih_menu_admin == "1":
        lihat_data_file()
    elif pilih_menu_admin == "2":
        tambah_data_file()
    elif pilih_menu_admin == "3":
        hapus_data_gudang()
    elif pilih_menu_admin == "4":
        edit_data_gudang()
    elif pilih_menu_admin == "0":
        menu_admin()
    else:
        print("pilihan yang anda masukan tidak ada pada obsi")
        menu_gudang_admin()


def menu_jadwal():
    clear()
    print('='*36)
    print("<<<<<<< Pilih Opsi Pada Menu >>>>>>>")
    print('='*36)
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Hapus Data")
    print("[4] Edit Data")
    print("[0] Back")
    print("<= = = = = = = = = = = = = = = = = =>")
    pilih_jadwal_admin = input("Pilih Opsi: ")
    if pilih_jadwal_admin == "1":
        lihat_data_jadwal()
    elif pilih_jadwal_admin == "2":
        tambah_data_jadwal()
    elif pilih_jadwal_admin == "3":
        hapus_data_jadwal()
    elif pilih_jadwal_admin == "4":
        edit_data_jadwal()
    elif pilih_jadwal_admin == "0":
        menu_admin()
    else:
        print("Masukan opsi yang valid")
        time.sleep(1.5)
        menu_jadwal()

def kembali_admin():
    input("\nTekan ENTER untuk kembali ke Menu...")
    menu_gudang_admin()

def kembali_kurir():
    input("\nTekan ENTER untuk kembali ke Menu...")
    menu_jadwal()

def lihat_data_file():
    clear()
    view_data()
    print("\n<==== MENU ====>")
    print("1) UrutKan Data")
    print("2) Cari Data")
    print("0) Kembali")
    print("<= = = = = = = = = = =>")  
    chose = input('\nPilih Menu --> ')
    if chose == "1":
        urutkan_data_file()
    elif chose == "2":
        cari_data_gudang()
    elif chose == "0":
        kembali_admin()
    else:
        print("masukkan input yang benar !!!")
        time.sleep(1.5)
        lihat_data_file()

def urutkan_data_file():
    file = f"{data_base}.csv"
    data_file = pd.read_csv(file)
    list_gudang = data_file.values.tolist()
    print("~"*30)
    print("1) urutkan berdasarkan nama")
    print("2) urutkan berdasarkan Jumlah")
    print("3) urutkan berdasarkan harga")
    print("4) kembali")
    pilihurut = input("masukan opsi: ")
    if pilihurut ==  "1":
        clear()
        quick_sort(list_gudang, 0, len(list_gudang)-1, 0)
        print("\n ===> Hasil Sorting berdasarkan Nama <===\n")
        print(tb(list_gudang, headers=["Nama", "Jumlah(kg)", "Harga"], tablefmt= "fancy_grid"))
        print("\n")
        urutkan_data_file()
    elif pilihurut == "2":
        clear()
        quick_sort(list_gudang, 0, len(list_gudang)-1, 1)
        print("\n ===> Hasil Sorting berdasarkan Jumlah <===\n")
        print(tb(list_gudang, headers=["Nama", "Jumlah(kg)", "Harga"], tablefmt= "fancy_grid"))
        print("\n")
        urutkan_data_file()
    elif pilihurut == "3":
        clear()
        quick_sort(list_gudang, 0, len(list_gudang)-1, 2)
        print("\n ===> Hasil Sorting berdasarkan Harga <===\n")
        print(tb(list_gudang, headers=["Nama", "Jumlah(kg)", "Harga"], tablefmt= "fancy_grid"))
        print("\n")
        urutkan_data_file()
    elif pilihurut == "4":
        lihat_data_file()
    else:
        print("masukkan input yang benar")
        time.sleep(1.5)
        urutkan_data_file()