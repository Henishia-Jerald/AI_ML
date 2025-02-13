# import sys
# from src.my_logger import logging

# def error_message_details(error, error_detail:sys):
#     _,_, tb_exc =error_detail.exc_info()
#     file_name = tb_exc.tb_frame.f_code.co_filename
#     line_no = tb_exc.tb_lineno
#     error_message = "Error has occured in the script name [{0}], line number [{1}] and error message [{2}]".format(file_name,line_no,str(error))


# class CustomException(Exception):
#     def __init__(self, error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message = error_message_details(error_message,error_detail)

#     def __str__(self):
#         return self.error_message



import sys
from src.my_logger import logging

def error_message_details(error, error_detail: sys):
    """Generate a detailed error message with filename and line number."""
    _, _, tb_exc = error_detail.exc_info()
    file_name = tb_exc.tb_frame.f_code.co_filename
    line_no = tb_exc.tb_lineno
    return "Error occurred in script [{0}], line number [{1}], error message: [{2}]".format(
        file_name, line_no, str(error)
    )

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
