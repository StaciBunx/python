import logging

logging.basicConfig(filename='log.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)
