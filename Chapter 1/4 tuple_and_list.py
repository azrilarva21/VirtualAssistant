def main():
    #List
    ages=[44,33,45,33,54]
    print(type(ages))
    ages.append(100)
    ages.insert(0,33)
    print(ages)
    #Tuples
    ages=(44,33,45,33,54)
    print(type(ages))
    ages.append(100)
    ages.insert(0,33)
    print(ages)


if __name__ == '__main__':main()