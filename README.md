# Self-Service-Cashier
## Latar Belakang

Seiring berjalannya suatu bisnis, maka diperlukan adanya inovasi yang dapat meningkatkan efisiensi bisnis serta mengurangi biaya operasi. Salah satu aplikasinya adalah dengan membuat self service cashier. Melalui sistem kasir ini, customer dapat memasukkan nama item yang dibeli, kuantitas pembelian, dan juga harga barang yang dibeli. Pada akhir proses, customer dapat mengetahui total harga belanjaannya dan juga jumlah diskon yang diperoleh. 

## Objektif

Tujuan dari project ini adalah untuk menciptakan sistem kasir yang dapat melakukan metode sebagai berikut:
1. Customer menginput barang, kuantitas barang, dan juga harga barang dengan metode add_item.
2. Apabila ada salah input, customer dapat mengubah:
   - Nama barang dengan metode update_item_name
   - Kuantitas barang dengan metode update_item_qty
   - Harga barang dengan metode update_item_price
3. Apabila customer ini menghapus barang dari keranjang belanjaannya, dapat menggunakan metode delete_item.
4. Apabila customer ini menghapus seluruh barang dari keranjang belanjaannya, dapat menggunakan metode reset_transaction.
5. Sebelum dapat menghitung total belanjaan, isi dari keranjang belanja customer diperiksa melalui metode check_order(). Metode ini memeriksa apakah ada nilai kosong ataupun nilai invalid pada keranjang customer.
6. Customer dapat menghitung seluruh total belanjaan dan juga diskon yang diperoleh melalui metode total_price. Berikut merupakan ketentuan pembelanjaan untuk memperoleh diskon:
    - Diskon sebesar 10% untuk pembelanjaan di atas Rp500.000,00.
    - Diskon sebesar 8% untuk pembelanjaan di atas Rp300.000,00.
    - Diskon sebesar 5% untuk pembelanjaan di atas Rp200.000,00.

## Flowchart
![image](https://user-images.githubusercontent.com/111668628/232254933-a7ed6124-ad9b-4853-9483-f845fcc3ab50.png)

## Penjelasan Fungsi Functions/ Attribute
1. **init()**  
  Melakukan inisiasi untuk class Transaction.
  self.dict untuk membuat dictionary yang akan digunakan untuk menympan transaksi
  self.tabel untuk membuat matriks 3x3 yang akan berisikan data pembelian.
  self.valid untuk memastikan data sudah valid
  
2. **add_item()**    
  Fungsi add_item digunakan untuk memasukkan item ke dalam dictionary.

3. **update_item_name()**    
  Fungsi digunakan untuk melakukan perubahan pada nama barang yang sudah ada dalam dictionary     pembelanjaan.

4. **update_item_price()**    
  Fungsi digunakan untuk merubah harga barang yang telah berada dalam dictionary pembelanjaan.

5. **update_item_qty()**   
` Fungsi digunakan untuk membuat perubahan pada kuantitas barang yang telah berada dalam           dictionary pembelanjaan.

6. **delete_item()**  
  Fungsi digunakan untuk menghapus barang yang tidak diinginkan di dalam dictionary               pembelanjaan.

7. **reset_transaction()**  
  Fungsi digunakan untuk menghapus semua barang di dalam keranjang belanjaan.

8. **check_order()**  
  Fungsi digunakan untuk memastikan data sudah valid, yaitu kuantitas barang, harga/pcs, total     harga harus lebih besar dari 0.
  
9. **total_price()**  
  Fungsi digunakan untuk mengecek total harga pembelanjaan.

## Demonstrasi dengan Test Case
1. **input:**  
  import selfcashier1 as k  
  transc = k.Transaction()  
  transc.add_item()  
  **output:**  
  Masukkan nama barang: cokelar  
Masukkan harga barang:10000  
Masukkan jumlah barang: 10  
![image](https://user-images.githubusercontent.com/111668628/232256832-9b8899cc-3e97-4505-91ad-1febfddc5cbf.png)  
Berikut merupakan pesanan anda saat ini.  
Apakah anda ingin menambahkan pesanan lain? (y/n)y  
Masukkan nama barang: roti  
Masukkan harga barang:9000  
Masukkan jumlah barang: 3  
![image](https://user-images.githubusercontent.com/111668628/232256862-ff65349c-c81a-4797-a23d-cda28c0c5945.png)   
Berikut merupakan pesanan anda saat ini.  
Apakah anda ingin menambahkan pesanan lain? (y/n)n  
Silakan lanjutkan ke tahap berikutnya.

2. **input:**  
transc.update_item_name()  
**output:**   
Sebutkan barang yang ingin diganti: cokelar  
Sebutkan barang pengganti: cokelat  
![image](https://user-images.githubusercontent.com/111668628/232256939-2d187e71-74e9-443e-8090-0550ea53372b.png)  
Berhasil menghapus cokelar dan diganti menjadi cokelat  

3. **input:**  
transc.update_item_price()  
**output:**  
Sebutkan barang yang harganya ingin anda ubah: roti  
Sebutkan harga barang yang baru: 8000  
![image](https://user-images.githubusercontent.com/111668628/232257228-a0f0a519-97a5-41d3-96c6-e12669ccb66c.png)  
Harga pada roti berhasil diubah menjadi 8000  

4. **input:**  
transc.update_item_qty()  
**output:**  
Sebutkan barang yang ingin diganti kuantitasnya: cokelat  
Sebutkan kuantitas barang yang baru: 20  
![image](https://user-images.githubusercontent.com/111668628/232257469-71607d8e-3c6c-4585-a642-b8e35e51c9f4.png)  
Kuantitas pada cokelat berhasil diubah menjadi 20  

5. **input:**  
transc.delete_item()    
**output:**  
Sebutkan nama barang yang ingin anda hapus: roti  
![image](https://user-images.githubusercontent.com/111668628/232257699-c2292423-8a1f-4895-ae1a-ede8a5b611d7.png)  
Berhasil menghapus roti  

6. **input:**  
transc.reset_transaction()  
**output:**  
Keranjang belanjaan anda masih kosong.

7. **input:**  
transc.add_item()  
**output:**  
Masukkan nama barang: kasur   
Masukkan harga barang:3000000  
Masukkan jumlah barang: 1  
![image](https://user-images.githubusercontent.com/111668628/232257839-c4ba615d-e8ad-49d2-bc91-ff576ffd6e34.png)  
Berikut merupakan pesanan anda saat ini.  
Apakah anda ingin menambahkan pesanan lain? (y/n)y  
Masukkan nama barang: kursi  
Masukkan harga barang:870000  
Masukkan jumlah barang: 1  
![image](https://user-images.githubusercontent.com/111668628/232257850-fb6b4d90-3247-4cf7-9a43-d5111a514021.png)  
Berikut merupakan pesanan anda saat ini.  
Apakah anda ingin menambahkan pesanan lain? (y/n)n  
Silakan lanjutkan ke tahap berikutnya.  

8. **input:**  
transc.check_order()  
**output:**  
![image](https://user-images.githubusercontent.com/111668628/232257883-31c70c7b-01b2-4875-9cea-7867b0f4f98f.png)

9. **input:**  
transc.total_price()  
**output:**  
![image](https://user-images.githubusercontent.com/111668628/232257893-adf5a716-8d35-4d48-9915-9795966a238e.png)

## Conclusion
Self-service cashier sudah dapat diaplikasikan dalam bisnis dan customer sudah dapat menggunakannya untuk berbelanja.
