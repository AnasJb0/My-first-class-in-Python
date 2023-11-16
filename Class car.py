class car():
    def __init__(self,name,color,model,energie) :
        self.name=name
        self.color=color
        self.model=model
        self.energie=energie
    def affichage(self):
        print("The name car is {} , the color is {} , the model is {} , the energie is {} horses".format(self.name,self.color,self.model,self.energie))

car1=car("Audi","Red","RS3",630)
car1.affichage()