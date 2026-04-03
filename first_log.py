import logging

logging.basicConfig(
    filename = 'password.log' ,
    level = logging.INFO ,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

correct_password = 'admin123'

def login():
    logging.info('Entered in login fun and taking user pass')
    password = input('Enter password')
    
    if password == correct_password: #admin123
        logging.info('Login Sucessful')
        print('Login Sucessful')
        logging.info('If condetion completed')
    else:
        logging.warning('Failed to login')
        print('Failed to login')
        logging.info('else condetion completed')

login()