class Country:
    def __init__(this, name, continent, president):
        this.name = name
        this.continent = continent
        this.president = president
    
    def changePresident(self, presName):
        self.presName = presName
        return self.presName

#changing object properties
myCountry = Country("Nigeria", "Africa", "Tinubu")
print(myCountry.name) #prints Nigeria

myCountry.name = "South Africa"
print(myCountry.name) #prints South Africa