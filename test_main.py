# TODO: ПРИМЕР №1
"""ДЛЯ ТЕКСТА from kivy.uix.label import Label"""
# from kivy.app import App
# from kivy.uix.label import Label
#
#
# # TODO: ПОНАДОБТСЯ UI КОД
# class MainApp(App):  # создаем подкласс App
#     def build(self):  # создаем метод build и переорпределяем его
#         label = Label(text='Привет!!!!',  # Создаем виджед Label и передаем size и pos hint
#                       size_hint=(.5, .5),
#                       # говорит Kivy о размерах что нужно использовать при создании виджета. Первое число x указывает на размер ширины элемента управления.
#                       # Второе число y указывает на размер высоты элемента управления.
#                       # Значеня обоих чисел должно быть в промежутке от 1 до 0
#                       pos_hint={'center_x': .5, 'center_y': .5})
#         return label
#
#
# if __name__ == '__main__':
#     # Для запуска приложения нужно инициализировать класс MainApp и вызвать метод run().
#     app = MainApp()
#     app.run()

# TODO: ПРИМЕР №2
# """ДЛЯ ИЗОБРАЖЕНИЯ from kivy.uix.image import Image"""
# from kivy.app import App
# from kivy.uix.image import Image
#
# # TODO: ИСПРАВИТЬ ОШИБКУ "libpng warning: iCCP: known incorrect sRGB profile"
#
# class MainApp(App):
#     def build(self):
#         img = Image(source=r'C:\Users\magomed\Desktop\pngwing.png', # Передаем путь к png,jpg и тд файлу осатльно как в примере выше
#                     size_hint=(1, .5),
#                     pos_hint={'center_x': .5, 'center_y': .5})
#         return img
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# TODO: ПРИМЕР №3
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#
# red = [1, 0, 0, 1]
# green = [0, 1, 0, 1]
# blue = [0, 0, 1, 1]
# purple = [1, 0, 1, 1]
#
#
# class HBoxLayoutExample(App):
#     def build(self):
#         # BoxLayout аргументы:
#         # padding(заполнение):Отступ padding между лейаутом и его дочерними элементами уточняется в пикселях
#         # orientation - "vertical/horizontal":Позволяет изменить значение orientation
#         #    для BoxLayout по умолчанию — с горизонтального на вертикальное.
#         # spacing: При помощи данного аргумента добавляется расстояние между дочерними виджетами.
#         layout = BoxLayout(orientation='vertical', padding=10, spacing=41)
#         colors = [red, green, blue, purple]
#
#         for i, value in enumerate(colors):
#             btn = Button(text=f'Button #{(i + 1)}',
#                          background_color=value
#                          )
#             layout.add_widget(btn)
#
#         return layout
#
#
# if __name__ == '__main__':
#     app = HBoxLayoutExample()
#     app.run()


# TODO: ПРИМЕР №4
from kivy.app import App
from kivy.uix.button import Button

# В данном коде вызывается button.bind(), а событие on_press ссылается на MainApp.on_press_button().
# Этот метод неявно принимает экземпляр виджета, который является самим объектом кнопки.
# Сообщение будет выводиться на stdout всякий раз при нажатии пользователем на кнопку.

# class MainApp(App):
#     def build(self):
#         button = Button(text='Hello from Kivy!',
#                         size_hint=(0.5, 0.5),
#                         pos_hint={'center_x': 0.5, 'center_y': 0.5},
#                         background_color=[1, 0, 1, 1])
#         button.bind(on_press=self.on_press_button)
#         return button
#
#     def on_press_button(self, instance):
#         print('Вы нажали кнопку!')
#
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# # TODO: ПРИМЕР №5
#
# from kivy.app import App
# from kivy.uix.button import Button
#
# class ButtonApp(App):
#     def build(self):
#         button = Button()
#         button.bind(on_press=self.on_press_button)
#         return button
#     def on_press_button(self, inct):
#         print('Вы нажали кнопку!')
#
# if __name__ == '__main__':
#     app = ButtonApp()
#     app.run()



