def cough_dec(func):
#cria o decorator
    def func_wrapper():
    #cria a função que vai abraçar // antes e/ou depois
        print('cough, cough...')
        #code before function question
        func()
        #funcao que tá sendo extendida e passada como arg
        print('cough, cough...')
        #code after function question
    return func_wrapper
    #retorno da wrapper

@cough_dec
#usando o decorator pra extender o comportamento da func question()
#sem modificar a function!!!
def question():
    print('Are you there?')

@cough_dec
#usando o decorator pra extender o comportamento a func answer()
#sem modificar a function!!!
def answer():
    print('No...')

question()
answer()

