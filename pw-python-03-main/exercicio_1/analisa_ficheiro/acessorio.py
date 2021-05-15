def pede_nome()->"String":
    while True:
        teclado = input('Insira o nome do ficheiro: ')
        try:
            open(teclado)
            for n in teclado:
                if n =='.':
                    tecladosplit = teclado.split('.')
                    if tecladosplit[1] == 'txt':
                        return tecladosplit[0]
                        exit()
        except IOError:
            print('não existe')

def gera_nome():
    nome_txt = pede_nome()
    return(nome_txt + '.json')

pede_nome()