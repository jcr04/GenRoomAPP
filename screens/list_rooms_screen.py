# list_rooms_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.dropdown import DropDown
import requests


class RoomItem(Button):
    def __init__(self, room_info, callback, **kwargs):
        super().__init__(**kwargs)
        self.room_info = room_info
        self.text = room_info.get('name', 'Unknown')
        self.callback = callback
        self.bind(on_release=self.show_details)

    def show_details(self, instance):
        self.callback(self.room_info)


class ListRoomsScreen(Screen):
    def __init__(self, **kwargs):
        super(ListRoomsScreen, self).__init__(**kwargs)
        self.create_ui_elements()

    def create_ui_elements(self):
        # Create and style UI elements here
        self._create_background()
        layout = self._create_layout()
        self.add_widget(layout)

    def _create_background(self):
        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)


    def _create_layout(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=(50, 20), spacing=20, size_hint=(0.4, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Styling the layout
        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.box_rect = Rectangle(pos=layout.pos, size=layout.size)
            Color(0.2, 0.2, 0.2, 1)
            self.box_line = Line(rectangle=(layout.x, layout.y, layout.width, layout.height), width=1.5)
        layout.bind(pos=self.update_box, size=self.update_box)

        # Title Bar
        title_label = Label(text='Listagem de Salas', font_size=20, size_hint_y=None, height=50, bold=True, color=(0.129, 0.588, 0.953, 1))
        layout.add_widget(title_label)

        # Details area
        self.details_label = Label(text='', font_size=18, color=(0, 0, 0, 1), halign='left', valign='top', size_hint_y=None, height=150)
        self.details_label.bind(size=self.details_label.setter('text_size'))
        layout.add_widget(self.details_label)

        # Dropdown and button setup
        self._setup_dropdown_and_buttons(layout)

        return layout

    def _setup_dropdown_and_buttons(self, layout):
        # Dropdown setup
        self.room_dropdown = DropDown()

        response = requests.get('http://127.0.0.1:5001/api/rooms')
        if response.status_code == 200:
            rooms = response.json()
            for room in rooms:
                room_btn = RoomItem(room_info=room, callback=self.update_details, size_hint_y=None, height=60)
                self.room_dropdown.add_widget(room_btn)
        else:
            # Adicionar código para lidar com erro ao buscar salas
            print(f"Error fetching rooms: {response.status_code}")

        main_button = Button(text='Selecione uma Sala', size_hint=(None, None), height=70, font_size=20, bold=True, background_color=(0.129, 0.588, 0.953, 1), color=(1, 1, 1, 1))
        main_button.bind(on_release=self.room_dropdown.open)
        layout.add_widget(main_button)

        # Back button setup
        back_button = Button(
            text='Voltar',
            size_hint=(None, None),
            height=50,
            font_size=16,
            bold=True,
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_release=self.navigate_to_menu)
        layout.add_widget(back_button)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def update_details(self, room_details):
        if room_details:
            details = (
                f"Nome: {room_details['name']}\n"
                f"Capacidade: {room_details['capacity']}\n"
                f"Descrição: {room_details['description']}"
            )
            self.details_label.text = details

    def update_box(self, instance, value):
        self.box_rect.pos = (instance.x - 10, instance.y - 10)  # Ajuste as coordenadas de posição
        self.box_rect.size = self.box_rect.size = (instance.width + 50, instance.height + 80)  # Ajuste as dimensões
        self.box_line.rectangle = (instance.x - 10, instance.y - 10, instance.width + 50, instance.height + 80)

    def navigate_to_menu(self, instance):
        self.manager.current = 'menu'
