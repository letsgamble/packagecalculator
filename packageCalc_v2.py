import sys

tpl = "\nPackages sent: {}\nPackages total weight: {} [kg]\nTotal unused space: {} [kg]\n" \
      "Most unused space package no. {}: {} [kg]\n"

how_many_elements = int(sys.argv[1])
element_weight = int()
package_weight = int()
total_weight_sent = int()
package_counter = int()
unused_space = int()
most_unused_space = int(0)
not_optimal_weight = int()
most_unused_space_no = int()

for elements_list in range(1, how_many_elements+1):
    elements_list = int(input())
    print(elements_list)
    element_weight = elements_list
    if element_weight == 0:
        print('Value 0 detected. Program stopped, calculations until this point.')
        break
    elif 1 <= element_weight <= 10:
        total_weight_sent += element_weight
        package_weight += element_weight
        if package_weight >= 20:
            if package_weight == 20:
                package_counter += 1
                package_weight = 0
            else:
                package_counter += 1
                unused_space = 20 - (package_weight - element_weight)
                package_weight = element_weight
                if unused_space > most_unused_space:
                    most_unused_space = unused_space
                    most_unused_space_no = package_counter
    else:
        print('Value lower than 1 or higher than 10 detected. Program stopped.')
        sys.exit()

if package_weight > 0:
    package_counter += 1

not_optimal_weight = package_counter * 20 - total_weight_sent

print(tpl.format(package_counter, total_weight_sent, not_optimal_weight, most_unused_space_no, most_unused_space))
