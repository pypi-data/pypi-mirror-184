from setuptools import setup, find_packages
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A cross platform Python package to automate sending and receiving of WhatsApp messages using PyAutoGUI.'

# Setting up
setup(
    name="WhatsAppBot_Nanda",
    version=VERSION,
    author="Nanda Kishore B",
    author_email="<pgsbssnk@gmail.com>",
    url='https://github.com/nandakishfast/WhatsAppBot_Nanda',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages('WhatsAppBot'),
    package_dir={'':'WhatsAppBot'},
    include_package_data = True,
    data_files = [('WhatsAppBot', ['WhatsAppBot/apple.jpg', 'WhatsAppBot/arvind.jpeg', 'WhatsAppBot/bottomleft.png',
                                   'WhatsAppBot/chat.sqlite', 'WhatsAppBot/close_contact.jpg', 'WhatsAppBot/ContactInfo.mp4',
                                   'WhatsAppBot/ContactInfoField1.mp4', 'WhatsAppBot/DateTimeFormat.mp4', 'WhatsAppBot/field2.png',
                                   'WhatsAppBot/field2group.png', 'WhatsAppBot/FirstChatUnread.mp4', 'WhatsAppBot/github.png',
                                   'WhatsAppBot/gmail.png', 'WhatsAppBot/instagram.png', 'WhatsAppBot/instructions.png',
                                   'WhatsAppBot/KebabMenu.mp4', 'WhatsAppBot/linkedin.png', 'WhatsAppBot/mac_whatsapp_squared.mp4',
                                   'WhatsAppBot/minimize.png', 'WhatsAppBot/MoveWhatsappIconToLeft.mp4', 'WhatsAppBot/nanda.jpg',
                                   'WhatsAppBot/new_group.jpeg', 'WhatsAppBot/niresh.jpeg', 'WhatsAppBot/phone.png',
                                   'WhatsAppBot/question.jpeg', 'WhatsAppBot/right_click_icon.jpg', 'WhatsAppBot/SearchBar.mp4',
                                   'WhatsAppBot/SendImage.mp4', 'WhatsAppBot/send_message.png', 'WhatsAppBot/showDesktop.mp4',
                                   'WhatsAppBot/temp_video_here.png', 'WhatsAppBot/topleft.png', 'WhatsAppBot/type_message.png',
                                   'WhatsAppBot/unreadbig.png', 'WhatsAppBot/unread_cordinate_off.mp4',
                                   'WhatsAppBot/unread_cordinate_on.mp4', 'WhatsAppBot/unread_correct.png',
                                   'WhatsAppBot/unread_wrong1.png', 'WhatsAppBot/unread_wrong2.png', 'WhatsAppBot/username.mp4',
                                   'WhatsAppBot/whatsappPath.mp4', 'WhatsAppBot/whatsapp_desktop.jpeg', 'WhatsAppBot/whatsapp_microsoft.jpeg',
                                   'WhatsAppBot/whatsapp_web.jpeg', 'WhatsAppBot/whatsapp_web_move.mp4', 'WhatsAppBot/wt_icon_crt.png',
                                   'WhatsAppBot/wt_icon_crt2.png', 'WhatsAppBot/wt_icon_with_new_msg.PNG', 'WhatsAppBot/wt_icon_wrong.png',
                                   'WhatsAppBot/wt_new_msg.mp4', 'WhatsAppBot/wt_no_new_msg.mp4', 'WhatsAppBot/__init__.py', 'WhatsAppBot/WhatsAppBot.py'])],
    install_requires=['pyautogui', 'scipy', 'pyperclip', 'numpy', 'pynput', 'tkvideo', 'Pillow'],
    extras_require={
        'win32': 'pywin32'
    },
    keywords=['WhatsApp', 'WhatsApp Bot', 'Chat Bot', 'automation'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)