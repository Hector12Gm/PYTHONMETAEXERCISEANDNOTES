http_status = 2000



match http_status:
    case 200 | 201:
        print('Success')
    case 500:
        print('Error')
    case 300:
        print('Nose')
    case _:
        print('Caso por defecto')