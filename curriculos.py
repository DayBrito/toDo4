### To Do 4 - Dayane
candidatos = []
# candidatos_total = []
count = 0
# candidatos_aprovados = []
requisitos = {'Cientista': ['python', 'pandas', 'liderança', 'SQL', 'criação', 'BI', 'desenvolvimento', 'base de dados'],
'Analista': ['python', 'SQL', 'BI', 'relatórios']}


print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')
if escolha == '1':
    while True:
        candidatos_cient = []
        menu = input('[1] Inserir dados dos candidatos\n[2] Sair\n') 
        if menu == '1':
            print('-----Iniciando cadastro de candidatos-----')
            candidatos = int(input('Digite a quantidade de candidatos para a vaga de Cientista de Dados: '))
            for i in range(candidatos):
                nome = input('Digite o nome completo do candidato: ')
                resumo = input('Digite o resumo do currículo: ')
                candidatos_cient.append([nome, resumo])
                count += 1
                
            for c in candidatos_cient:
                verifica = 0
                for j in requisitos['Cientista']:
                    if j.upper() in c[1].upper():
                        verifica += 1
                        
                if verifica > 0:
                    print(f'\nCandidato(a) {c[0]} está apto para a vaga')
                elif verifica == 0:
                    print(f'\nCandidato(a) {c[0]} não está apto para a vaga')
                
    
        elif menu == '2':
             print('\nAté logo!')
             break
        else:
            print('Opção inválida, tente novamente.')
            print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
            escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')
        print(f'\n-A quantidade de candidatos foi: {count}-')

        print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
        escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')

            

elif escolha == '2':
    while True:
        candidatos_analist = []
        verifica = 0
        menu = input('Olá! Selecione a opção desejada:\n\n[1] Inserir dados dos candidatos\n[2] Sair\n') 
        if menu == '1':
            print('-----Iniciando cadastro de candidatos-----')
            candidatos = int(input('Digite a quantidade de candidatos para a vaga de Analista de Dados: '))
            for i in range(candidatos):
                nome = input('Digite o nome completo do candidato: ')
                resumo = input('Digite o resumo do currículo: ')
                candidatos_analist.append([nome, resumo])
                count += 1

            for d in candidatos_analist:
                verifica = 0
                for k in requisitos['Analista']:
                    if k.upper() in d[1].upper():
                        verifica += 1
                    
                if verifica > 0:
                    print(f'\nCandidato(a) {d[0]} está apto para a vaga')
                elif verifica == 0:
                    print(f'\nCandidato(a) {d[0]} não está apto para a vaga')
                
            
        elif menu == '2':
             print('\nAté logo!')
             break
        else:
            print('Opção inválida, tente novamente.')
            print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
            escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')
        print(f'\n-A quantidade de candidatos foi: {count}-')
        print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
        escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')

elif escolha == '3':
    print('\nAté logo!')
    
else:
    print('-----Olá, sejá bem vindo ao portal de vagas----- \nSelecione uma vaga para candidatar-se:')
    escolha = input('[1] Cientista de Dados\n[2] Analista de Dados\n[3] Sair\nDigite: ')