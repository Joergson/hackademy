import code

print("--> Current Terminal output:")

a_list = [1,2,3]

b_list = []

c_list = [3,5,6,2]

another_list = ["harry","ron","hermione"]

yanother_list = [1,"harry",3.4,"blue"]

the_sum = code.my_sum(a_list)
print("Summe: " + str(the_sum))

the_prod = code.my_prod(a_list)
print("Produkt: " + str(the_prod))

the_count = code.my_count(a_list)
print("Anzahl: " + str(the_count))

the_prod0 = code.my_prod(b_list)
print("Produkt: " + str(the_prod0))

the_count_less_5 = code.my_count_less_5(c_list)
print("Anzahl < 5: " + str(the_count_less_5))

the_count_ones = code.my_count_ones(a_list)
print("Anzahl = 1: " + str(the_count_ones))

the_max = code.my_max(c_list)
print("Max Wert: " + str(the_max))