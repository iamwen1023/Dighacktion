import pandas


if __name__ == '__main__':

    questions_path = '../data/questions.csv'
    answers_path = '../data/answers.csv'

    # // add primary theme...
    questions = pandas.read_csv(questions_path, sep=";")
    questions = questions.drop(columns=["status", "reference_id", "date_created", "date_modified"])

    # print(questions.head())

    answers = pandas.read_csv(answers_path, sep=";")
    answers = answers.drop(columns=["date_modified"])
    answers = answers[~answers['details'].str.contains('merci')]
    # print(answers.head())

    # merged_df = pandas.merge(questions, answers, left_on='id', right_on='question_id', how='inner')

    # Iterate aver the questions and answers, and create a new dataframe
    new_df = pandas.DataFrame(columns=["conversation_id", "user_id",])


    print(merged_df.head())
    # df = pd.read_csv("titanic.csv")
    # print(df.shape)
    # print(df.columns.tolist())


# dire qu'on fait la v2 de crossdoc, qui'il ya un gain de temps
# expliquer ce qu'on copte faire apres ce weekend
# Parler de la base de donnée de 750 questions reponses, qu'on l'utilise

# Decision tree