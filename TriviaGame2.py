import psycopg2

connection = psycopg2.connect(
    database="Hackathon_1", 
    user='postgres',
    password='1948',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()	

class Trivia :
    def ready_to_play(self) : 
        while True :
                user_choice =(input('''
                Welcome to Trivia
                _________________
        
               Harry Potter Trivia!!
               Find out how well you know Happy Potter...

               Are you ready to start (Y/N): '''))
                choice = user_choice.lower()
                try :
                    if choice == 'y' or choice == 'n' :
                        if choice == 'y' :
                            print(f'\nLet\'s begin your Harry Potter trivia game\n')
                            return choice
                        else:
                            print('\nGoodbye\n')
                    else:
                        print('\nYou have made an invalid choice\n')
                except ValueError : 
                    print('\nPlease enter a letter from the choices provided\n')

                
    def start_game(self) : 
        question_num = 0
        guesses = []
        score = 0
        query = f"SELECT question FROM question WHERE trivia_id = 1"
        cursor.execute(query)
        question_result = cursor.fetchall()
        for question in question_result :
            print(f'\n{question[0]}\n')
            query_user = f"""
            SELECT answer_option
            FROM answer
            JOIN question ON answer.question_id = question.question_id
            """
            cursor.execute(query_user)
            answer_results = cursor.fetchall() 
            for i in range(4 * question_num, 4 * (question_num + 1)):
                print(answer_results[i][0])
            
            guess = input('Enter your answer: ').lower()
            guesses.append(guess)
            query_user = f"""
            SELECT answer
            FROM correct_answer
            WHERE question_id = {question_num + 1}
            """
            cursor.execute(query_user)
            correct_answer_results = cursor.fetchone()
            print(correct_answer_results)
            correct_answer = correct_answer_results[0]
            if guess == correct_answer.lower() :
                score += 1
                print('\nCORRECT!')
                print(score)
            else :
                print('\nINCORRECT')
                print(f'The correct answer is: {correct_answer}')
            question_num += 1
            
        final_score = int(score/10*100)
        if final_score < 50 :
            print(f'\nYour score is: {final_score}\nYou and Harry Potter barley know eachother\n')
        elif final_score < 70 :
            print(f'\nYour score is: {final_score}\nYou and Harry Potter and aquaintances\n')
        elif final_score < 90 :
            print(f'\nYour score is: {final_score}\nYou and Harry Potter and pretty good friends\n')
        else :
            print('WOW! You and Harry Potter are best friends')
    
    
   
        
            
            
         

    
    # for option in options[]
user = Trivia()
user.ready_to_play()
user.start_game()