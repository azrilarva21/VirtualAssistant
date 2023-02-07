def main():
    out=open("test.txt","a")
    out.write(" \nname:salama")
    out.write(" \nname:dema")
    out.close()
    read_file=open("test.txt","r")
    for line in read_file:
        print(line)
    read_file.close()


if __name__ == '__main__':main()