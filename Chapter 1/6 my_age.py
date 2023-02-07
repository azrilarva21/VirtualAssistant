from datetime import datetime


def main():
    year_birth = input("Masukan tahun ulang tahunmu:")
    year_now = datetime.now().year
    my_age = year_now-int(year_birth)
    print("Umur kamu adalah {} tahun".format(my_age))


if __name__ == '__main__':main()