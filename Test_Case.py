#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selfcashier1 as k
transc = k.Transaction()


# In[2]: Masukkan nama barang: cokelar
Masukkan harga barang:10000
Masukkan jumlah barang: 10
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| cokelar |                 10 |       10000 |        100000 |
Berikut merupakan pesanan anda saat ini.
Apakah anda ingin menambahkan pesanan lain? (y/n)y
Masukkan nama barang: roti
Masukkan harga barang:9000
Masukkan jumlah barang: 3
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| cokelar |                 10 |       10000 |        100000 |
| roti    |                  3 |        9000 |         27000 |
Berikut merupakan pesanan anda saat ini.
Apakah anda ingin menambahkan pesanan lain? (y/n)n
Silakan lanjutkan ke tahap berikutnya.


transc.add_item()


# In[3]: Sebutkan barang yang ingin diganti: cokelar
Sebutkan barang pengganti: cokelat
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| roti    |                  3 |        9000 |         27000 |
| cokelat |                 10 |       10000 |        100000 |
Berhasil menghapus cokelar dan diganti menjadi cokelat


transc.update_item_name()


# In[4]: Sebutkan barang yang harganya ingin anda ubah: roti
Sebutkan harga barang yang baru: 8000
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| roti    |                  3 |        8000 |         24000 |
| cokelat |                 10 |       10000 |        100000 |
Harga pada roti berhasil diubah menjadi 8000


transc.update_item_price()


# In[5]: Sebutkan barang yang ingin diganti kuantitasnya: cokelat
Sebutkan kuantitas barang yang baru: 20
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| roti    |                  3 |        8000 |         24000 |
| cokelat |                 20 |       10000 |        200000 |
Kuantitas pada cokelat berhasil diubah menjadi 20


transc.update_item_qty()


# In[6]: Sebutkan nama barang yang ingin anda hapus: roti
|         |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:--------|-------------------:|------------:|--------------:|
| cokelat |                 20 |       10000 |        200000 |
Berhasil menghapus roti


transc.delete_item()


# In[7]: Keranjang belanjaan anda masih kosong.


transc.reset_transaction()


# In[8]: Masukkan nama barang: kasur
Masukkan harga barang:3000000
Masukkan jumlah barang: 1
|       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
Berikut merupakan pesanan anda saat ini.
Apakah anda ingin menambahkan pesanan lain? (y/n)y
Masukkan nama barang: kursi
Masukkan harga barang:870000
Masukkan jumlah barang: 1
|       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
| kursi |                  1 |  870000     |    870000     |
Berikut merupakan pesanan anda saat ini.
Apakah anda ingin menambahkan pesanan lain? (y/n)n
Silakan lanjutkan ke tahap berikutnya.


transc.add_item()


# In[9]: |       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
| kursi |                  1 |  870000     |    870000     |
Pesanan anda sudah benar. Silakan lanjutkan ke proses pembayaran.


transc.check_order()


# In[10]: |       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
| kursi |                  1 |  870000     |    870000     |
Pesanan anda sudah benar. Silakan lanjutkan ke proses pembayaran.


transc.total_price()


# In[ ]: |       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
| kursi |                  1 |  870000     |    870000     |
Pesanan anda sudah benar. Silakan lanjutkan ke proses pembayaran.
|       |   Kuantitas Barang |   Harga/pcs |   Total Harga |
|:------|-------------------:|------------:|--------------:|
| kasur |                  1 |       3e+06 |         3e+06 |
| kursi |                  1 |  870000     |    870000     |
Selamat anda mendapatkan diskon sebesar: 387000.0. Total pesanan anda adalah 3483000.0




