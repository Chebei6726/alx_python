#!/usr/bin/python3
from add_0 import add
#define a and b
a=1
b=2
result= add(a,b)
output_format="{a} + {b}={result}"
print(output_format.format(a=a,b=b,result=result))
if __name__ == '__main__':
    print()