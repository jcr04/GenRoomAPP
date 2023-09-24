from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

# Simulação de chamada à API para atualizar detalhes de uma sala
def update_room_in_database(room_id, data):
    # Aqui você pode chamar a API real para atualizar a sala
    updated_room = {'id': room_id, **data}  # Simulação de sala atualizada
    return updated_room

class UpdateRoomScreen(Screen):
    def __init__(self, room_id, **kwargs):
        super(UpdateRoomScreen, self).__init__(**kwargs)
        self.room_id = room_id

        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)
        
        self.name_input = TextInput(hint_text="Nome da sala", multiline=False)
        self.capacity_input = TextInput(hint_text="Capacidade", multiline=False)
        self.description_input = TextInput(hint_text="Descrição", multiline=False)
        
        layout.add_widget(Label(text="Atualizar sala"))
        layout.add_widget(self.name_input)
        layout.add_widget(self.capacity_input)
        layout.add_widget(self.description_input)

        update_button = Button(text="Atualizar",  size_hint=(0.5, None), size_hint_y=None, height=50, pos_hint={'center_x': 0.5})
        update_button.bind(on_press=self.update_room)
        layout.add_widget(update_button)

        back_button = Button(
            text='Voltar', 
            size_hint=(0.2, None), 
            height=50, 
            font_size=18, 
            bold=True, 
            background_color=(0.8, 0.2, 0.2, 1), 
            color=(1,1,1,1)
        )
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def update_room(self, instance):
        name = self.name_input.text
        capacity = self.capacity_input.text
        description = self.description_input.text

        data = {
            'name': name,
            'capacity': capacity,
            'description': description
        }
        
        updated_room = update_room_in_database(self.room_id, data)
        # Atualizar a interface do usuário ou navegar para uma nova tela, mostrando os detalhes atualizados

    def go_back(self, instance):
        # Switch to previous screen or a specific screen
        self.manager.current = 'create_room'
