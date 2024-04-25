def checkKabisat(tahun):
    if (tahun%4==0 and tahun%100!=0) or (tahun%400==0):
        print(f"{tahun} merupakan tahun kabisat")
    else:
        print(f"{tahun} bukan merupakan tahun kabisat")
        
checkKabisat(2024)