from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

class Ex1(App):
    def __init__(self, **kwargs):
        super(Ex1, self).__init__(**kwargs)
        self.operation = ""
    def build(self):
        layout = GridLayout(cols=2)
        self.button = Button(text="Calculer")
        self.button.bind(on_press=self.calculate)
        self.nombre1 = TextInput(multiline=False)
        self.nombre2 = TextInput(multiline=False)
        self.resultat = Label(text="")
        self.checkbox_add = CheckBox()
        self.checkbox_add.bind(active=self.action_checkbox)
        self.checkbox_sub = CheckBox()
        self.checkbox_sub.bind(active=self.action_checkbox)
        self.checkbox_mul = CheckBox()
        self.checkbox_mul.bind(active=self.action_checkbox)
        self.checkbox_div = CheckBox()
        self.checkbox_div.bind(active=self.action_checkbox)
        layout.add_widget(self.button)
        layout.add_widget(self.nombre1)
        layout.add_widget(self.nombre2)
        layout.add_widget(self.resultat)
        layout.add_widget(Label(text="Addition :"))
        layout.add_widget(self.checkbox_add)
        layout.add_widget(Label(text="Soustraction :"))
        layout.add_widget(self.checkbox_sub)
        layout.add_widget(Label(text="Multiplication :"))
        layout.add_widget(self.checkbox_mul)
        layout.add_widget(Label(text="Division :"))
        layout.add_widget(self.checkbox_div)
        return layout

    def action_checkbox(self, checkbox, value):
        if value:
            checkbox.active = True
            for cb in [self.checkbox_add, self.checkbox_sub, self.checkbox_mul, self.checkbox_div]:
                if cb != checkbox:
                    cb.active = False
        else:
            checkbox.active = False
        if self.checkbox_add.active:
            self.operation = "add"
        elif self.checkbox_sub.active:
            self.operation = "sub"
        elif self.checkbox_mul.active:
            self.operation = "mul"
        elif self.checkbox_div.active:
            self.operation = "div"

    def calculate(self, instance):
        try:
            num1 = float(self.nombre1.text)
            num2 = float(self.nombre2.text)
            if self.operation == "add":
                self.resultat.text = str(num1 + num2)
            elif self.operation == "sub":
                self.resultat.text = str(num1 - num2)
            elif self.operation == "mul":
                self.resultat.text = str(num1 * num2)
            elif self.operation == "div":
                if num2 != 0:
                    self.resultat.text = str(num1 / num2)
                else:
                    self.resultat.text = "Erreur : la division par 0 est impossible"
        except ValueError:
            self.resultat.text = "Erreur : Entrez des nombres valides."


if __name__ == "__main__":
    Ex1().run()
