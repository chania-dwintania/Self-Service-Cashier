import pandas as pd
from tabulate import tabulate
class Transaction:  
  def __init__(self):
    \'\'\' Melakukan inisialisasi kelas Transaction
    self.dict untuk membuat dictionary yang akan digunakan untuk menympan transaksi
    self.tabel untuk membuat matriks 3x3 yang akan berisikan data pembelian.            
    self.valid untuk memastikan data sudah valid\'\'\'    
    self.dict = {}        
    self.tabel = [[0, 0, 0] for i in range(3)]\n        
    self.valid = True
    def add_item(self):        
      \'\'\'Fungsi add_item digunakan untuk memasukkan item ke dalam dictionary.\'\'\'        
      while True:            
        barang = input(\'Masukkan nama barang: \').lower()            
        harga = int(input(\'Masukkan harga barang:\'))            
        kuantitas = int(input(\'Masukkan jumlah barang: \'))            
        if type(harga)!= int:                
          print("Format harga tidak sesuai")            
        elif type(kuantitas)!=int:                
          print(\'Format kuantitas barang tidak sesuai\')            
        else:               
          if barang in self.dict:                    
            self.dict[barang][0] += kuantitas                    
            self.dict[barang][2] += kuantitas*harga                
          else:                    
            add_dict = {barang: [kuantitas, harga, kuantitas*harga]}                    
            self.dict.update(add_dict)            
            self.tampilkan_pesanan()            
            print(\'Berikut merupakan pesanan anda saat ini.\')            
      add_more = input(\'Apakah anda ingin menambahkan pesanan lain? (y/n)\').lower()            
      if add_more == \'n\':                
        print(\'Silakan lanjutkan ke tahap berikutnya.\')                
        break                    
    def update_item_name(self):        
      \'\'\'Fungsi digunakan untuk melakukan perubahan pada nama barang yang sudah ada dalam dictionary pembelanjaan.\'\'\'        
      barang = input(\'Sebutkan barang yang ingin diganti: \').lower()        
      barang_pengganti = input(\'Sebutkan barang pengganti: \').lower()        
      try:            
        a = self.dict[barang]            
        self.dict.pop(barang)            
        self.dict.update({barang_pengganti: a})            
        self.tampilkan_pesanan()            
        print(f\'Berhasil menghapus {barang} dan diganti menjadi {barang_pengganti}\')
      except KeyError:            
        print(\'Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda\')            
    def update_item_price(self):        
      \'\'\'Fungsi digunakan untuk merubah harga barang yang telah berada dalam dictionary pembelanjaan.\'\'\'        
        barang = input(\'Sebutkan barang yang harganya ingin anda ubah: \').lower()\n        try: \n            harga_pengganti = int(input(\'Sebutkan harga barang yang baru: \'))\n            if type(harga_pengganti)!= int:\n                print(\'Format harga salah\')\n            else:\n                self.dict[barang][1] = harga_pengganti\n                self.dict[barang][2] = harga_pengganti*self.dict[barang][0]\n                self.tampilkan_pesanan()\n                print(f\'Harga pada {barang} berhasil diubah menjadi {harga_pengganti}\')\n        except KeyError:\n            print(\'Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda sehingga tidak dapat mengganti harga.\')\n            \n    def update_item_qty(self):\n        \'\'\'Fungsi digunakan untuk membuat perubahan pada kuantitas barang yang telah berada dalam dictionary pembelanjaan.\'\'\'\n        barang = input(\'Sebutkan barang yang ingin diganti kuantitasnya: \').lower()\n        try:\n            kuantitas_pengganti = int(input(\'Sebutkan kuantitas barang yang baru: \'))\n            if type(kuantitas_pengganti) != int:\n                print(\'Format kuantitas salah\')\n            else:\n                self.dict[barang][0] = kuantitas_pengganti\n                self.dict[barang][2] = kuantitas_pengganti*self.dict[barang][1]\n                self.tampilkan_pesanan()\n                print(f\'Kuantitas pada {barang} berhasil diubah menjadi {kuantitas_pengganti}\')\n        except KeyError:\n            print(\'Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda sehingga tidak dapat mengganti kuantitas.\')\n    \n    def delete_item(self):\n        \'\'\'Fungsi digunakan untuk menghapus barang yang tidak diinginkan di dalam dictionary pembelanjaan.\'\'\'\n        barang = input(\'Sebutkan nama barang yang ingin anda hapus: \')\n        \n        try:\n            self.dict.pop(barang)\n            self.tampilkan_pesanan()\n            print(f\'Berhasil menghapus {barang}\')\n        except KeyError:\n            print(f\'Mohon maaf. Tidak ada item tersebut dalam keranjang belanjaan anda.\')\n            \n    def reset_transaction(self):\n        \'\'\'Fungsi digunakan untuk menghapus semua barang di dalam keranjang belanjaan.\'\'\'\n        self.dict.clear()\n        self.tampilkan_pesanan()\n    \n    def tampilkan_pesanan(self):\n        \'\'\'Fungsi digunakan untuk menampilkan pesanan yang sudah ada di dalam dictionary pembelanjaan.\'\'\'\n        if not self.dict:\n            print(\'Keranjang belanjaan anda masih kosong.\')\n            return\n\n        data = pd.DataFrame(self.dict).T\n        data.columns = ["Kuantitas Barang","Harga/pcs", "Total Harga"]\n        print(data.to_markdown())\n\n    def check_order(self):\n        \'\'\'Fungsi digunakan untuk memastikan data sudah valid, yaitu kuantitas barang, harga/pcs, total harga harus lebih besar dari 0.\'\'\'\n        try:\n            data = pd.DataFrame(self.dict).T\n            data.columns = ["Kuantitas Barang","Harga/pcs", "Total Harga"]\n        \n            for index, row in data.iterrows():\n                if row["Kuantitas Barang"] <= 0 or row["Harga/pcs"] <= 0 or row["Total Harga"] <= 0:\n                    self.valid = False\n        \n            if self.valid == True:\n                self.tampilkan_pesanan()\n                print(\'Pesanan anda sudah benar. Silakan lanjutkan ke proses pembayaran.\')\n            else:\n                self.tampilkan_pesanan()\n                print(\'Terdapat kesalahan pada harga atau kuantitas belanjaan anda.\')\n        except ValueError:\n            print(\'Keranjang belanjaan anda masih kosong.\')\n\n            \n    def total_price(self):\n        \'\'\'Fungsi digunakan untuk mengecek total harga pembelanjaan.\'\'\'\n        self.check_order()\n        if self.valid == True:\n            total_harga = 0\n        for i in self.dict:\n            total_harga += self.dict[i][2]\n            \n        if total_harga >= 500_000:\n            diskon = 0.1*total_harga\n            harga_akhir = total_harga - diskon\n            self.tampilkan_pesanan()\n            print(f\'Selamat anda mendapatkan diskon sebesar: {diskon}. Total pesanan anda adalah {harga_akhir}\')\n        elif total_harga >= 300_000:\n            diskon = 0.08*total_harga\n            harga_akhir = total_harga - diskon\n            self.tampilkan_pesanan()\n            print(f\'Selamat anda mendapatkan diskon sebesar: {diskon}. Total pesanan anda adalah {harga_akhir}\')\n        elif total_harga >= 200_000:\n            diskon = 0.05*total_harga\n            harga_akhir = total_harga - diskon\n            self.tampilkan_pesanan()\n            print(f\'Selamat anda mendapatkan diskon sebesar: Rp.{diskon}. Total pesanan anda adalah {harga_akhir}\')\n        else:\n            self.tampilkan_pesanan()\n            print(f\'Total pesanan anda adalah Rp.{harga_akhir}\')')

