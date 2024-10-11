# Relational and Boolean Operators in Python

# Define two numbers
a = 10
b = 20

# Relational Operators
print("Relational Operators:")
is_equal = a == b
print(f"Is {a} equal to {b}? {is_equal}")

is_not_equal = a != b
print(f"Is {a} not equal to {b}? {is_not_equal}")

is_greater = a > b
print(f"Is {a} greater than {b}? {is_greater}")

is_less = a < b
print(f"Is {a} less than {b}? {is_less}")

is_greater_equal = a >= b
print(f"Is {a} greater than or equal to {b}? {is_greater_equal}")

is_less_equal = a <= b
print(f"Is {a} less than or equal to {b}? {is_less_equal}")

# Define two more numbers
c = 15
d = 15

# Additional Relational Operators
print("\nAdditional Relational Operators:")
is_equal_cd = c == d
print(f"Is {c} equal to {d}? {is_equal_cd}")

is_not_equal_cd = c != d
print(f"Is {c} not equal to {d}? {is_not_equal_cd}")

is_greater_cd = c > d
print(f"Is {c} greater than {d}? {is_greater_cd}")

is_less_cd = c < d
print(f"Is {c} less than {d}? {is_less_cd}")

is_greater_equal_cd = c >= d
print(f"Is {c} greater than or equal to {d}? {is_greater_equal_cd}")

is_less_equal_cd = c <= d
print(f"Is {c} less than or equal to {d}? {is_less_equal_cd}")

# Boolean Operators
print("\nBoolean Operators:")
# Using 'and' operator
and_result = (a < b) and (c == d)
print(f"({a} < {b}) and ({c} == {d}) is {and_result}")

# Using 'or' operator
or_result = (a < b) or (c != d)
print(f"({a} < {b}) or ({c} != {d}) is {or_result}")

# Using 'not' operator
not_result = not (a > b)
print(f"not ({a} > {b}) is {not_result}")

# Combining relational and boolean operators
combined_result = (a < b) and (c == d) or not (a > b)
print(f"({a} < {b}) and ({c} == {d}) or not ({a} > {b}) is {combined_result}")
