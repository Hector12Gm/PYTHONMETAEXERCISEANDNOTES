def divive(a,b):
    return a / b

try:
    ans = print(divive(2,0))
except Exception as e:
    match ZeroDivisionError:
        case 'division by zero':
            print(e.__class__)
    print("Something when run")


