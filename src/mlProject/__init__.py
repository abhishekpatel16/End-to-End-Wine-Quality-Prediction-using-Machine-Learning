import os  # Importing the os module to interact with the operating system
import sys  # Importing the sys module to access system-specific parameters and functions
import logging  # Importing the logging module to log messages

# Defining the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Defining the directory where log files will be stored
log_dir = "logs"
# Creating the full file path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")
# Creating the logs directory if it does not already exist
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging module
logging.basicConfig(
    level=logging.INFO,  # Setting the logging level to INFO
    format=logging_str,  # Specifying the log message format
    handlers=[
        logging.FileHandler(log_filepath),  # Logging messages to a file
        logging.StreamHandler(sys.stdout)  # Logging messages to the console
    ]
)

# Creating a logger instance with a custom name
logger = logging.getLogger("mlProjectLogger")