from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Adicione o nome "Genroom" como um rótulo
        genroom_label = Label(
            text='Genroom',
            font_size=36,
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5}
        )

        # Adicione o nome da faculdade como um rótulo
        college_label = Label(
            text='Faculdade Santa-Terezinha-CEST',
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5}
        )

        # Botão para navegar para outra página (substitua com ação real)
        navigate_button = Button(
            text='Navegar para Outra Página',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        navigate_button.bind(on_release=self.navigate_to_other_page)

        # Adicione os widgets à tela
        self.add_widget(genroom_label)
        self.add_widget(college_label)
        self.add_widget(navigate_button)

    def navigate_to_other_page(self, instance):
        # Aqui você pode adicionar a lógica para navegar para outra página
        pass
