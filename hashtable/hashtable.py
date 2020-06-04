class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HashTableEntry({repr(self.key)}, {repr(self.value)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class SLL:
    def __init__(self, node=None):
        self.head = None
        self.tail = None

    def add_to_tail(self, key, value):
        new_node = HashTableEntry(key, value)

        # there's nothing in linked list
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, key):
        current = self.head

        if current.key == key:
            self.head = self.head.next
            return current.value

        previous = current
        current = current.next

        while current is not None:
            if current.key == key:
                previous.next = current.next
                return current.value

            else:
                previous = previous.next
                current = current.next

        return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here

        self.capacity = capacity
        self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        # load factor is the number of slots filled divided by capacity?

        total = 0

        for i in range(len(self.storage)):
            if self.storage[i] != None:

                current = self.storage[i].head

                while current.next is not None:
                    total += 1

                    current = current.next

                total += 1

        return total / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        # byte object is returned after converting key into bytes
        # specify encoding because other machines might have different default encoding
        bytes_obj = str(key).encode("utf-8")
        djb2_val = 5381
        total_val = 0

        for char in bytes_obj:
            total_val += ((djb2_val << 5) + djb2_val) + char
            total_val &= 0xffffffff

        return total_val

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # check if key is already in storage
        if self.storage[index] != None:

            # if key is already in storage, overwrite current value

            current = self.storage[index].head

            while current.next is not None:
                if current.key == key:
                    # overwrite the value
                    current.value = value

                current = current.next

            if current.key == key:
                current.value = value
            else:
                self.storage[index].add_to_tail(key, value)

        else:
            # if key is not in storage, create a new linked list passing in the key and value as the value

            self.storage[index] = SLL()
            self.storage[index].add_to_tail(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # self.storage[index] is a node with tuple as a value
        # if self.storage[index].key is not equal to the key, traverse the linked list
        if self.storage[index].head.key == key:
            self.storage[index].head.value = None

        else:
            current = self.storage[index].head

            while current.next is not None:
                if current.key == key:
                    current.value = None

                current = current.next

            # current.next is now None, the last current will be the tail
            if current.key == key:
                current.value = None

            else:
                return "Key not found!"

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # if self.storage[index].key == key, return the value
        # if self.storage[index].key is not the key, traverse the linked list
        # if not found return None

        index = self.hash_index(key)

        if self.storage[index].head.key == key:
            return self.storage[index].head.value

        else:

            current = self.storage[index].head

            while current.next is not None:
                if current.key == key:
                    return current.value

                current = current.next

            if current.key == key:
                return current.value

            else:
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # create a copy of the old storage
        storage_copy = self.storage
        # change value of capacity
        self.capacity = new_capacity
        # change value of storage
        self.storage = [None] * self.capacity

        # loop through items of the array
        # if item.next is None, move to next index
        for i in range(len(storage_copy)):
            # each item is a linked list
            if storage_copy[i] != None:

                # traverse the linked list and rehash each item
                current = storage_copy[i].head

                while current.next is not None:
                    self.put(current.key, current.value)
                    current = current.next

                # current value will now be the tail
                index = self.hash_index(current.key)

                self.put(current.key, current.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(ht.get_load_factor())

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
