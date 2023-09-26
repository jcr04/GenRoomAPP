from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Fundo azul
        with self.canvas:
            Color(0.129, 0.588, 0.953, 1)  # Cor azul
            self.background = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=self.update_background)
        
        layout_button = BoxLayout(orientation='vertical', padding=20, spacing=10)
   
            # Title Bar
        title_label = Label(text='Menu', font_size=20, size_hint_y=None, height=30, bold=True, color=(0.9, 0.9, 0.9, 1))
        layout_button.add_widget(title_label)  
                   
        # Botão para criar
        create_button = Button(text="Criar", size_hint=(0.5, None), height=60, pos_hint={'center_x': 0.5})
        create_button.bind(on_press=self.create_room)
        
        # Botão para editar
        edith_button = Button(text="Editar", size_hint=(0.5, None), height=60, pos_hint={'center_x': 0.5})
        edith_button.bind(on_press=self.edith_room)
        
        # Botão para ver
        view_button = Button(text="Ver", size_hint=(0.5, None), height=60, pos_hint={'center_x': 0.5})
        view_button.bind(on_press=self.view_room)
        
        # Botão para deletar
        delete_button = Button(text="Deletar", size_hint=(0.5, None), height=60, pos_hint={'center_x': 0.5})
        delete_button.bind(on_press=self.delete_room)
        
        # Adicione os botões ao layout    
        self.add_widget(layout_button)
        self.add_widget(create_button)
        self.add_widget(edith_button)
        self.add_widget(view_button)
        self.add_widget(delete_button) 
        
    # janela ajustavel
    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size    
    
    def create_room(self, instance):
        name = self.name_input.text
        room_type = self.room_type_button.text
        capacity = int(self.capacity_input.text)
        description = self.description_input.text
        room_category = self.category_button.text
        shift = self.shift_button.text
        self.manager.current = 'create_room'
        
    def view_room(self, instance):
        name = self.name_input.text
        room_type = self.room_type_button.text
        capacity = self.capacity_input.text
        description = self.description_input.text
        category = self.category_button.text
        shift = self.shift_button.text
        self.manager.current = 'list'   
        
    def edith_room(self, instance):
        name = self.name_input.text
        room_type = self.room_type_button.text
        capacity = self.capacity_input.text
        description = self.description_input.text
        category = self.category_button.text
        shift = self.shift_button.text
        self.manager.current = 'update_room'
        
    def delete_room(self, instance):
        name = self.name_input.text
        room_type = self.room_type_button.text
        capacity = self.capacity_input.text
        description = self.description_input.text
        category = self.category_button.text
        shift = self.shift_button.text

