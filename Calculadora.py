from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')

GUI = Builder.load_file('tela.kv')




class MinhaCalculadora(App):
    def build(self):
        return GUI
    OPERECAO = ''

    def soma(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} +'
        MinhaCalculadora.OPERECAO = 'SOMA'

    def multiplicacao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} *'
        MinhaCalculadora.OPERECAO = 'MULTIPLICAÇÃO'

    def subtracao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} -'
        MinhaCalculadora.OPERECAO = 'SUBTRAÇÃO'

    def divisao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} /'
        MinhaCalculadora.OPERECAO = 'DIVISAO'

    def resultado(self):
        MinhaCalculadora.NUMBER_TWO = GUI.ids['input'].text
        if MinhaCalculadora.OPERECAO == 'SOMA':
            MinhaCalculadora.resultado = float(MinhaCalculadora.NUMBER_ONE) + float(MinhaCalculadora.NUMBER_TWO)
            MinhaCalculadora.NUMBER_ONE = MinhaCalculadora.resultado
            GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} +'
            GUI.ids['input'].text = f'{MinhaCalculadora.resultado}'
        elif MinhaCalculadora.OPERECAO == 'SUBTRAÇÃO':
            MinhaCalculadora.resultado = float(MinhaCalculadora.NUMBER_ONE) - float(MinhaCalculadora.NUMBER_TWO)
            MinhaCalculadora.NUMBER_ONE = MinhaCalculadora.resultado
            GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} -'
            GUI.ids['input'].text = f'{MinhaCalculadora.resultado}'
        elif MinhaCalculadora.OPERECAO == 'MULTIPLICAÇÃO':
            MinhaCalculadora.resultado = float(MinhaCalculadora.NUMBER_ONE) * float(MinhaCalculadora.NUMBER_TWO)
            MinhaCalculadora.NUMBER_ONE = MinhaCalculadora.resultado
            GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} *'
            GUI.ids['input'].text = f'{MinhaCalculadora.resultado}'
        elif MinhaCalculadora.OPERECAO == 'DIVISAO':
            MinhaCalculadora.resultado = float(MinhaCalculadora.NUMBER_ONE) / float(MinhaCalculadora.NUMBER_TWO)
            MinhaCalculadora.NUMBER_ONE = MinhaCalculadora.resultado
            GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} /'
            GUI.ids['input'].text = f'{MinhaCalculadora.resultado}'
        else:
            pass



    GUI.ids['divisao'].bind(on_press=divisao)
    GUI.ids['multiplicacao'].bind(on_press=multiplicacao)
    GUI.ids['subtracao'].bind(on_press=subtracao)
    GUI.ids['soma'].bind(on_press=soma)
    GUI.ids['resultado'].bind(on_press=resultado)



if __name__ == '__main__':
    MinhaCalculadora().run()
