from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse
from openai import OpenAI


def index(request):

    context = {
        "form": MessageForm()
    }
    return render(request, "chat/templates/index.html", context)


def send(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

            form_content = form.cleaned_data["content"]

            # Point to the local server
            # client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

            # history = [
            #     {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
            #     {"role": "user", "content": f"{form_content}"},
            # ]

            # while True:
            #     completion = client.chat.completions.create(
            #         model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
            #         messages=history,
            #         temperature=0.7,
            #         stream=True,
            #     )

            #     new_message = {"role": "assistant", "content": ""}

            #     for chunk in completion:
            #         if chunk.choices[0].delta.content:
            #             print(chunk.choices[0].delta.content, end="", flush=True)
            #             new_message["content"] += chunk.choices[0].delta.content

            #     history.append(new_message)

            # return HttpResponse("Success!")

            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

            system = """
Tu es un assistant qui aide les personnels de santea mieux identifier les maladies digestives en pediatrie.
Les prompts qui te sont envoyes sont des questions posees par les medecins et les infirmiers.
Tu dois repondre a ces questions en donnant des informations pertinentes et utiles pour aider a identifier les maladies digestives en pediatrie.
Les personnes qui t'utilisent s'attendent a ce que tu fournisses des reponses bien raisonnees qui sont a la fois correctes et utiles en se, si c'est possible sur les questions et reponses possibles.

La requete principale, a laquelle tu dois repondre est la question entouree des champs <main> et </main>

Pour t'aider a repondre a la question, nous te fournissons des conversations precedentes qui contiennent des informations pertinentes sur la question.
Elles ont ete selectionnees pour t'aider a repondre a la question, grace a une analyse des conversations precedentes. Chaque conversation que l'ona jugee proche est entouree des champs <context> et </context>. Similaire ne veut pas dire identique, mais les conversations precedentes peuvent contenir des informations utiles pour repondre a la question."""

            test = "Quel traitement pour une découverte d’HP suite à fibro pour de grosses gastralgies et en fait HP découverte seulement à l’immunofluorescence! Tt propose: Amox Inexium et flagyl"

            completion = client.chat.completions.create(
                model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": test}
                ],
                temperature=0.7,
            )

            print(completion.choices[0].message)

            return HttpResponse(completion.choices[0].message.content)

        return HttpResponse("Invalid form")
