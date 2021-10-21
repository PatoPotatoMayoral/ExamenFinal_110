def main():
    x = int(input())
    lista =[]
    if x <= 0:
        print('Error')
    else:
        for i in range (x):
            z = int(input())
            if z %2==0:
                r =z**2
                lista.append(r)
            else :
                y = z**3
                lista.append(y)
        print (lista)


    pass


if __name__ == '__main__':
    main()
