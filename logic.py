import pygame
from time import sleep

# pygame.init() #initizalize the pygame

# screen = pygame.display.set_mode((800, 600))  #put height and width in the tuple, create the screen


#game loop
running = False
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#game logic
gameOn = True
team1_pts = 0
team2_pts = 0
team1_strikes = 0
team2_strikes = 0
answer_reveaked = False
round_num = 0
round_start = False
total_round_pts = 0
game_selection = ""
name_selection = True
name_satisfied = "Y"
while gameOn == True:
    print("Welcome to Family Feud!  Each game has three rounds plus a fast money round!\n")
    game_selection = input("Please select the game you would like to play \n Game 1 \n Game 2\n Please enter the game as you see it: ")
    if game_selection == "Game 1":
        #import csv
        game1 = open("Copy of Family Feud Question Database - Game 1.csv", newline = "")
        print(game1)
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
        if name_satisfied == "Y":
            name_selection = False
        elif name_satisfied == "N":
            name_selection = True
    print("Thank you! Now Let the games begin!")


    gameOn = False