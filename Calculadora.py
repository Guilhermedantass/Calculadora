from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')

from kivy.core.window import Window
from kivy.uix.widget import Widget

GUI = Builder.load_file('tela.kv')


class MinhaCalculadora(App):

    OPERECAO = ''
    NUMBER_ONE = ''
    NUMBER_TWO=''
    resultado=''

    def build(self):
        return GUI

    def soma(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} +'
        MinhaCalculadora.OPERECAO = 'SOMA'
        GUI.ids['input'].text = ''

    def multiplicacao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} *'
        MinhaCalculadora.OPERECAO = 'MULTIPLICAÇÃO'
        GUI.ids['input'].text = ''

    def subtracao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} -'
        MinhaCalculadora.OPERECAO = 'SUBTRAÇÃO'
        GUI.ids['input'].text = ''

    def divisao(self):
        MinhaCalculadora.NUMBER_ONE = GUI.ids['input'].text
        GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} /'
        MinhaCalculadora.OPERECAO = 'DIVISAO'
        GUI.ids['input'].text = ''

    def elevacao_por2(self):
        numero = float(GUI.ids['input'].text)**2
        GUI.ids['input'].text = f'{numero}'

    def umSobreX(self):
        numero = 1/float(GUI.ids['input'].text)
        GUI.ids['input'].text = f'{numero}'

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
            try:
                MinhaCalculadora.resultado = float(MinhaCalculadora.NUMBER_ONE) / float(MinhaCalculadora.NUMBER_TWO)
                MinhaCalculadora.NUMBER_ONE = MinhaCalculadora.resultado
                GUI.ids['operacao'].text = f'{MinhaCalculadora.NUMBER_ONE} /'
                GUI.ids['input'].text = f'{MinhaCalculadora.resultado}'
            except:
                GUI.ids['operacao'].text = f'Error'
                GUI.ids['input'].text = f''

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

    def zero(self, numero=None):
        if numero:
            GUI.ids['input'].text += f'{numero}'
        else:
            GUI.ids['input'].text += f'0'

    def ce(self):
        GUI.ids['input'].text = ''

    def c(self):
        MinhaCalculadora.NUMBER_ONE = ''
        MinhaCalculadora.OPERECAO = ''
        GUI.ids['input'].text = ''
        GUI.ids['operacao'].text = ''

    GUI.ids['divisao'].bind(on_press=divisao)
    GUI.ids['multiplicacao'].bind(on_press=multiplicacao)
    GUI.ids['subtracao'].bind(on_press=subtracao)
    GUI.ids['soma'].bind(on_press=soma)
    GUI.ids['resultado'].bind(on_press=resultado)
    GUI.ids['elevacaopor2'].bind(on_press=elevacao_por2)
    GUI.ids['umSobreX'].bind(on_press=umSobreX)
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


c = MinhaCalculadora()


class MyKeyboardListener(Widget):

    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'numpadadd':
            c.soma()
        elif keycode[1] == 'numpadsubstract':
            c.subtracao()
        elif keycode[1] == 'numpadmul':
            c.multiplicacao()
        elif keycode[1] == 'numpaddivide':
            c.divisao()
        elif keycode[1] == 'enter' or keycode[1] == 'numpadenter':
            c.subtracao()
        elif keycode[1] == '1' or keycode[1] == 'numpad1':
            c.um()
        elif keycode[1] == '2' or keycode[1] == 'numpad2':
            c.dois()
        elif keycode[1] == '3' or keycode[1] == 'numpad3':
            c.tres()
        elif keycode[1] == '4' or keycode[1] == 'numpad4':
            c.quatro()
        elif keycode[1] == '5' or keycode[1] == 'numpad5':
            c.cinco()
        elif keycode[1] == '6' or keycode[1] == 'numpad6':
            c.seis()
        elif keycode[1] == '7' or keycode[1] == 'numpad7':
            c.sete()
        elif keycode[1] == '8' or keycode[1] == 'numpad8':
            c.oito()
        elif keycode[1] == '9' or keycode[1] == 'numpad9':
            c.nove()
        elif keycode[1] == '0' or keycode[1] == 'numpad0':
            c.zero()

        return True


if __name__ == '__main__':
    MyKeyboardListener()
    c.run()

