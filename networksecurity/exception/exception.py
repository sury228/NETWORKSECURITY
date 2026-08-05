import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.filename = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.filename = None

    def __str__(self):
        location = f"[{self.filename}] at line number: [{self.lineno}]" if self.filename is not None else "[unknown location]"
        return f"Error occurred in script: {location} error message: [{self.error_message}]"
    
    
# if __name__ == "__main__":
#     try:
#         logger.info("ENTER THE TRY BLOCK")
#         a = 1/0
#         print("this will not be printed", a)

#     except Exception as e:
#         raise NetworkSecurityException(e, sys) from e
    