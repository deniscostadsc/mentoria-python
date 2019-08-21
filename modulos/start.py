import sys

from funcoes import fib, fat, fatfib


result = fib(int(sys.argv[1]))
print(result)
result = fat(int(sys.argv[1]))
print(result)
result = fatfib(int(sys.argv[1]))
print(result)

print(sys.path)
