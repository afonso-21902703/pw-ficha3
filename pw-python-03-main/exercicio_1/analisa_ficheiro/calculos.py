def calcula_linhas(nome_ficheiro):
    try:
        file = open(nome_ficheiro, 'r')
        conteudo = file.read()
        c.split = conteudo.split('\n')
        n = 0
        for i in c.split:
            n+= 1
        return n
    except:    
        print('É impossível abrir o ficheiro com o nome ', nome_ficheiro)
        exit()

def calcula_carateres(nome_ficheiro):
    try:
        file = open(nome_ficheiro, 'r')
        conteudo = file.read(nome_ficheiro)
        n = 0
        for i in conteudo:
            n+= 1
        return n
    except OSError:
        print('É impossível abrir o ficheiro com o nome ', nome_ficheiro)
        exit()

def calcula_palavra_comprida(nome_ficheiro):
    try:
        file = open(nome_ficheiro, 'r')
        conteudo = file.read(nome_ficheiro)
        palavra = ''
        for word in conteudo.split():
            if len(word) > len(palavra):
                palavra = word
        return palavra
    except OSError:
        print('É impossível abrir o ficheiro com o nome ', nome_ficheiro)
        exit()

def calcula_ocorrencia_de_letras(nome_ficheiro):
    dicionario = {}
    try:
        file = open(nome_ficheiro, 'r')
        conteudo = file.read(nome_ficheiro)
        for n in conteudo:
            if n != '\n':
                dicionario[n] += 1
            else:
                dicionario[n] = 1
        return dicionario
    except OSError:
        print('É impossível abrir o ficheiro com o nome ', nome_ficheiro)
        exit()