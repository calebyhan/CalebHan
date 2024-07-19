import os
import re
import random


class Game:
    def __init__(self):
        self.francs = 1000
        self.reichsmark = 10
        self.danger = 0
        self.distance = 0
        self.days = 0
        self.inventory = ["Handheld Radio", "First-aid kit", "Survival kit", "Rations"]

    @staticmethod
    def _info():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("La Resistance is an Oregon Trail themed game based in 1944 designed to be difficult and may require strategy to beat the game.")
        print("You are a SOE agent tasked with delivering a crucial letter to an agent situated in Berlin. This must be done covertly since the Germans have learned of this plan.")
        print("\nThe goal of this game is to reach the final destination, Berlin, from Dover. There is a mandatory stop at Paris for resources and information.")
        print("You are to deliver secret intel crucial to defeating the Third Reich to a fellow spy in Berlin. If you get caught, there is no going back. Germany does not treat enemy spies kindly.")
        print("\nFor more detailed information and mechanics, please read the README.")

        input()

    def _menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.distance == 0:
                print("Welcome to France. Good luck.\n")
            if self.distance == 1000:
                print("Welcome to Germany. Good luck.\n")
            print("\t[0] Edit inventory")
            print("\t[1] View stats")
            print("\t[2] View shop")

            menu = input("\nChoose an option, or press enter to start: ")

            if menu == "":
                break
            elif int(menu) in [0, 1, 2]:
                if int(menu) == 0:
                    self._remove_item()
                elif int(menu) == 1:
                    self._stats()
                elif int(menu) == 2 and self.distance < 1000:
                    self._france_shop()
                elif int(menu) == 2 and self.distance >= 1000:
                    self._german_shop()
            else:
                print("Invalid input.")

    def _setup(self):
        self._info()

        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            self.difficulty = int(input("Select a difficulty: [0] Easy, [1] Medium, [2] Hard, [3] Insane: "))
            if self.difficulty in [0, 1, 2, 3]:
                break
            print("Invalid input.\n")

        self._menu()

    def _main(self):
        while self.distance < 1500:
            crossed = False
            if self.distance < 1000:
                crossed = True
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                method = int(input("Select a method of travel: [0] train, [1] hitchhiking, [2] walking, [3] steal a car: "))
                if method in [0, 1, 2, 3]:
                    if method == 0:
                        if "Train ticket" not in self.inventory:
                            print("You do not have a train ticket.")
                        else:
                            success = [80, 70, 60, 50]
                            reported = [15, 12, 10, 5]
                            roll = random.randint(0, 100)
                            if roll < success[self.difficulty]:
                                print("You successfully rode the train.")
                                self.inventory.remove("Train ticket")
                                self.distance += 400
                            elif reported[self.difficulty] < roll < success[self.difficulty] + reported[self.difficulty]:
                                print("You successfully rode the train but someone got suspicious of you and will report you.")
                                self.inventory.remove("Train ticket")
                                self.distance += 400
                                self.danger += 5
                            else:
                                print("A patrolling SS guard found an error in your documents and you got arrested.")
                                if not self._ss():
                                    return True
                                else:
                                    pass
                    elif method == 1:
                        success = [50, 40, 30, 20]
                        reported = [5, 10, 15, 20]
                        roll = random.randint(0, 100)
                        if roll < success[self.difficulty]:
                            print("You successfully found a generous person.")
                            self.distance += 250
                        elif reported[self.difficulty] < roll < success[self.difficulty] + reported[self.difficulty]:
                            print("You found a person but they are suspicious of you and will report you.")
                            self.distance += 250
                            self.danger += 5
                        else:
                            print("You were unsuccessful in finding a ride.")
                    elif method == 2:
                        if random.randint(0, 100) < 80:
                            print("You had a nice day of walking.")
                            self.distance += 50
                        else:
                            print("Someone saw you while you were walking.")
                            self.distance += 50
                            self.danger += 5
                    else:
                        success = [30, 20, 10, 5]
                        reported = [30, 25, 20, 15]
                        roll = random.randint(0, 100)
                        if roll < success[self.difficulty]:
                            print("You successfully stole a car.")
                            self.distance += 300
                        elif reported[self.difficulty] < roll < success[self.difficulty] + reported[self.difficulty]:
                            print("You stole a car but someone saw you and they are suspicious of you and will report you.")
                            self.distance += 300
                            self.danger += 5
                        else:
                            print("You were arrested while attempting to steal a car.")
                            if not self._ss():
                                return True
                            else:
                                pass
                    input()
                    break
                else:
                    print("Invalid input.\n")

            if random.randint(0, 100) < self.danger:
                print("You were found sleeping by an investigating SS guard from a previous report.")
                if not self._ss():
                    return True
                else:
                    pass

            if crossed and self.distance >= 1000:
                self.distance = 1000
                self._menu()
        return False

    def _game_over(self, died):
        os.system('cls' if os.name == 'nt' else 'clear')
        if died:
            print("Game over. You died.")
            print(f"\nDistance: {str(self.distance)}")

            input()
        else:
            print("You successfully delivered the message. Good job.")
            print(f"\nDistance: {str(self.distance)}")

            days = [12, 10, 7, 5]
            if days[self.difficulty] > self.days:
                score = self.francs / 10 + self.reichsmark * 10 + days[self.difficulty] - self.days * 50 - self.danger / 5
            else:
                score = self.francs / 10 + self.reichsmark * 10 - (self.days - days[self.difficulty]) * 25 - self.danger / 5
            score -= self.danger

            print(f"Score: {score}")

            input()

    def _remove_item(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("Inventory:")
            for i, item in enumerate(self.inventory):
                print(f"\t[{str(i)}]: {item}")

            item_remove = input("\nChoose an item to remove, press enter to quit: ")

            if item_remove == "":
                break
            elif int(item_remove) in list(range(0, len(self.inventory))):
                self.inventory.pop(int(item_remove))
                print("\nUpdated inventory: " + ", ".join(self.inventory))
                break
            else:
                print("Invalid input.\n")

    def _france_shop(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("France shop")
        print("\t[0] Train Ticket: 500 francs")
        print("\t[1] Revolver: 750 francs")
        print("\t[2] 6 bullets: 50 francs")
        print("\t[3] Extra camping supplies: 250 francs")

        while True:
            fshop = input("\nEnter the number of the item you want to buy. Press enter to quit: ")

            if fshop == "":
                break
            elif int(fshop) in [0, 1, 2, 3]:
                if int(fshop) == 0 and self.francs >= 500:
                    self.francs -= 500
                    self.inventory.append("Train ticket")
                elif int(fshop) == 1 and self.francs >= 750:
                    self.francs -= 750
                    self.inventory.append("Revolver")
                elif int(fshop) == 2 and self.francs >= 50:
                    self.francs -= 50
                    found = False
                    for item in self.inventory:
                        if re.search(r"\d Bullets", item) is None:
                            item = str(int(item[0]) + 6) + " Bullets"
                            found = True
                    if not found:
                        self.inventory.append("6 Bullets")
                elif int(fshop) == 3 and self.francs >= 250:
                    self.francs -= 250
                    self.inventory.append("Extra camping supplies")
                    self.inventory.append("")
                else:
                    print("Not enough money.")
            else:
                print("Invalid input.\n")

    def _german_shop(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("German shop")
        print("\t[0] Train Ticket: 7 reichsmark")
        print("\t[1] 6 bullets: 0.5 reichsmark")
        print("\t[2] Radio antenna: 3 reichsmark")
        print("\t[3] Fake passport: 7 reichsmark")
        print("\t[4] Disguise kit: 1 reichsmark")

        while True:
            gshop = input("\nEnter the number of the item you want to buy. Press enter to quit: ")

            if gshop == "":
                break
            elif int(gshop) in [0, 1, 2, 3, 4]:
                if int(gshop) == 0 and self.reichsmark >= 7:
                    self.reichsmark -= 7
                    self.inventory.append("Train ticket")
                elif int(gshop) == 1 and self.reichsmark >= 0.5:
                    self.reichsmark -= 0.5
                    found = False
                    for item in self.inventory:
                        if re.search(r"\d Bullets", item) is None:
                            item = str(int(item[0]) + 6) + " Bullets"
                            found = True
                    if not found:
                        self.inventory.append("6 Bullets")
                elif int(gshop) == 2 and self.reichsmark >= 3:
                    self.reichsmark -= 3
                    self.inventory.append("Radio antenna")
                elif int(gshop) == 3 and self.reichsmark >= 7:
                    self.reichsmark -= 7
                    self.inventory.append("Extra camping supplies")
                elif int(gshop) == 4 and self.reichsmark >= 1:
                    self.reichsmark -= 1
                    self.inventory.append("Disguise kit")
                else:
                    print("Not enough money.")
            else:
                print("Invalid input.\n")

    def _ss(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You got caught by an SS guard and he is walking you to his superior. However, he has not checked your pockets.")
        while True:
            ss = int(input("Do you want to [0] Attack him and run, [1] Shoot him, [2] Stay put: "))
            if ss in [0, 1, 2]:
                if ss == 0:
                    if random.randint(0, 4) == 4:
                        print("You deliver a knockout punch to the SS guard, who is caught unaware. You escape freely.")
                        return True
                    else:
                        print("You punch the SS guard but he is quick to recover and shoots you.")
                        return False
                elif ss == 1:
                    if "Revolver" in self.inventory:
                        for item in self.inventory:
                            if re.search("\d Bullets", item) is None:
                                if int(item[0]) >= 1:
                                    if random.randint(0, 1) == 0:
                                        print("You quickly pull out your gun and shoot the SS guard in the back of the head. You escape freely.")
                                        return True
                                    else:
                                        print("You draw your gun but it gets stuck in your shirt. The SS guard shoots you.")
                                        return False
                                else:
                                    print("You pull out your gun but realize you have no bullets. It is too late. The guard shoots you.")
                                    return False
                else:
                    if "Fake passport" not in self.inventory:
                        if "Disguise kit" not in self.inventory:
                            print("You are led to the SS' superior and he deems you as a spy. You are sent to a concentration camp.")
                            return False
                        else:
                            if random.randint(0, 4) == 0:
                                print("Your disguise works. You walk free.")
                                return True
                            else:
                                print("You are led to the SS' superior and he deems you as a spy. You are sent to a concentration camp.")
                                return False
                    else:
                        print("You show the superior your fake passport and you are left free.")
                        return True
            else:
                print("Invalid input.\n")

    def _stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("STATS\n")
        print(f"Distance: {str(self.distance)}")
        print(f"Danger: {str(self.danger)}")
        print(f"Francs: {str(self.francs)}, Reichsmark: {str(self.reichsmark)}")

        input()

    def play(self):
        self._setup()
        died = self._main()
        self._game_over(died)
