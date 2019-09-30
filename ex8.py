def print_list():

    list1 = [1, 'Hello', 8, 'World']
    list2 = [10, 'Again', list1]
    list1[2] = 'Beautiful'

    print(list1)
    print(list2)
    print(list1[1])
    print(list2[2][3])
    print(list1[:-2])

    sum_list = list1 + list2[:2]
    print(sum_list)

    mult_list = list1 * 2
    print(mult_list)

    distros_list = ['Debian', 'Ubuntu']

    distros_list.append('Red Hat')
    print(distros_list)

    distros_list = distros_list + ['Gentoo', 'Fedora', 'Arch']
    print(distros_list)

    print("List Lenght: {}".format(len(distros_list)))

    distros_list.insert(1, 'Kali Linux')
    print(distros_list)

    distros_list[1:3] = [] #Remove Kali Linux and Ubuntu
    print(distros_list)

    del distros_list[3] #Remove Fedora
    print(distros_list)

    distros_list.pop()  #Remove Arch
    print(distros_list)

    distros_list.pop(1)  #Remove Red Hat
    print(distros_list)

    distros_list.remove('Gentoo')

    distros_list.reverse()
    print(distros_list)

    distros_list.sort()
    print(distros_list)

    a, b, c = [1,2,3]
    print(a)
    print(b)
    print(c)


    #TUPLES
    distros_tuple = ('Debian', 'Kali Linux', 'Ubuntu')
    print(distros_tuple[1])
    #distros_tuple[1] = 'Arch' #error

    distros_tuple = ('Debian', 'Arch', 'Ubuntu') # reassign the var

    print(distros_tuple)

if __name__ == '__main__':
    print_list()