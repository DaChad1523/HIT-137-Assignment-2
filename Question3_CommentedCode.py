global_variable = 100 #fixing spelling mistake varable > variable
my_dict = {'key11': 'value1', 'key12': 'value2', 'key13': 'value3'} #fixing spelling mistake ke > key

def process_numbers(numbers): #numbers is now the variable put into the function
    global global_variable
    local_variable = 5   #fixing spelling mistake varable > variable

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(my_set) #my_set is now sent straight into the function

def modify_dict():
    local_varable = 10
    my_dict['key14'] = f"value{local_varable}" #ke14 > key14, also i think it wants the value to be 'value10' so i added a string to it.

modify_dict()

#def update_global():
    #global global_variable       not needed as the function is not used.
    #global_variable += 10

#for i in range(5):     not needed as it doesnt affect the code at all.
    #print(i)
    #i += 1

if my_set is not None and my_dict['key14'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)