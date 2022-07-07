# o objetivo do algoritmo é simular o cálculo dos 3 tipos básicos de aposta:
# GRUPO, DUQUE DE DEZENA E MILHAR

# grupo: tem como o objetivo acertar o grupo do primeiro resultado impresso
# DD: tem como o objetivo acertar duas dezenas entre as 5 dezenas sorteadas
# milhar: tem como o objetivo acertar a primeira milhar sorteada (na cabeça)

from ast import While
import random


# sorteio grupo:
# o quinto numero das listas sempre será o usado para fazer o sorteio do grupo

dicionario = {'aveztruz' : "01", "aguia" : "02", "burro" : "03"}


bichos  = {
    "avestruz": ["01", "02", "03", "04", "01"],
    "aguia" : ["05", "06","07", "08", "02"],
    "burro" : ["09", "10", "11", "12", "03"],
    "borboleta" : ["13", "14", "15", "16", "04"],
    "cachorro" : ["17", "18", "19", "20", "05"],
    "cabra" : ["21", "22", "23", "24", "06" ],
    "carneiro" : ["25", "26", "27", "28", "07"],
    "camelo" : ["29", "30", "31", "32", "08" ],
    "cobra" : ["33", "34", "35", "36","09"],
    "coelho" : ["37", "38", "39", "40","10"],
    "cavalo" : ["41", "42", "43", "44", "11"],
    "elefante" : ["45", "46", "47", "48", "12"],
    "galo" : ["49", "50", "51", "12", "13"],
    "gato" : ['53','54','55','56', "14"],
    "jacare" : ['57','58','59','60', "15"],
    "leao" : ['61','62','63','64', "16"],
    "macaco" : ['65','66','67','68', "17"],
    "porco" : ['69','70','71','72', "18"],
    "pavao" : ['73','74','75','76', "19"],
    "peru" : ['77','78','79','80', "20"],
    "touro" : ['81','82','83','84', "21"],
    "tigre" : ['85','86','87','88', "22"],
    "urso" : ['89','90','91','92', "23"],
    "viado" : ['93','94','95','96', "24"],
    "vaca" : ['97','98','99','00', "25"],
}



# sortear dois numeros de dois algarismos
numero = random.randint(0,99)



for k, v in bichos.items():
    for i in v:
        if str(numero) == i:
            print(numero)
            print(f"{k}, grupo:{v[4]}")
       
    
# resultado = "97", "49"





# print(f"{resultado}, {resultado[1]})

