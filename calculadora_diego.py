#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('### Calculadora em Python ###\n')


# In[ ]:


print("Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n") 


# In[ ]:


z = input('Digite sua opção (1/2/3/4): ')

if z == "1":
#criando a função soma:

    x = input("\nDigite o primeiro número: ")
    y = input("\nDigite o segundo número: ")
    def soma(x, y):
        res_soma = int(x) + int(y);
        print('\n\n%s' %(int(x)) + ' + ''%r' %(int(y)) + " = " + str(res_soma))
    soma(x, y)
elif z == "2":
#criando a função subtração:

    x = input("\nDigite o primeiro número: ")
    y = input("\nDigite o segundo número: ")
    def subt(x, y):
        res_subt = int(x) - int(y);
        print('\n\n%s' %(int(x)) + ' - ''%r' %(int(y)) + " = " + str(res_subt))
    subt(x, y)
elif z == "3":
#criando a função multiplicação:

    x = input("\nDigite o primeiro número: \n")
    y = input("\nDigite o segundo número: \n")
    def mult(x, y):
        res_mult = int(x) * int(y);
        print('\n\n%s' %(int(x)) + ' * ''%r' %(int(y)) + " = " + str(res_mult))
    mult(x, y)
elif z == "4":
#criando a função divisão:

    x = input("\nDigite o primeiro número: ")
    y = input("\nDigite o segundo número: ")
    def divs(x, y):
        res_divs = int(x) / int(y);
        print('\n\n%s' %(int(x)) + ' / ''%r' %(int(y)) + " = " + str(res_divs))
    divs(x, y)
else:
    print('Opção inexistente!')


# In[ ]:




