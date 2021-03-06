# Bismillahirrahmanirrahim.

sectrails.py merupakan program ini dibuat untuk melakukan scanning subdomain dengan menggunakan 
engine yang dimiliki Securitytrails.com memanfaatkan Publik API dan Secret Key (dengan cara 
mendaftar akun).

----------------------------------------------------------------------------------------

# KEBUTUHAN

Untuk bisa menjalankan program ini diperlukan bahasa pemrograman Python dan instalasi dependensi / 
install library yang digunakan oleh Python agar dapat berjalan sebagaimana mestinya. Program ini 
berjalan pada CLI sehingga dibutuhkan 'command prompt' pada Windows atau 'Terminal' pada Linux / Nix 
Berikut cara melakukan instalasinya

- Unzip aplikasi menggunakan
 **Linux**

- sudo unzip sectrails.zip

**Windows**

- klik kanan pada folder > extract to folder

**Cek versi python dan pip dengan menjalankan command pada terminal**

- python3 --version
- pip3 --version

# _-Apabila belum memiliki Python dan pip-_
**Linux Debian**

- sudo apt install python3
- sudo apt install python3-pip / sudo install apt python-pip
- sudo apt update

**Windows**

- Kunjungi website https://www.python.org/downloads/
- Download Python versi 3 yang tertera pada awal halaman, berwarna kotak kuning
- Lakukan instalasi sebagaimana biasa pada Windows
- Apabila sudah selesai instalasi, buka command prompt dan arahkan ke folder dimana file tersimpan

**Cek versi python dan pip dengan menjalankan command pada command prompt**

- python3 --version
- pip3 --version

**Mac OS**

- brew install python3
- brew install python3-pip / sudo apt install  python-pip

----------------------------------------------------------------------------------------

# _-Apabila sudah terinstall Python maka langkah selanjutnya yakni instalasi library dengan command:_

- pip install -r requirements.txt
- pip3 install -r requirements.txt

Tunggu hingga proses selesai maka program siap untuk digunakan

----------------------------------------------------------------------------------------

# CARA PENGGUNAAN

agar dapat berjalan sebagaimana fungsinya diperlukan akses sebagai user tertinggi dalam hal ini 
root

- sudo python3 sectrails.py

**--CONTOH PENGGUNAAN--**

![image](https://user-images.githubusercontent.com/95019755/149071090-1744c26e-f0ad-4369-836c-6e39af0c4aa0.png)


Masukkan nama domain : (disini diminta untuk memasukkan nama domain tanpa 'http' atau 'https', 
cth: domain.com)

Please provide a file name to save : (disini diminta untuk memasukkan nama file yang mana di simpan 
dalam bentuk .txt, cth : save-scan.txt)

----------------------------------------------------------------------------------------

**-CATATAN-**

Hasil scan dalam format json akan langsung di save secara default dengan nama:
data_file.json

Kekurangan:
- hanya dapat diimplementasikan untuk mencari domain saja
- belum bisa membuat format JSON secara khusus
- terdapat limit pencarian

----------------------------------------------------------------------------------------

**Mohon maaf apabila ada fungsi yang tidak bejalan.**
