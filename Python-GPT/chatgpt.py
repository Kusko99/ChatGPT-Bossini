import openai

def criar_pergunta(
        OPENAI_API_KEY,
        assunto,
        tipo,
        dificuldade,
        pergunta_exemplo = None
):
    openai.api_key = OPENAI_API_KEY
    assunto = f'Elabore uma pergunta sobre {assunto}'
    tipo = f'Ela deve ser do tipo {tipo}' + ' com 4 alterativas' if tipo == "Alternativa" else ''
    dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}'
    pergunta_exemplo = f'Ultilize essa pergunta como exemplo: {pergunta_exemplo}' if pergunta_exemplo != None and pergunta_exemplo != '\n' else ''
    prompt = f'{assunto}. {tipo}. {dificuldade}. {pergunta_exemplo}.'
    print(prompt)
    reposta = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 105
    )
    return reposta.choices[0].text.strip()

def responder_pergunta(
        OPENAI_API_KEY,
        pergunta_a_ser_respondida
):
    openai.api_key = OPENAI_API_KEY
    prompt = f'Responda a seguinte pergunta: {pergunta_a_ser_respondida}'
    resposta = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 150
    )
    return resposta.choices[0].text.strip