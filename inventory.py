file = open ("db-inventory.txt","a")
while True:
    tidak = input ("input data inventory baru ? (ya/tidak)")
    if tidak == 'tidak' or tidak == 'tidak':
        file = open ("db-inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        break
    elif tidak == 'ya' or tidak == 'ya':
        print("-----------------------------")
        x = input ("Masukkan nama perangkat : ")
        y = input ("Masukkan lokasi : ")
        file.write("Nama perangkat : " +x + ", Lokasi : " + y +"\n")
        print("----------------------")
file.close()
