# list_rooms_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.dropdown import DropDown


# Simulação de chamada à API para obter detalhes de uma sala.
def get_room_details(room_name):
    rooms_database = {
        'Sala 11': {
            'name': 'Sala 11',
            'capacity': 30,
            'equipments': ['Projetor', 'Ar-condicionado'],
            'description': 'Uma sala para reuniões e apresentações.'
        },
        'Sala 12': {
            'name': 'Sala 12',
            'capacity': 20,
            'equipments': ['Projetor'],
            'description': 'Sala para pequenas reuniões.'
        },
        'Laboratório 1': {
            'name': 'Laboratório 1',
            'capacity': 25,
            'equipments': ['Computadores', 'Ar-condicionado', 'Projetor'],
            'description': 'Laboratório para aulas práticas.'
        }
    }
    return rooms_database.get(room_name, None)


class RoomItem(Button):
    def __init__(self, room_info, callback, **kwargs):
        super().__init__(**kwargs)
        self.room_info = room_info
        self.text = room_info.get('name', 'Unknown')
        self.callback = callback
        self.bind(on_release=self.show_details)

    def show_details(self, instance):
        room_details = get_room_details(self.text)
        self.callback(room_details)


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
        mock_rooms = [{'name': 'Sala 11'}, {'name': 'Sala 12'}, {'name': 'Laboratório 1'}]
        for room in mock_rooms:
            room_btn = RoomItem(room_info=room, callback=self.update_details, size_hint_y=None, height=60)
            self.room_dropdown.add_widget(room_btn)

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
        back_button.bind(on_release=self.go_back_to_create_room)
        layout.add_widget(back_button)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def update_details(self, room_details):
        if room_details:
            details = (
                f"Nome: {room_details['name']}\n"
                f"Capacidade: {room_details['capacity']}\n"
                f"Equipamentos: {', '.join(room_details['equipments'])}\n"
                f"Descrição: {room_details['description']}"
            )
            self.details_label.text = details

    def update_box(self, instance, value):
        self.box_rect.pos = instance.pos
        self.box_rect.size = instance.size
        self.box_line.rectangle = (instance.x, instance.y, instance.width, instance.height)

    def go_back_to_create_room(self, instance):
        # Switch to "create_room" screen
        self.manager.current = 'create_room'
