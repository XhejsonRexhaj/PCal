class Calculator:

    __name = None
    __portion = None
    __fats = None
    __carbs = None
    __proteins = None

    __fatsKcalPerGr = 9.0
    __carbsKcalPerGr = 4.0
    __proteinsKcalGr = 4.0

    __fatsKcal = None
    __carbsKcal = None
    __proteinsKcal = None

    __calorySum = None

    def __init__(self, name = " ", portion = 0.0, fats = 0.0, carbs = 0.0,  proteins = 0.0):
        self.__name = name
        self.__portion = portion
        self.__fats = fats
        self.__carbs = carbs
        self.__proteins = proteins

    def getName(self):
        return self.__name
    
    def getPortion(self):
        return self.__portion
    
    def getFats(self):
        return self.__fats
    
    def getCarbs(self):
        return self.__carbs
    
    def getProteins(self):
        return self.__proteins
    
    def calculateCalories(self):
        self.__fatsKcal = self.__fats * self.__fatsKcalPerGr
        self.__carbsKcal = self.__carbs * self.__carbsKcalPerGr
        self.__proteinsKcal = self.__proteins * self.__proteinsKcalGr

        self.__calorySum = self.__fatsKcal + self.__carbsKcal + self.__proteinsKcal

        return self.__calorySum

    