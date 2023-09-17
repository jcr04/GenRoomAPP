from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class CreateRoomScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateRoomScreen, self).__init__(**kwargs)

        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.update_background)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Nome da sala
        self.name_input = TextInput(hint_text='Nome da sala', size_hint_y=None, height=44)

        # Tipo de sala - usando um DropDown para seleção
        self.room_type_dropdown = DropDown()
        for room_type in ['Sala-Aula', 'Laboratório', 'Auditório']: # Adicione mais tipos conforme necessário
            btn = Button(text=room_type, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.room_type_dropdown.select(btn.text))
            self.room_type_dropdown.add_widget(btn)
        self.room_type_button = Button(text='Tipo de Sala', size_hint_y=None, height=44)
        self.room_type_button.bind(on_release=self.room_type_dropdown.open)
        self.room_type_dropdown.bind(on_select=lambda instance, x: setattr(self.room_type_button, 'text', x))

        # Capacidade
        self.capacity_input = TextInput(hint_text='Capacidade', size_hint_y=None, height=44)

        # Descrição
        self.description_input = TextInput(hint_text='Descrição', size_hint_y=None, height=88)

        # Categoria da sala - usando um DropDown para seleção
        self.category_dropdown = DropDown()
        for category in ['Salas de aulas', 'Laboratórios', 'Auditórios']: # Adicione mais categorias conforme necessário
            btn = Button(text=category, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.category_dropdown.select(btn.text))
            self.category_dropdown.add_widget(btn)
        self.category_button = Button(text='Categoria da Sala', size_hint_y=None, height=44)
        self.category_button.bind(on_release=self.category_dropdown.open)
        self.category_dropdown.bind(on_select=lambda instance, x: setattr(self.category_button, 'text', x))

        # Turno - usando um DropDown para seleção
        self.shift_dropdown = DropDown()
        for shift in ['Matutino', 'Vespertino', 'Noturno']:
            btn = Button(text=shift, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.shift_dropdown.select(btn.text))
            self.shift_dropdown.add_widget(btn)
        self.shift_button = Button(text='Turno', size_hint_y=None, height=44)
        self.shift_button.bind(on_release=self.shift_dropdown.open)
        self.shift_dropdown.bind(on_select=lambda instance, x: setattr(self.shift_button, 'text', x))

        # Botão para criar a sala
        create_button = Button(text="Criar Sala", size_hint_y=None, height=50)
        create_button.bind(on_release=self.create_room)

        layout.add_widget(self.name_input)
        layout.add_widget(self.room_type_button)
        layout.add_widget(self.capacity_input)
        layout.add_widget(self.description_input)
        layout.add_widget(self.category_button)
        layout.add_widget(self.shift_button)
        layout.add_widget(create_button)

        self.add_widget(layout)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def create_room(self, instance):
        # Aqui, você irá interagir com sua API para criar uma sala com os detalhes fornecidos
        # por exemplo: chamando a função que cria a sala no Genroom.py
        # Usando os inputs fornecidos pelo usuário, ex:
        name = self.name_input.text
        room_type = self.room_type_button.text
        capacity = int(self.capacity_input.text) # Convertendo para int
        description = self.description_input.text
        room_category = self.category_button.text
        shift = self.shift_button.text
        
        # Se conectar com a API e enviar os dados aqui.
        pass
