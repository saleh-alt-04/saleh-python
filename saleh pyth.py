from time import sleep
from random import randint

money = 0
help_score = 2
helpline = ["A) The 50/50", "B) The Audience", "C) The Telephone"]


def ask_question(question, answers, correct, amount, audience, phone):
  print(question)
  sleep(3)
  for answer in answers:
    print(answer)
    sleep(1)
  player_answer = input("What is your answer?A,B,C,D or H for helpline) ")
  if player_answer.upper() == "H":
    use_helpline(correct, amount, audience, phone)
  elif user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    global help_score
    if help_score > 0:
      help()
      for answer in answers:
        print(answer)
        sleep(1)
      user_answer2 = input("What is your answer?(A-D or J for joker) ")
      if user_answer2.upper() == "J":
        use_joker(correct, amount, audience, phone)
      elif user_answer2.upper() == correct:
        print(" ")
        correct_answer(amount)
        sleep(2)
      else:
        print(" ")
        game_over()
    else:
      print(" ")
      game_over()

