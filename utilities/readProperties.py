import configparser as cfp

config = cfp.RawConfigParser()
config.read("/Users/davud/PycharmProjects/hybridFramework_mac/configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
