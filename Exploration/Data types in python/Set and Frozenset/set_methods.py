sample_set = set({})
sample_set.add('abdul')
print(f'sample_set - {sample_set}')
sample_set.add('abdul')
print(f'sample_set - {sample_set}')
sample_set.add('mubi')
print(f'sample_set - {sample_set}')
sample_set_2 = sample_set.copy()
print(f'sample_set_2 - {sample_set_2}')
sample_set.add('rayan')
print(f'sample_set - {sample_set}')
print(f'sample_set_2 - {sample_set_2}')
sample_set_2.remove('abdul')
print(f'sample_set_2 - {sample_set_2}')
sample_set.clear()
print(f'sample_set - {sample_set}')
list_out = list(sample_set_2)
print(list_out)
