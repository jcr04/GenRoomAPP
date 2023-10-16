from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

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

class DeleteRoomScreen(Screen):
    def __init__(self, **kwargs):
        super(DeleteRoomScreen, self).__init__(**kwargs)
  
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
        main_layout = self._create_main_layout()
        self.add_widget(main_layout)

    def _create_background(self):
        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)

    def _create_main_layout(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=60)

        # Title Bar

        # Details area
        self.details_label = Label(text='', font_size=18, color=(0, 0, 0, 1), halign='left', valign='top', size_hint_y=None, height=150)
        self.details_label.bind(size=self.details_label.setter('text_size'))
        main_layout.add_widget(self.details_label)

        # Dropdown and button setup
        self._setup_dropdown_and_buttons(main_layout)
        self._setup_button(main_layout)

        return main_layout

    def _setup_dropdown_and_buttons(self, main_layout):
        # Dropdown setup
        self.room_dropdown = DropDown()
        mock_rooms = [{'name': 'Sala 11'}, {'name': 'Sala 12'}, {'name': 'Laboratório 1'}]
        for room in mock_rooms:
            room_btn = RoomItem(room_info=room, callback=self.update_details, size_hint_y=None, height=60)
            self.room_dropdown.add_widget(room_btn)

        main_button = Button(text='Selecione uma Sala',  size_hint=(0.5, None), height=50, pos_hint={'center_x': 0.5}, font_size=18, bold=True, background_color=(0.129, 0.588, 0.953, 1), color=(1, 1, 1, 1))
        main_button.bind(on_release=self.room_dropdown.open)
        main_layout.add_widget(main_button)
        
               
    def _setup_button(self, main_layout):

        # Adicione o botão "Deletar" depois de definir back_button_layout
        delete_button = Button(
            text='Deletar',
            size_hint=(0.5, None),
            height=60,
            font_size=18,
            bold=True,
            background_color=(0.2, 0.8, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        # Back button setup
        back_button_layout = BoxLayout(orientation='horizontal', spacing=200, size_hint=(0.6, 0.6), pos_hint={'center_y': 0.5})

        back_button = Button(
            text='Voltar',
            size_hint=(0.5, None),
            height=50,
            font_size=18,
            bold=True,
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_release=self.navigate_to_menu)
        back_button_layout.add_widget(delete_button)
        back_button_layout.add_widget(back_button)
        
        main_layout.add_widget(back_button_layout)

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


    def navigate_to_menu(self, instance):
        self.manager.current = 'menu'

