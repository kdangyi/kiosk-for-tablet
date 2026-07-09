from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase


# 한글 폰트 등록
LabelBase.register(
    name="Nanum",
    fn_regular="fonts/NanumGothic.ttf"
)


MENU_DATA = [
    {
        "name": "김치찌개",
        "price": "8000원",
        "image": "images/kimchi.jpg"
    },
    {
        "name": "불고기",
        "price": "10000원",
        "image": "images/bulgogi.jpg"
    },
    {
        "name": "라면",
        "price": "5000원",
        "image": "images/noodle.jpg"
    }
]


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(
            cols=2,
            spacing=20,
            padding=20
        )

        for menu in MENU_DATA:

            card = BoxLayout(
                orientation="vertical"
            )

            img = Image(
                source=menu["image"],
                size_hint_y=0.6,
                font_name="Nanum"
            )

            name = Label(
                text=menu["name"],
                font_size=25,
                font_name="Nanum"
            )

            price = Label(
                text=menu["price"],
                font_size=20,
                font_name="Nanum"
            )

            btn = Button(
                text="주문하기",
                size_hint_y=0.3,
                font_name="Nanum"
            )

            card.add_widget(img)
            card.add_widget(name)
            card.add_widget(price)
            card.add_widget(btn)

            layout.add_widget(card)

        self.add_widget(layout)