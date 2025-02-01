import logging

logging.basicConfig(level=logging.DEBUG,filename="mylog.log",filemode='w',
                    format="python-app: %(process)d %(name)s - %(levelname)s - %(message)s - %(asctime)s") # if this line not present then you will get loggig from warning


logging.debug("debug error occured in code..")
logging.info("admin logged in ..")
logging.warning("warning: less disk space...check it..")
logging.error("file not found..")
logging.critical("critical: app crashed..")

username="Sharath"
logging.info(f" {username} has logged in")

try:
  a=10
  b=0
  c=a/b
except Exception as ex:
  logging.error("Exception occured",exc_info=True)