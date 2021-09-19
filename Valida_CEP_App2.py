import requests
import PySimpleGUI as sg

#   ____ _____ ____   __     ___    _     ___ ____   ___  
#  / ___| ____|  _ \  \ \   / / \  | |   |_ _|  _ \ / _ \ 
# | |   |  _| | |_) |  \ \ / / _ \ | |    | || | | | | | |
# | |___| |___|  __/    \ V / ___ \| |___ | || |_| | |_| |
#  \____|_____|_|        \_/_/   \_\_____|___|____/ \___/ 

# Autor Elizeu Barbosa Abreu: https://github.com/elizeubarbosaabreu
# Este projeto foi baseado em um projeto que roda via terminal https://dev.to/mph7/como-consumir-uma-api-em-python-ffk

sg.theme('Reddit')

layout = [[sg.Text('VALIDA CEP APP', font=('Arial 16'))],
          [sg.Text('''Este App verifica se um determinado CEP é válido,
retornando o nome do logradouro, bairro, cidade,
UF, caso disponíveis... ''', font=('Arial 10'))],
          [sg.Text(
              'Digite um CEP'), sg.Input(
                  key='-INPUT-', size=(15, 1)), sg.Button(
                      'Consultar')],
          [sg.Text(
                  'https://github.com/elizeubarbosaabreu')]
          
    ]
window = sg.Window('VALIDA CEP APP', layout, resizable=True, element_justification='c')

while True:
    event, values = window.read()    
    if event == sg.WINDOW_CLOSED:
        break
    
    cep = values['-INPUT-']
            
    if len(cep) != 8:
        sg.Popup('ERRO!!', '''Quantidade de dígitos inválida.
Use apenas números sem pontos ou tracinhos. Ex.: 76916000''')
        continue
        
    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    address_data = request.json()
    
    
    if "erro" not in address_data:
        
        logradouro = address_data['logradouro']
        if logradouro == '':
            logradouro = 'valor nulo'
            
        complemento = address_data['complemento']
        if complemento == '':
            complemento = 'valor nulo'
            
        bairro = address_data['bairro']
        if bairro == '':
            bairro = 'valor nulo'
        
        localidade = address_data['localidade']
        if localidade == '':
            localidade = 'valor nulo'
          
        uf = address_data['uf']
        if uf == '':
            uf = 'valor nulo'
           
        sg.Popup('CEP LOCALIZADO!', f'''
CEP: {cep}
LOGRADOURO: {logradouro}
COMPLEMENTO: {complemento}
BAIRRO: {bairro}
CIDADE: {localidade}
ESTADO: {uf}

fonte: https://viacep.com.br
''')
    else:
        sg.Popup('CEP NÃO LOCALIZADO!!!', f'{cep} não localizado em nosso banco de dados!!!')
    

window.close()
