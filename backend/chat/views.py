from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.http import HttpResponse, HttpResponseRedirect
from openai import OpenAI
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from dataclasses import dataclass
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

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
        query_text = request.body.decode("utf-8")

        CHROMA_PATH = "./RAG/chroma"

        PROMPT_TEMPLATE = """
        Tu es un assistant qui aide les personnels de santea mieux identifier les maladies digestives en pediatrie
        Les prompts qui te sont envoyes sont des questions posees par les medecins et les infirmiers.
Tu dois repondre a ces questions en donnant des informations pertinentes et utiles pour aider a identifier les maladies digestives en pediatrie.
Les personnes qui t'utilisent s'attendent a ce que tu fournisses des reponses bien raisonnees qui sont a la fois correctes et utiles en se, si c'est possible sur les questions et reponses possibles. Ta langue principale est le francais, tu dois repondre en francais.

        {context}

        ---

        Answer the question based on the above context: {question}
        """

        embedding_function = OpenAIEmbeddings()
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

        # Search the DB.
        results = db.similarity_search_with_relevance_scores(query_text, k=3)
        if len(results) == 0 or results[0][1] < 0.7:
            # Si aucune similarites n'est trouvee
            #
            #
            #
            return HttpResponse("Unable to find matching results.")

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)

        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

        system = """
Tu es un assistant qui aide les personnels de santea mieux identifier les maladies digestives en pediatrie.
Les prompts qui te sont envoyes sont des questions posees par les medecins et les infirmiers.
Tu dois repondre a ces questions en donnant des informations pertinentes et utiles pour aider a identifier les maladies digestives en pediatrie.
Les personnes qui t'utilisent s'attendent a ce que tu fournisses des reponses bien raisonnees qui sont a la fois correctes et utiles en se, si c'est possible sur les questions et reponses possibles.

La requete principale, a laquelle tu dois repondre est la question entouree des champs <main> et </main>

Pour t'aider a repondre a la question, nous te fournissons des conversations precedentes qui contiennent des informations pertinentes sur la question.
Elles ont ete selectionnees pour t'aider a repondre a la question, grace a une analyse des conversations precedentes. Chaque conversation que l'ona jugee proche est entouree des champs <context> et </context>. Similaire ne veut pas dire identique, mais les conversations precedentes peuvent contenir des informations utiles pour repondre a la question."""

        print("completion")
        completion = client.chat.completions.create(
            model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        Message.objects.create(
            content=completion.choices[0].message.content,
            is_prompt=False
        )

        print(completion.choices[0].message.content)
        return HttpResponse(completion.choices[0].message.content)

    return HttpResponse("Invalid form")
