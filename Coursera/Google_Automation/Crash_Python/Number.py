#!/usr/bin/env python3
print("Pon el número a revisar")
x = int(input())
def revisar_numero(x):
    for i in range(1,x+1):
        if x % i == 0:
            n = int(x / i)
            print(f"se ocupa los números {str(i)}x{str(n)}={str(x)}")
revisar_numero(x)
