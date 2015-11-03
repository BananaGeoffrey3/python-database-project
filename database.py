datalist = []

while 1 == 1:
    query = input('query ')

    if query in datalist:
        print('obj',datalist.index(query))

    elif query == 'print datalist':
        print(datalist)

    elif query == 'rm':
        rmobj = int(input('rm obj '))
        if rmobj:
            datalist.remove(rmobj)
        else:
            print('error')
            print(datalist)

    else:
        datalist.append(query)
        print(query,'added to datalist')

    datalist.sort()
