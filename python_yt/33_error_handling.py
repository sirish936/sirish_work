try:
    a=1
    print(b) # risky code
except:
    print('Error')
else:
    print('No Error')
finally:
    print("always")

try:
    a=1
    print(b) # risky code
except Exception as e:
    print('Error', e)
else:
    print('No Error')
finally:
    print("always")

try:
    print('raise Exception')
    raise Exception
except Exception as e:
    print('Handled raised Exception', e)
finally:
    print("always")

try:
    print('raise Exception')
    raise Exception('this is raised Exception')
except Exception as e:
    print('Handled raised Exception', e)
finally:
    print("always")