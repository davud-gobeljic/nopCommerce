import logging

class LogGen:
     @staticmethod
     def loggen():
          logger = logging.getLogger()
          fhandler = logging.FileHandler(
              filename='/Users/davud/PycharmProjects/hybridFramework_mac/logs/automation.log', mode='a')
          formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
          fhandler.setFormatter(formatter)
          logger.addHandler(fhandler)
          logger.setLevel(logging.INFO)
          return logger