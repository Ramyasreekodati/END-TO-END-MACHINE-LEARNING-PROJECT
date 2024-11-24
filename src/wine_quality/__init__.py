import os       #for direction and file path manipulation
import sys      # for accessing system-level features
import logging  #for configuring and using the logging system 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
                # format for log messages. It includes the timestamp, logging level , module name and the message.

log_dir = "logs"    # The directory name where log files will be stored
log_filepath = os.path.join(log_dir,"running_logs.log") 
os.makedirs(log_dir, exist_ok=True) # ensures the directory exists, creating it if necessay


logging.basicConfig(
    level= logging.INFO, # captures info and above (info,warining,error,critical and recorded) ignore debug
    format= logging_str,     # how log should be appear

    handlers=[
        logging.FileHandler(log_filepath), # write log messages to the specified file
        logging.StreamHandler(sys.stdout)   # outputs log messages to the console
    ]
)

logger = logging.getLogger("mlProjectLogger") # now this logger can now be used for logging throughout the project.
 