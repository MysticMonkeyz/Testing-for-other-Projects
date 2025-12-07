def boosting(func):
    def boostinner():
        boost, atk, name = func()
        if (int(boost) + 1) > 3:
            print(f"{str(name)} attempted to <placeholder explanation> but failed")
        else:
            boost = int(boost) + 1
            atk = int(atk) + 1
            return boost, atk, name
            



class monster:
    
    def __init__(self, placeholder : str):       
        self.placeholder = placeholder
        self.total_en = 0
        self.en_list = []
    
        
    #Tallies up amount of monsters
    def total(self):
        if self not in self.en_list:
            self.total_en += 1 
            self.en_list.append(self)
            print(self.en_list)
        else:
            print("monster already added")


class XS(monster):
    
    en_name = "XS"
    
  
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.en_hp = 5.0
        self.ATK_PWR = 2.0
        self.Boost = 0

   
    #Monster increasing it's attack    
    def boost_atk(self):
        self.Boost += 1
        if self.Boost >= 3:
            print(f"{XS.en_name} attempted to <placeholder explanation> but failed")
            self.Boost = 3
            return
        self.ATK_PWR += 1 
        print(f"{XS.en_name} <placeholder explanation> boosting it's attack power")

    
    #Monster taking damage
    def take_damage(self, amount):
        self.en_hp -= amount
        if self.en_hp <= 0:
            self.en_list.remove(self)
            self.total_en -= 1 
            print(f"{self.en_name} has been defeated!")
        else:    
            print(f"{self.en_name} has {self.en_hp} hp left")   
            
            
    #Monster Attacking
    def attack(self, player_hp):
        print(f"{self.en_name} attacks with {self.ATK_PWR} attack power.")
        player_hp -= self.ATK_PWR
        return player_hp

    
    @boosting 
    def yeh_mate(self):
        return self.Boost, self.ATK_PWR, self.en_name



dog = XS("dog")  
cat = dog
print(cat.yeh_mate())
