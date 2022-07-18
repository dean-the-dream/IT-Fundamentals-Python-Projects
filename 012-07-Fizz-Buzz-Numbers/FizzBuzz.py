for i in range(1,101):
    fizz, buzz='', ''
    if(not i % 3):
        fizz = 'Fizz'
    if(not i % 5):
        buzz = 'Buzz'
    print(fizz+buzz) if (fizz or buzz) else print(i)