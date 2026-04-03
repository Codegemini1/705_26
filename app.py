import logging

logging.basicConfig(
    filename = 'calculator.log' ,
    level = logging.ERROR ,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def devide(a,b):
    try:
        result = a/b
        return result
    except Exception as e:
        logging.error(e)
        logging.error(f'value for a is {a} and b is {b}')


print(devide(10,2))
print(devide(10,0))
print(devide(0,0))
print(devide(5,'Hello'))