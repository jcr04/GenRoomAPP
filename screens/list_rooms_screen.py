# list_rooms_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown

class RoomItem(Button):
    def __init__(self, room_info, **kwargs):
        super().__init__(**kwargs)
        self.room_info = room_info
        self.text = room_info.get('name', 'Unknown')
        # Você pode adicionar mais detalhes da sala aqui se necessário

class ListRoomsScreen(Screen):
    def __init__(self, **kwargs):
        super(ListRoomsScreen, self).__init__(**kwargs)
        
        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1) # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # DropDown para listar as salas
        self.room_dropdown = DropDown()
        # Você pode preencher este dropdown com dados da sua API quando a tela for carregada
        # Aqui é apenas um exemplo mockup
        mock_rooms = [{'name': 'Sala A'}, {'name': 'Sala B'}, {'name': 'Laboratório 1'}]
        for room in mock_rooms:
            room_btn = RoomItem(room_info=room, size_hint_y=None, height=44)
            self.room_dropdown.add_widget(room_btn)
        
        main_button = Button(text='Selecione uma Sala', size_hint=(None, None))
        main_button.bind(on_release=self.room_dropdown.open)
        layout.add_widget(main_button)

        self.add_widget(layout)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    # Adicione métodos para carregar os dados da sala da sua API e preencher o dropdown aqui
    # Por exemplo:
    # def load_rooms_from_api(self):
    #     rooms = api_call_to_get_rooms() 
    #     for room in rooms:
    #         room_btn = RoomItem(room_info=room, size_hint_y=None, height=44)
    #         self.room_dropdown.add_widget(room_btn)
