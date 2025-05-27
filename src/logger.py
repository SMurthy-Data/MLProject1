import logging,os
from datetime import datetime

LOG_FILE=f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
LOG_DIR=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_DIR,exist_ok=True)

LOG_PATH= os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# import sys

# def get_error_details(error):
#     _,_,exc_tb = sys.exc_info()
#     file_path = exc_tb.tb_frame.f_code.co_filename
#     error_message = "Error in path: [{0}]\nLine Number: [{1}]\nError Message: [{2}]".format(
#         file_path,exc_tb.tb_lineno,error
#     )

#     return error_message

# class CustomException(Exception):
#     def __init__(self, error):
#         error_details = get_error_details(error)
#         super().__init__(error_details)
#         # self.error_details = error_details

# def divide(a,b):
#     return a / b

# if __name__=="__main__":
#     try:
#         result = divide(0,a)
#     except Exception as e:
#         custom_exception = CustomException(e)
#         logging.error(custom_exception)
#     else:
#         print(result)