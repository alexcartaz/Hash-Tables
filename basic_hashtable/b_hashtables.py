
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class BasicHashTable:
    def __init__(self, capacity):
        self.storage = [Pair(None,None)] * capacity

def djb2(string, max):
    hash = 5381
    for c in string:
        hash = (hash * 33) + ord(c)
    return hash % max

def hash_table_insert(BasicHashTable, key, value):
    table_index = djb2(key, len(BasicHashTable.storage))
    if BasicHashTable.storage[table_index].value != None:
        print('Warning, overwriting existing data on insert')
    BasicHashTable.storage[table_index] = Pair(key,value)

def hash_table_remove(BasicHashTable, key):
    table_index = djb2(key, len(BasicHashTable.storage))
    if BasicHashTable.storage[table_index].value == None:
        print('Warning, removing a value of None')
    BasicHashTable.storage[table_index] = Pair(None,None)


def hash_table_retrieve(BasicHashTable, key):
    table_index = djb2(key, len(BasicHashTable.storage))
    return BasicHashTable.storage[table_index].value

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
