from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
          
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # Blue color
            self.background = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(size=self.update_background)
        
        layout_button = BoxLayout(orientation='vertical', padding=20, spacing=10)
   
        title_label = Label(text='Menu', font_size=20, size_hint_y=None, height=30, bold=True, color=(0.9, 0.9, 0.9, 1))
        layout_button.add_widget(title_label)  
        
        button_layout = BoxLayout(orientation='vertical', spacing=10)
        buttons_text = ['Criar', 'Editar', 'Ver', 'Deletar']
        functions = [self.create_room, self.edith_room, self.view_room, self.delete_room]
        
        for i in range(4):
            button = Button(text=buttons_text[i], size_hint=(0.5, None), height=60, pos_hint={'center_x': 0.5})
            button.bind(on_press=functions[i])
            button_layout.add_widget(button)
        
        layout_button.add_widget(button_layout)
        self.add_widget(layout_button)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size
    
    def create_room(self, instance):
        # Ajuste a lógica aqui
        self.manager.current = 'create_room'
    
    def view_room(self, instance):
        # Ajuste a lógica aqui
        self.manager.current = 'list'
    
    def edith_room(self, instance):
        # Ajuste a lógica aqui
        self.manager.current = 'update_room'
        
    def delete_room(self, instance):
        self.manager.current = 'delete'
        pass


