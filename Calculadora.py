from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')

from kivy.core.window import Window

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

    def um(self):
        GUI.ids['input'].text += f'1'

    def dois(self):
        GUI.ids['input'].text += f'2'

    def tres(self):
        GUI.ids['input'].text += f'3'

    def quatro(self):
        GUI.ids['input'].text += f'4'

    def cinco(self):
        GUI.ids['input'].text += f'5'

    def seis(self):
        GUI.ids['input'].text += f'6'

    def sete(self):
        GUI.ids['input'].text += f'7'

    def oito(self):
        GUI.ids['input'].text += f'8'

    def nove(self):
        GUI.ids['input'].text += f'9'

    def zero(self, numero):
        GUI.ids['input'].text += f'{numero}'

    def ce(self):
        GUI.ids['input'].text = ''

    def c(self):
        MinhaCalculadora.NUMBER_ONE = ''
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = ''
        MinhaCalculadora.OPERECAO = ''

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'numpadadd':
            self.soma()
        elif keycode[1] == 'numpadsubstract':
            self.subtracao()
        elif keycode[1] == 'numpadmul':
            self.multiplicacao()
        elif keycode[1] == 'numpaddivide':
            self.divisao()
        elif keycode[1] == 'enter' or keycode[1] == 'numpadenter':
            self.subtracao()
        return True

    GUI.ids['divisao'].bind(on_press=divisao)
    GUI.ids['multiplicacao'].bind(on_press=multiplicacao)
    GUI.ids['subtracao'].bind(on_press=subtracao)
    GUI.ids['soma'].bind(on_press=soma)
    GUI.ids['resultado'].bind(on_press=resultado)
    GUI.ids['ce'].bind(on_press=ce)
    GUI.ids['c'].bind(on_press=c)
    GUI.ids['1'].bind(on_press=um)
    GUI.ids['2'].bind(on_press=dois)
    GUI.ids['3'].bind(on_press=tres)
    GUI.ids['4'].bind(on_press=quatro)
    GUI.ids['5'].bind(on_press=cinco)
    GUI.ids['6'].bind(on_press=seis)
    GUI.ids['7'].bind(on_press=sete)
    GUI.ids['8'].bind(on_press=oito)
    GUI.ids['9'].bind(on_press=nove)
    GUI.ids['0'].bind(on_press=zero)


if __name__ == '__main__':
    MinhaCalculadora().run()

