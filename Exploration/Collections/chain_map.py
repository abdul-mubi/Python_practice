# A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. 
# It is often much faster than creating a new dictionary and running multiple update() calls.

from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chain_map = ChainMap(baseline,adjustments)
print(chain_map)
print('-------------------------------------')

keys = chain_map.keys()
print(keys)
print(list(keys))
print('-------------------------------------')

values = chain_map.values()
print(values)
print(list(values))
print('-------------------------------------')

for key, val in chain_map.items():
    print(key,val)
print('-------------------------------------')

chain_map.update({'final':123, 'final2':456})
print(chain_map)
print('-------------------------------------')
