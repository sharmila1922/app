from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_nav import screen_helper
import pymysql
import re
from kivy.properties import ObjectProperty
from kivymd.toast import toast
from kivy.core.window import Window

conn = pymysql.connect(host="localhost", user="root", password="Sharmi@2020", db="SnowRemovalApp")
cursor = conn.cursor()

Window.size = (450,580)

screen_helper = """
#: import get_color_from_hex kivy.utils.get_color_from_hex

ScreenManager:
    id: sm
    TopPage:
        MDFloatLayout:
            md_bg_color: 43/255, 135/255, 168/255, 1
            Image:
                source: "images/1.png"
                size_hint: .24,.24
                pos_hint: {"center_x":.5, "center_y":.55}
                canvas.before:
                    Color:
                        rgb: 1,1,1,1
        MDLabel:
            text: "SNOW REMOVAL"
            pos_hint: {"center_x":.7, "center_y":.4}
            haling: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_size: "38sp"
            font_name: "Comic"
        MDRoundFlatButton:
            text: "HOME"
            pos_hint: {"center_x":.5, "center_y":.3}
            font_size: 20
            md_bg_color: 0, 0, 0, 1
            on_press: app.root.current='menu'
    MenuScreen:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    CustomerRegistration:
        id: customerreg
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ServiceProviderReg:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
<MenuScreen>
    name: 'menu'
    MDBottomNavigation:
        md_bg_color: 43/255, 135/255, 168/255, 1
        MDBottomNavigationItem:
            name: "screen1"
            text: "Home"
            color:  1, 0, 0, 0.9
            font_name: "Comic"
            font_size: 20
            MDLabel:
                text: "Welcome to Snow Removal App"
                font_name: "Comic"
                font_size: 40
                halign: "center"
        MDBottomNavigationItem:
            name: "screen2"
            text: "Admin"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "ADMIN LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                MDTextField:
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                Widget:
                    size_hint_y: None
                    height: 30
        MDBottomNavigationItem:
            name: "screen3"
            text: "Service"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "SERVICE PROVIDER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='serviceproviderreg'
                Widget:
                    size_hint_y: None
                    height: 15
        MDBottomNavigationItem:
            name: "screen4"
            text: "Customer"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "CUSTOMER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id: email
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    id: password
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_release: app.receive_data(email,password)
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='customerreg'
                Widget:
                    size_hint_y: None
                    height: 15
<CustomerRegistration>
    name: 'customerreg'
    MDCard:
        size_hint: None,None
        size: 600,650
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 10
        spacing: 10
        orientation: "vertical"
        MDLabel:
            text: "Customer Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        MDTextField:
            id: name
            hint_text: "Name"
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        MDTextField:
            id: email
            mode: "round"
            hint_text: "Email"
            font_name: "Comic"
            icon_right: "email"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDTextField:
            id: phone
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "phone"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDTextField:
            id: password
            mode: "round"
            hint_text: "Password"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        MDTextField:
            id: address
            mode: "round"
            hint_text: "Address"
            font_name: "Comic"
            icon_right: "address"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDTextField:
            id: longitude
            mode: "round"
            hint_text: "Longitude"
            font_name: "Comic"
            icon_right: "longitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDTextField:
            id: latitude
            mode: "round"
            hint_text: "Latitude"
            font_name: "Comic"
            icon_right: "latitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_release: root.send_data()
        Widget:
            size_hint_y: None
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Customer Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'

<ServiceProviderReg>
    name: 'serviceproviderreg'
    MDCard:
        size_hint: None,None
        size: 500,600
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 5
        spacing: 3
        orientation: "vertical"
        MDLabel:
            text: "Service Provider Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        MDTextField:
            id: name
            hint_text: "Name"
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        MDTextField:
            id: email
            mode: "round"
            hint_text: "Email"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDTextField:
            mode: "round"
            hint_text: "Password"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        MDTextField:
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDTextField:
            mode: "round"
            hint_text: "Address"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDTextField:
            mode: "round"
            hint_text: "Profile Picture"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDTextField:
            mode: "round"
            hint_text: "Lic ense"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDTextField:
            mode: "round"
            hint_text: "ID Proof"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            spacing: 3
            font_size: 20
        Widget:
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Service Provider Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'
<UploadFileService>:
    name: 'uploadservice'
"""


class TopPage(Screen):
    pass

class MenuScreen(Screen):
    pass

class CustomerRegistration(Screen):
    pass

class ServiceProviderReg(Screen):
    pass


sm = ScreenManager()
sm.add_widget(TopPage(name="toppage"))
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(CustomerRegistration(name="customerreg"))
sm.add_widget(ServiceProviderReg(name="serviceproviderreg"))



class MainApp(MDApp):
    sm = ObjectProperty(None)

    def send_data(self):
        app = App.get_running_app()
        name = app.sm.CustomerRegistration('customerreg').ids['name'].text
        email = app.sm.CustomerRegistration('customerreg').ids['email'].text
        phone = app.sm.CustomerRegistration('customerreg').ids['phone'].text
        password = app.sm.CustomerRegistration('customerreg').ids['password'].text
        address = app.sm.CustomerRegistration('customerreg').ids['address'].text
        longitude = app.sm.CustomerRegistration('customerreg').ids['longitude'].text
        latitude = app.sm.CustomerRegistration('customerreg').ids['latitude'].text

        cursor.execute("insert into customer(name,email,phone,password,address,longitude,latitude) values('" + str(
            name) + "' , '" + str(email) + "' , '" + str(phone) + "' , '" + str(password) + "' , '" + str(
            address) + "' , '" + str(longitude) + "' , '" + str(latitude) + "')")
        conn.commit()
        toast("Registration Successfull")

    def __init__(self, **kwargs):
        self.title = "Snow Removal App"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(screen_helper)


if __name__ == "__main__":
    MainApp().run()