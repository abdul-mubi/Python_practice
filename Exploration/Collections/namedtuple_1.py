# We can call a variable inside tuple by using index
# But in namedtuple we can can a varibale inside namedtuple using name
# In-build methods: _make, _asdict, _replace, _fileds, _field_defaults

from collections import namedtuple

x = namedtuple('course_details',["course_name","coding_language"],defaults=['python'])
t = x('data_science','python')
print(x)
print(t)
print(t.course_name)
print(t.coding_language)
print('---------------------------------------------------------')
my_list = ['AI','java_script']
t = x._make(my_list)
print(t)
print('---------------------------------------------------------')
print(t._asdict())
my_dict = t._asdict()
print(my_dict)
print('---------------------------------------------------------')
replaced_t = t._replace(coding_language='java')
print(replaced_t)
print(t)
print('---------------------------------------------------------')
print(t._fields) #it return defined filed names inside namedtuple
print('---------------------------------------------------------')
print(t._field_defaults) #it return given default value as dict with key as last component inside namedtuple and value as given default value 

