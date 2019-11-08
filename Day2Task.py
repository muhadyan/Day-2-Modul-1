# Di dalam kandang terdapat kambing dan ayam sebanyak 13 ekor.
# Jika jumlah kaki hewan tersebut 32 2kor,
# maka jumlah kambing dan ayam masing-masing adalah....

kambing = 4
ayam = 2
JmlHewan = 13
JmlKaki = 32
Kaki_hewan_1 = ayam
Kaki_hewan_2 = kambing

Hewan1 = int((JmlKaki-(Kaki_hewan_2*JmlHewan))/(Kaki_hewan_1-Kaki_hewan_2))
Hewan2 = int((JmlKaki-(Kaki_hewan_1*JmlHewan))/(Kaki_hewan_2-Kaki_hewan_1))

print('Jumlah ayam ada', int(Hewan1))
print('Jumlah kambing ada', int(Hewan2))



# bikin biar kalo nambah jenis hewan ga perlu ngeubah rumusnya! Ex: Tambahin Sapi!



#Tugas 2
TotHewan = int(input('Ketik total hewan? : '))
TotKaki = int(input('Ketik total kaki hewan? : '))
KakiHewanA = int(input('Ketik jumlah kaki hewan A? : '))
KakiHewanB = int(input('Ketik jumlah kaki hewan B? : '))

HewanA = int((TotKaki-(KakiHewanB*TotHewan))/(KakiHewanA-KakiHewanB))
HewanB = int((TotKaki-(KakiHewanA*TotHewan))/(KakiHewanB-KakiHewanA))

print('hewan A = ', HewanA, ' hewan B = ', HewanB)