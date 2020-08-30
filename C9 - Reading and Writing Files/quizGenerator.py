#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
from pathlib import Path

required_dir = '/Users/Johnny/Desktop/Programming/Python/Process Automation/C9 - Reading and Writing Files'
n_files = 35

print('---- Quiz generator! ----\nBeginning program...')

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# The 'dir name' has to be defined so that we can save off the quiz and answer files to the correct places
quiz_dir = required_dir + '/Questions/'
ans_dir = required_dir + '/Answers/'

if not Path(quiz_dir).exists():
    Path(quiz_dir).mkdir()
    Path(ans_dir).mkdir()

print('Setting up quiz and answer directories...\nQuizzes will be saved to:\n' +
      quiz_dir + '\nAnswers will be saved to:\n' + ans_dir)

# Generate 35 quiz files.
for n in range(n_files):

    print('Creating quiz number: ' + str(n) + '...')

    # TODO: Create the quiz and answer key files.
    quiz_base_name = 'quiz-' + str(n) + '.txt'
    ans_base_name = 'ans-' + str(n) + '.txt'
    quiz_path = quiz_dir + quiz_base_name
    ans_path = ans_dir + ans_base_name

    # TODO: Write out the header for the quiz.
    header = '---- Quiz number: ' + str(n) + ' ----\n\n'

    quiz_file = open(quiz_path, 'w')
    quiz_file.write(header)

    ans_file = open(ans_path, 'w')
    ans_file.write(header)

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for i in range(len(states)):
        question = '%s. What is the capital of %s?\n' % (i, states[i])
        answer = '%s. %s\n' % (i, capitals[states[i]])
        quiz_file.write(question)
        ans_file.write(answer)

    quiz_file.close()
    ans_file.close()
