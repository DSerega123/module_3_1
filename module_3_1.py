calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(str):
    str_u = str.upper()
    str_l = str.lower()
    str_ = len(str),str_u,str_l
    count_calls()
    return str_

def is_contains(string, list_to_search):
    for i in range(0,len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    string = string.lower()
    count_calls()
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

