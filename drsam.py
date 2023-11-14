import re
import pandas as pd

def filter_questions(messages):
    question_messages = []
    question_pattern = r"\?"

    for message in messages:
        if isinstance(message, str) and re.search(question_pattern, message):
            question_messages.append(message)

    return question_messages


# Beispiel-Daten
messages = pd.read_csv('daten.csv')
column_data = messages.iloc[:, 2]
 # Corrected variable name

question_messages = filter_questions(column_data)
print(question_messages)  # Corrected variable name
