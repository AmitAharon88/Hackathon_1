import psycopg2

connection = psycopg2.connect(
    database="Hackathon_1", 
    user='postgres',
    password='Schroon3',
    host='localhost', #or IP address
    port='5432'
)

cursor = connection.cursor()	

class Trivia :
    def choose_topic(self) : 
        while True :
            try :
                user_choice =int(input('''
                Welcome to Trivia
                _________________
        
                Trivia topic:
                1: Harry Potter
                2: The office
              
                Select your topic: '''))
                if user_choice == 1 or user_choice == 2 :
                    query = f"SELECT topic FROM trivia_topics WHERE trivia_id = {user_choice} LIMIT 1" 
                    cursor.execute(query)
                    topic_name = cursor.fetchone()
                    print(f'\nLet\'s begin your {topic_name[0]} trivia game\n')
                    return user_choice
                else:
                    print('\nYou have made an invalid choice\n')
            except ValueError : 
                print('\nPlease enter a number from the choices provided\n')

                
    def start_game(self) : 
        user_choice = self.choose_topic()
        if user_choice == 1 :
            question_num = 0
        else :
            question_num = 10
        guesses = []
        score = 0
        query = f"SELECT question FROM question where trivia_id = {user_choice}"
        cursor.execute(query)
        question_result = cursor.fetchall()
        for question in question_result :
            print(question[0])
            query_user = f"""
            SELECT answer_option
            FROM answer
            JOIN question ON answer.question_id = question.question_id
            JOIN trivia_topics ON question.trivia_id = trivia_topics.trivia_id
            WHERE trivia_topics.trivia_id = {user_choice} AND answer.question_id = question.question_id
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
                print('CORRECT!')
            else :
                print('INCORRECT')
                print(f'The correct answer is: {correct_answer}')
            question_num += 1
            
        final_score = int(score/10*100)
    
    
   
        
            
            
         

    
    # for option in options[]
user = Trivia()
user.start_game()