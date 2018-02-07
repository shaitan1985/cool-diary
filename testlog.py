import logging

with open('mylog.log', 'w') as f:
    pass

def logging_debug(*args):


    formatt = '[%(levelname)s] %(asctime).19s [%(filename)s_Line:%(lineno)d] %(message)s'

    logging.basicConfig(
        level=logging.DEBUG,
        format=formatt,
        filename = 'mylog.log'
    )

    logger = logging.getLogger()

    logger.debug(args)