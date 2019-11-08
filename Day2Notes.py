# DIGIT
x = 18
y = 2

# hitungan dasar
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# type untuk ngecek type sebuah variable
print(type(x / y))

# int untuk ngeubah variable selain integer jadi integer
print(int(x / y))

# float untuk ngeubah variable selain float jadi float
print(float('1234.890'))

# ** untuk pangkat
print(y ** 2)
# pow itu cara lain untuk pangkat
print(pow(y, 2))

# akar pangkat
print(4 ** (1/2))
print(27 ** (1/3))

# % untuk modulus alias sisa bagian
print(27 % 4)

# abs untuk mencari nilainya doang (tanpa + atau -)
x = -90.321
print(abs(x))

# max berguna nyari angka terbesar
print(max(2, 3, 120, 5, 6, 1, 8, 9, 10))
# min berguna nyari angka terkecil
print(min(4, 2, 120, 5, 6, 1, 8, .17564, 10))

# round untuk pembulatan
print(round(3.67856))
print(round(3.67856, 2))

# cari teori di bawah ini!
print(.1 + .2)
# biar normal maka dibikin begini:
print(round((.1 + .2), 1))


# cara import library (biar keluar rumus-rumus mtk)
import math

# math.floor buat pembulatan ke bawah
print(math.floor(3.9))
# math.ceil buat pembulatan ke atas
print(math.ceil(3.1))

# math.sqrt untuk akar pangkat 2
print(math.sqrt(144))

# math.factorial untuk factorial (ex: 3! = 3 x 2 x 1 = 6)
print(math.factorial(3))



# Materi 2
nama = input('Halo, namamu siapa? : ')
print(f'Selamat datang {nama}')
angka = int(input('Masukkan angka : '))     # harus pake int karna angka yg di inputan akan selalu string
print(f'Kuadrat dari {angka} = {angka ** 2}')