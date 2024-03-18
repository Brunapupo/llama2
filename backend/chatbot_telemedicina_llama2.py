
import os
import replicate

#Definindo a chama da api dentro do python llhama
os.environ["REPLICATE_API_TOKEN"] = "r8_ZBCtnclmoAfS0AcucB8Fhn5IO9b6zyA3hi9yI"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

# Prompts
pre_prompt = "A anemia é uma condição médica caracterizada pela redução na quantidade de glóbulos vermelhos ou na concentração de hemoglobina no sangue. Isso resulta em uma menor capacidade do sangue de transportar oxigênio para os tecidos do corpo, podendo causar sintomas como fadiga, palidez, falta de ar e tontura. As causas da anemia podem ser variadas, incluindo deficiências nutricionais (como falta de ferro, vitamina B12 ou ácido fólico), perdas sanguíneas crônicas, doenças crônicas, infecções, ou condições genéticas. O diagnóstico é feito por meio de exames de sangue, e o tratamento depende da causa subjacente, podendo incluir suplementação nutricional, medicamentos, ou em casos mais graves, transfusões de sangue."
prompt_input = "O que é anemia?"

# Generate LLM response
output = api.run("meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3", # LLM model
                        input={"prompt": f"{pre_prompt} {prompt_input} Assistente: ", # Prompts
                        "temperature":0.1, "top_p":0.9, "max_length":10000, "repetition_penalty":1})  # Model parameters

for item in output:
    print(item, end="")

