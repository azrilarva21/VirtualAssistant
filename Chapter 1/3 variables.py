def main():
    amount=30
    data="{} is high".format(amount)
    # data="%s is high"% amount
    print(data)
    print(type(data))
    print(len(data))
    print(data[1])


if __name__ == '__main__':main()