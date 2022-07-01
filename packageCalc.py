tpl = "\nPackages sent: {}\nPackages total weight: {} [kg]\nTotal unused space: {} [kg]\nMost unused space: {} [kg]\n"

current_elements_weight = int()
package_counter = int()
package_weight_counter = int()
most_weight_difference = int()
weight_difference = int()
total_unused_space = int()
last_element = int()
file_name = 'in.txt'

with open(file_name) as file:
    only_one_package = sum(int(line) for line in file)
    if only_one_package <= 20:
        print('Shall we send this', only_one_package, 'KG package alone?')

with open(file_name) as file:
    for element_weight in file:
        element_weight = int(element_weight)
        if 1 <= element_weight <= 10:
            current_elements_weight += element_weight
            if current_elements_weight > 20:
                last_element = element_weight
                last_element = last_element
                current_elements_weight -= element_weight
                weight_difference = 20 - current_elements_weight
                if weight_difference > most_weight_difference:
                    most_weight_difference = weight_difference
                package_weight_counter += current_elements_weight
                package_counter += 1
                package_counter = package_counter
                total_unused_space = package_counter * 20 - package_weight_counter
                current_elements_weight = element_weight
        else:
            print('Wrong value provided! You broke the program!')

if last_element > 0:
    package_counter += 1
    package_weight_counter += last_element
    weight_difference = 20 - last_element
    total_unused_space = package_counter * 20 - package_weight_counter
    if weight_difference > most_weight_difference:
        most_weight_difference = weight_difference
    print(tpl.format(package_counter, package_weight_counter, total_unused_space, most_weight_difference))
