import logging

"""
Objective: track event logs in code.

What may be tracked?
- Timestamp
- Level of severity (in order, DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Module
- Custom messages

Notes:
- to print outputs a simple print() is usually preferrable
"""

# basicConfig -> set the file and format to which the logs must be written, plus the minimum level of logs to write (all logs below this level won't be written)
logging.basicConfig("events.log", format='%(asctime)s ; %(levelname)s ; %(module)s ; %(message)s', level = logging.DEBUG)

# Main objects: LOGGER
logger = logging.getLogger(__name__)

# - Log messages at runtime
logger.debug("...")
logger.info("...")
logger.warning("...")
logger.error("...")
logger.critical("...")

# - Filter log messages
logger.addFilter()

# - Pass filtered log messages to a HANDLER, which determines where messages go
#   e.g. all messages to a file, messages of error severity and higher to stdout (standard output), messages of critical level to an email address
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler("events.log", encoding = "charmap")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)
sh.setFormatter(formatter)
logger.addHandler(sh)

mh = logging.SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['admin@example.com'],
    subject='Application Error'
)
mh.setLevel(logging.CRITICAL)
mh.setFormatter(formatter)
logger.addHandler(mh)

