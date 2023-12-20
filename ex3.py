from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=5, rows=5)
        for i in range(25):
            btn = Button(background_color='white')
            btn.bind(on_press=self.change_color)
            layout.add_widget(btn)
        return layout

    def change_color(self, instance):
        if instance.background_color == [1, 1, 1, 1]:
            instance.background_color = [0, 1, 1, 1]
        else:
            instance.background_color = [1, 1, 1, 1]


if __name__ == '__main__':
    MyApp().run()
