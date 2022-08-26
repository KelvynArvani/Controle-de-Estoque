import pandas as pd
import os

def apaga():
    planilha = pd.read_excel('estoque.xlsx')
    consulta = input('Digite o código do produto para pesquisa de remoção ou pressione "ENTER" para Voltar: ')
    if consulta == '' or consulta == '':
        os.system('cls')
        pass
    else:
        try:
            consulta = int(consulta)
            retorno = planilha.loc[planilha['REF'] == consulta]
            print(f'\n{retorno}\n')
        except:
            os.system('cls')
            print('Digite um código de produto válido!\n')
            apaga()
        endereco = input('Digite o numero da linha a ser apagada ou pressione "ENTER" para voltar: ')
        if endereco == '' or endereco == ' ':
            os.system('cls')
            pass
        else:
            endereco = int(endereco)
            planilha.drop(endereco, axis=0, inplace=True, errors='ignore')
            planilha.to_excel('estoque.xlsx', index=False)
            os.system('cls')
            print('\n**Produto deletado com sucesso**\n')    
        