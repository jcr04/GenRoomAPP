from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import requests


class UpdateRoomScreen(Screen):
    def __init__(self, room_id, **kwargs):
        super(UpdateRoomScreen, self).__init__(**kwargs)
        self.room_id = room_id
        self.create_ui_elements()

    def create_ui_elements(self):
        layout = self._create_layout()
        self._set_background()
        self.add_widget(layout)

    def _create_layout(self):
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

    # Criar o Dropdown antes de vinculá-lo ao botão
        self.room_dropdown = DropDown(auto_dismiss=False)
        self.populate_room_dropdown()

    # Criar um layout superior para acomodar o título e o botão de seleção de sala
        top_layout = BoxLayout(orientation='horizontal', spacing=10)
        top_layout.add_widget(Label(text="Atualizar sala", size_hint_x=None, width=150))

    # Botão de seleção de sala
        select_button = Button(text='Selecione uma Sala', size_hint=(None, None), height=50)
        select_button.bind(on_release=self.room_dropdown.open)
        top_layout.add_widget(select_button)

        layout.add_widget(top_layout)  # Adiciona o top_layout ao layout principal

    # Inicializando os TextInput
        self.name_input = TextInput(hint_text="Nome da sala", multiline=False)
        self.capacity_input = TextInput(hint_text="Capacidade", multiline=False)
        self.description_input = TextInput(hint_text="Descrição", multiline=False)

    # Adicionando os demais widgets ao layout principal
        layout.add_widget(self.name_input)
        layout.add_widget(self.capacity_input)
        layout.add_widget(self.description_input)
        layout.add_widget(self._create_update_button())
        layout.add_widget(self._create_back_button())

        return layout

    
    def _set_background(self):
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)

    def _create_update_button(self):
        button = Button(text="Atualizar", size_hint=(0.5, None), height=50, pos_hint={'center_x': 0.5})
        button.bind(on_press=self.update_room)
        return button
    
    def _create_back_button(self):
        button = Button(text='Voltar', size_hint=(0.2, None), height=50, font_size=18, bold=True, background_color=(0.8, 0.2, 0.2, 1), color=(1, 1, 1, 1))
        button.bind(on_release=self.navigate_to_menu)
        return button
    
    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size
        
    def populate_room_dropdown(self):
        rooms_url = 'http://127.0.0.1:5001/api/rooms'
        response = requests.get(rooms_url)

        if response.status_code == 200:
            rooms = response.json()
        for room in rooms:
            btn = Button(text=str(room['id']), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.on_room_select(btn.text))
            self.room_dropdown.add_widget(btn)
        else:
            print(f'Error fetching rooms: {response.status_code}')

    def on_room_select(self, room_id):
        self.room_id = room_id
        self.room_dropdown.dismiss()
        print(f'Selected Room ID: {self.room_id}')


    def update_room(self, instance):
        url = f'http://127.0.0.1:5001/api/rooms/{self.room_id}/update'
        
        data = {
            'name': self.name_input.text,
            'capacity': self.capacity_input.text,
            'description': self.description_input.text
        }
        
        if not all(data.values()):
            print('Error: All fields are required!')
            return

        response = requests.put(url, json=data)

        if response.status_code == 200:
            print('Room updated successfully')
        else:
            error_message = response.text or f'Unable to update room - {response.status_code}'
            print(f'Error: {error_message}')

    def navigate_to_menu(self, instance):
        self.manager.current = 'menu'
