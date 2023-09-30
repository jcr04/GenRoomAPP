from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
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
        
        self.name_input = TextInput(hint_text="Nome da sala", multiline=False)
        self.capacity_input = TextInput(hint_text="Capacidade", multiline=False)
        self.description_input = TextInput(hint_text="Descrição", multiline=False)
        
        elements = [
            Label(text="Atualizar sala"),
            self.name_input,
            self.capacity_input,
            self.description_input,
            self._create_update_button(),
            self._create_back_button()
        ]
        
        for element in elements:
            layout.add_widget(element)
        
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
