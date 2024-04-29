import pandas
import os
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI


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

    merged_df = pandas.merge(
        questions, answers, left_on="id", right_on="question_id", how="inner"
    )

    for index, row in questions.iterrows():

        print(row)
        print("=====================================")

        path = f"../RAG/data/question_{row['id']}.md"

        content = str(row['title']) + ":\n" + str(row['details'])

        with open(path, "w") as f:
            f.write(content)
            f.write("\n\n")

    for index, row in answers.iterrows():

        print(row)
        print("=====================================")

        path = f"../RAG/data/question_{row['question_id']}.md"
        content = str(row['details'])

        with open(path, "a") as f:
            f.write(content)

        # conversation = f"conv_{row['id_x']}.md"

        # content = row['title'] + " " + str(row['details_x'])

        # with open(conversation, "a") as f:
            # f.write(f"question: {content}\n")

    # engine = create_engine('sqlite:///qa.db')
    # merged_df.to_sql('qa', con=engine, if_exists='replace')

    # db = SQLDatabase(engine=engine)
    # test = db.run("SELECT COUNT(*) FROM qa")

    # # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
    # chain = create_sql_query_chain(llm, db)


    # df = pd.read_csv("titanic.csv")
    # print(df.shape)
    # print(df.columns.tolist())


# dire qu'on fait la v2 de crossdoc, qui'il ya un gain de temps
# expliquer ce qu'on copte faire apres ce weekend
# Parler de la base de donnée de 750 questions reponses, qu'on l'utilise

# Decision tree
