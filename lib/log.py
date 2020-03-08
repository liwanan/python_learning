# /usr/bin/python
# -*- coding: utf8 -*-

import json
import logging
import logging.config
import os

pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def set_log_conf(filename=os.path.join(pardir, "config", "logconf.json"), level=logging.DEBUG):
    pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logdir = os.path.join(pardir, "log")
    if not os.path.exists(logdir):
        try:
            os.mkdir(logdir)
        except FileExistsError as error:
            raise error
    if not os.path.exists(filename):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(os.path.join(logdir, "debug.log"))
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(filename)s %(name)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        console = logging.StreamHandler()        
        logger.addHandler(handler)
        logger.addHandler(console)

        logger.error("%s: no such file", filename)
        logger.info("now write log to %s", os.path.join(logdir, "debug.log"))
        return False
    with open(filename, "r") as loghandler:
        config = json.load(loghandler)
        logging.config.dictConfig(config)
    


if __name__ == '__main__':
    set_log_conf()