from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

def b1_press(*args,**kwargs):
    print("b1")

def b2_press(*args,**kwargs):
    print("b2")


class BackButton (Button):
    def __init__ (self,*args , **kwargs):
        super().__init__(text = kwargs["text"])
        self.manager=kwargs["manager"]

    def on_press_START(self,*args,**kwargs):
        print("b1")
        self.manager.current="settings"
    def on_press_settings(self,*args,**kwargs):
        print("b2")
        self.manager.current="finish"
    def on_press_finish(self,*args,**kwargs):
        print("b8")
        self.manager.current="start"


class MyApp(App):
    def build(self):
        #b1 = Button(text="main")
        #b1.on_press = b1_press
        #b2 = Button(text="sattings")
        #b2.bind(on_press=b2_press)
        
        #l = BoxLayout(padding=8)
        #l.add_widget(b1)
        #l.add_widget(b2)

        self.manager = ScreenManager()
        #b1 = BackButton(text="start",manager=self.manager)
        b2 = BackButton(text="settings",manager=self.manager)
        b8 = BackButton(text="finish",manager=self.manager)

        
        
        s1=Screen(name="start")
        s2=Screen(name="settings")
        s3=Screen(name="1")
        s4=Screen(name="1")
        s5=Screen(name="1")
        s6=Screen(name="1")
        s7=Screen(name="1")
        s8=Screen(name="finish")

        b1=Button(text="start")
        b1.bind(on_press = b2.on_press_START())

        s1.add_widget(b1)
        s2.add_widget(b2)
        s8.add_widget(b8)

        self.manager.add_widget(s1)
        self.manager.add_widget(s2)
        self.manager.add_widget(s8)
        self.manager.current = "start"

        


        return self.manager

app = MyApp()
app.run()