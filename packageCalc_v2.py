import sys
tpl = "\nPackages sent: {}\nPackages total weight: {} [kg]\nTotal unused space: {} [kg]\nMost unused space: {} [kg]\n"
how_many_elements = int(sys.argv[1])

for element_weight in range(1, how_many_elements+1):
    element_weight = int(input())
    print(element_weight)
    if 1 <= element_weight <= 10:
        print('od jeden do dziesiec')
    if element_weight == 0:
        print('zero')
        break
    else:
        print('blad')
        sys.exit()
