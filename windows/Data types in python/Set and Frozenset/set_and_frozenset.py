# what is difference between set and list in py

# Both sets and lists in Python are used to store collections of items, 
# but they have some key differences in terms of their characteristics and use cases:

# Ordering:
# List: Lists are ordered collections, meaning the elements are stored in a specific order and can be accessed using indices.
# Set: Sets are unordered collections. They do not guarantee the order of elements, and you cannot access elements using indices.

# Duplicates:
# List: Lists can contain duplicate elements.
# Set: Sets do not allow duplicate elements. Any duplicate elements are automatically removed.

# Mutability:
# List: Lists are mutable, meaning you can change, add, or remove elements after the list is created.
# Set: Sets are also mutable. You can add and remove elements, but you cannot change elements directly because they don't have indices.

# Membership Testing:
# List: To check if an element is in a list, the membership testing operation takes linear time (O(n)) because it needs to search through the list.
# Set: Sets use hash-based indexing for quick membership testing. This makes membership testing in sets very fast (close to O(1)).

# Use Cases:
# List: Lists are suitable for maintaining an ordered sequence of elements, and they allow duplicates. Use lists when you care about the order of items or when you need to store multiple occurrences of the same item.
# Set: Sets are useful when you need to store a collection of unique elements and do not care about their order. They are particularly efficient for membership testing and removing duplicates.

set1 = {1,2,10,8,3,5,1,-9}
print(set1)
print(set1.pop())

# set and frozenset are both data types in Python used to store collections of unique elements, 
# but they have a crucial difference in terms of mutability:

# Mutability:
# set: A set is mutable, meaning you can add or remove elements from it after it's created. 
#      Sets are unordered collections, and their elements are not indexed.
# frozenset: A frozenset is immutable, meaning once it's created, you cannot add or remove elements from it. 
#            It is essentially a read-only version of a set.

my_frozenset = frozenset({1,2,3,5,1})
print(my_frozenset)