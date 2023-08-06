# PythonAdvanceLogger
Python Advance logger capable to log every event with django default logger, elasticsearch, and file log
This package use as a python standard logger as a base logger and add extra features for better log handling 
by lesser actions in python and django

This package aims to create log like asp.net logger which capable to distribute log over elasticsearch, file, and other
extra loggers

This package contains 4 main modules:
* Python default logger
* Elasticsearch logger (Using http requests)
* file logger

Install package by:
    


How to setup package in django:

After installation advanceLogging package from pypi, you can setup you logger as a shown below:

```
elsConf = ElasticSearchConf(hosts=["your host: port"],
                            user="username",
                            password="pass",
                            indicator="your elastic index",
                            maxConnection=10)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "advance_logger": {
            "format": "%(asctime)s %(created)f %(filename)s %(funcName)s %(levelname)s %(levelno)s %(lineno)d %(module)s"
                      " %(name)s %(levelname)s %(message)s %(pathname)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            "class": "advanceLogger.AdvanceLogFormatter"
        }
    },
    "handlers": {
        "console": {
            "class": "advanceLogger.AdvanceLogHandler",
            "formatter": "advance_logger",
            "els_conf": elsConf
        }
    },
    "loggers": {
        # Make sure to replace the following logger's name for yours
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    }
}
```

After define logger in your django settings.py you can use this logger every place of your codes like below:

```angular2html
import logging

logger = logging.getLogger("django_structlog_demo_project")


class Startup:
    def __init__(self):
        logger.info("start app", extra={"extraParams": 1})
        logger.debug("start app")
        logger.error('test')
        requests.get('https://reqres.in/api/users?page=2')
```