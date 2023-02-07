def main():
    age=input("Masukan umur anda:")
    if(int(age)>=8 and int(age)<=10):
        print("Balita")
    elif(int(age)>=11 and int(age)<=15):
        print("Anak anak")
    elif(int(age)>=16 and int(age)<=18):
        print("Remaja")
    elif(int(age)>=19 and int(age)<=30):
        print("Pemuda")
    else:
        print("Tua")


if __name__ == '__main__':main()