from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '500')

GUI = Builder.load_file('tela.kv')


class MinhaCalculadora(App):
    def build(self):
        return GUI

    def teste(self):
        self.root.ids['operacao'].text += 'X'

    def on_start(self):
        self.root.ids['x'].on_press = self.teste


MinhaCalculadora().run()
