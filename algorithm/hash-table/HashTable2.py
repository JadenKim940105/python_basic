hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save(key, value):
    key = get_key(key)
    hash_table[hash_func(key)] = value

def getData(key):
    return hash_table[hash_func(get_key(key))]

save('jaden', 123123)
print(getData('jaden'))