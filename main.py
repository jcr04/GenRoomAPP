from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen

class GenroomApp(App):
    def build(self):
        # Crie o gerenciador de telas
        sm = ScreenManager()

        # Adicione a tela inicial (Home) ao gerenciador de telas
        sm.add_widget(HomeScreen(name='home'))

        return sm

if __name__ == '__main__':
    GenroomApp().run()
