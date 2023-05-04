from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Tarefas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Adicione uma tarefa:"))
        self.tarefa = TextInput(multiline=False)
        self.add_widget(self.tarefa)
        self.add_widget(Button(text="Adicionar", on_press=self.adicionar_tarefa))
        self.lista = Label(text="")
        self.add_widget(self.lista)

    def adicionar_tarefa(self, instancia):
        self.lista.text += self.tarefa.text + "\n"
        self.tarefa.text = ""

class TarefasApp(App):
    def build(self):
        return Tarefas()

if __name__ == "__main__":
    TarefasApp().run()
