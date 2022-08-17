import random
from pick import pick

possible_actions = ['rock', 'paper', 'scissors']

def set_pc_choice() -> str:
  pc_choice = random.choice(possible_actions)
  return pc_choice

def get_user_choice() -> str:
  title = '(Move with [j],[k]) Select your choice: '
  option, index = pick(possible_actions, title, indicator='=>', default_index=0)
  return option
  
def decide_who_wins(user_choice: str, pc_choice: str):
  def win_msg(winner):
    print(f'-------- {winner} wins! 😃 --------')

  if user_choice == pc_choice:
    print('-------- Tie! 😅 --------')
  
  if user_choice == 'rock':
    if pc_choice == 'paper': win_msg(pc_choice)
    if pc_choice == 'scissors': win_msg(user_choice)

  if user_choice == 'paper':
    if pc_choice == 'rock': win_msg(user_choice)
    if pc_choice == 'scissors': win_msg(pc_choice)

  if user_choice == 'scissors':
    if pc_choice == 'rock': win_msg(pc_choice)
    if pc_choice == 'paper': win_msg(user_choice)

  print(f'😁 Your choice: {user_choice}, 🤖 Computer choice: {pc_choice}')

def run_game():
  counter = 0

  def play_again(counter):
    answer = input('😉 Play again?(y/n)')
    answer.lower()
    if answer == 'y': return True
    else: 
      print(f'You played {counter} times. See you later!🖐️')
      return False

  while True:
    counter += 1
    user_choice = get_user_choice()
    pc_choice = set_pc_choice()
    decide_who_wins(user_choice, pc_choice)

    if play_again(counter) == False: break

run_game()

  