# # import os
# # import time

# # class Lapangan:
# #     def __init__(self, jenis, jadwal):
# #         self.jenis = jenis
# #         self.jadwal = jadwal

# #     def tampilkan_jadwal(self):
# #         os.system('cls')
# #         for i, jadwal in enumerate(self.jadwal):
# #             print(f"{i+1}. {jadwal}")
# #         time.sleep(2)

# #     def pesan_lapangan(self, tanggal, jam_mulai, jam_selesai):
# #         jadwal_baru = f"{tanggal} {jam_mulai}-{jam_selesai}"
# #         for jadwal in self.jadwal:
# #             if jadwal_baru == jadwal:
# #                 os.system('cls')
# #                 print("The schedule is booked!")
# #                 time.sleep(2)
# #                 break
# #         else:
# #             self.jadwal.append(jadwal_baru)
# #             os.system('cls')
# #             print("successfully booked!")
# #             time.sleep(2)

# #     def batal_pesan_lapangan(self, tanggal, jam_mulai, jam_selesai):
# #         jadwal_batal = f"{tanggal} {jam_mulai}-{jam_selesai}"
# #         if jadwal_batal in self.jadwal:
# #             self.jadwal.remove(jadwal_batal)
# #             os.system('cls')
# #             print("succesfully cancellation booked")
# #             time.sleep(2)
# #         else:
# #             os.system('cls')
# #             print("Schedule not found!")
# #             time.sleep(2)

# # class Booking:
# #     def __init__(self):
# #         self.lapangan_futsal = Lapangan("Futsal", [])
# #         self.lapangan_bulutangkis = Lapangan("Bulutangkis", [])

# #     def tampilkan_menu(self):
# #         os.system('cls')
# #         print("1. Tampilkan jadwal bookingan lapangan futsal")
# #         print("2. Tampilkan jadwal bookingan lapangan bulutangkis")
# #         print("3. Booking lapangan futsal")
# #         print("4. Booking lapangan bulutangkis")
# #         print("5. Batalkan bookingan lapangan futsal")
# #         print("6. Batalkan bookingan lapangan bulutangkis")
# #         print("0. Exit")

# #     def main(self):
# #         while True:
# #             self.tampilkan_menu()
# #             pilihan = input("Menu (0/1/2/3/4/5/6): ")
# #             if pilihan == "1":
# #                 self.lapangan_futsal.tampilkan_jadwal()
# #             elif pilihan == "2":
# #                 self.lapangan_bulutangkis.tampilkan_jadwal()
# #             elif pilihan == "3":
# #                 tanggal = input("Date (YYYY-MM-DD): ")
# #                 jam_mulai = input("Start Time (HH:MM): ")
# #                 jam_selesai = input("End Time (HH:MM): ")
# #                 self.lapangan_futsal.pesan_lapangan(tanggal, jam_mulai, jam_selesai)
# #             elif pilihan == "4":
# #                 tanggal = input("Tanggal (YYYY-MM-DD): ")
# #                 jam_mulai = input("Start Time (HH:MM): ")
# #                 jam_selesai = input("End Time (HH:MM): ")
# #                 self.lapangan_bulutangkis.pesan_lapangan(tanggal, jam_mulai, jam_selesai)
# #             elif pilihan == "5":
# #                 tanggal = input("Date (YYYY-MM-DD): ")
# #                 jam_mulai = input("Start Time (HH:MM): ")
# #                 jam_selesai = input("End Time (HH:MM): ")
# #                 self.lapangan_futsal.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
# #             elif pilihan == "6":
# #                 tanggal = input("Date (YYYY-MM-DD): ")
# #                 jam_mulai = input("Start Time (HH:MM): ")
# #                 jam_selesai = input("End Time (HH:MM): ")
# #                 self.lapangan_bulutangkis.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
# #             elif pilihan == "0":
# #                 os.system('cls')
# #                 print("Thank You! My sista Zainab said it")
# #                 break
# #             else:
# #                 os.system('cls')
# #                 print("option is not available")
# #                 time.sleep(2)
                
# # if __name__ == "__main__":
# #     booking = Booking()
# #     booking.main()



# import os
# import time

# class zainab:
#     def __init__(self, jenis, jadwal, harga_sewa):
#         self.jenis = jenis
#         self.jadwal = jadwal
#         self.harga_sewa = harga_sewa

#     def tampilkan_jadwal(self):
#         os.system('cls')
#         for i, jadwal in enumerate(self.jadwal):
#             print(f"{i+1}. {jadwal}")
#         time.sleep(2)

#     def pesan_lapangan(self, tanggal, jam_mulai, jam_selesai, dp):
#         jadwal_baru = f"{tanggal} {jam_mulai}-{jam_selesai}"
#         for jadwal in self.jadwal:
#             if jadwal_baru == jadwal:
#                 os.system('cls')
#                 print("The schedule is booked!")
#                 time.sleep(2)
#                 break
#         else:
#             self.jadwal.append(jadwal_baru)
#             os.system('cls')
#             print("successfully booked!")
#             print(f"field booking price: {self.harga_sewa}")
#             print(f"your DP : {dp}")
#             time.sleep(4)

#     def batal_pesan_lapangan(self, tanggal, jam_mulai, jam_selesai):
#         jadwal_batal = f"{tanggal} {jam_mulai}-{jam_selesai}"
#         if jadwal_batal in self.jadwal:
#             self.jadwal.remove(jadwal_batal)
#             os.system('cls')
#             print("succesfully cancellation booked")
#             time.sleep(2)
#         else:
#             os.system('cls')
#             print("Schedule not found!")
#             time.sleep(2)

# class Booking:
#     def __init__(self):
#         self.lapangan_futsal = zainab("Futsal", [], 150000)
#         self.lapangan_bulutangkis = zainab("Bulutangkis", [], 200000)

#     def tampilkan_menu(self):
#         os.system('cls')
#         print("1. Tampilkan jadwal bookingan lapangan futsal")
#         print("2. Tampilkan jadwal bookingan lapangan bulutangkis")
#         print("3. Booking lapangan futsal")
#         print("4. Booking lapangan bulutangkis")
#         print("5. Batalkan bookingan lapangan futsal")
#         print("6. Batalkan bookingan lapangan bulutangkis")
#         print("0. Exit")

#     def main(self):
#         while True:
#             self.tampilkan_menu()
#             pilihan = input("Menu (0/1/2/3/4/5/6): ")
#             if pilihan == "1":
#                 self.lapangan_futsal.tampilkan_jadwal()
#             elif pilihan == "2":
#                 self.lapangan_bulutangkis.tampilkan_jadwal()
#             elif pilihan == "3":
#                 tanggal = input("Date (YYYY-MM-DD): ")
#                 jam_mulai = input("Start Time (HH:MM): ")
#                 jam_selesai = input("End Time (HH:MM): ") #tarok disini ya kaa
#                 print("Max DP : 150000")
#                 dp = int(input("DP you want to pay: "))
#                 self.lapangan_futsal.pesan_lapangan(tanggal, jam_mulai, jam_selesai, dp)
#             elif pilihan == "4":
#                 tanggal = input("Date (YYYY-MM-DD): ")
#                 jam_mulai = input("Start Time (HH:MM): ")
#                 jam_selesai = input("End Time (HH:MM): ") #sama ini 
#                 print("Max DP : 200000")
#                 dp = int(input("DP you want to pay: "))
#                 self.lapangan_bulutangkis.pesan_lapangan(tanggal, jam_mulai, jam_selesai, dp)
#             elif pilihan == "5":
#                 tanggal = input("Date (YYYY-MM-DD): ")
#                 jam_mulai = input("Start Time (HH:MM): ")
#                 jam_selesai = input("End Time (HH:MM): ")
#                 self.lapangan_futsal.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
#             elif pilihan == "6":
#                 tanggal = input("Date (YYYY-MM-DD): ")
#                 jam_mulai = input("Start Time (HH:MM): ")
#                 jam_selesai = input("End Time (HH:MM): ")
#                 self.lapangan_bulutangkis.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
#             elif pilihan == "0":
#                 os.system('cls')
#                 print("Thank You! My sista zainab said it")
#                 break
#             else:
#                 os.system('cls')
#                 print("Menu not found!")
#                 time.sleep(2)

# if __name__ == "__main__" :
#     booking = Booking()
#     booking.main()

import os
import time

class zainab:
    def __init__(self, jenis, jadwal, harga_sewa):
        self.jenis = jenis
        self.jadwal = jadwal
        self.harga_sewa = harga_sewa

    def tampilkan_jadwal(self):
        os.system('cls')
        for i, jadwal in enumerate(self.jadwal):
            print(f"{i+1}. {jadwal}")
        time.sleep(2)

    def pesan_lapangan(self, tanggal, jam_mulai, jam_selesai, dp):
        jadwal_baru = f"{tanggal} {jam_mulai}-{jam_selesai}"
        for jadwal in self.jadwal:
            if jadwal_baru == jadwal:
                os.system('cls')
                print("The schedule is booked!")
                time.sleep(2)
                break
        else:
            self.jadwal.append(jadwal_baru)
            os.system('cls')
            print("successfully booked!")
            print(f"field booking price: {self.harga_sewa}")
            print(f"your DP : {dp}")
            time.sleep(4)

    def batal_pesan_lapangan(self, tanggal, jam_mulai, jam_selesai):
        jadwal_batal = f"{tanggal} {jam_mulai}-{jam_selesai}"
        if jadwal_batal in self.jadwal:
            self.jadwal.remove(jadwal_batal)
            os.system('cls')
            print("succesfully cancellation booked")
            time.sleep(2)
        else:
            os.system('cls')
            print("Schedule not found!")
            time.sleep(2)

class Booking:
    def __init__(self):
        self.lapangan_futsal = zainab("Futsal", [], 150000)
        self.lapangan_bulutangkis = zainab("Bulutangkis", [], 200000)

    def tampilkan_menu(self):
        os.system('cls')
        print("="*45)
        print("Selamat Datang di Program Booking Lapangan")
        print("="*45)
        print("1. Tampilkan jadwal bookingan lapangan futsal")
        print("2. Tampilkan jadwal bookingan lapangan bulutangkis")
        print("3. Booking lapangan futsal")
        print("4. Booking lapangan bulutangkis")
        print("5. Batalkan bookingan lapangan futsal")
        print("6. Batalkan bookingan lapangan bulutangkis")
        print("0. Exit")

    def main(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Menu (0/1/2/3/4/5/6): ")
            if pilihan == "1":
                self.lapangan_futsal.tampilkan_jadwal()
            elif pilihan == "2":
                self.lapangan_bulutangkis.tampilkan_jadwal()
            elif pilihan == "3":
                tanggal = input("Date (YYYY-MM-DD): ")
                jam_mulai = input("Start Time (HH:MM): ")
                jam_selesai = input("End Time (HH:MM): ")
                print("Max DP : 150000")
                print("Harga yang tertera di atas adalah harga booking perjam!")
                print("Jika anda menginginkan booking lebih dari 1 jam, maka booking dapat dipesan ulang!")
                dp = int(input("DP you want to pay: "))
                self.lapangan_futsal.pesan_lapangan(tanggal, jam_mulai, jam_selesai, dp)
            elif pilihan == "4":
                tanggal = input("Date (YYYY-MM-DD): ")
                jam_mulai = input("Start Time (HH:MM): ")
                jam_selesai = input("End Time (HH:MM): ")
                print("Max DP : 200000")
                dp = int(input("DP you want to pay: "))
                self.lapangan_bulutangkis.pesan_lapangan(tanggal, jam_mulai, jam_selesai, dp)
            elif pilihan == "5":
                tanggal = input("Date (YYYY-MM-DD): ")
                jam_mulai = input("Start Time (HH:MM): ")
                jam_selesai = input("End Time (HH:MM): ")
                self.lapangan_futsal.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
            elif pilihan == "6":
                tanggal = input("Date (YYYY-MM-DD): ")
                jam_mulai = input("Start Time (HH:MM): ")
                jam_selesai = input("End Time (HH:MM): ")
                self.lapangan_bulutangkis.batal_pesan_lapangan(tanggal, jam_mulai, jam_selesai)
            elif pilihan == "0":
                os.system('cls')
                print("*"*34)
                print("Thank You! My sista zainab said it")
                print("*"*34)
                break
            else:
                os.system('cls')
                print("Menu not found!")
                time.sleep(2)
if __name__ == "__main__" :
    booking = Booking()
    booking.main()