from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase


# 한글 폰트 등록
LabelBase.register(
    name="Nanum",
    fn_regular="fonts/NanumGothic.ttf"
)


# class KioskApp(App):

#     def build(self):

#         layout = BoxLayout(
#             orientation="vertical",
#             padding=20,
#             spacing=20
#         )

#         title = Label(
#             text="우리 식당 키오스크",
#             font_size=40,
#             font_name="Nanum"
#         )

#         menu_button = Button(
#             text="메뉴 보기",
#             font_size=30,
#             font_name="Nanum"
#         )

#         order_button = Button(
#             text="주문 확인",
#             font_size=30,
#             font_name="Nanum"
#         )

#         layout.add_widget(title)
#         layout.add_widget(menu_button)
#         layout.add_widget(order_button)

#         return layout


# KioskApp().run()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from menu import MenuScreen


class KioskApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(
            MenuScreen(
                name="menu"
            )
        )

        return sm


KioskApp().run()