import pygame
from round import *
from time import sleep

class Game:
    def __init__(self):
        #pygame.init()
        self.clock = pygame.time.clock()


    
    def run(self):
        dt = self.clock.tick() / 1000
        Game_1 = gameCreate('Copy of Family Feud Question Database - Game 1.csv')
        Game_2 = gameCreate('slay')
        print("Welcome to Family Feud!  Each game has three rounds plus a fast money round!\n")
        game_selection = input("Please select the game you would like to play \n Game 1 \n Game 2\n Please enter the game as you see it: ")
        if game_selection == "Game 1":
            pass
        else:
            pass
        while name_selection == True:
            print(f"Thank you for selecting {game_selection}. Please enter your team names below.")
            team1_name = input("Please enter Team 1's name: ")
            sleep(1)
            print(f"Thank you. Team 1's name is {team1_name}")
            team2_name = input("Please enter Team 2's name: ")
            sleep(1)
            print(f"Thank you. Team 2's name is {team2_name}")
            name_satisfied = input(f"Are you satisfied with Team 1: {team1_name} and Team 2: {team2_name}?\n Please enter Y/N: ")
            if name_satisfied == "N":
                name_selection = False
            elif name_satisfied == "Y":
                name_selection = True
                print("Thank you! Now Let the games begin!")
                round_start = True
                while round_start == True:
                    prompt=("We ask one hundred people..")
                    print(prompt, q1_dict["Question"])
                    ans1 = input("Your answer please: ")
                    possible_answers = list(q1_dict.values())
                    if ans1 in possible_answers:
                        print(f"Yay your answer {ans1} is in there! ")
                        team1_pts += 10
                    else:
                        print("no")
                        team1_strikes += 1
                    if team1_strikes == 3:
                        print("you lose")
                        gameOn = False


if __name__ == '__main__':
    game = Game()
    game.run()