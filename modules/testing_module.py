import string_helper

my_string = "This is A test my dood!@.."

print(string_helper.change_case(my_string))

p1, p2 = string_helper.split_in_half(my_string)

print(p1)
print(p2)

print(string_helper.remove_special_characters(my_string))