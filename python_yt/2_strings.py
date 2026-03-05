str ='sirish'
str1 = "Year"
str2 = '''Hi
Hello
How are you
'''
print(len(str))
print(len(str1))
print(len(str2)) #counts/incluses spaces as well
print(str.upper())
print(str1.lower())
print(str.startswith('s'))
print(str.endswith('r'))
print(str.count('i'))
print(str.replace('s','S'))
print('HI'.join('Nimmakayala'))
str3 = str.split('i')
print(str3)
print(str[0])
print(str[1])
print(str[2])
# S I R I S H - index starts from 0
print(str[1:4])
print(str[1:])
print(str[:3])
print(str[-1])
print(str[-6])
print(str[-1:])
print(str[:-1])
print(str[3:-1])
print(str[-6:-1])
print(str[-1:-6])
