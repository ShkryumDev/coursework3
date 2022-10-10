import logging


logger_one = logging.getLogger('one')
logger_two = logging.getLogger('two')
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/log.log')
logging.basicConfig(level=logging.INFO)
formatter_one = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)
logger_two.addHandler(console_handler)
logger_one.addHandler(file_handler)
logger_one.info(f'Запрос /api/posts')
