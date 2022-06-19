import configparser

con=configparser.RawConfigParser()
con.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url =con.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username =con.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password =con.get('common info', 'password')
        return password
