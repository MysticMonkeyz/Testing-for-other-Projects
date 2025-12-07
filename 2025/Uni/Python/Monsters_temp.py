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







class S(monster):
    
    en_name = "S"
    
  
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.en_hp = 10.0
        self.ATK_PWR = 3.0
        self.Boost = 0

   
    #Monster increasing it's attack    
    def boost_atk(self):
        self.Boost += 1
        if self.Boost >= 3:
            print(f"{S.en_name} attempted to <placeholder explanation> but failed")
            self.Boost = 3
            return
        self.ATK_PWR += 1 
        print(f"{S.en_name} <placeholder explanation> boosting it's attack power")

    
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



class M(monster):
    
    en_name = "M"
    
  
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.en_hp = 15.0
        self.ATK_PWR = 4.0
        self.Boost = 0

   
    #Monster increasing it's attack    
    def boost_atk(self):
        self.Boost += 1
        if self.Boost >= 3:
            print(f"{M.en_name} attempted to <placeholder explanation> but failed")
            self.Boost = 3
            return
        self.ATK_PWR += 1 
        print(f"{M.en_name} <placeholder explanation> boosting it's attack power")

    
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



class L(monster):
    
    en_name = "L"
    
  
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.en_hp = 20.0
        self.ATK_PWR = 5.0
        self.Boost = 0

   
    #Monster increasing it's attack    
    def boost_atk(self):
        self.Boost += 1
        if self.Boost >= 3:
            print(f"{L.en_name} attempted to <placeholder explanation> but failed")
            self.Boost = 3
            return
        self.ATK_PWR += 1 
        print(f"{L.en_name} <placeholder explanation> boosting it's attack power")

    
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



class XL(monster):
    
    en_name = "XL"
    
  
    def __init__(self, placeholder):
        super().__init__(placeholder)
        self.en_hp = 25.0
        self.ATK_PWR = 6.0
        self.Boost = 0

   
    #Monster increasing it's attack    
    def boost_atk(self):
        self.Boost += 1
        if self.Boost >= 3:
            print(f"{XL.en_name} attempted to <placeholder explanation> but failed")
            self.Boost = 3
            return
        self.ATK_PWR += 1 
        print(f"{XL.en_name} <placeholder explanation> boosting it's attack power")

    
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



monster1 = XS("placeholder")
monster1.total()
monster2 = XS("placeholder")
monster2.total()

monster1.attack(30)

monster1.boost_atk()


monster1.take_damage(45)

