

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [LinkedPair()] * capacity

def djb2(string, max):
    hash = 5381
    for c in string:
        hash = (hash * 33) + ord(c)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    table_index = djb2(key, len(hash_table.storage))
    node = hash_table.storage[table_index]
    
    notInserted = True
    while notInserted == True:
    
        if node.key == None or node.key == key:
            node.key = key
            node.value = value
            notInserted = False
        else:
            if node.next != None:
                node = node.next
            else:
                newNode = LinkedPair(key,value)
                node.next = newNode
                notInserted = True

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    table_index = djb2(key, len(hash_table.storage))
    node = hash_table.storage[table_index]

    previousNode = None
    found = False

    while found == False:
        if node.key == None or node.key == key:
            node.key = None
            node.value = None
            found = True
            if node.next != None:
                if previousNode == None:
                    hash_table.storage[table_index] = node.next
                else:
                    previousNode.next = node.next
        else:
            previousNode = node
            node = node.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    table_index = djb2(key, len(hash_table.storage))
    node = hash_table.storage[table_index]

    while True:
        if node.key == None:
            return None
        if node.key == key:
            return node.value
        if node.next == None:
            return None
        else:
            node = node.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    old_len = len(hash_table.storage)
    new_hash_table = HashTable(old_len*2)
    for i in range(old_len):
        new_hash_table.storage[i] = hash_table.storage[i]
    return new_hash_table

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")

Testing()
