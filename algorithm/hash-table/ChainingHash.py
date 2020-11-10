hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(key, value):
    index_key = get_key(key)
    hash_addr = hash_func(index_key)
    if hash_table[hash_addr] != 0:
        for index in range(len(hash_table[hash_addr])):
            if hash_table[hash_addr][index][0] == index_key:
                hash_table[hash_addr][index][1] = value
                return
        hash_table[hash_addr].append([index_key, value])
    else:
        hash_table[hash_addr] = [[index_key, value]]

def read_data(key):
    index_key = get_key(key)
    hash_addr = hash_func(index_key)
    if hash_table[hash_addr] != 0:
        for index in range(len(hash_table[hash_addr])):
            if hash_table[hash_addr][index][0] == index_key:
                return hash_table[hash_addr][index][1]
        return None
    else:
        return None
print(hash('xcv') % 8)
print(hash('d') % 8)

save_data('xcv', 111)
save_data('d', 222)

print(read_data('xcv'))
print(read_data('d'))