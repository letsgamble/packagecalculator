# 1 package <= 20 kg
# 1 element range 1, 10 kg (end if smaller or bigger)
# if 1 element = 0 kg then end
#
# 1. how many packages sent
# 2. how many kg sent
# 3. not used space (how many packages * 20 - kg sent)
# 4. which had most not used space
import sys

current_package_weight = float()
package_max_kg = float(20)
element_weight = float({})
elements_number = int(sys.argv[1])

for package_max_kg in element_weight:
    if element_weight == range(1, 10):
        print(element_weight + "KG element added to the package")
        current_package_weight += element_weight
else:
    print("Next package needed")



