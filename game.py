human_turn= input ('human_turn :')
computer_turn = 'paper'

if human_turn == 'rock' and computer_turn == 'scissors': 
      print ('Human Wins!') 

if human_turn == 'paper' and computer_turn == 'rock': 
      print ('Human Wins!') 

if human_turn == 'scissors' and computer_turn == 'paper' :
      print ('Human Wins!') 

if human_turn == 'scissors' and computer_turn == 'rock':
    print ('Computer Wins!')
  
if human_turn == 'paper' and computer_turn == 'scissors':
        print ('Computer Wins!')

if human_turn == 'rock' and computer_turn == 'paper':
        print ('Computer Wins!')

else :
    print ('Draw!')
