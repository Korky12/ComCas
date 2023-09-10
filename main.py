
import random
from colorama import init
from colorama import Fore
import colorama
import time
import os
import sys



#http://patorjk.com/software/taag/#p=display&f=Bulbhead&t=MAIN%20MENU  k
#menu
print('')
print('')
print(f'         {Fore.LIGHTCYAN_EX}  ___  _____  __  __     ___    __    ___  ____  _  _  _____  {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX} / __)(  _  )(  \/  )   / __)  /__\  / __)(_  _)( \( )(  _  ) {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX}( (__  )(_)(  )    (   ( (__  /(__)\ \__ \ _)(_  )  (  )(_)(  {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX} \___)(_____)(_/\/\_)   \___)(__)(__)(___/(____)(_)\_)(_____) {Fore.RESET}')
print(f'         {Fore.LIGHTBLACK_EX} -----------------------------------------------------------{Fore.RESET}')
time.sleep(1)
print(f'                                                                                                    ')
print(f"         {Fore.LIGHTMAGENTA_EX}Vítejte v naší hře            DEV by Jakub Hošek & Matěj Mrkus{Fore.RESET}")  #hosku to uvítání nejak přepis, to "Vítejte v naší hře", dej tam neco jinyho je to dogshitXD
print(f'                                                                                                    ')
print(f'                                                                                                    ')
with open("points.txt","r") as file:
  points = file.read()
if points == "":
  points = 500
  points = str(points)
  with open("points.txt","w") as file:
    file.write(points)
  print(f"                       {Fore.LIGHTGREEN_EX} Právě máte {points} bodů{Fore.RESET}")
  points = int(points)
else:
  print(f"                       {Fore.LIGHTGREEN_EX} Právě máte {points} bodů{Fore.RESET}")
  points = int(points)
xd = (0)

print(f"{Fore.YELLOW}                             NAČÍTÁNÍ...{Fore.RESET}")  

time.sleep(4)
os.system('delete')
print('')
print('')
print(f'         {Fore.LIGHTCYAN_EX}  ___    __    ___  ____  _  _  _____  {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX} / __)  /__\  / __)(_  _)( \( )(  _  ) {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX}( (__  /(__)\ \__ \ _)(_  )  (  )(_)( {Fore.RESET}')
print(f'         {Fore.LIGHTCYAN_EX} \___)(__)(__)(___/(____)(_)\_)(_____) {Fore.RESET}')
time.sleep(1)
print(f'                                                                                                    ')
print('                                                                                                     ')
print(f"         {Fore.LIGHTMAGENTA_EX}          Vítejte v Casínu.            {Fore.RESET}")
time.sleep(1)
if xd == 0:
    casino_choice = input(
        f"         {Fore.LIGHTBLUE_EX}Jakou hru by jste si chtěli zahrát? Máme na výběr:\n{Fore.LIGHTGREEN_EX} Flip coin\n Kámen Nůžky Papírn\n Hádání čísel\n Ruleta\n Pro výběr čehokoliv napište počáteční písmeno.{Fore.RESET}\n"
    ).lower()
 #flipthecoin-----------------------------------------------------   
    if casino_choice == "f":
      print(f"{Fore.LIGHTCYAN_EX} ____  __    ____  ____    ____  _   _  ____     ___  _____  ____  _  _\n( ___)(  )  (_  _)(  _ \  (_  _)( )_( )( ___)   / __)(  _  )(_  _)( \( )\n )__)  )(__  _)(_  )___/    )(   ) _ (  )__)   ( (__  )(_)(  _)(_  )  (\n(__)  (____)(____)(__)     (__) (_) (_)(____)   \___)(_____)(____)(_)\_)\n{Fore.RESET}")
      time.sleep(0.5)
      print(f"{Fore.LIGHTBLUE_EX}Vítejte ve hře Flip the coin{Fore.RESET}")
      coin = input(f"{Fore.LIGHTBLUE_EX}Zadejte vaši stranu mince,hlava nebo orel \n{Fore.RESET}")
      time.sleep(1)
      num = random.randint(1, 2)
      if num == 1:
          result = "hlava"
      elif num == 2:
          result = "orel"   
      if coin == result:
        print(f"{Fore.LIGHTGREEN_EX}Dobrá práce, výhráli jste.{Fore.RESET} ")
        points = points + 20
        print("Právě máte:")
        print(points)
        points = str(points)
        with open("points.txt","w") as file:
          file.write(points)
        points = int(points)
      else: 
        print(f"{Fore.LIGHTRED_EX}Prohráli jste.{Fore.RESET}")
        points = points - 10
        print("Právě máte:")
        print(points)
        points = str(points)
        with open("points.txt","w") as file:
          file.write(points)
        points = int(points)
          
#kamen nuzky papir-------------------------------------------------    
    if casino_choice == "k":
        rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

        paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
        scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
        all_list = [rock, paper, scissors]

        user_choose = int(
            input(
                "Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky\n"
            ))
        user_picture = all_list[user_choose]

        computer_choose = random.randint(0, 2)
        computer_picture = all_list[computer_choose]

        print(f"Uživatel si vybral:\n {user_picture}")
        print(f"Počítač si vybral:\n {computer_picture}")
        if user_choose == computer_choose:
            print("Remíza")
        elif user_choose == 0 and computer_choose == 1:
          print(f"{Fore.LIGHTRED_EX}Prohrál jsi, počítač vyhrává{Fore.RESET}")
          points = points + 20
          print("Právě máte:")
          print(points)
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        elif user_choose == 0 and computer_choose == 2:
          print(f"{Fore.LIGHTGREEN_EX}Vyhrál jsi, počítač prohrává{Fore.RESET}")
          points = points + 20
          print("Právě máte:")
          print(points)
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        elif user_choose == 1 and computer_choose == 0:
          print(f"{Fore.LIGHTGREEN_EX}Vyhrál jsi, počítač prohrává{Fore.RESET}")
          points = points + 20
          print("Právě máte:")
          print(points)
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        elif user_choose == 1 and computer_choose == 2:
          print(f"{Fore.LIGHTRED_EX}Prohrál jsi, počítač vyhrává{Fore.RESET}")
          points = points - 10
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        elif user_choose == 2 and computer_choose == 0:
          print(f"{Fore.LIGHTRED_EX}Prohrál jsi, počítač vyhrává{Fore.RESET}")
          points = points - 10
          print("Právě máte:")
          print(points)
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        elif user_choose == 2 and computer_choose == 1:
          print(f"{Fore.LIGHTGREEN_EX}Vyhrál jsi, počítač prohrává{Fore.RESET}")
          points = points + 20
          print("Právě máte:")
          print(points)
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
#--------------------------------------------------------------------------------    
    if casino_choice == "h":

        choicefrombot = random.randint(1, 100)

        choicefromplayer = random.randint(1, 100)

        print(choicefromplayer)

        hadanichoice = input(f"[V]ětší, [M]enší nebo [J]ackpot?\n")
        hadanichoice = hadanichoice.lower()

        if hadanichoice == "j":
            if choicefromplayer != choicefrombot:
              print(f"{Fore.LIGHTRED_EX}To si bohužel neuhádl...{Fore.RESET}")
              points = points - 10
              print("Právě máte:")
              print(points)
              points = str(points)
              with open("points.txt","w") as file:
                file.write(points)
              points = int(points)
            elif choicefromplayer == choicefrombot:
              print(f"{Fore.LIGHTGREEN_EX}Ano, správně, je to tak!{Fore.RESET}") 
              points = points + 100
              print("Právě máte:")
              print(points)
              points = str(points)
              with open("points.txt","w") as file:
                file.write(points)
              points = int(points)
        
        elif hadanichoice == "m":  
          if choicefromplayer > choicefrombot:
            print(f" {Fore.LIGHTGREEN_EX}Ano, správně, je to tak!{Fore.RESET}")
            points = points + 20
            print("Právě máte:")
            print(points)
            points = str(points)
            with open("points.txt","w") as file:
                file.write(points)
            points = int(points)
          else:
            print(f"{Fore.LIGHTRED_EX}To si bohužel neuhádl...{Fore.RESET}")
            points = points - 10
            print("Právě máte:")
            print(points) 
            points = str(points)
            with open("points.txt","w") as file:
              file.write(points)
            points = int(points)
       

        if hadanichoice == "v":
          if choicefromplayer < choicefrombot:  
            print(f" {Fore.LIGHTGREEN_EX}Ano, správně, je to tak!{Fore.RESET}")
            points = points + 20
            print("Právě máte:")
            print(points)
            points = str(points)
            with open("points.txt","w") as file:
                file.write(points)
            points = int(points)
          else:
            print(f"{Fore.LIGHTRED_EX}To si bohužel neuhádl...{Fore.RESET}")
            points = points - 10
            print("Právě máte:")
            print(points)
            points = str(points)

            with open("points.txt","w") as file:
              file.write(points)
            points = int(points)
#


            #############################################################################################################xxx
    elif casino_choice == "r":
      bet = input(f" {Fore.LIGHTBLUE_EX} Vsadte si na:\n Sudé(2x)\n Liché(2x)\n Menší(0-18) (3x)\n Větší(19-36)(3x)\n Konkrétní číslo(10x)\n{Fore.RESET}")
      bet = bet.lower()
      money = int(input("Kolik peněz chcete vložit?\n"))
      if money > points:
        print("To určitě. Vypínám se...")
        exit()
      else:
        pass
      time.sleep(2)
      os.system("clear")
      ruleta = random.randint(0,36)
      
      if bet == "s":
        if ruleta % 2 == 0:
          print(ruleta)
          print(f"{Fore.LIGHTGREEN_EX}Výhra!!! Vezmi si svoje těžce vydělané peníze a hrát dál.{Fore.RESET}")
          points = points + (money * 2)
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        else:
          print(ruleta)
          print(f"{Fore.LIGHTRED_EX}Prohra... Zkus to ještě jednou :){Fore.RESET}")
          points = points - money
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
      elif bet == "l":
        if ruleta % 2 != 0:
          print(ruleta)
          print(f"{Fore.LIGHTGREEN_EX}Výhra!!! Vezmi si svoje těžce vydělané peníze a hrát dál.{Fore.RESET}")
          points = points + (money * 2)
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        else:
          print(ruleta)
          print(f"{Fore.LIGHTRED_EX}Prohra... Zkus to ještě jednou :){Fore.RESET}")
          points = points - money
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
      elif bet == "m":
        if ruleta < 19:
          print(ruleta)
          print(f"{Fore.LIGHTGREEN_EX}Výhra!!! Vezmi si svoje těžce vydělané peníze a hrát dál.{Fore.RESET}")
          points = points + (money * 3)
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        else:
          print(ruleta)
          print(f"{Fore.LIGHTRED_EX}Prohra... Zkus to ještě jednou :){Fore.RESET}")
          points = points - money
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
      elif bet == "v":
        if ruleta > 18:
          print(ruleta)
          print(f"{Fore.LIGHTGREEN_EX}Výhra!!! Vezmi si svoje těžce vydělané peníze a hrát dál.{Fore.RESET}")
          points = points + (money * 3)
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        else:
          print(ruleta)
          print(f"{Fore.LIGHTRED_EX}Prohra... Zkus to ještě jednou :){Fore.RESET}")
          points = points - money
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
      elif bet == "k":
        bet2 = int(input("Zadejte cislo na které chcete vsadit:\n"))  
        if ruleta == bet2:
          print(ruleta)
          print(f"{Fore.LIGHTGREEN_EX}Výhra!!! Vezmi si svoje těžce vydělané peníze a hrát dál.{Fore.RESET}")
          points = points + (money * 10)
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
        else:
          print(ruleta)
          print(f"{Fore.LIGHTRED_EX}Prohra... Zkus to ještě jednou :){Fore.RESET}")
          points = points - money
          print("Právě máte:")
          print(points) 
          points = str(points)
          with open("points.txt","w") as file:
            file.write(points)
          points = int(points)
#-------------------------------------------------     
      
elif casino_choice == "kubamatej":
  
  print("Co tady děláš???")

elif casino_choice == "rickroll":
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

