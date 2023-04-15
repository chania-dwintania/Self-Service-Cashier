import pandas as pd
from tabulate import tabulate

class Transaction:
    
    def __init__(self):
        ''' Melakukan inisialisasi kelas Transaction
            self.dict untuk membuat dictionary yang akan digunakan untuk menympan transaksi
            self.tabel untuk membuat matriks 3x3 yang akan berisikan data pembelian.
            self.valid untuk memastikan data sudah valid
            '''
        
        self.dict = {}
        self.tabel = [[0, 0, 0] for i in range(3)]
        self.valid = True
        
    def add_item(self):
        '''Fungsi add_item digunakan untuk memasukkan item ke dalam dictionary.'''
        
        while True:
            barang = input('Masukkan nama barang: ').lower()
            harga = int(input('Masukkan harga barang:'))
            kuantitas = int(input('Masukkan jumlah barang: '))
            if type(harga)!= int:
                print("Format harga tidak sesuai")
            elif type(kuantitas)!=int:
                print('Format kuantitas barang tidak sesuai')
            else:
                if barang in self.dict:
                    self.dict[barang][0] += kuantitas
                    self.dict[barang][2] += kuantitas*harga
                else:
                    add_dict = {barang: [kuantitas, harga, kuantitas*harga]}
                    self.dict.update(add_dict)
            self.tampilkan_pesanan()
            print('Berikut merupakan pesanan anda saat ini.')
            add_more = input('Apakah anda ingin menambahkan pesanan lain? (y/n)').lower()
            if add_more == 'n':
                print('Silakan lanjutkan ke tahap berikutnya.')
                break
                
    def update_item_name(self):
        '''Fungsi digunakan untuk melakukan perubahan pada nama barang yang sudah ada dalam dictionary pembelanjaan.'''
        barang = input('Sebutkan barang yang ingin diganti: ').lower()
        barang_pengganti = input('Sebutkan barang pengganti: ').lower()
        try:
            a = self.dict[barang]
            self.dict.pop(barang)
            self.dict.update({barang_pengganti: a})
            self.tampilkan_pesanan()
            print(f'Berhasil menghapus {barang} dan diganti menjadi {barang_pengganti}')
        except KeyError:
            print('Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda')
        
    def update_item_price(self):
        '''Fungsi digunakan untuk merubah harga barang yang telah berada dalam dictionary pembelanjaan.'''
        barang = input('Sebutkan barang yang harganya ingin anda ubah: ').lower()
        try: 
            harga_pengganti = int(input('Sebutkan harga barang yang baru: '))
            if type(harga_pengganti)!= int:
                print('Format harga salah')
            else:
                self.dict[barang][1] = harga_pengganti
                self.dict[barang][2] = harga_pengganti*self.dict[barang][0]
                self.tampilkan_pesanan()
                print(f'Harga pada {barang} berhasil diubah menjadi {harga_pengganti}')
        except KeyError:
            print('Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda sehingga tidak dapat mengganti harga.')
            
    def update_item_qty(self):
        '''Fungsi digunakan untuk membuat perubahan pada kuantitas barang yang telah berada dalam dictionary pembelanjaan.'''
        barang = input('Sebutkan barang yang ingin diganti kuantitasnya: ').lower()
        try:
            kuantitas_pengganti = int(input('Sebutkan kuantitas barang yang baru: '))
            if type(kuantitas_pengganti) != int:
                print('Format kuantitas salah')
            else:
                self.dict[barang][0] = kuantitas_pengganti
                self.dict[barang][2] = kuantitas_pengganti*self.dict[barang][1]
                self.tampilkan_pesanan()
                print(f'Kuantitas pada {barang} berhasil diubah menjadi {kuantitas_pengganti}')
        except KeyError:
            print('Mohon maaf. Tidak ada item tersebut dalam keranjang belanja anda sehingga tidak dapat mengganti kuantitas.')
    
    def delete_item(self):
        '''Fungsi digunakan untuk menghapus barang yang tidak diinginkan di dalam dictionary pembelanjaan.'''
        barang = input('Sebutkan nama barang yang ingin anda hapus: ')
        
        try:
            self.dict.pop(barang)
            self.tampilkan_pesanan()
            print(f'Berhasil menghapus {barang}')
        except KeyError:
            print(f'Mohon maaf. Tidak ada item tersebut dalam keranjang belanjaan anda.')
            
    def reset_transaction(self):
        '''Fungsi digunakan untuk menghapus semua barang di dalam keranjang belanjaan.'''
        self.dict.clear()
        self.tampilkan_pesanan()
    
    def tampilkan_pesanan(self):
        '''Fungsi digunakan untuk menampilkan pesanan yang sudah ada di dalam dictionary pembelanjaan.'''
        if not self.dict:
            print('Keranjang belanjaan anda masih kosong.')
            return

        data = pd.DataFrame(self.dict).T
        data.columns = ["Kuantitas Barang","Harga/pcs", "Total Harga"]
        print(data.to_markdown())

    def check_order(self):
        '''Fungsi digunakan untuk memastikan data sudah valid, yaitu kuantitas barang, harga/pcs, total harga harus lebih besar dari 0.'''
        try:
            data = pd.DataFrame(self.dict).T
            data.columns = ["Kuantitas Barang","Harga/pcs", "Total Harga"]
        
            for index, row in data.iterrows():
                if row["Kuantitas Barang"] <= 0 or row["Harga/pcs"] <= 0 or row["Total Harga"] <= 0:
                    self.valid = False
        
            if self.valid == True:
                self.tampilkan_pesanan()
                print('Pesanan anda sudah benar. Silakan lanjutkan ke proses pembayaran.')
            else:
                self.tampilkan_pesanan()
                print('Terdapat kesalahan pada harga atau kuantitas belanjaan anda.')
        except ValueError:
            print('Keranjang belanjaan anda masih kosong.')

            
    def total_price(self):
        '''Fungsi digunakan untuk mengecek total harga pembelanjaan.'''
        self.check_order()
        if self.valid == True:
            total_harga = 0
        for i in self.dict:
            total_harga += self.dict[i][2]
            
        if total_harga >= 500_000:
            diskon = 0.1*total_harga
            harga_akhir = total_harga - diskon
            self.tampilkan_pesanan()
            print(f'Selamat anda mendapatkan diskon sebesar: {diskon}. Total pesanan anda adalah {harga_akhir}')
        elif total_harga >= 300_000:
            diskon = 0.08*total_harga
            harga_akhir = total_harga - diskon
            self.tampilkan_pesanan()
            print(f'Selamat anda mendapatkan diskon sebesar: {diskon}. Total pesanan anda adalah {harga_akhir}')
        elif total_harga >= 200_000:
            diskon = 0.05*total_harga
            harga_akhir = total_harga - diskon
            self.tampilkan_pesanan()
            print(f'Selamat anda mendapatkan diskon sebesar: Rp.{diskon}. Total pesanan anda adalah {harga_akhir}')
        else:
            self.tampilkan_pesanan()
            print(f'Total pesanan anda adalah Rp.{harga_akhir}')
