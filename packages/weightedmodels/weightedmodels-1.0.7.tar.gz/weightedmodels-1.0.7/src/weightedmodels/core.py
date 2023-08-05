from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class WeightedModels:
    def __init__(self, models, trainSplit = 0.85, randomState = 69420):
        if type(models) is list:
            self.__models = models
        else:
            raise TypeError("Initiatization expected a list of models, but instead received " + str(type(models)))

        if trainSplit >= 1:
            raise Exception("trainSplit expected to be less than 1")

        self.trainSplit = trainSplit
        self.randomState = randomState
        self.__weights = []
            
    def getModelWeights(self):
        if not self.__weights:
            raise Exception("Models are not fitted yet. Use .fit() before calling .showWeights()")            
        
        return self.__weights
            
    def fit(self, X, y):
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(X, y, train_size=self.trainSplit, random_state=self.randomState)
        
        for model in self.__models:
            model.fit(self.__X_train, self.__y_train)  
        
        self.__calculateWeights()  
        
    def __calculateWeights(self):
        preds = []
        acc = []
        for model in self.__models:
            preds.append(model.predict(self.__X_test))
        
        for pred in preds:
            acc.append(mean_squared_error(self.__y_test, pred))
            
        tempo = list(map(lambda x: (sum(acc)-x),acc))
        self.__weights = list(map(lambda x: x/sum(tempo) ,tempo))
        
    def predict(self, X):
        if not self.__weights:
            raise Exception("Models are not fitted yet. Use .fit() before calling .predict()")
        
        preds = []
        for model in self.__models:
            preds.append(model.predict(X))
        
        for i in range(len(preds)):
            preds[i] = (list(map(lambda x: x * self.__weights[i], preds[i])))
            
        return [sum(x) for x in zip(*preds)]
