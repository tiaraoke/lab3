#Program1

#ini merupakan modal
modal = 100000000

print("Modal awal usaha yaitu",modal)

#b adalah bulan
for b in range (1,9):

#mengubah persen menjadi desimal
    if(b>=1 and b<=2):
        hasil1 = modal * 0
        print("Laba bulan ke -",b,"sebesar = ",hasil1)
    if(b>=3 and b<=4):
        hasil2 = modal * 0.01
        print("Laba bulan ke -",b,"sebesar = ",hasil2)
    if(b>=5 and b<=7):
        hasil3 = modal * 0.05
        print("Laba bulan ke -",b,"sebesar = ",hasil3)
    if(b==8):
        hasil4 = modal * 0.02
        print("Laba bulan ke -",b,"sebesar = ",hasil4)
#Contoh 5% = 5/100 = 0.05