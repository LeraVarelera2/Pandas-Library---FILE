# 1. Unduh file student.csv (SUDAH)
print('1. Unduh file student.csv (SUDAH)')

# 2. Baca file student.csv ke dalam DataFrame menggunakan Pandas (SUDAH)
import pandas as pd
import numpy as np

print('\n2. Membaca File')
df = pd.read_csv('students.csv')
print("Data Students:") 
print(df)

# 3. Tampilkan 5 baris pertama dari DataFrame
print('\n3. Tampilkan 5 Baris Pertama')
print("5 Baris petama")
print(df.head())

# 4. Tampilkan informasi tentang Data Frame menggunakan info() dan describe()
print('\n4. Tampilkan informasi data frame')
df.info() 
print(df.describe())

# 5. Tambahkan kolom baru bernama STATUS dengan aturan:
'''
- Jika nilai grade  >= 80 (80-100), maka status "LULUS"
- Jika tidak maka Status adalah "TIDAK LULUS"
'''
print('\n 5. Tambahkan kolom baru bernama STATUS')
df['Status'] = np.where(df['Grade'] >= 80, 'Lulus', 'Tidak Lulus') 
print(df)

# 6. Menyimpan DataFrame yang telah diupgrade ke dalam File Baru. 
print('\n 6. Menyimpan file yang sudah diupdate ke file baru Students_processed.csv')
df.to_csv('Student_processed.csv',index=False) 
print(df)

# 7. Hitung nilai rata-rata Mahasiswa
print('\n 7. Hitung nilai rata-rata Mahasiswa')
rata_rata = df['Grade'].mean()
print("Rata-rata nilai Mahasiswa:",rata_rata)

# 8. Kelompokkan data berdasarkan Status dan Hitung Jumlah Mahasiswa untuk setiap Statusnya. 
print('\n 8. Kelompokkan data berdasarkan Status')
kelompokan_status = df.groupby('Grade').size()
print(kelompokan_status)



