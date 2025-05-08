# CRUD and 
# Dict, list, Json
# filter & sort, sorted and map function
# datetime function
# file system and path system
# SQL Database, Excel sheet related Library
# Automation Related Functionality
# Oops (Class, Object and Inheritance)
# I want to learn Python

# Dict , List
def dict_practice():
    # Create
    my_dict={
        'k1':1,
        "k2": 'v2',
        "k3": [1,2,3],
        "k4": {
            'k11': 1,
            'k22': 2
        }
    }

    return my_dict

# read
def dict_read():
    result=dict_practice()
    print(f'keys: {result.keys()}')
    print(f'Values: {result.values()}')
    print(f'items: {result.items()}')
    for k, v in result.items():
        print(f"{k}: {v}")
        
def dict_update():
    # updatd({})
    result=dict_practice()
    result.update({'k5': 5})
    print(f'Updated Dict: {result}')
    result['k5']=55
    print(f'Updated 2times Dict: {result}')

    
def dict_delete():
    result=dict_practice()
    print(f"Key List: {list(result.keys())}")
    if 'k4' in list(result.keys()):
        # result.clear()
        result.pop('k2')
    else:
        print('fail')
    print(f'result: {result}')

def dict_sort():
    result=dict_practice()
    


def dict_operation():
    dict_read()
    dict_update()
    dict_delete()
    
    
dict_operation()

# list method
l=[1,2,3,4,5]

l1=[i for i in l]
l1.append(6)

print(l1, l)
    
