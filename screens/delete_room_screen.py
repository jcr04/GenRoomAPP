from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Simulação de chamada à API para obter detalhes de uma sala.

class DeleteRoomScreen(Screen):
    
    def __init__(self, room_id, **kwargs):
        super(DeleteRoomScreen, self).__init__(**kwargs)
        self.room_id = room_id
        room_id = 123  # substituia pelo id da sala
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # 
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)
        
        ##
        # A de fazer uma mudança
        select_button = Button(
            text="Selecione uma Sala",
            size_hint=(0.5, None),
            size=(100, 50),
            background_color=(0.129, 0.588, 0.953, 1),
            color=(1, 1, 1, 1),
            pos_hint={'top': 3.0, 'left': 1.0}
        )
        layout.add_widget(select_button)
        ##
        
        label = Label(text="")
        layout.add_widget(label)

        delete_button = Button(text="Deletar", size_hint=(0.5, None), background_color=(0.2, 0.8, 0.2, 1), size_hint_y=None, height=50, pos_hint={'center_x': 0.5})
        delete_button.bind(on_press=self.delete_room)
        layout.add_widget(delete_button)
    
        back_button = Button(
            text='Voltar', 
            size_hint=(0.2, None), 
            height=50, 
            font_size=18, 
            bold=True, 
            background_color=(0.8, 0.2, 0.2, 1),  # Cor azul
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_release=self.navigate_to_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)       

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def delete_room(self, instance):
        # Implementar a lógica para deletar a sala com base no self.room_id
        # chamada à API 
        # Após deletar, você pode atualizar a interface do usuário ou navegar para uma nova tela
        updated_room = DeleteRoomScreen(self.room_id)
        pass
    
    def navigate_to_menu(self, instance):
        self.manager.current='menu'
        