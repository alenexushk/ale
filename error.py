
try:
    input('What is your name? ')
    print(name)
    
except TypeError as t:
    print('TypeError triggered')

except NameError as n:
    print('NameError triggered')
    print(str(n))
    
except Exception as e:
    print('General exception')
    print(str(e))
       
