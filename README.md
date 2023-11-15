
# Quiz Project

This is a Quiz project in my study Dr. Angela Yu's Python Bootcamp.

You have a file with questions that you must complete with True/False answer, and after you will get the score result.

## Requirments

Create a Quiz project that asks questions and checks if user answers correctly. After completing all the questions, the user will get final score.

## Overview
#### data.py
This is file with quiz data in format: question and answer.

#### question_model.py
One class is created in this file, which helps convert data to the correct format.

#### quiz_brain.py
* There is one class created in this file QuizBrain.
    * Method _init_ which have argument "list" and have data:
      * _question_number_ - shows current question number
      * _list_ - there is list with data
      * _score_ - current user score
    * Method _still_has_questions_ check if left questions in the list.
    * Method _next_question_ has two statements, if method _still_has_questions_ return "True" the program still asks questions, else stops and print the final score.
      * current_question - shows current question with data from _init_ method.
    * Method _check_answer_ has two statements, if _user_answer_ from method _next_question_ is equal to the question answer then user will get congratulatory message and +1 to his score, else print text about the wrong answer. At the end of this method user also will get text with the current score.

#### main.py
* Import data from files _quiz_brain_, _data_ and _quiz_brain_.
* Create empy list _question_bank_.
* Create for cycle and add all data to the list _question_bank_.
* Create while cycle with method _quiz.still_has_questions_.
* Print congratulation message and final user scores after _quiz.still_has_questions_ equal to "False".
