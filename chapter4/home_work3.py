def fn():
    n = input("Enter the number: ")
    n = int(n)
    list_n = []
    for i in range(1, n*3+1):
        list_n.append(i)
    print(list_n)

fn()
