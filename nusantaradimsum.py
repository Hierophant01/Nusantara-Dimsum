#fungsi
def garis():
    print(43*"=")
def garis1():
    print(33*"=")
def garis2():
    print(51*"=")
def showmenu():
    print("\n")
    print("             NUSANTARA DIMSUM              ")
    print("        laper bos?? Nusantara Dimsum aja   ")
    garis()
    print("|     Menu        | Kode  |  Harga Satuan |")
    garis()
    print("|1| Dimsum ayam   |  DA   |   Rp.2000     |")
    print("|2| Dimsum udang  |  DU   |   Rp.2500     |")
    print("|3| Dimsum cumi   |  DC   |   Rp.2500     |")
    print("|4| Dimsum gurita |  DG   |   Rp.3000     |")
    print("|5| Milk Tea      |  MT   |   Rp.5000     |")
    garis()
    print("*Dapatkan free milk tea dengan pembelian minimal 20pcs \n")

datapembelian = []
def proses():
    global datapembelian
    totalpembelian = 0
    pesananan = int(input("ingin pesan berapa varian? : "))
    pembeli = input("Atas nama siapa pesanan ini dibuat? : ")
    varke = 0
    while (varke < pesananan) :
        print("varian ke - :", + varke + 1)
        varke = varke + 1

        kodemenu = input("Masukan kode menu DA/DU/DC/DG/MT : ")

        if kodemenu == "DA" or kodemenu == "da":
            harga=2000
        elif kodemenu == "DU" or kodemenu == "du":
            harga=2500
        elif kodemenu == "DC" or kodemenu == "dc":
            harga=2500
        elif kodemenu == "DG" or kodemenu == "dg":
            harga=3000
        elif kodemenu == "MT" or kodemenu == "mt":
            harga=5000
        else:
            print("ERROR!")

        bbeli = int(input("Mau berapa banyak yang di beli? : "))
        garis2()
        totalpembelian = totalpembelian + bbeli

        datamenu = []
        #data 0
        datamenu.append(pembeli)
        #data 1
        datamenu.append(kodemenu)
        #data 2
        datamenu.append(harga)
        #data 3
        datamenu.append(bbeli)
        #data 4
        datamenu.append(harga * bbeli)
        #Memanggil semua data
        datapembelian.append(datamenu)

    #voucher gratis
    if totalpembelian >= 20:
        print("*Selamat anda mendapatkan free 1 milktea ")
        print("Gunakan kode berikut : MLKTEA20")
        voc = input("Masukan kode voucher anda : ")
        while (voc != 'MLKTEA20'):
            print('ERROR! Silahkan masukan kode kembali')
            voc = input("Masukan kode voucher anda : ")

        freemilktea = []
        freemilktea.append(pembeli)
        freemilktea.append('MT')
        freemilktea.append(0) # harga nya 0
        freemilktea.append('    1') # hanya dapet 1 milktea
        freemilktea.append(0) # total harga 0 (1 * 0)
        datapembelian.append(freemilktea)

def output():
    print("\n===================================================")
    print("\t\tNota pembayaran Dimsum")
    print("===================================================")
    print("|  No.  |   Kode   |  Harga  | Banyak |   Jumlah  |")
    print("|       |  Pesanan | satuan- |  Beli  |   Harga-  |")
    print("===================================================")
    nomor = 0
    jbayar = 0
    while nomor < len(datapembelian):
        data = datapembelian[nomor]
        nomor = nomor + 1
        print('   ',nomor,'      ',data[1],'    Rp.',data[2],'   ',data[3],'   Rp.',data[4])
        jbayar = jbayar + data[4]

    garis2()
    print("                          Jumlah Bayar Rp.",+(jbayar))
    pajak = jbayar * 0.1
    print("                          Pajak 10%    Rp.",round(pajak))
    tbayar = jbayar + pajak
    print("                          Total  Bayar Rp.",round(tbayar))
    garis2()
    print(' Terima kasih atas pembelianya Tn/Ny. : ',data[0])
    garis2()

#input
print("\n")
garis1()
print("\tNUSANTARA DIMSUM")
print("Laper bos?? Nusantara Dimsum aja")
garis1()
print("1. Lihat menu & Pesan")
print("2. Exit")
userinput = input("Masukan pilihan : ")
if userinput == "2" :
    print("\n Sampai jumpa lagi..")
elif userinput == "1":
    showmenu()
    proses()
    pilihan = input("Ingin tambah pesanan? y/n : ")
    while (pilihan == 'y'):
        proses()
        pilihan = input("Ingin tambah pesanan? y/n : ")
    output()

