import sys
tpl = "\nPackages sent: {}\nPackages total weight: {} [kg]\nTotal unused space: [kg]\nMost unused space: [kg]\n"
how_many_elements = int(sys.argv[1])
element_weight = int()
package_weight = int()
total_weight_sent = int()
package_counter = int()

for elements_list in range(1, how_many_elements+1):
    elements_list = int(input())
    print(elements_list)
    element_weight = elements_list
    if element_weight == 0:
        print('Value 0 detected. Program stopped, calculations until this point.')
        break
    elif 1 <= element_weight <= 10:
        package_weight += element_weight
        if package_weight >= 20:
            package_counter += 1
            print('Packages sent: ', package_counter, total_weight_sent)
            package_weight = 0
    else:
        print('Value less than 1 or more than 10 detected. Program stopped.')
        sys.exit()

print(tpl.format(package_counter, total_weight_sent))
