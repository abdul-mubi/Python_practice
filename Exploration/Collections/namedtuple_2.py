from collections import namedtuple

x = namedtuple('course_details','course_name coding_language fees', defaults=[2000])
y = namedtuple('course_details','course_name,coding_language')
print(x._fields)
print(y._fields)

t = x('AI','python')
print(t)

replaced_t = t._replace(fees=5000)
print(replaced_t)
print(t)

