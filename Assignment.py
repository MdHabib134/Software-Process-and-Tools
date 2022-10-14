import random
options = ["rock", "paper", "scissor"]


class Assignment(object):
    def show_detail(self):
        print('Wel come to Rock - Paper - Scissor game:\n - Rock\n - Paper\n - Scissor\nType any of them to play with '
              'computer')

    def play_game(self, choice, computer_choice):
        if choice == computer_choice:
            return 'Draw'
        elif choice == "rock":
            if computer_choice == "scissor":
                return 'You win'
            else:
                return 'Computer win'
        elif choice == "paper":
            if computer_choice == "rock":
                return 'You win'
            else:
                return 'Computer win'
        elif choice == "scissor":
            if computer_choice == "paper":
                return 'You win'
            else:
                return 'Computer win'

    def game_playing(self):
        while True:
            decide = input("Options :\n1. Quit\n2. Restart\nEnter Your Option: ")
            if decide == '1':
                print('Finished! See yo soon!')
                return False
            if decide == '2':
                print('Restarted Game!')
                return True
            else:
                print('Invalid options,', end=' ')
                continue

    def rock_paper_scissor(self):
        round_plays = user_point = computer_point = 0
        running = True
        self.show_detail()
        while running:
            computer_choice = random.choice(options)
            if user_point == 5:
                print('---------------------------------\nTotal round played:', round_plays, '\nYou got:', user_point,
                      '\nComputer got:', computer_point, '\nYou Have won the game! Congrats!!')
                running = self.game_playing()
                if running:
                    self.show_detail()
                    round_plays = user_point = computer_point = 0
                if not running:
                    break
                    # running = False
            if computer_point == 5:
                print('1/2')
                print('---------------------------------\nTotal round played:', round_plays, '\nComputer got:',
                      computer_point, '\nYou got:', user_point, '\nComputer has won the game! Congrats!!')
                running = self.game_playing()
                if running:
                    self.show_detail()
                    round_plays = user_point = computer_point = 0
                if not running:
                    break
                    # running = False
            my_choice = input("Type your choice (Q to quit the game): ")
            my_choice = my_choice.strip()
            if my_choice.lower() in options:
                round_plays += 1
                game = self.play_game(my_choice, computer_choice)
                print('Round Number:', round_plays)
                print("You choose", my_choice, "Computer choose", computer_choice)
                if game == 'You win':
                    user_point += 1
                    print('So you won')
                if game == 'Computer win':
                    computer_point += 1
                    print('So computer won')
                if game == 'Draw':
                    print('Ahh! It is a Draw')
                print('Your point:', user_point, ' Computer points:', computer_point)
            elif my_choice.lower() == 'q':
                print("--------------------------------------------------\nUntil now you've played", round_plays,
                      "times "
                      "and get", user_point, "points!!\nBut you've quit the game! Thank you for playing!")
                # round_plays = user_point = computer_point = 0
                break
            else:
                print('Invalid ', end='')
                continue


# Assignment().rock_paper_scissor()
