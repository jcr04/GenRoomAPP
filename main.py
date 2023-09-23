from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.list_rooms_screen import ListRoomsScreen
from screens.update_room_screen import UpdateRoomScreen
from screens.create_room_screen import CreateRoomScreen
from screens.home_screen import HomeScreen

class GenroomApp(App):
    def build(self):
        # Crie o gerenciador de telas
        sm = ScreenManager()

        # Adicione a tela inicial (Home) ao gerenciador de telas
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CreateRoomScreen(name='create_room'))
        sm.add_widget(ListRoomsScreen(name='list'))
        sm.add_widget(UpdateRoomScreen(room_id='some_room_id', name='update_room'))
        return sm

if __name__ == '__main__':
    GenroomApp().run()
