from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)
            
        # continuação da tela azul
        self.bind(size=self.update_background)
        
        #imagem - logo
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(400, 300), spacing=10, pos_hint={'center_x': 0.5})
        image = Image(source='screens\Logo.png')
        layout.add_widget(image)
        
        # imagem no centro em cima
        image_center = Image(source='screens/Logo.png', size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5, 'top': 0.9})
        self.add_widget(image_center)
                
    # janela ajustavel
    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size
        
        # Adicione o nome "Genroom" como um rótulo
        genroom_label = Label(
            text='Genroom',
            font_size=36,
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'top': 0.8}
        )

        # Caixas de entrada de usuário e senha
        user_input = TextInput(
            hint_text='Usuário',
            size_hint=(None, None),
            size=(336, 50),
            pos_hint={'top': 0.6, 'center_x': 0.5}
        )

        password_input = TextInput(
            hint_text='Senha',
            password=True,
            size_hint=(None, None),
            size=(336, 50),
            pos_hint={'top': 0.5, 'center_x': 0.5}
        )

        # Botão de login
        menu_button = Button(
            text='Entrar',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'top': 0.4, 'center_x': 0.5}
        )
        menu_button.bind(on_release=self.navigate_to_menu)

        # Adicione os widgets à tela
        self.add_widget(genroom_label)
        self.add_widget(user_input)
        self.add_widget(password_input)
        self.add_widget(menu_button)

    def navigate_to_menu(self, instance):
        self.manager.current = 'menu'  # 'menu' é o nome da tela do menu
        