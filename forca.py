import random

def criar_cabeca():
    print(" O")

def criar_tronco():
    print("|", end="")

def criar_braco_esquerdo():
    print("/", end="")

def criar_braco_direito():
    print("\\")

def criar_perna_direita():
    print("\\")

def criar_perna_esquerda():
    print("/ ", end="")

def criar_boneco():
    criar_cabeca()
    criar_braco_esquerdo()
    criar_tronco()
    criar_braco_direito()
    criar_perna_esquerda()
    criar_perna_direita()

def letras_repetidas():
    print("")

def menu():
    print("=" * 35)
    print(" " * 10 + " Jogo da forca " + " " * 10)
    print(" " * 8 + " Seja bem vindo (a)! " + " " * 6)
    print("=" * 35)
    print("Escolha o tema da palavra da forca")
    print("1 - Nome de países")
    print("2 - Nome de animais")
    print("=" * 35)
    resp = input()
    while resp != "1" and resp != "2":
        print("Insira uma opção válida!")
        resp = input()
    print("=" * 35)
    print()
    escolher_tema(resp)

def escolher_tema(escolha):
    if escolha == "1":
        criar_boneco()
        pais = random.randint(1, len(paises))
        for letra in paises[pais]:
            if letra == " " or letra == "-":
                print("  ", end="")
            else:
                print("_ ", end="")
    elif escolha == "2":
        animal = random.randint(1, len(animais))
    

paises = [
    "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra",
    "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia",
    "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão",

    "Bahamas", "Bahrein", "Bangladesh", "Barbados", "Belarus",
    "Bélgica", "Belize", "Benin", "Bolívia",
    "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei",
    "Bulgária", "Burkina Faso", "Burundi", "Butão",

    "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar",
    "Cazaquistão", "Chade", "Chile", "China", "Chipre",
    "Colômbia", "Comores", "Congo",
    "Coreia do Norte", "Coreia do Sul",
    "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",

    "Dinamarca", "Djibuti", "Dominica",

    "Egito", "El Salvador", "Emirados Árabes Unidos",
    "Equador", "Eritreia", "Eslováquia", "Eslovênia",
    "Espanha", "Estados Unidos", "Estônia",
    "Etiópia", "Eswatini",

    "Fiji", "Filipinas", "Finlândia", "França",

    "Gabão", "Gâmbia", "Gana", "Geórgia",
    "Granada", "Grécia", "Guatemala",
    "Guiana", "Guiné", "Guiné-Bissau",
    "Guiné Equatorial",

    "Haiti", "Honduras", "Hungria",

    "Iêmen", "Ilhas Marshall", "Ilhas Salomão",
    "Índia", "Indonésia", "Irã", "Iraque",
    "Irlanda", "Islândia", "Israel", "Itália",

    "Jamaica", "Japão", "Jordânia",

    "Kiribati", "Kuwait",

    "Laos", "Lesoto", "Letônia", "Líbano",
    "Libéria", "Líbia", "Liechtenstein",
    "Lituânia", "Luxemburgo",

    "Madagáscar", "Malásia", "Malaui",
    "Maldivas", "Mali", "Malta",
    "Marrocos", "Maurício", "Mauritânia",
    "México", "Micronésia", "Moçambique",
    "Moldávia", "Mônaco", "Mongólia",
    "Montenegro", "Myanmar",

    "Namíbia", "Nauru", "Nepal",
    "Nicarágua", "Níger", "Nigéria",
    "Noruega", "Nova Zelândia",

    "Omã",

    "Países Baixos", "Palau", "Panamá",
    "Papua-Nova Guiné", "Paquistão",
    "Paraguai", "Peru", "Polônia",
    "Portugal", "Quênia",

    "Reino Unido", "República Centro-Africana",
    "República Democrática do Congo",
    "República Dominicana", "República Tcheca",
    "Romênia", "Ruanda", "Rússia",

    "Samoa", "San Marino",
    "Santa Lúcia", "São Cristóvão e Nevis",
    "São Marino",
    "São Tomé e Príncipe",
    "São Vicente e Granadinas",
    "Senegal", "Serra Leoa", "Sérvia",
    "Seychelles",
    "Singapura", "Síria", "Somália",
    "Sri Lanka", "Sudão", "Sudão do Sul",
    "Suécia", "Suíça", "Suriname",

    "Tailândia", "Tajiquistão", "Tanzânia",
    "Timor-Leste", "Togo", "Tonga",
    "Trinidad e Tobago", "Tunísia",
    "Turcomenistão", "Turquia", "Tuvalu",

    "Ucrânia", "Uganda", "Uruguai", "Uzbequistão",

    "Vanuatu", "Vaticano", "Venezuela", "Vietnã",

    "Zâmbia", "Zimbábue", "Palestina"
]

animais = [
    "abutre", "águia", "alce", "alpaca", "anta", "antílope", "arara", "arraia", 
    "atum", "avestruz", "babuíno", "bagre", "bemtevi", "besouro", "bisão", "bode", 
    "boi", "búfalo", "burro", "cabra", "cabrito", "cacatua", "cachorro", "cágado", 
    "calopsita", "camaleão", "camarão", "camelo", "camundongo", "canário", "capivara", 
    "caranguejo", "carneiro", "cascavel", "castor", "cavalo", "cegonha", "cervo", 
    "chimpanzé", "cisne", "codorna", "coelho", "coiote", "condor", "coral", "cordeiro", 
    "coruja", "corvo", "crocodilo", "doninha", "dromedário", "égua", "elefante", "ema", 
    "esponja", "esquilo", "faisão", "falcão", "flamingo", "formiga", "frango", "furão", 
    "galinha", "galo", "gambá", "ganso", "garça", "garoupa", "gato", "gavial", 
    "gavião", "gazela", "girafa", "gorila", "guaxinim", "guepardo", "hamster", "hiena", 
    "hipopótamo", "iguana", "jabuti", "jacaré", "javali", "jiboia", "jumento", "kiwi", 
    "lacraia", "lagarto", "lagosta", "leão", "leitão", "leopardo", "lhama", "lince", 
    "lobo", "lontra", "lula", "macaco", "mamba", "marmota", "medusa", "morcego", 
    "naja", "onça", "orangotango", "ouriço", "ovelha", "pacu", "panda", "pantera", 
    "papagaio", "pardal", "pato", "pavão", "pelicano", "perereca", "periquito", 
    "peru", "pinguim", "piranha", "píton", "pogona", "polvo", "pombo", "porco", 
    "puma", "quimera", "rã", "raposa", "rato", "rinoceronte", "rolinha", "sabiá", 
    "salamandra", "salmão", "sapo", "sardinha", "siri", "sucuri", "tamanduá", "tartaruga", 
    "tatu", "teiu", "texugo", "tigre", "tilápia", "touro", "tritão", "tubarão", 
    "tucano", "urso", "urubu", "vaca", "zebra"
]
  
menu()