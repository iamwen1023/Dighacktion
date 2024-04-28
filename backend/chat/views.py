from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from openai import OpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI


def index(request):

    context = {
        "form": MessageForm(),
        "messages": Message.objects.all(),
    }
    return render(request, "chat/templates/index.html", context)


# Get an input from the user and send it to the local server
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def send(request):

    if request.method == "POST":

        # Get the request from the user in the body of the request
        content = request.body.decode("utf-8")

#         print(content)

#         client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#         system = """
# Tu es un assistant qui aide les personnels de santea mieux identifier les maladies digestives en pediatrie.
# Les prompts qui te sont envoyes sont des questions posees par les medecins et les infirmiers.
# Tu dois repondre a ces questions en donnant des informations pertinentes et utiles pour aider a identifier les maladies digestives en pediatrie.
# Les personnes qui t'utilisent s'attendent a ce que tu fournisses des reponses bien raisonnees qui sont a la fois correctes et utiles en se, si c'est possible sur les questions et reponses possibles.

# La requete principale, a laquelle tu dois repondre est la question entouree des champs <main> et </main>

# Pour t'aider a repondre a la question, nous te fournissons des conversations precedentes qui contiennent des informations pertinentes sur la question.
# Elles ont ete selectionnees pour t'aider a repondre a la question, grace a une analyse des conversations precedentes. Chaque conversation que l'ona jugee proche est entouree des champs <context> et </context>. Similaire ne veut pas dire identique, mais les conversations precedentes peuvent contenir des informations utiles pour repondre a la question."""

#         print("completion")
#         completion = client.chat.completions.create(
#             model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
#             messages=[
#                 {"role": "system", "content": system},
#                 {"role": "user", "content": content}
#             ],
#             temperature=0.7,
#         )

#         Message.objects.create(
#             content=completion.choices[0].message.content,
#             is_prompt=False
#         )

#         print(completion.choices[0].message.content)
#         return HttpResponse(completion.choices[0].message.content)

        engine = create_engine('sqlite:///qa.db')
        merged_df.to_sql('qa', con=engine, if_exists='replace')

        db = SQLDatabase(engine=engine)
        llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        chain = create_sql_query_chain(llm, db)



    return HttpResponse("Invalid form")
