from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import smtplib

class TarefasApp(App):
    def enviar_email(self, assunto, mensagem, destinatario):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.login("gustavo.roldam@gmail.com", "roldam2004")
            message = 'Subject: {}\n\n{}'.format(assunto, mensagem)
            server.sendmail("roldam2004@gmail.com", destinatario, message)
            server.quit()
            print("Email enviado com sucesso!")
        except:
            print("Ocorreu um erro ao enviar o email.")

    def add_tarefa(self, task, horario, destinatario):
        self.tarefas.append({'task': task, 'horario': horario, 'destinatario': destinatario})
        self.enviar_email("Lembrete de Tarefa", task + " está agendada para as " + horario, destinatario)

    def build(self):
        self.tarefas = []

        layout = GridLayout(cols=2)

        task_label = Label(text="Tarefa:")
        horario_label = Label(text="Horário:")
        destinatario_label = Label(text="Destinatário:")

        self.task_input = TextInput(multiline=False)
        self.horario_input = TextInput(multiline=False)
        self.destinatario_input = TextInput(multiline=False)

        add_button = Button(text="Adicionar Tarefa")
        add_button.bind(on_press=lambda x: self.add_tarefa(self.task_input.text, self.horario_input.text, self.destinatario_input.text))

        layout.add_widget(task_label)
        layout.add_widget(self.task_input)
        layout.add_widget(horario_label)
        layout.add_widget(self.horario_input)
        layout.add_widget(destinatario_label)
        layout.add_widget(self.destinatario_input)
        layout.add_widget(add_button)

        return layout

if __name__ == "_main_":
    TarefasApp().run()