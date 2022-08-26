import pandas as pd
import os

#Realiza cadastros dentro do arquivo xlsx
def cadastro():
    while True:
        planilha = pd.read_excel('estoque.xlsx')
        referencia = input('\nDigite o Código de referência do produto para cadastro ou pressione "Enter" para voltar: ')
        try:
            if referencia == '' or referencia == ' ':
                os.system('cls')
                break
        except:
            pass
        try:            
            referencia = int(referencia)
        except:
            os.system('cls')
            print('Digite um codigo de referência válido ("apenas números")')
            cadastro()
            break

        descricao = input('\nDigite a "Descrição" do produto: ')
        if descricao.isnumeric():
            os.system('cls')
            print('**Digite apenas "Letras" para "Descrição"!**\n')
            cadastro()
            break
        else:
            descricao = descricao.upper()

        cor = input('\nDigite a "COR" do produto: ')
        if cor.isnumeric():
            os.system('cls')
            print('**Digite apenas "Letras" para "Descrição"!**\n')
            cadastro()
            break
        else:
            cor = cor.upper()
            
        tamanho_p = input('\nDigite um valor de estoque para "Tamanho P": ')
        tamanho_p = tamanho_p.replace(',', '.')
        try:
            tamanho_p = int(tamanho_p)
        except:
            os.system('cls')
            print('**Digite apenas o valor em "Números" para "Tamanho P"!**\n')
            cadastro()
            break

        tamanho_m = input('\nDigite um valor de estoque para "Tamanho M": ')
        tamanho_m = tamanho_m.replace(',', '.')
        try:
            tamanho_m = int(tamanho_m)
        except:
            os.system('cls')
            print('**Digite apenas o valor em "Números" para "Tamanho M"!**\n')
            cadastro()
            break

        tamanho_g = input('\nDigite um valor de estoque para "Tamanho G": ')
        tamanho_g = tamanho_g.replace(',', '.')
        try:
            tamanho_g = int(tamanho_g)
        except:
            os.system('cls')
            print('**Digite apenas o valor em "Números" para "Tamanho G"!**\n')
            cadastro()
            break

        tamanho_gg = input('\nDigite um valor de estoque para "Tamanho GG": ')
        tamanho_gg = tamanho_gg.replace(',', '.')
        try:
            tamanho_gg = int(tamanho_gg)
        except:
            os.system('cls')
            print('**Digite apenas o valor em "Números" para "Tamanho GG"!**\n')
            cadastro()
            break

        preco = input('\nDigite o preço do produto: ')
        preco = preco.replace(',', '.')
        try:
            preco = float(preco)
        except:
            os.system('cls')
            print('**Digite apenas o valor em "Números" para "PREÇO"! ex "00,00"**\n')
            cadastro()
            break


        # Cadastro dos produtos em células
        planilha = planilha.append({'REF': referencia, 'DESCRIÇÃO':descricao, 'CORES': cor, 'TAMANHO P':tamanho_p, 'TAMANHO M':tamanho_m, 'TAMANHO G':tamanho_g, 'TAMANHO GG':tamanho_gg,'PREÇO': f'R$ '+ f'{preco}'}, ignore_index=True)
        # Salva a planilha 
        consulta = referencia
        retorno = planilha.loc[planilha['REF'] == consulta]
        os.system('cls')
        while True:
            print(retorno)
            finaliza = input(
            '\nOs dados estão corretos?\n'
            '\n"1" para SIM\n'
            '"2" para NÃO\n\n'
            'Insira sua opção: ')
            if finaliza == '1':
                planilha.to_excel('estoque.xlsx', index=False)
                os.system('cls')
                print('**Produto cadastrado com sucesso**\n')
                print('Deseja cadastrar outro produto?')
                break
            elif finaliza == '2':
                endereco = input('\nDigite o numero da linha a ser "Removida": ')
                os.system('cls')
                endereco = int(endereco)
                planilha.drop(endereco, axis=0, inplace=True, errors='ignore')
                print("**Item Removido**")
                cadastro()
                break
            else:
                os.system('cls')
                print('**Opção Invalida**')