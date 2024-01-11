from tkinter import *
import unicodedata
from ttkbootstrap .style import Style

style = Style(theme="darkly")

root = style.master


text = Text(root)
text.tag_config('right', justify='right', foreground='yellow')  # Mensagem do usuario na direita e colorido

def remove(b):
    normaliza = unicodedata.normalize('NFKD', b)
    return ''.join([c for c in normaliza if not unicodedata.combining(c)])

def click(event=None):
    b = a.get().lower()
    if b:  # Adicionado para verificar se a entrada do usuario não está vazia
        send = 'Você:' + " " + a.get()
        text.insert(END, '\n' + send, 'right')
    if b == 'sim':                      # TRIBUTOS
        text.insert(END, '\n' + 'Fernanda: Tudo bem! Gostaria de saber sobre *Impostos*, *Tributos* ou \ngostaria de uma breve *explicação sobre Educação Fiscal*?')
    elif b == 'não':
        text.insert(END, '\n' + 'Fernanda: Ok, volte quando estiver interessado...')
    elif b == 'tributos':
        text.insert(END, '\n' + 'Fernanda: Ótimo! A tributação é um assunto amplo, \nabrangendo diversos tipos de impostos e regras em diferentes países. \nVocê *Gostaria* ou *Não Gostaria* de um resumo sobre o assunto?')
    elif b == 'gostaria':
        text.insert(END, '\n' + 'Fernanda: Tributação é o processo pelo qual \num governo coleta dinheiro dos cidadãos e das empresas \npara financiar suas atividades e serviços públicos \ncomo educação, saúde, segurança e infraestrutura. \nIsso é feito por meio da imposição de impostos, \ntaxas e contribuições obrigatórias. \n\nVocê gostaria de saber sobre *Dúvidas Tributos* ou *impostos*?')
    elif b == '1':
        text.insert(END, '\n' + """Fernanda: Tributo e imposto são conceitos relacionados, mas têm diferenças importantes. Tributo é uma obrigação imposta pelo Estado para arrecadar recursos.\n
É uma grande área que se subdivide em áreas menores: taxas, impostos e contribuição de melhoria. \nTodo tributo é compulsório e só pode ser criado ou extinto por meio de lei. \nPor outro lado, imposto é uma categoria específica de tributo. 
  \nSegundo o Código Tributário Nacional, imposto é o tributo cuja obrigação tem por fato gerador uma situação independente de qualquer atividade estatal específica, relativa ao contribuinte. 
  \nEm geral, os impostos incidem sobre a renda, o patrimônio ou o consumo. \nportanto, todo imposto é um tributo, mas nem todo tributo é um imposto. Gostaria de alguns *exemplos*?""")
    elif b == 'exemplos':
        text.insert(END, '\n' + """Fernanda: Impostos: São tributos que incidem sobre patrimônio, renda e consumo. Alguns exemplos incluem Imposto de Renda da Pessoa Jurídica (IRPJ), Imposto sobre a Exportação (IE), Imposto sobre a Importação (II), Imposto sobre a propriedade Territorial Rural (ITR), Imposto sobre operações de Crédito (IOF), Imposto sobre Produtos Industrializados (IPI).'
                                 \nTaxas: Estão diretamente relacionadas a uma contraprestação de serviços do Estado, como taxa de iluminação pública, taxa de expedição de documentos, de limpeza urbana, etc.
                                 \nContribuições de melhoria: Podem ser cobradas pelo ente público em decorrência de obras públicas que valorizem o imóvel do contribuinte.
                                 \nContribuições especiais: Fazem parte de uma espécie de tributo que pode ser dividida em três categorias: Contribuições sociais, destinadas a financiar os direitos sociais e previdenciários, como PIS/COFINS, CSLL, CPRB; Contribuições de Intervenção no Domínio Econômico, como a CIDE Combustíveis ou CIDE Remessas Exterior; Contribuição com uma categoria profissional ou econômica, como CREA, CRM, sindicatos, etc.
                                 \nEmpréstimos compulsórios: São tributos instituídos pela União, em casos de guerra externa ou sua iminência, ou em caso de calamidade pública que provoque despesas extraordinárias""")

    elif b == 'não gostaria':
        text.insert(END, '\n' + 'Fernanda: Ok, Gostaria de falar sobre *Impostos* ou *Dúvidas Tributos*?')

    # DÚVIDAS TRIBUTOS
    elif b == 'dúvidas tributos':
        text.insert(END, '\n' + 'Fernanda: Quais dúvidas você possui? Escolha uma das opções abaixo:'
                                '\n\n*Diferença entre Impostos e Tributos*\n\n'
                                'Caso sua dúvida não esteja aqui, acesse esse link:')
    elif b == 'diferença entre impostos e tributos':
        text.insert(END, '\n' + 'Fernanda: Tributo e imposto são conceitos relacionados, mas têm diferenças importantes. \n'
                                'Tributo é  uma obrigação imposta pelo Estado para arrecadar recursos. \n'
                                'É uma grande área que se subdivide em áreas menores: taxas, impostos e contribuição de melhoria. \n'
                                'Todo tributo é compulsório e só pode ser criado ou extinto por meio de lei. \n'
                                'Por outro lado, imposto é uma categoria específica de tributo. \n'
                                'Segundo o Código Tributário Nacional, imposto é o tributo cuja obrigação tem por fato gerador uma situação independente de qualquer atividade estatal específica, relativa ao contribuinte. \n'
                                'Em geral, os impostos incidem sobre a renda, o patrimônio ou o consumo.\n '
                                '\n\nPortanto, todo imposto é um tributo, mas nem todo tributo é um imposto.')
    # EDUCAÇÃO FISCAL
    elif b == 'explicação educação fiscal':
        text.insert(END, '\n' + 'Fernanda: A Educação Fiscal é um conjunto de ações educativas que visam possibilitar a compreensão da função socioeconômica dos tributos e como eles podem ser usados em benefício à sociedade.\n '
                                'Ela é essencial para entender o papel do Estado e como ele pode proporcionar atividades essenciais. \n'
                                'Além disso, entendendo os conceitos fiscais, é possível saber todos os impostos e tributos que devem ser pagos, contribuindo para que a regularidade de empresas e pessoas físicas com a Receita fique em dia.\n\n'
                                'Gostaria de conversar sobre *Impostos*, *Tributos* ou ir para *Dúvidas Educação Fiscal*?')
    elif b == 'dúvidas educação fiscal':
        text.insert(END, '\n' + 'Fernanda: Quais suas dúidas sobre a educação fiscal?\n\n'
                                '*Qualquer escola possui educação fiscal?*\n'
                                '*O que se estuda?*\n'
                                '*Como posso me formar na área?*\n'
                                '')
    elif b == 'qualquer escola possui educação fiscal?':
        text.insert(END, '\n' + 'Fernanda: Não, pois é necessário um professor formado nessa área, instituições de ensino nas quais não possuem este profissional não poderão ter esta disciplina.')
    elif b == 'como posso me formar na área?':
        text.insert(END, '\n' + 'Fernanda: Existem cursos específicos sobre educação fiscal que podem ser realizados por qualquer pessoa interessada no assunto. '
                                '\nEsses cursos podem ser oferecidos por instituições de ensino, organizações governamentais ou não governamentais. '
                                '\n\nAqui o link de um curso sobre Educação Fiscal oferecido pelo governo: ')
    elif b == 'o que se estuda?':
        text.insert(END, '\n' + 'Fernanda: Em sala de aula, os estudantes aprendem o que são os tributos e como eles devem ser usados para se ter uma melhoria na realidade social das pessoas, por meio de serviços públicos eficientes. '
                                '\nAlém disso, eles passam a ser motivados a observar como os impostos são recolhidos e aplicados na sociedade. '
                                '\nA Educação Fiscal visa estimular a conscientização da sociedade sobre a importância, necessidade e justificativa para o pagamento de tributos.')

    # IMPOSTOS
    elif b == 'impostos':
        text.insert(END, '\n' + 'Fernanda: No Brasil, temos diversos impostos. '
                                'Você *gostaria* ou *não gostaria* de um resumo geral sobre o assunto?')
    elif b == 'gostaria':
        text.insert(END, '\n' + '')
    elif b == 'não gostaria':
        text.insert(END, '\n' + '')
    else:
        text.insert(END, '\n' + 'Fernanda: Desculpe, não entendo...')

    a.delete(0, 'end')  # Adicionado para apagar a mensagem após ser enviada

# Configurando botôes
text.grid(row=0, column=0, columnspan=2)

a = Entry(root, width=40)
send = Button(root, text='Enviar', bg='white', width=20, command=click)
send.grid(row=1, column=1)
a.grid(row=1, column=0)

root.title('FernandaBot')
root.bind('<Return>', click)

# Mover a mensagem inicial de Fernanda para fora da função click
text.insert(END, '\n' + 'Fernanda: Olá, Sou a Fernanda, um ChatBot sobre educação fiscal. \nGostaria de tirar algumas dúvidas sobre Educação Fiscal?')

root.mainloop()
