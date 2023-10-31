import os
import pandas as pd
from tabulate import tabulate as tb
import sys
import time
from admin import view_data_jadwal
from admin import linear_search
import admin
from admin import quick_sort

def loadingtext(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.5)


def menu_kurir():
    os.system('cls')
    print('='*36)
    print("<<<<<<< Pilih Opsi Pada Menu >>>>>>>")
    print('='*36)
    print("[1] Lihat Jadwal pengiriman")
    print("[2] tujuan pengiriman")
    print("[3] Keluar")
    print("<= = = = = = = = = = = = = = = = = =>")
    print("")
    pilih_menu_kurir = input("Pilih Opsi: ")
    if pilih_menu_kurir == "1":
        view_data_jadwal()
        print("""
        >>>>> Pilih Opsi <<<<<

        [1] Ubah Status Pengiriman
        [2] Cari Data
        [3] Urutkan Data
        [4] Kembali ke Menu
        """)
        while True:
            pilih = input("Masukkan opsi : ")
            if pilih == "1":
                confirm = input("Apakah anda yakin?(y/n): ")
                if confirm.lower() == "y":
                    file_jadwal = "jadwal_pengiriman.csv"
                    data_jadwal = pd.read_csv(file_jadwal)
                    nomer = int(input('\nMasukkan baris yang akan anda ubah statusnya : '))
                    data_jadwal.loc[nomer-1,'Status'] = "Sudah Terkirim"
                    data_jadwal.to_csv(file_jadwal, index = False)
                    admin.ketik("Status berhasil dirubah...")
                    print("\n \t<< Hasil Perubahan >>")
                    view_data_jadwal()
                    print("")
                    x= input("Kik ENTER Untuk Kembali Ke Menu ....")
                    menu_kurir()
                elif confirm.lower() == "n":
                    menu_kurir()
            elif pilih == "2":
                def search():
                    file_jadwal = "jadwal_pengiriman"
                    print("\n\n1) cari berdasarkan Tanggal")
                    print("2) cari berdasarkan Nama")
                    print("3) cari berdasarkan Kota")
                    print("4) cari berdasarkan Barang")
                    print("5) cari berdasarkan Berat(kg)")
                    print("6) cari berdasarkan Status")
                    print("0) kembali")
                    opsi = input("masukan opsi: ")
                    if opsi == "1":
                        view_data_jadwal()
                        settanggal = input("Tanggal berapa yang mau di cari?(yyyy-mm-dd) : ")
                        linear_search(settanggal, 0, file_jadwal)
                        search()
                    elif opsi == "2":
                        cari_jumlah = input("Nama apa yang di cari? : ")
                        linear_search(cari_jumlah, 1, file_jadwal)
                        search()
                    elif opsi == "3":
                        cari_jumlah = input("jumlah berapa yang dicari? : ")
                        linear_search(cari_jumlah, 2, file_jadwal)
                        search()
                    elif opsi == "4":
                        cari_jumlah = input("jumlah berapa yang dicari? : ")
                        linear_search(cari_jumlah, 3, file_jadwal)
                        search()
                    elif opsi == "5":
                        cari_jumlah = int(input("jumlah berapa yang dicari? : "))
                        linear_search(cari_jumlah, 4, file_jadwal)
                        search()
                    elif opsi == "6":
                        cari_harga = int(input("harga yang yang dicari? : "))
                        linear_search(cari_harga, 5, file_jadwal)
                        search()
                    elif opsi == "0":
                        menu_kurir()
                    else:
                        print("Invalid Input masukan input yang benar")
                        search()
                search()
            elif pilih == "3":
                urutkan_data_jadwal()
            elif pilih == "4":
                print("Kembali ke Menu")
                time.sleep(1.5)
                menu_kurir()
            else:
                print("Opsi tidak ada, Masukan opsi yang benar!")
                time.sleep(1.5)
                continue

    elif pilih_menu_kurir == "2":
        is_reverse = True
        while is_reverse:
            os.system('cls')
            tujuan_pengiriman()
            userFalse = True
            while userFalse:
                loop = input("APAKAH ANDA INGIN MENCARI ROUTE LAGI ? y/n : ").lower()
                if loop == 'y':
                    userFalse = False
                    continue
                elif loop == 'n':
                    menu_kurir()
                else:
                    print("Input Invalid")
                    print("Masukkan Huruf y/n")
                    continue
    elif pilih_menu_kurir == "3":
        print("Anda Akan Keluar")
        loadingtext("Sedang Logout")
        exit()
    else:
        print("pilihan yang anda masukan tidak ada pada obsi")
        menu_kurir()

def tujuan_pengiriman():
    print("\n<<<<<<< MENEMUKAN ROUTE TERDEKAT ANTAR KOTA >>>>>>>\n")
    print('='*36)
    print("JEMBER\t\t\t BONDOWOSO\t\t BANYUWANGI\nLUMAJANG\t\t BESUKI\t\t\t SITUBONDO\nPROBOLINGGO")
    print('='*36)
    list_jarak = {
        'jember': {'bondowoso': 40, 'banyuwangi': 103, 'lumajang': 73.8},
        'bondowoso': {'jember': 40, 'situbondo': 34.7, 'besuki': 35.6},
        'banyuwangi': {'jember': 103, 'situbondo': 96},
        'lumajang': {'jember': 73.8, 'probolinggo': 45},
        'besuki': {'probolinggo': 61, 'situbondo': 39.5, 'bondowoso' : 35.6},
        'situbondo' : {'besuki' : 39.5, 'banyuwangi' : 96, 'bondowoso' : 34.7},
        'probolinggo' : {'besuki' : 61, 'lumajang' : 45}
    }

    route_kurir = []
    kota_asal = input("TEMPAT ANDA SEKARANG : ").lower()
    kota_tujuan = input("MASUKKAN KOTA TUJUAN : ").lower()

    if (kota_asal not in list_jarak) or (kota_tujuan not in list_jarak):
        print("INPUT INVALID")
        tujuan_pengiriman()
    elif (kota_asal == kota_tujuan):
        print(f"\nANDA TELAH BERADA DALAM KOTA {kota_asal.upper()}")
    else: 
        route = FindRoute(kota_asal, list_jarak)

        tmp_kotaTujuan = kota_tujuan

        while tmp_kotaTujuan != kota_asal:
            route_kurir.append(tmp_kotaTujuan)
            tmp_kotaTujuan = route[tmp_kotaTujuan]

        route_kurir.reverse()
        print("")
        print(f"ROUTE DARI {kota_asal.upper()} ke {kota_tujuan.upper()} TERDEKAT :")
        print("")
        for i in range(len(route_kurir)):
            print(f'ROUTE KE - {i + 1} : {route_kurir[i].upper()}')


def FindRoute (kota_asal, list_jarak):
    nilai_jarak = sys.maxsize
    jarak = {kota : nilai_jarak for kota in list_jarak}
    jarak[kota_asal] = 0
    visited = []
    route_kota = {}

    while len(visited) < len(list_jarak):
        crr_kota = None
        for kota in list_jarak:
            if kota not in visited and (crr_kota is None or jarak[kota] < jarak[crr_kota]):
                crr_kota = kota
        
        visited.append(crr_kota)
        for tujuan, nilai_jarak in list_jarak[crr_kota].items():
            tmp_jarak = jarak[crr_kota] + nilai_jarak
            if tmp_jarak < jarak[tujuan]:
                jarak[tujuan] = tmp_jarak
                route_kota[tujuan] = crr_kota
    
    return route_kota

def urutkan_data_jadwal():
    os.system('cls')
    print("")
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
        nextPage = input("Klik Enter Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "2":
        notCompleted = df.loc[df['Status'] == "Belum Dikirim"].values.tolist()
        print("\n ===> Hasil Sorting berdasarkan Jumlah <===\n")
        print(tb(notCompleted, headers=["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt= "fancy_grid"))
        print("\n")
        nextPage = input("Klik Enter Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "3":
        Completed = df.loc[df['Status'] == "Sudah Terkirim"].values.tolist()
        print("\n ===> Hasil Sorting berdasarkan Jumlah <===\n")
        print(tb(Completed, headers=["Tanggal", "Nama", "Kota", "Barang", "Berat(kg)", "Status"], tablefmt= "fancy_grid"))
        print("\n")
        nextPage = input("Klik Enter Untuk Kembali ....")
        urutkan_data_jadwal()
    elif pilihurut == "4":
        menu_kurir()
    else:
        print("masukkan input yang benar")
        time.sleep(1.5)
        urutkan_data_jadwal()


def kembali_kurir():
    input("\nTekan ENTER untuk kembali ke Menu...")
    menu_kurir()