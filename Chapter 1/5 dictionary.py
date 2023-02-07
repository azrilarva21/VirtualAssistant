def main():
    student={'name':"hussein alrubaye",'age':27,'salary':232.5}
    student['name']="Hussein Ahmed"
    student["dept"]="software engineer"
    print(student,type(student))

    del student["dept"]
    print(student,type(student))

    print(student['name'])
    print(student['age'])

    student.clear()
    print(student,type(student))


if __name__ == '__main__':main()