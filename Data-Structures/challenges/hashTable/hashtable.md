# Hashtables

Hash - A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array. Buckets - A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs. Collisions - A collision is what happens when more than one key gets hashed to the same location of the hashtable.

## Challenge

### Implement a Hashtable Class with the following methods:

- add
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get
  - Arguments: key
  - Returns: Value associated with that key in the table
- contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency

### The approach used is to convert the key of the input into index and put the key value object in the hashtable, that contains a linked list for the collisions.

### Big O Notation

#### Time: O(1)

#### Space: O(N)

## API

- Create a hashtable with the following methods:
  - `add` which takes in both the key and value. Hash the key, and add the key and value pair to the table, handling collisions as needed.
  - `get` that takes in the key and returns the value from the table.
  - `contains` that takes in the key and returns a boolean, indicating if the key exists in the table already.
  - `hash` that takes in an arbitrary key and returns an index in the collection.
- Insert key, value pair in the hashtable.
- Hash keys to determine is which index it should be added.
- Make a link_list to handle collisions.
- Retrieve the value of the bucket using its key.
- Determine if a specific key is inside the hashtable or not.

[code](https://github.com/amarh-ayman/401_data-structures-and-algorithms/blob/main/Data-Structures/challenges/hashTable/hashtable.py)

[test](https://github.com/amarh-ayman/401_data-structures-and-algorithms/blob/main/Data-Structures/challenges/tests/test_hashtable.py)
