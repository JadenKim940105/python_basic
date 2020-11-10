hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_func(key):
    return key % 8

def save_data(key, value):
    index_key = get_key(key)
    hash_addr = hash_func(index_key)
    if hash_table[hash_addr] != 0:
        for index in range(hash_addr, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_addr] = [index_key, value]

def read_data(key):
    index_key = get_key(key)
    hash_addr = hash_func(index_key)
    if hash_table[hash_addr] != 0:
        for index in range(hash_addr, len(hash_table)): # hash_addr 부터 hash_table 의 끝까지 순회
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

