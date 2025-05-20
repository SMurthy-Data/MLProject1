import sys

def get_error_details(error):
    _,_,exc_tb = sys.exc_info()
    file_path = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in path: [{0}]\nLine Number: [{1}]\nError Message: [{2}]".format(
        file_path,exc_tb.tb_lineno,error
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error):
        error_details = get_error_details(error)
        super().__init__(error_details)
        self.error_details = error_details



