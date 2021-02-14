# rock_paper_scissors.py


import random


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

rps = [scissors, rock, paper]
player_choice = int(input("무엇을 선택할까요? 가위는 0, 바위는 1, 보는 2: \n"))
com_choice = random.randint(0, 2)

print("\n당신의 선택: ")
print(rps[player_choice])
print("컴퓨터 선택: ")
print(rps[com_choice])

if player_choice == 0 and com_choice == 2 or\
    player_choice == 1 and com_choice == 0 or\
    player_choice == 2 and com_choice == 1:
    print("당신이 이겼습니다!")
elif player_choice == com_choice:
    print("무승부입니다.")
else:
    print("당신이 졌습니다.")
