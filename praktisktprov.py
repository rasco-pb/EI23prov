#Author Oscar Palm Blomberg
#Date 2024-09-25

tal = []

user_input = (input("skriv ditt/dinna tal här: "))

for i in user_input:
    if " " != i:
        tal.append(int(i))

for i in tal:
    print(f"{i} * 1 =  {i*1}")
    print(f"{i} * 2 =  {i*2}")
    print(f"{i} * 3 =  {i*3}")
    print(f"{i} * 4 =  {i*4}")
    print(f"{i} * 5 =  {i*5}")
    print(f"{i} * 6 =  {i*6}")
    print(f"{i} * 7 =  {i*7}")
    print(f"{i} * 8 =  {i*8}")
    print(f"{i} * 9 =  {i*9}")
    print(f"{i} * 10 =  {i*10}")