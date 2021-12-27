from __future__ import print_function
from pprint import pprint

class Datasheet_Profiles:
    def __init__(self,Profiles_Battlefield_role,Profiles_Name,Profiles_Movement,Profiles_Weapon_Skill,Profiles_Ballistic_Skill,Profiles_Strength,Profiles_Toughness, Profiles_Wounds, Profiles_Attacks, Profiles_Leadership,Profiles_Armour_Save,Profiles_Abilites):
            self.Battlefield_role = Profiles_Battlefield_role
            self.Name = Profiles_Name
            self.Movement = Profiles_Movement
            self.Weapon_Skill = Profiles_Weapon_Skill
            self.Ballistic_Skill = Profiles_Ballistic_Skill
            self.Strength = Profiles_Strength
            self.Toughness = Profiles_Toughness
            self.Wounds = Profiles_Wounds
            self.Attacks = Profiles_Attacks
            self.Leadership = Profiles_Leadership
            self.Armour_Save = Profiles_Armour_Save
            self.Abilites =  Profiles_Abilites

class Datasheet_Weapons:
    #def __init__(self,)
    Weapons_Name = "Name"
    Weapons_Range = "12''"
    Weapons_Type = "Rapid fire 1"
    Weapons_Strength = 3
    Weapons_Armour_Penetration = 0
    Weapons_Damage = 1
    Weapons_Abilites = []

n1=Datasheet_Profiles("troops","NECRON WARRIORS","5''",3,3,4,4,1,1,10,4,"none")
n2=Datasheet_Profiles("troops","Cadian Shock Troops","6''",4,4,3,3,1,1,6,5,"-")

'''print("Выберете число от 1 до 2")
i = int(input())
print('\n')
if i == 1:
    print("Battlefield role = ",n1.Battlefield_role,'\n')
    print("Name = ",n1.Name,'\n')
    print("Movement = ",n1.Movement,'\n')
    print("Weapon Skill = ",n1.Weapon_Skill,'\n')
    print("Ballistic Skill = ",n1.Ballistic_Skill,'\n')
    print("Strength = ",n1.Strength,'\n')
    print("Toughness = ",n1.Toughness,'\n')
    print("Wounds = ",n1.Wounds,'\n')
    print("Attacks = ",n1.Attacks,'\n')
    print("Leadership = ",n1.Leadership,'\n')
    print("Armour Save = ",n1.Armour_Save,'\n')
    print("Abilites = ",n1.Abilites,'\n')
elif (i==2):
    print("Battlefield role= ",n2.Battlefield_role,'\n')
    print("Name= ",n2.Name,'\n')
    print("Movement= ",n2.Movement,'\n')
    print("Weapon Skill= ",n2.Weapon_Skill,'\n')
    print("Ballistic Skill= ",n2.Ballistic_Skill,'\n')
    print("Strength= ",n2.Strength,'\n')
    print("Toughness= ",n2.Toughness,'\n')
    print("Wounds= ",n2.Wounds,'\n')
    print("Attacks= ",n2.Attacks,'\n')
    print("Leadership= ",n2.Leadership,'\n')
    print("Armour Save= ",n2.Armour_Save,'\n')
    print("Abilites= ",n2.Abilites,'\n')
print("!!!!!!!")
pprint(vars(n1))
print("!!!")
print(n2.Name)
'''
