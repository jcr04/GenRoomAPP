from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.menu_screen import MenuScreen
from screens.delete_room_screen import DeleteRoomScreen
from screens.list_rooms_screen import ListRoomsScreen
from screens.update_room_screen import UpdateRoomScreen
from screens.create_room_screen import CreateRoomScreen
from screens.home_screen import HomeScreen

class GenroomApp(App):
    def build(self):
        # Crie o gerenciador de telas
        sm = ScreenManager()

        # Adicione as telas ao gerenciador de telas
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CreateRoomScreen(name='create_room'))
        sm.add_widget(ListRoomsScreen(name='list'))
        sm.add_widget(UpdateRoomScreen(room_id='some_room_id', name='update_room'))
        sm.add_widget(DeleteRoomScreen(name='delete', room_id=123))

        # Defina a tela inicial como HomeScreen
        sm.current = 'home'
        
        return sm


if __name__ == '__main__':
    GenroomApp().run()
