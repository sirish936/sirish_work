a = [1,'sirish',True,2.2]
for i in a:
    print(i)

b='sirish'
for i in b:
    print(i)

for i in b:
    if(i =='r'):
        print("sirish")
    else: print('python')

i = 1
while(i<5):
    print(i)
    i=i+1
    print(i)
    print('sirish')

sum=0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+i
print(sum)

for i in range(2,20,3):
    print(i)

for i in range(20,10,-1):
    print(i)

mobiles=['iphone','oneplus','samsung','mi','realme','vivo','poco']
for mobile in mobiles:
    if mobile == 'iphone': print('mobile phone '+mobile+' is costly')
    else: print('mobile phone '+mobile+' is cheap')
