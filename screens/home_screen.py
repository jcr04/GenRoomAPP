from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Fundo azul
        with self.canvas.before:
            Color(0.129, 0.588, 0.953, 1)  # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)

        # Adicione o nome "Genroom" como um rótulo
        genroom_label = Label(
            text='Genroom',
            font_size=36,
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5}
        )

        # Adicione o nome da faculdade como um rótulo
        college_label = Label(
            text='Faculdade Santa-Terezinha-CEST',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5}
        )

        # Caixas de entrada de usuário e senha
        user_input = TextInput(
            hint_text='Usuário',
            size_hint=(None, None),
            size=(336, 50),
            pos_hint={'top': 0.8, 'center_x': 0.5}
        )

        password_input = TextInput(
            hint_text='Senha',
            password=True,
            size_hint=(None, None),
            size=(336, 50),
            pos_hint={'top': 0.7, 'center_x': 0.5}
        )

        # Botão de login
        login_button = Button(
            text='Entrar',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'top': 0.6, 'center_x': 0.5}
        )
        login_button.bind(on_release=self.navigate_to_other_page)

        # Adicione os widgets à tela
        self.add_widget(genroom_label)
        self.add_widget(college_label)
        self.add_widget(user_input)
        self.add_widget(password_input)
        self.add_widget(login_button)

    def navigate_to_other_page(self, instance):
        self.manager.current = 'outra_tela'  # 'outra_tela' é o nome da próxima tela

