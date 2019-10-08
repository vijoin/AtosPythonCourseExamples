def print_list():

    #List syntax
    list1 = [1, 'Hello', 8, 'World']   #List supports different data types
    print(list1)

    #Access an element
    list2 = [10, 'Again', list1]
    print(list2)
    print(list1[2])
    print(list1[1])
    print(list2[2][3])

    #Slice the list
    print(list1[:-2])
    print(list1[1:2])

    #IndexError
    #print(list2[3])

    #Replace an element
    list1[2] = 'Beautiful'
    print(list1)

    #Sum lists
    sum_list = list1 + list2[:2]
    print(sum_list)

    #multiply a list
    mult_list = list1 * 2
    print(mult_list)

    #Let's work with a list of Linux Distributions
    distros_list = ['Debian', 'Ubuntu']

    #Add an item at the end
    distros_list.append('Red Hat')
    print(distros_list)

    #Add a whole list to form a bigger list
    distros_list = distros_list + ['Gentoo', 'Fedora', 'Arch']
    print(distros_list)

    #What's the lenght of the list?
    print("List Lenght: {}".format(len(distros_list)))

    #How to insert an item in a specific point
    distros_list.insert(1, 'Kali Linux')
    print(distros_list)

    #Remove several items with slicing
    distros_list[1:3] = [] #Remove Kali Linux and Ubuntu
    print(distros_list)

    #Another way to remove an item
    del distros_list[3] #Remove Fedora
    print(distros_list)

    #A third way to remove, but this is different
    #This returns the removed value
    removed_distros = list()
    removed_distros.append(distros_list.pop())  #Remove Arch
    print(distros_list)
    print(removed_distros)

    #Let's add a new item with the recent removed distro
    removed_distros.append(distros_list.pop(1))  #Remove Red Hat
    print(distros_list)
    print(removed_distros)

    #Remove and item by its content
    distros_list.remove('Gentoo')

    distros_list.reverse()
    print(distros_list)

    distros_list.sort()
    print(distros_list)

    #Do you remember multiple assign?
    #Here we call it "Unpacking"
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

    #Let's solve a problem
    #High Score
    #Exercism.io / Python / High Score

if __name__ == '__main__':
    print_list()