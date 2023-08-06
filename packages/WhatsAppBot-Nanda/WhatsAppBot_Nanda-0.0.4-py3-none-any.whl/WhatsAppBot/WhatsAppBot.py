from datetime import datetime
import pyautogui as pag
from scipy.spatial import distance
import os
import sys
import sqlite3
import time
import pyperclip
import re
import copy
import random
import numpy as np
import pkg_resources

if sys.platform == 'win32':
    from io import BytesIO
    import win32clipboard
if sys.platform == 'darwin':
    import subprocess

from tkinter import messagebox
from pynput import mouse
from tkvideo import tkvideo
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
# below may be for only windows`
from PIL import ImageTk, Image
import webbrowser


class WhatsAppBot:

    def __init__(self, setup_name):
        self.__DATA_PATH = pkg_resources.resource_filename('WhatsAppBot', '/')
        self.__setupDBSchema()
        # this is a reserved keyword
        # will be called by user in constructor to create a new setup
        if setup_name.lower() == 'create a new setup':
            # below variables for setup
            self.__current_setup_name = None
            self.__version = None
            self.__input_field_for_text = None
            self.__label_for_coordinates = None
            self.__label_for_color = None
            self.__window_having_coordinates_or_color_or_input_field = None
            self.__root = None
            self.__listener = None
            self.__x = None
            self.__y = None
            self.__r = None
            self.__g = None
            self.__b = None
            self.__root_for_instructions = None
            self.__instructions = None
            self.__methods = {'__whatsappCoordinates': self.__whatsappCoordinates,
                              '__whatsappNewMsgs': self.__whatsappNewMsgs,
                              '__unreadOn': self.__unreadOn, '__contactInfoCoordinates': self.__contactInfoCoordinates,
                              '__contactInfoField1Coordinates': self.__contactInfoField1Coordinates,
                              '__contactInfoField2Coordinates': self.__contactInfoField2Coordinates,
                              '__contactInfoField2CoordinatesForGroup': self.__contactInfoField2CoordinatesForGroup,
                              '__closeContactInfoField': self.__closeContactInfoField,
                              '__latestMessageCoordinates': self.__latestMessageCoordinates,
                              '__copyAfterLatestMessageCoordinates': self.__copyAfterLatestMessageCoordinates,
                              '__typeMessageCoordinates': self.__typeMessageCoordinates,
                              '__firstChatUnderFilterCoordinates': self.__firstChatUnderFilterCoordinates,
                              '__minimizeWhatsappCoordinates': self.__minimizeWhatsappCoordinates,
                              '__showDesktopCoordinates': self.__showDesktopCoordinates,
                              '__topLeftInChat': self.__topLeftInChat, '__bottomRightInChat': self.__bottomRightInChat,
                              '__userNameOfWtBot': self.__userNameOfWtBot, '__defaultGroup': self.__defaultGroup,
                              '__finish': self.__finish,
                              '__msStoreContactInfoCoordinates': self.__msStoreContactInfoCoordinates,
                              '__msStoreContactInfoField1Coordinates': self.__msStoreContactInfoField1Coordinates,
                              '__msStoreContactInfoField2Coordinates': self.__msStoreContactInfoField2Coordinates,
                              '__msStoreContactInfoField2CoordinatesForUnsaved': self.__msStoreContactInfoField2CoordinatesForUnsaved,
                              '__msStoreCloseContactInfoField': self.__msStoreCloseContactInfoField,
                              '__sendMessageCoordinates': self.__sendMessageCoordinates,
                              '__sendImageCoordinates': self.__sendImageCoordinates,
                              '__searchBarCoordinates': self.__searchBarCoordinates,
                              '__unreadChatCoordinates': self.__unreadChatCoordinates,
                              '__whatsappPathScreen': self.__whatsappPathScreen,
                              '__filterByCoordinates': self.__filterByCoordinates,
                              '__unreadCoordinates': self.__unreadCoordinates,
                              '__closeFilterCoordinates': self.__closeFilterCoordinates,
                              '__firstChatUnderCoordinates': self.__firstChatUnderCoordinates,
                              '__secondChatUnderCoordinates': self.__secondChatUnderCoordinates,
                              '__timeDelay': self.__timeDelay,
                              '__kebabMenuFilterCoordinates': self.__kebabMenuFilterCoordinates
                              }
            self.__instructionsScreen()

        else:
            if self.__setupNameExistsInDb(setup_name) is False:
                print(
                    'No such setup exists. First you have to create a new setup by calling WhatsAppBot("create a new '
                    'setup")')
                exit()
            self.__current_setup_name = setup_name
            setup_in_db = self.__selectAllOfSetup(setup_name)
            [setup,
             wt_version,
             whatsapp_path,
             whatsapp_coordinates_x,
             whatsapp_coordinates_y,
             whatsapp_new_msg_r,
             whatsapp_new_msg_g,
             whatsapp_new_msg_b,
             whatsapp_no_new_msg_r,
             whatsapp_no_new_msg_g,
             whatsapp_no_new_msg_b,
             unread_chat_filter_coordinates_x,
             unread_chat_filter_coordinates_y,
             unread_chat_filter_on_r,
             unread_chat_filter_on_g,
             unread_chat_filter_on_b,
             unread_chat_filter_off_r,
             unread_chat_filter_off_g,
             unread_chat_filter_off_b,
             kebab_menu_coordinates_x,
             kebab_menu_coordinates_y,
             contact_info_coordinates_x,
             contact_info_coordinates_y,
             contact_info_field1_coordinates_x,
             contact_info_field1_coordinates_y,
             contact_info_field2_coordinates_x,
             contact_info_field2_coordinates_y,
             contact_info_field2_coordinates_for_group_x,
             contact_info_field2_coordinates_for_group_y,
             contact_info_field2_coordinates_for_unsaved_x,
             contact_info_field2_coordinates_for_unsaved_y,
             close_contact_info_coordinates_x,
             close_contact_info_coordinates_y,
             latest_message_coordinates_x,
             latest_message_coordinates_y,
             copy_latest_message_coordinates_x,
             copy_latest_message_coordinates_y,
             type_message_coordinates_x,
             type_message_coordinates_y,
             first_chat_under_filter_coordinates_x,
             first_chat_under_filter_coordinates_y,
             second_chat_under_filter_coordinates_x,
             second_chat_under_filter_coordinates_y,
             minimize_whatsapp_coordinates_x,
             minimize_whatsapp_coordinates_y,
             show_desktop_coordinates_x,
             show_desktop_coordinates_y,
             top_left_in_chat_x,
             top_left_in_chat_y,
             bottom_right_in_chat_x,
             bottom_right_in_chat_y,
             send_message_coordinates_x,
             send_message_coordinates_y,
             send_image_coordinates_x,
             send_image_coordinates_y,
             search_bar_coordinates_x,
             search_bar_coordinates_y,
             kebab_menu_for_filter_coordinates_x,
             kebab_menu_for_filter_coordinates_y,
             filter_by_coordinates_x,
             filter_by_coordinates_y,
             unread_coordinates_x,
             unread_coordinates_y,
             close_filter_coordinates_x,
             close_filter_coordinates_y,
             delay,
             mouse_delay,
             type_delay,
             time_format,
             user_name_of_wt_bot,
             default_group] = setup_in_db
            self.__whatsapp_path = whatsapp_path
            self.__wt_version = wt_version
            self.__whatsapp_coordinates = (
                whatsapp_coordinates_x, whatsapp_coordinates_y)
            self.__whatsapp_new_msg = (
                whatsapp_new_msg_r, whatsapp_new_msg_g, whatsapp_new_msg_b)
            self.__whatsapp_no_new_msg = (
                whatsapp_no_new_msg_r, whatsapp_no_new_msg_g, whatsapp_no_new_msg_b)
            self.__unread_chat_filter_coordinates = (
                unread_chat_filter_coordinates_x, unread_chat_filter_coordinates_y)
            self.__unread_chat_filter_on = (
                unread_chat_filter_on_r, unread_chat_filter_on_g, unread_chat_filter_on_b)
            self.__unread_chat_filter_off = (
                unread_chat_filter_off_r, unread_chat_filter_off_g, unread_chat_filter_off_b)
            self.__kebab_menu_coordinates = (
                kebab_menu_coordinates_x, kebab_menu_coordinates_y)
            self.__contact_info_coordinates = (
                contact_info_coordinates_x, contact_info_coordinates_y)
            self.__contact_info_field1_coordinates = (
                contact_info_field1_coordinates_x, contact_info_field1_coordinates_y)
            self.__contact_info_field2_coordinates = (
                contact_info_field2_coordinates_x, contact_info_field2_coordinates_y)
            self.__contact_info_field2_coordinates_for_group = (
                contact_info_field2_coordinates_for_group_x, contact_info_field2_coordinates_for_group_y)
            self.__contact_info_field2_coordinates_for_unsaved = (
                contact_info_field2_coordinates_for_unsaved_x, contact_info_field2_coordinates_for_unsaved_y)
            self.__close_contact_info_coordinates = (
                close_contact_info_coordinates_x, close_contact_info_coordinates_y)
            self.__latest_message_coordinates = (
                latest_message_coordinates_x, latest_message_coordinates_y)
            self.__copy_latest_message_coordinates = (
                copy_latest_message_coordinates_x, copy_latest_message_coordinates_y)
            self.__type_message_coordinates = (
                type_message_coordinates_x, type_message_coordinates_y)
            self.__first_chat_under_filter_coordinates = (
                first_chat_under_filter_coordinates_x, first_chat_under_filter_coordinates_y)
            self.__second_chat_under_filter_coordinates = (
                second_chat_under_filter_coordinates_x, second_chat_under_filter_coordinates_y)
            self.__minimize_whatsapp_coordinates = (
                minimize_whatsapp_coordinates_x, minimize_whatsapp_coordinates_y)
            self.__show_desktop_coordinates = (
                show_desktop_coordinates_x, show_desktop_coordinates_y)
            self.__top_left_in_chat = (
                top_left_in_chat_x, top_left_in_chat_y)
            self.__bottom_right_in_chat = (
                bottom_right_in_chat_x, bottom_right_in_chat_y)
            self.__user_name_of_wt_bot = user_name_of_wt_bot
            self.__default_group = default_group
            self.__send_message_coordinates = (
                send_message_coordinates_x, send_message_coordinates_y)
            self.__send_image_coordinates = (
                send_image_coordinates_x, send_image_coordinates_y)
            self.__search_bar_coordinates = (
                search_bar_coordinates_x, search_bar_coordinates_y)
            self.__kebab_menu_for_filter_coordinates = (
                kebab_menu_for_filter_coordinates_x, kebab_menu_for_filter_coordinates_y)
            self.__filter_by_coordinates = (
                filter_by_coordinates_x, filter_by_coordinates_y)
            self.__unread_coordinates = (
                unread_coordinates_x, unread_coordinates_y)
            self.__close_filter_coordinates = (
                close_filter_coordinates_x, close_filter_coordinates_y)
            self.__whatsapp_time_format = time_format
            self.__time_format = '12' if '%p' in self.__whatsapp_time_format else '24'
            self.__width = pag.size()[0]
            self.__height = pag.size()[1]
            self.__current_open_chat = 'Nothing'
            self.__delay = delay
            self.__mouse_delay = mouse_delay
            self.__type_delay = type_delay
            self.__openWhatsApp()
            self.__goToDefaultGroup()
            self.__minimizeWhatsapp()
            self.__new_messages = []

    def __commitDBChanges(self):
        self.__conn.commit()

    def __setupDBSchema(self):
        file = self.__DATA_PATH + 'chat.sqlite'
        self.__conn = sqlite3.connect(file)
        self.__cur = self.__conn.cursor()
        self.__cur.executescript('''
        
        CREATE TABLE IF NOT EXISTS SETUP(
            setup_name TEXT PRIMARY KEY,
            wt_version TEXT,
            whatsapp_path TEXT,
            whatsapp_coordinates_x INTEGER,
            whatsapp_coordinates_y INTEGER,
            whatsapp_new_msg_r INTEGER,
            whatsapp_new_msg_g INTEGER,
            whatsapp_new_msg_b INTEGER,
            whatsapp_no_new_msg_r INTEGER,
            whatsapp_no_new_msg_g INTEGER,
            whatsapp_no_new_msg_b INTEGER,
            unread_chat_filter_coordinates_x INTEGER,
            unread_chat_filter_coordinates_y INTEGER,
            unread_chat_filter_on_r INTEGER,
            unread_chat_filter_on_g INTEGER,
            unread_chat_filter_on_b INTEGER,
            unread_chat_filter_off_r INTEGER,
            unread_chat_filter_off_g INTEGER,
            unread_chat_filter_off_b INTEGER,
            kebab_menu_coordinates_x INTEGER,
            kebab_menu_coordinates_y INTEGER,
            contact_info_coordinates_x INTEGER,
            contact_info_coordinates_y INTEGER,
            contact_info_field1_coordinates_x INTEGER,
            contact_info_field1_coordinates_y INTEGER,
            contact_info_field2_coordinates_x INTEGER,
            contact_info_field2_coordinates_y INTEGER,
            contact_info_field2_coordinates_for_group_x INTEGER,
            contact_info_field2_coordinates_for_group_y INTEGER,
            contact_info_field2_coordinates_for_unsaved_x INTEGER,
            contact_info_field2_coordinates_for_unsaved_y INTEGER,
            close_contact_info_coordinates_x INTEGER,
            close_contact_info_coordinates_y INTEGER,
            latest_message_coordinates_x INTEGER,
            latest_message_coordinates_y INTEGER,
            copy_latest_message_coordinates_x INTEGER,
            copy_latest_message_coordinates_y INTEGER,
            type_message_coordinates_x INTEGER,
            type_message_coordinates_y INTEGER,
            first_chat_under_filter_coordinates_x INTEGER,
            first_chat_under_filter_coordinates_y INTEGER,
            second_chat_under_filter_coordinates_x INTEGER,
            second_chat_under_filter_coordinates_y INTEGER,
            minimize_whatsapp_coordinates_x INTEGER,
            minimize_whatsapp_coordinates_y INTEGER,
            show_desktop_coordinates_x INTEGER,
            show_desktop_coordinates_y INTEGER,
            top_left_in_chat_x INTEGER,
            top_left_in_chat_y INTEGER,
            bottom_right_in_chat_x INTEGER,
            bottom_right_in_chat_y INTEGER,
            send_message_coordinates_x INTEGER,
            send_message_coordinates_y INTEGER,
            send_image_coordinates_x INTEGER,
            send_image_coordinates_y INTEGER,
            search_bar_coordinates_x INTEGER,
            search_bar_coordinates_y INTEGER,
            kebab_menu_for_filter_coordinates_x INTEGER,
            kebab_menu_for_filter_coordinates_y INTEGER,
            filter_by_coordinates_x INTEGER,
            filter_by_coordinates_y INTEGER,
            unread_coordinates_x INTEGER,
            unread_coordinates_y INTEGER,
            close_filter_coordinates_x INTEGER,
            close_filter_coordinates_y INTEGER,
            delay REAL,
            mouse_delay REAL,
            type_delay REAL,
            time_format REAL,
            user_name_of_wt_bot TEXT,
            default_group TEXT
        );

        CREATE TABLE IF NOT EXISTS USERS(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT UNIQUE,
            user_name TEXT,
            is_saved_contact INTEGER
        );

        CREATE TABLE IF NOT EXISTS GROUPS(
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT
        );

        CREATE TABLE IF NOT EXISTS MESSAGE_STATUS(
            message_status_id INTEGER PRIMARY KEY,
            meaning TEXT
        );

        CREATE TABLE IF NOT EXISTS MESSAGES(
            user_id INTEGER,
            group_id INTEGER,
            date TEXT,
            message TEXT,
            message_status_id INTEGER,
            CONSTRAINT fk_user
                FOREIGN KEY (user_id)
                REFERENCES USERS(user_id),
            CONSTRAINT fk_group
                FOREIGN KEY (group_id)
                REFERENCES GROUPS(group_id),
            CONSTRAINT fk_msg_status
                FOREIGN KEY (message_status_id)
                REFERENCES MESSAGE_STATUS(message_status_id)
        );          
        ''')

        self.__cur.execute(
            '''SELECT COUNT(user_id) FROM USERS WHERE user_id=0;''')
        user_0_in_db = self.__cur.fetchone()
        if user_0_in_db[0] == 0:
            self.__cur.execute(
                '''INSERT INTO USERS(user_id,phone_number,user_name) VALUES (0,'00000 000000','Not Applicable');''')

        self.__cur.execute(
            '''SELECT COUNT(group_id) FROM GROUPS WHERE group_id=0;''')
        group_0_in_db = self.__cur.fetchone()
        if group_0_in_db[0] == 0:
            self.__cur.execute(
                '''INSERT INTO GROUPS(group_id,group_name) VALUES (0,'Not Applicable');''')

        self.__cur.execute('''SELECT COUNT(meaning) FROM MESSAGE_STATUS;''')
        msg_status_in_db = self.__cur.fetchone()
        if msg_status_in_db[0] == 0:
            self.__cur.execute(
                '''INSERT INTO MESSAGE_STATUS(message_status_id,meaning) VALUES (0,'SENT TO');''')
            self.__cur.execute(
                '''INSERT INTO MESSAGE_STATUS(message_status_id,meaning) VALUES (1,'RECEIVED FROM');''')

        self.__cur.execute(
            '''SELECT COUNT(setup_name) FROM SETUP WHERE setup_name='Create a new setup';''')
        # this is reserved setup name
        # will be called by user in constructor to create a new setup
        setup_in_db = self.__cur.fetchone()
        if setup_in_db[0] == 0:
            self.__cur.execute(
                '''INSERT INTO SETUP(setup_name) VALUES ('Create a new setup');''')

        self.__commitDBChanges()

    def __setupNameExistsInDb(self, setup_name):
        self.__cur.execute(
            '''SELECT COUNT(setup_name) FROM SETUP WHERE setup_name=?;''', (setup_name,))
        setup_in_db = self.__cur.fetchone()
        if setup_in_db[0] == 0:
            return False
        return True

    def __selectAllOfSetup(self, setup_name):
        self.__cur.execute(
            '''SELECT * FROM SETUP WHERE setup_name=?;''', (setup_name,))
        setup_in_db = self.__cur.fetchone()
        return setup_in_db

    def __userExistsInDb(self, phone_number):
        self.__cur.execute(
            '''SELECT COUNT(user_id) FROM USERS WHERE phone_number=?;''', (phone_number,))
        user_in_db = self.__cur.fetchone()
        if user_in_db[0] == 0:
            return False
        return True

    def __addUserInDb(self, phone_number, user_name, is_saved_contact):
        self.__cur.execute(
            '''INSERT INTO USERS(phone_number, user_name, is_saved_contact) VALUES (?,?,?);''',
            (phone_number, user_name, is_saved_contact))
        self.__commitDBChanges()

    def __getUserDetailsInDBWithPhone(self, phone_number):
        self.__cur.execute(
            '''SELECT user_id, phone_number, user_name, is_saved_contact FROM USERS WHERE phone_number=?;''',
            (phone_number,))
        user_details = self.__cur.fetchone()
        return user_details

    def __getUserDetailsInDBWithUserName(self, user_name):
        self.__cur.execute(
            '''SELECT user_id, phone_number, user_name, is_saved_contact FROM USERS WHERE user_name=?;''', (user_name,))
        user_details = self.__cur.fetchone()
        return user_details

    def __getUserDetailsInDBWithUserId(self, user_id):
        self.__cur.execute(
            '''SELECT user_id, phone_number, user_name, is_saved_contact FROM USERS WHERE user_id=?;''', (user_id,))
        user_details = self.__cur.fetchone()
        return user_details

    def __updateUserDetailsInDB(self, user_name, is_saved_contact, phone_number):
        self.__cur.execute(
            '''UPDATE USERS SET user_name=?,is_saved_contact=? WHERE phone_number=?;''',
            (user_name, is_saved_contact, phone_number))
        self.__commitDBChanges()

    def __getUserIdInDB(self, ph_no_or_name):
        self.__cur.execute(
            '''SELECT user_id FROM USERS WHERE phone_number=? OR user_name=?;''', (ph_no_or_name, ph_no_or_name))
        user_id_in_list = self.__cur.fetchone()
        if user_id_in_list is None:
            return None
        return user_id_in_list[0]

    def __groupExistsInDb(self, group_name):
        self.__cur.execute(
            '''SELECT COUNT(group_id) FROM GROUPS WHERE group_name=?;''', (group_name,))
        group_in_db = self.__cur.fetchone()
        if group_in_db[0] == 0:
            return False
        return True

    def __addGroupInDb(self, group_name):
        self.__cur.execute(
            '''INSERT INTO GROUPS(group_name) VALUES (?);''', (group_name,))
        self.__commitDBChanges()

    def __getGroupIdInDB(self, group_name):
        self.__cur.execute(
            '''SELECT group_id FROM GROUPS WHERE group_name=?;''', (group_name,))
        group_id_in_list = self.__cur.fetchone()
        if group_id_in_list is None:
            return None
        return group_id_in_list[0]

    def __getGroupNameInDB(self, group_id):
        self.__cur.execute(
            '''SELECT group_name FROM GROUPS WHERE group_id=?;''', (group_id,))
        group_name_in_list = self.__cur.fetchone()
        if group_name_in_list is None:
            return None
        return group_name_in_list[0]

    def __insertMessageWithoutCommit(self, user_id, group_id, date, message, message_status_id):
        self.__cur.execute(
            '''INSERT INTO MESSAGES(user_id, group_id, date, message, message_status_id) VALUES (?,?,?,?,?);''',
            (user_id, group_id, date, message, message_status_id))

    def __openWhatsApp(self):
        if self.__whatsapp_path is not None:
            if sys.platform == 'darwin':
                os.system('open ' + self.__whatsapp_path)
            else:
                os.system(self.__whatsapp_path)
            time.sleep(3 * self.__delay)
        elif self.__whatsapp_coordinates is not None:
            pag.leftClick(
                self.__whatsapp_coordinates[0], self.__whatsapp_coordinates[1], self.__mouse_delay)
            time.sleep(3 * self.__delay)
        else:
            print('whatsapp path not found')
            print('whatsapp coordinates also not available\n')
            print('try setup again')
            exit()

    def __minimizeWhatsapp(self):
        if self.__show_desktop_coordinates is not None:
            pag.leftClick(
                self.__show_desktop_coordinates[0], self.__show_desktop_coordinates[1], self.__mouse_delay)
            time.sleep(2 * self.__delay)
        elif self.__minimize_whatsapp_coordinates is not None:
            pag.leftClick(self.__minimize_whatsapp_coordinates[0], self.__minimize_whatsapp_coordinates[1],
                          self.__mouse_delay)
            time.sleep(2 * self.__delay)
        else:
            print('minimize whatsapp coordinates not found')
            print('try setup again')
            exit()

    def __goToSearchBar(self):
        # pag.hotkey('ctrl', 'f')
        # time.sleep(2 * self.__delay)
        # pag.hotkey('ctrl', 'alt', '/')

        if self.__search_bar_coordinates is not None:
            pag.leftClick(self.__search_bar_coordinates[0], self.__search_bar_coordinates[1],
                          self.__mouse_delay)
            time.sleep(2 * self.__delay)
        else:
            print('search bar coordinates not found')
            print('try setup again')
            exit()

    def __goToSearchBarInChat(self):
        pag.hotkey('ctrl', 'shift', 'f')
        time.sleep(self.__delay)

    # below function sets whatsapp window to the one it looks when it is first started
    # removes any searches(typed number or name) made in the search bar
    # scrolls the chat section on the left to the top most
    def __goToWhatsappDefaultState(self):
        self.__goToSearchBar()
        if sys.platform == 'darwin':
            pag.hotkey('command', 'a', interval=self.__type_delay)
        else:
            pag.hotkey('ctrl', 'a')

        pag.press('backspace')
        pag.moveTo(self.__first_chat_under_filter_coordinates[0],
                   self.__first_chat_under_filter_coordinates[1], self.__mouse_delay)
        pag.scroll(25 * self.__height)

    def __copy(self):
        if sys.platform == 'darwin':
            pag.hotkey('command', 'c', interval=self.__type_delay)
        else:
            pag.hotkey('ctrl', 'c')
        # check if in macOS (cmnd or cntrl)

    def __paste(self):
        if sys.platform == 'darwin':
            pag.hotkey('command', 'v', interval=self.__type_delay)
        else:
            pag.hotkey('ctrl', 'v')

    def __emptyClipBoard(self):
        pyperclip.copy('')

    def __copyTextToClipBoard(self, text):
        pyperclip.copy(text)

    def __getContactOrGroupInfoWindowsDesktop(self):
        pag.leftClick(
            self.__contact_info_coordinates[0], self.__contact_info_coordinates[1], self.__mouse_delay)
        time.sleep(3 * self.__delay)

        pag.tripleClick(
            self.__contact_info_field1_coordinates[0], self.__contact_info_field1_coordinates[1])
        pag.hotkey('ctrl', 'a')
        time.sleep(self.__delay)
        self.__emptyClipBoard()
        self.__copy()
        field1 = pyperclip.paste()
        print('field1', field1)
        return field1

        # pag.leftClick(
        #     self.__contact_info_field2_coordinates[0], self.__contact_info_field2_coordinates[1], self.__mouse_delay)
        # pag.hotkey('ctrl','a')
        # time.sleep(self.__delay)
        # self.__emptyClipBoard()
        # self.__copy()
        # field2 = pyperclip.paste()
        # print('field2',field2)

        # if field1.startswith('+'):
        #     is_saved_contact = 0
        #     pag.leftClick(
        #         self.__contact_info_field2_coordinates_for_unsaved[0], self.__contact_info_field2_coordinates_for_unsaved[1],self.__mouse_delay)
        #     pag.hotkey('ctrl','a')
        #     time.sleep(self.__delay)
        #     self.__emptyClipBoard()
        #     self.__copy()
        #     field2 = pyperclip.paste()
        #     print('field2',field2)
        #     phone_number = field1
        #     user_name = field2[1:]

        #     pag.leftClick(
        #         self.__close_contact_info_coordinates[0], self.__close_contact_info_coordinates[1], self.__mouse_delay)
        #     time.sleep(self.__delay)

        #     if self.__userExistsInDb(phone_number) is False:
        #         self.__addUserInDb(phone_number, user_name, is_saved_contact)
        #         user_id_in_db = self.__getUserIdInDB(phone_number)
        #         return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

        #     user_id_in_db, phone_number_in_db, user_name_in_db, is_saved_contact_in_db = self.__getUserDetailsInDBWithPhone(
        #         phone_number)
        #     if (user_name_in_db != user_name or is_saved_contact != is_saved_contact_in_db):
        #         self.__updateUserDetailsInDB(
        #             user_name, is_saved_contact, phone_number)
        #     return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

        # pag.leftClick(
        #     self.__close_contact_info_coordinates[0], self.__close_contact_info_coordinates[1], self.__mouse_delay)
        # time.sleep(self.__delay)

        # if field2.startswith('+'):
        #     is_saved_contact = 1
        #     phone_number = field2
        #     user_name = field1
        #     if self.__userExistsInDb(phone_number) is False:
        #         self.__addUserInDb(phone_number, user_name, is_saved_contact)
        #         user_id_in_db = self.__getUserIdInDB(phone_number)
        #         return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

        #     user_id_in_db, phone_number_in_db, user_name_in_db, is_saved_contact_in_db = self.__getUserDetailsInDBWithPhone(
        #         phone_number)
        #     if (user_name_in_db != user_name or is_saved_contact != is_saved_contact_in_db):
        #         self.__updateUserDetailsInDB(
        #             user_name, is_saved_contact, phone_number)
        #     return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

        # group_name = field1
        # if (self.__groupExistsInDb(group_name)):
        #     group_id = self.__getGroupIdInDB(group_name)
        # else:
        #     self.__addGroupInDb(group_name)
        #     group_id = self.__getGroupIdInDB(group_name)
        # return ['Group Chat', group_id, group_name]

    def __getContactOrGroupInfo(self):
        if self.__wt_version == 'Whatsapp Desktop Windows from Microsoft Store':
            return self.__getContactOrGroupInfoWindowsDesktop()
        pag.leftClick(
            self.__kebab_menu_coordinates[0], self.__kebab_menu_coordinates[1], self.__mouse_delay)
        time.sleep(3 * self.__delay)
        pag.leftClick(
            self.__contact_info_coordinates[0], self.__contact_info_coordinates[1], self.__mouse_delay)
        time.sleep(3 * self.__delay)

        pag.tripleClick(
            self.__contact_info_field2_coordinates_for_group[0], self.__contact_info_field2_coordinates_for_group[1])
        time.sleep(self.__delay)
        self.__copy()
        field2 = pyperclip.paste()

        pag.tripleClick(
            self.__contact_info_field1_coordinates[0], self.__contact_info_field1_coordinates[1])
        time.sleep(self.__delay)
        self.__copy()
        field1 = pyperclip.paste()

        if field2.lower().startswith('group'):
            group_name = field1
            if self.__groupExistsInDb(group_name):
                group_id = self.__getGroupIdInDB(group_name)
            else:
                self.__addGroupInDb(group_name)
                group_id = self.__getGroupIdInDB(group_name)
            pag.leftClick(
                self.__close_contact_info_coordinates[0], self.__close_contact_info_coordinates[1], self.__mouse_delay)
            time.sleep(2 * self.__delay)
            return ['Group Chat', group_id, group_name]

        pag.tripleClick(
            self.__contact_info_field2_coordinates[0], self.__contact_info_field2_coordinates[1])
        time.sleep(self.__delay)
        self.__copy()
        field2 = pyperclip.paste()

        pag.leftClick(
            self.__close_contact_info_coordinates[0], self.__close_contact_info_coordinates[1], self.__mouse_delay)
        time.sleep(2 * self.__delay)
        if field2.startswith('~'):
            is_saved_contact = 0
            phone_number = field1
            user_name = field2[1:]
        else:
            is_saved_contact = 1
            phone_number = field2
            user_name = field1

        if self.__userExistsInDb(phone_number) is False:
            self.__addUserInDb(phone_number, user_name, is_saved_contact)
            user_id_in_db = self.__getUserIdInDB(phone_number)
            return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

        user_id_in_db, phone_number_in_db, user_name_in_db, is_saved_contact_in_db = self.__getUserDetailsInDBWithPhone(
            phone_number)
        if user_name_in_db != user_name or is_saved_contact != is_saved_contact_in_db:
            self.__updateUserDetailsInDB(
                user_name, is_saved_contact, phone_number)
        return ['Personal Chat', user_id_in_db, user_name, phone_number, is_saved_contact]

    def __openChat(self, ph_no_or_name):
        if self.__insideSameChat(ph_no_or_name):
            return
        self.__goToWhatsappDefaultState()
        # go to searchbar again
        self.__goToSearchBar()
        pag.typewrite(ph_no_or_name, self.__type_delay)
        time.sleep(self.__delay)
        # pag.press('Enter')
        pag.leftClick(self.__first_chat_under_filter_coordinates[0], self.__first_chat_under_filter_coordinates[1],
                      self.__mouse_delay)
        time.sleep(3 * self.__delay)
        self.__current_open_chat = copy.deepcopy(ph_no_or_name)

    def __getContactOrGroupInfoOf(self, ph_no_or_name):
        self.__openChat(ph_no_or_name)
        contact_info = self.__getContactOrGroupInfo()
        self.__current_open_chat = copy.deepcopy(contact_info)
        return contact_info

    def __retrieveUserInfo(self, ph_no_or_name):
        user_info = self.__getUserDetailsInDBWithPhone(ph_no_or_name)
        if user_info is not None:
            return user_info
        user_info = self.__getUserDetailsInDBWithUserName(ph_no_or_name)
        if user_info is not None:
            return user_info
        self.__getContactOrGroupInfoOf(ph_no_or_name)
        user_info = self.__getUserDetailsInDBWithPhone(ph_no_or_name)
        if user_info is not None:
            return user_info
        user_info = self.__getUserDetailsInDBWithUserName(ph_no_or_name)
        if user_info is not None:
            return user_info

    def __goToDefaultGroup(self):
        self.__openChat(self.__default_group)

    def __deselectSelectedText(self):
        # clicking on type message box deselects
        x = self.__type_message_coordinates[0]
        y = self.__type_message_coordinates[1]
        pag.leftClick(x, y, self.__mouse_delay)
        time.sleep(self.__delay)
        if sys.platform == 'win32':
            pag.press('esc')
            time.sleep(self.__delay)

    def __scrollDownTillEndOfChat(self):
        # x is pixel from left to right. Example : width -> (0-1920)
        # y is pixel from top to bottom. Example : height -> (0-1080)
        x1 = self.__top_left_in_chat[0]
        y1 = self.__top_left_in_chat[1]
        x2 = self.__bottom_right_in_chat[0]
        y2 = self.__bottom_right_in_chat[1]

        # move mouse to middle of chat screen and start scrolling down to end of chat
        pag.moveTo(int((x1 + x2) * 0.5), int((y1 + y2) * 0.5),
                   self.__mouse_delay)

        x_points = random.sample(range(x1 + 10, x2 - 10), 10)
        y_points = random.sample(range(y1 + 10, y2 - 10), 10)
        # for holding 100 pixel values of points inside chat
        pixels = []
        for x in x_points:
            for y in y_points:
                pixels.append(pag.pixel(x, y))

        # numpy array faster than python list
        pixels = np.array(pixels)

        # track how much scrolling down is done
        scroll_length = 0
        while scroll_length < 51 * self.__height:
            index = 0
            non_matching_pixels = 0
            # scroll down
            pag.scroll(-1 * self.__height)
            scroll_length += self.__height
            for x in x_points:
                for y in y_points:
                    current_pixel = pag.pixel(x, y)
                    if (pixels[index][0] == current_pixel[0] and pixels[index][1] == current_pixel[1] and pixels[index][
                        2] == current_pixel[2]):
                        pass
                    else:
                        non_matching_pixels += 1
                        pixels[index][0] = current_pixel[0]
                        pixels[index][1] = current_pixel[1]
                        pixels[index][2] = current_pixel[2]
                    index += 1
            # if all pixels in chat are same, then it means the screen is static
            # which means end of chat is reached
            if non_matching_pixels == 0:
                break
        return scroll_length

    def __selectAndCopyMessages(self, scroll_length):
        # x is pixel from left to right. Example : width -> (0-1920)
        # y is pixel from top to bottom. Example : height -> (0-1080)
        x1 = self.__top_left_in_chat[0]
        y1 = self.__top_left_in_chat[1]
        x2 = self.__bottom_right_in_chat[0]
        y2 = self.__bottom_right_in_chat[1]

        some_msg_selected = False

        # if (x2,y2) is unfortunately between 2 messages gap, nothing will be selected
        # so, we move y2 little by little up, until we are able to select some message
        # we verify some message is selected, by copying it
        no_of_times_tried = 0
        while y1 + 10 < y2 and some_msg_selected is False and no_of_times_tried < 10:
            pag.mouseDown(x2, y2, 'left', self.__mouse_delay)
            pag.moveTo(x1, int(y1 + (y2 - y1) * 0.2), self.__mouse_delay)
            pag.mouseUp(None, None, 'left')
            self.__emptyClipBoard()
            self.__copy()
            selected_text = pyperclip.paste()
            self.__deselectSelectedText()
            no_of_times_tried += 1
            if selected_text == '':
                y2 -= 3
            else:
                some_msg_selected = True

        if some_msg_selected == False:
            return ''

        # we now have the right value of y2 from where we can copy select messages
        pag.mouseDown(x2, y2, 'left', self.__mouse_delay)
        pag.moveTo(x1, int(y1 + (y2 - y1) * 0.2), self.__mouse_delay)
        time.sleep(self.__delay)
        # scroll up just a little more than the scrolled down length
        pag.scroll(scroll_length + self.__height)
        time.sleep(self.__delay)
        pag.moveTo(x1, y1, self.__mouse_delay)
        pag.mouseUp(None, None, 'left')
        self.__emptyClipBoard()
        self.__copy()
        selected_text = pyperclip.paste()
        self.__deselectSelectedText()
        return selected_text

    # loops for a very long time if only image or sticker in chat
    # as stickers and images can't be copied as text can be

    def __selectAndCopyMessagesTopToBottom(self):
        # x is pixel from left to right. Example : width -> (0-1920)
        # y is pixel from top to bottom. Example : height -> (0-1080)
        x1 = self.__top_left_in_chat[0]
        y1 = self.__top_left_in_chat[1]
        x2 = self.__bottom_right_in_chat[0]
        y2 = self.__bottom_right_in_chat[1]

        # move mouse to middle of chat screen and scroll up to move above previously read msg
        pag.moveTo(int((x1 + x2) * (0.5)), int((y1 + y2) * (0.5)),
                   self.__mouse_delay)
        pag.scroll(3500)
        some_msg_selected = False

        # if (x1,y1) is unfortunately between 2 messages gap, nothing will be selected
        # so we move y1 little by little down, until we are able to select some message
        # we verify some message is selected, by copying it
        while y1 + 10 < y2 and some_msg_selected == False:
            pag.mouseDown(x1, y1, 'left', self.__mouse_delay)
            pag.moveTo(x2, int(y1 + (y2 - y1) * 0.8), self.__mouse_delay)
            pag.mouseUp(None, None, 'left')
            self.__emptyClipBoard()
            self.__copy()
            selected_text = pyperclip.paste()
            self.__deselectSelectedText()
            if selected_text == '':
                y1 += 1
            else:
                some_msg_selected = True

        if some_msg_selected == False:
            return ''

        # we now have the right value of y1 from where we can copy select messages
        pag.mouseDown(x1, y1, 'left', self.__mouse_delay)
        pag.moveTo(x2, int(y1 + (y2 - y1) * 0.8), self.__mouse_delay)
        time.sleep(self.__delay)
        # scroll down
        pag.scroll(-1 * 35 * self.__height)
        time.sleep(self.__delay)
        pag.moveTo(x2, y2, self.__mouse_delay)
        pag.mouseUp(None, None, 'left')
        self.__emptyClipBoard()
        self.__copy()
        selected_text = pyperclip.paste()
        self.__deselectSelectedText()
        return selected_text

    def __getLastMsgFromGrp(self, group_id):
        self.__cur.execute(
            'SELECT user_id,group_id,date,message,message_status_id FROM MESSAGES WHERE group_id = ? ORDER BY date DESC LIMIT 1;',
            (group_id,))
        details = self.__cur.fetchone()
        if details is None:
            return None

        user_id, group_id, date_time_string, message, message_status_id = details
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.strptime(date_time_string, format_in_db)
        # if self.__time_format == '24':
        #     format_in_wt = '%H:%M, %d/%m/%Y'
        # else:
        #     format_in_wt = '%I:%M %p, %d/%m/%Y'
        date_time_string = (date_time_object.strftime(
            self.__whatsapp_time_format)).lower()
        if date_time_string[0] == '0' and self.__time_format == '12':
            date_time_string = date_time_string[1:]

        wt_exported_format_of_last_msg = '[' + date_time_string + '] '
        if int(message_status_id) == 0:
            wt_exported_format_of_last_msg += self.__user_name_of_wt_bot
        else:
            user_id, phone_number, user_name, is_saved_contact = self.__getUserDetailsInDBWithUserId(
                user_id)
            if int(is_saved_contact) == 1:
                wt_exported_format_of_last_msg += user_name
            else:
                wt_exported_format_of_last_msg += phone_number

        wt_exported_format_of_last_msg += ': '
        wt_exported_format_of_last_msg += message
        return wt_exported_format_of_last_msg

    def __getLastMsgFromPersonal(self, user_id):
        self.__cur.execute(
            'SELECT user_id,group_id,date,message,message_status_id FROM MESSAGES WHERE group_id = ? AND user_id = ? ORDER BY date DESC LIMIT 1;',
            (0, user_id))
        details = self.__cur.fetchone()
        if details is None:
            return None

        user_id, group_id, date_time_string, message, message_status_id = details
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.strptime(date_time_string, format_in_db)
        # if self.__time_format == '24':
        #     format_in_wt = '%H:%M, %d/%m/%Y'
        # else:
        #     format_in_wt = '%I:%M %p, %d/%m/%Y'
        date_time_string = (date_time_object.strftime(
            self.__whatsapp_time_format)).lower()
        if date_time_string[0] == '0' and self.__time_format == '12':
            date_time_string = date_time_string[1:]

        wt_exported_format_of_last_msg = '[' + date_time_string + '] '
        if int(message_status_id) == 0:
            wt_exported_format_of_last_msg += self.__user_name_of_wt_bot
        else:
            user_id, phone_number, user_name, is_saved_contact = self.__getUserDetailsInDBWithUserId(
                user_id)
            if int(is_saved_contact) == 1:
                wt_exported_format_of_last_msg += user_name
            else:
                wt_exported_format_of_last_msg += phone_number

        wt_exported_format_of_last_msg += ': '
        wt_exported_format_of_last_msg += message
        return wt_exported_format_of_last_msg

    def __closenessToPixel(self, rgb1, rgb2):
        return distance.euclidean(rgb1, rgb2)

    def __getUnreadChatFilterState(self):
        current_pixel_color = pag.pixel(
            self.__unread_chat_filter_coordinates[0], self.__unread_chat_filter_coordinates[1])
        closeness_to_filter_on = self.__closenessToPixel(
            current_pixel_color, self.__unread_chat_filter_on)
        closeness_to_filter_off = self.__closenessToPixel(
            current_pixel_color, self.__unread_chat_filter_off)
        if closeness_to_filter_on < closeness_to_filter_off:
            return "ON"
        else:
            return "OFF"

    def __turnOnUnreadChatFilter(self):
        if self.__wt_version == 'Whatsapp Desktop Windows from Microsoft Store':
            pag.leftClick(
                self.__kebab_menu_for_filter_coordinates[0], self.__kebab_menu_for_filter_coordinates[1],
                self.__mouse_delay)
            time.sleep(2 * self.__delay)
            pag.leftClick(
                self.__filter_by_coordinates[0], self.__filter_by_coordinates[1], self.__mouse_delay)
            time.sleep(2 * self.__delay)
            pag.moveTo(
                self.__unread_coordinates[0], self.__unread_coordinates[1], self.__mouse_delay)
            pag.click(clicks=2)
            time.sleep(2 * self.__delay)
            return
        if self.__getUnreadChatFilterState() == "OFF":
            pag.leftClick(
                self.__unread_chat_filter_coordinates[0], self.__unread_chat_filter_coordinates[1], self.__mouse_delay)
            time.sleep(2 * self.__delay)

    def __turnOffUnreadChatFilter(self):
        if self.__wt_version == 'Whatsapp Desktop Windows from Microsoft Store':
            pag.leftClick(
                self.__close_filter_coordinates[0], self.__close_filter_coordinates[1], self.__mouse_delay)
            time.sleep(self.__delay)
            return
        if self.__getUnreadChatFilterState() == "ON":
            pag.leftClick(
                self.__unread_chat_filter_coordinates[0], self.__unread_chat_filter_coordinates[1], self.__mouse_delay)
            time.sleep(2 * self.__delay)

    def newMessagesThere(self):
        if self.__whatsapp_coordinates is None:
            print('whatsapp coordinates not available. Do setup again')
            exit()
        if (self.__whatsapp_new_msg is None) or (self.__whatsapp_no_new_msg is None):
            print('whatsapp pixels for new messages not available. Do setup again')
            exit()
        current_pixel_color = pag.pixel(
            self.__whatsapp_coordinates[0], self.__whatsapp_coordinates[1])
        closeness_to_new_msg = self.__closenessToPixel(
            current_pixel_color, self.__whatsapp_new_msg)
        closeness_to_no_new_msg = self.__closenessToPixel(
            current_pixel_color, self.__whatsapp_no_new_msg)
        if closeness_to_new_msg < closeness_to_no_new_msg:
            return True
        return False

    def __insideSameChat(self, contact_info):
        if self.__current_open_chat == contact_info:
            return True
        if isinstance(contact_info, str):
            if isinstance(self.__current_open_chat, str):
                return False
            else:
                if self.__current_open_chat[0] == 'Group Chat':
                    if self.__current_open_chat[2] == contact_info:
                        return True
                    else:
                        return False
                if self.__current_open_chat[1] == 'Personal Chat':
                    if self.__current_open_chat[2] == contact_info or self.__current_open_chat[3] == contact_info:
                        return True
                    else:
                        return False
        if contact_info[0] == 'Group Chat':
            if contact_info[2] == self.__current_open_chat:
                return True
            else:
                return False
        if contact_info[1] == 'Personal Chat':
            if contact_info[2] == self.__current_open_chat or contact_info[3] == self.__current_open_chat:
                return True
            else:
                return False

    def __lookForNewMessagesWindowsDesktop(self):
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        # change 5 to infinite
        for cntr in range(5):
            self.__goToWhatsappDefaultState()
            self.__turnOnUnreadChatFilter()

            # storing the state, to know whether we are opening a new chat

            # x is pixel from left to right. Example : width -> (0-1920)
            # y is pixel from top to bottom. Example : height -> (0-1080)
            x1 = self.__top_left_in_chat[0]
            y1 = self.__top_left_in_chat[1]
            x2 = self.__bottom_right_in_chat[0]
            y2 = self.__bottom_right_in_chat[1]

            # move mouse to middle of chat screen
            pag.moveTo(int((x1 + x2) * (0.5)), int((y1 + y2) * (0.5)),
                       self.__mouse_delay)

            x_points = random.sample(range(x1 + 10, x2 - 10), 10)
            y_points = random.sample(range(y1 + 10, y2 - 10), 10)
            # for holding 100 pixel values of points inside chat
            pixels = []
            for x in x_points:
                for y in y_points:
                    pixels.append(pag.pixel(x, y))

            # numpy array faster than python list
            pixels = np.array(pixels)
            # pixels is the stored state

            pag.leftClick(
                self.__first_chat_under_filter_coordinates[0], self.__first_chat_under_filter_coordinates[1],
                self.__mouse_delay)
            # move mouse to middle of chat screen
            pag.moveTo(int((x1 + x2) * (0.5)),
                       int((y1 + y2) * (0.5)), self.__mouse_delay)
            time.sleep(2 * self.__delay)
            index = 0
            non_matching_pixels = 0
            for x in x_points:
                for y in y_points:
                    current_pixel = pag.pixel(x, y)
                    if (pixels[index][0] == current_pixel[0] and pixels[index][1] == current_pixel[1] and pixels[index][
                        2] == current_pixel[2]):
                        pass
                    else:
                        non_matching_pixels += 1
                        pixels[index][0] = current_pixel[0]
                        pixels[index][1] = current_pixel[1]
                        pixels[index][2] = current_pixel[2]
                    index += 1
            # if all pixels in chat are same, then it means the screen is static
            # which means we clicked on the same chat in the filter, so click second chat
            if non_matching_pixels == 0:
                pag.leftClick(
                    self.__second_chat_under_filter_coordinates[0], self.__second_chat_under_filter_coordinates[1],
                    self.__mouse_delay)
                time.sleep(2 * self.__delay)

            self.__turnOffUnreadChatFilter()
            contact_info = self.__getContactOrGroupInfo()
            print("contactinfo, currentopenchat")
            print(contact_info, self.__current_open_chat)
            if contact_info == self.__current_open_chat:
                break

            self.__current_open_chat = contact_info

            # move mouse to middle of chat screen
            pag.moveTo(int((x1 + x2) * (0.5)),
                       int((y1 + y2) * (0.5)), self.__mouse_delay)
            pag.scroll(-25 * self.__height)

            pag.rightClick(
                self.__latest_message_coordinates[0], self.__latest_message_coordinates[1], self.__mouse_delay)
            time.sleep(self.__delay)
            pag.hotkey('ctrl', 'a')
            pag.hotkey('ctrl', 'c')
            copied_text = pyperclip.paste()

            print("copiedtext, contactinfo")
            print(copied_text, contact_info)
            if copied_text is None or copied_text == '':
                continue

            date_time_object = datetime.now()
            format_in_db = '%Y-%m-%d %H:%M'
            date_time_string = date_time_object.strftime(format_in_db)

            self.__new_messages.append([contact_info, copied_text])

            # if contact_info[0]=='Group Chat':
            #     group_id = contact_info[1]
            #     group_name = contact_info[2]
            #     self.__insertMessageWithoutCommit(0,group_id,date_time_string,copied_text,1)
            #     self.__commitDBChanges()
            #     msg_representation = ['Group Chat',group_name,[date_time_string,'Not Applicable','00000 000000',copied_text]]
            #     self.__new_messages.append(msg_representation)
            # elif contact_info[0]=='Personal Chat':
            #     user_id = contact_info[1]
            #     user_name = contact_info[2]
            #     phone_number = contact_info[3]
            #     self.__insertMessageWithoutCommit(user_id,0,date_time_string,copied_text,1)
            #     self.__commitDBChanges()
            #     msg_representation = ['Personal Chat',user_name,phone_number,[date_time_string,copied_text]]
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def __lookForNewMessages(self):
        if self.__wt_version == 'Whatsapp Desktop Windows from Microsoft Store':
            return self.__lookForNewMessagesWindowsDesktop()
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()

        if (self.__whatsapp_coordinates is not None) and (self.__whatsapp_new_msg is not None) and (
                self.__whatsapp_no_new_msg is not None):
            new_msgs_there_flag = self.newMessagesThere()
        else:
            new_msgs_there_flag = True

        while new_msgs_there_flag:
            self.__goToWhatsappDefaultState()
            self.__turnOnUnreadChatFilter()
            pag.leftClick(
                self.__first_chat_under_filter_coordinates[0], self.__first_chat_under_filter_coordinates[1],
                self.__mouse_delay)
            self.__turnOffUnreadChatFilter()
            scroll_length = self.__scrollDownTillEndOfChat()
            contact_info = self.__getContactOrGroupInfo()

            if (self.__whatsapp_coordinates is not None) and (self.__whatsapp_new_msg is not None) and (
                    self.__whatsapp_no_new_msg is not None):
                new_msgs_there_flag = self.newMessagesThere()

            # print("contactinfo, currentopenchat")
            # print(contact_info, self.__current_open_chat)
            if self.__insideSameChat(contact_info):
                break
            copied_text = self.__selectAndCopyMessages(scroll_length)
            self.__current_open_chat = copy.deepcopy(contact_info)
            # print("copiedtext, contactinfo")
            # print(copied_text, contact_info)
            if contact_info[0] == 'Group Chat':
                group_id = contact_info[1]
                wt_exported_format_of_last_msg = self.__getLastMsgFromGrp(
                    group_id)
            elif contact_info[0] == 'Personal Chat':
                user_id = contact_info[1]
                wt_exported_format_of_last_msg = self.__getLastMsgFromPersonal(
                    user_id)
            if wt_exported_format_of_last_msg is None:
                last_msg_available_in_db = False
            else:
                index = (copied_text.lower()).find(
                    wt_exported_format_of_last_msg.lower())
                if (index == -1):
                    last_msg_available_in_db = False
                else:
                    last_msg_available_in_db = True
                    copied_text = copied_text[index +
                                              len(wt_exported_format_of_last_msg):]

            lines = copied_text.split('\n')
            intermediate_representation_msg = []
            if contact_info[0] == 'Group Chat':
                group_id = contact_info[1]
                group_name = contact_info[2]
                intermediate_representation_msg.append('Group Chat')
                intermediate_representation_msg.append(group_id)
                intermediate_representation_msg.append(group_name)
                intermediate_representation_msg.append(
                    [])  # for holding messages

            if contact_info[0] == 'Personal Chat':
                user_id = contact_info[1]
                user_name = contact_info[2]
                phone_number = contact_info[3]
                intermediate_representation_msg.append('Personal Chat')
                intermediate_representation_msg.append(user_id)
                intermediate_representation_msg.append(user_name)
                intermediate_representation_msg.append(phone_number)
                intermediate_representation_msg.append(
                    [])  # for holding messages

            if (self.__time_format == '12'):
                regex_msg_start = re.compile(
                    r"\[(1[0-2]:[0-5][0-9]|[1-9]:[0-5][0-9])\s(am|pm|AM|PM|Am|Pm), (\d\d/\d\d/\d\d\d\d|\d\d/\d\d\d\d/\d\d|\d\d\d\d/\d\d/\d\d)\] ([^:]+):\s([^\n]+)")
            elif (self.__time_format == '24'):
                regex_msg_start = re.compile(
                    r"\[(0[0-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]), (\d\d/\d\d/\d\d\d\d|\d\d/\d\d\d\d/\d\d|\d\d\d\d/\d\d/\d\d)\] ([^:]+):\s([^\n]+)")
            for i in range(len(lines)):
                matched = regex_msg_start.search(lines[i])
                if (matched is None) and (len(intermediate_representation_msg[-1]) != 0) and lines[i] != '':
                    # go to messages field which is last indexed, go to last message in list, get last field which is
                    # the msg typed
                    intermediate_representation_msg[-1][-1][-1] = intermediate_representation_msg[-1][-1][-1] + '\n' + \
                                                                  lines[i]

                if matched is not None:
                    if self.__time_format == '12':
                        time_ = matched.group(1)
                        period = matched.group(2)
                        date = matched.group(3)
                        date_time_string = time_ + ' ' + period + ', ' + date
                        ph_no_or_name = matched.group(4)
                        msg = matched.group(5)
                    else:
                        time_ = matched.group(1)
                        date = matched.group(2)
                        date_time_string = time_ + ', ' + date
                        ph_no_or_name = matched.group(3)
                        msg = matched.group(4)

                    if ph_no_or_name == self.__user_name_of_wt_bot:
                        # if the user has sent a message, it means he has read all above chat so make messages field
                        # empty this happens only when a new person (or from unseen group) msgs for the first time
                        # as no previous chat of him is available
                        intermediate_representation_msg[-1] = []
                        continue

                    # if self.__time_format == '12':
                    #     date_time_string = date + ' ' + time + ' ' + period
                    #     format = '%d/%m/%Y %I:%M %p'
                    #     date_time_object = datetime.strptime(
                    #         date_time_string, format)
                    # else:
                    #     date_time_string = date + ' ' + time
                    #     format = '%d/%m/%Y %H:%M'
                    #     date_time_object = datetime.strptime(
                    #         date_time_string, format)

                    date_time_object = datetime.strptime(
                        date_time_string, self.__whatsapp_time_format)
                    format_in_db = '%Y-%m-%d %H:%M'
                    date_time_string = date_time_object.strftime(format_in_db)

                    current_msg_annotated = [
                        date_time_object, date_time_string]
                    if intermediate_representation_msg[0] == 'Group Chat':
                        contact_info_of_user = self.__retrieveUserInfo(
                            ph_no_or_name)
                        if contact_info_of_user is None:
                            # if it is none, it means the contact which sent msg in group is not saved
                            # and no private conversation with that contact is initiated
                            # so it is not possible to go into that contact chat with search

                            # insert with username empty
                            # ph_no_or_name will be phone number as contact is not saved
                            self.__addUserInDb(
                                phone_number=ph_no_or_name, user_name='', is_saved_contact=0)
                            contact_info_of_user = self.__getUserDetailsInDBWithPhone(
                                ph_no_or_name)
                        current_msg_annotated.append(contact_info_of_user[0])
                        current_msg_annotated.append(contact_info_of_user[1])
                        current_msg_annotated.append(contact_info_of_user[2])

                    current_msg_annotated.append(msg)
                    intermediate_representation_msg[-1].append(
                        current_msg_annotated)
            # print('intermediate_representation_msg')
            # print(intermediate_representation_msg)
            if len(intermediate_representation_msg[-1]) == 0:
                # no new msgs
                pass
            else:
                if intermediate_representation_msg[0] == 'Group Chat':
                    group_id = intermediate_representation_msg[1]
                    msg_status_id = 1
                    for z in range(len(intermediate_representation_msg[-1])):
                        date_time = intermediate_representation_msg[-1][z][1]
                        user_id = intermediate_representation_msg[-1][z][2]
                        msg = intermediate_representation_msg[-1][z][5]
                        self.__insertMessageWithoutCommit(
                            user_id, group_id, date_time, msg, msg_status_id)
                        # remove date_time_object,user_id,group_id
                        intermediate_representation_msg[-1][z].pop(0)
                        intermediate_representation_msg[-1][z].pop(1)
                    intermediate_representation_msg.pop(1)
                    self.__commitDBChanges()
                elif intermediate_representation_msg[0] == 'Personal Chat':
                    group_id = 0
                    user_id = intermediate_representation_msg[1]
                    msg_status_id = 1
                    for z in range(len(intermediate_representation_msg[-1])):
                        date_time = intermediate_representation_msg[-1][z][1]
                        msg = intermediate_representation_msg[-1][z][2]
                        self.__insertMessageWithoutCommit(
                            user_id, group_id, date_time, msg, msg_status_id)
                        # remove date_time_object,user_id
                        intermediate_representation_msg[-1][z].pop(0)
                    intermediate_representation_msg.pop(1)
                    self.__commitDBChanges()
                self.__new_messages.append(intermediate_representation_msg)
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def __goToTypeMessageBox(self):
        x = self.__type_message_coordinates[0]
        y = self.__type_message_coordinates[1]
        pag.leftClick(x, y, self.__mouse_delay)
        time.sleep(self.__delay)

    def __sendText(self, ph_no_or_name, text):
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        self.__openChat(ph_no_or_name)
        user_id = self.__getUserIdInDB(ph_no_or_name)
        # if it is none this chat is being initiated for first time
        # or this whatsappbot has not seen it
        if user_id is None:
            self.__getContactOrGroupInfo()
            # not directly taking values from the above called function
            # as if the number is not saved and chat is not initiated
            # it is impossible to send msg in whatsapp
            # so even after searching in chat, it would not have opened
            # so getContactInfo will return the last open chat details
            user_id = self.__getUserIdInDB(ph_no_or_name)
            # if user_id is obtained then means we are inside the
            # intended chat as called in this function (ph_no_or_name)
            if user_id is None:
                self.__goToDefaultGroup()
                self.__minimizeWhatsapp()
                print('No such contact in your whatsapp ->', ph_no_or_name)
                return
        self.__goToTypeMessageBox()
        self.__copyTextToClipBoard(text)
        self.__paste()
        pag.leftClick(
            self.__send_message_coordinates[0], self.__send_message_coordinates[1], self.__mouse_delay)
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.now()
        date_time_string = date_time_object.strftime(format_in_db)
        self.__insertMessageWithoutCommit(user_id, 0, date_time_string, text, 0)
        self.__commitDBChanges()
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def __sendTextToGroup(self, group_name, text):
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        self.__openChat(group_name)
        group_id = self.__getGroupIdInDB(group_name)
        # if it is none this chat is being initiated for first time
        # or this whatsappbot has not seen it
        if group_id is None:
            self.__getContactOrGroupInfo()
            # not directly taking values from the above called function
            # as if the number is not saved and chat is not initiated
            # it is impossible to send msg in whatsapp
            # so even after searching in chat, it would not have opened
            # so getContactInfo will return the last open chat details
            group_id = self.__getGroupIdInDB(group_name)
            # if group_id is obtained then means we are inside the
            # intended chat as called in this function (group_name)
            if group_id is None:
                self.__goToDefaultGroup()
                self.__minimizeWhatsapp()
                print('No such group in your whatsapp ->', group_name)
                return
        self.__goToTypeMessageBox()
        self.__copyTextToClipBoard(text)
        self.__paste()
        pag.leftClick(
            self.__send_message_coordinates[0], self.__send_message_coordinates[1], self.__mouse_delay)
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.now()
        date_time_string = date_time_object.strftime(format_in_db)
        self.__insertMessageWithoutCommit(
            0, group_id, date_time_string, text, 0)
        self.__commitDBChanges()
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def sendMultipleMessages(self, list_of_replies):
        # list_of_replies = [['Personal Chat',ph_no_or_name,[[msg1_type,msg1],[msg2_type,msg2],[msg3_type,msg3]]],
        # ['Group Chat',group_name,[['Image',img_location],['Text',text_msg]]],[],[]]
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        for reply in list_of_replies:
            if len(reply) != 3:
                print('Must be of length 3.', reply)
                continue
            personal_or_grp = reply[0]
            ph_no_or_name = reply[1]
            msgs = reply[2]
            if personal_or_grp == 'Personal Chat':
                self.__openChat(ph_no_or_name)
                user_id = self.__getUserIdInDB(ph_no_or_name)
                # if it is none this chat is being initiated for first time
                # or this whatsappbot has not seen it
                if user_id is None:
                    self.__getContactOrGroupInfo()
                    # not directly taking values from the above called function
                    # as if the number is not saved and chat is not initiated
                    # it is impossible to send msg in whatsapp
                    # so even after searching in chat, it would not have opened
                    # so getContactInfo will return the last open chat details
                    user_id = self.__getUserIdInDB(ph_no_or_name)
                    # if user_id is obtained then means we are inside the
                    # intended chat as called in this function (ph_no_or_name)
                    if user_id is None:
                        continue

                for msg in msgs:
                    if len(msg) != 2:
                        print('Msg must have 2 parameters. But provided', msg)
                        continue

                    if msg[0] == 'Text':
                        self.__goToTypeMessageBox()
                        self.__copyTextToClipBoard(msg[1])
                        self.__paste()
                        pag.leftClick(
                            self.__send_message_coordinates[0], self.__send_message_coordinates[1], self.__mouse_delay)
                        format_in_db = '%Y-%m-%d %H:%M'
                        date_time_object = datetime.now()
                        date_time_string = date_time_object.strftime(format_in_db)
                        self.__insertMessageWithoutCommit(
                            user_id, 0, date_time_string, msg[1], 0)

                    elif msg[0] == 'Image':
                        self.__goToTypeMessageBox()
                        self.__copyImageToClipboard(msg[1])
                        self.__paste()
                        time.sleep(5 * self.__delay)
                        pag.leftClick(
                            self.__send_image_coordinates[0], self.__send_image_coordinates[1], self.__mouse_delay)
                        format_in_db = '%Y-%m-%d %H:%M'
                        date_time_object = datetime.now()
                        date_time_string = date_time_object.strftime(format_in_db)
                        msg_in_db = 'Sent image at location:' + msg[1]
                        self.__insertMessageWithoutCommit(user_id, 0, date_time_string, msg_in_db, 0)

                    else:
                        print('msg[0] must be Image or Text, but provided', msg[0])

            elif personal_or_grp == 'Group Chat':
                self.__openChat(ph_no_or_name)
                group_id = self.__getGroupIdInDB(ph_no_or_name)
                # if it is none this chat is being initiated for first time
                # or this whatsappbot has not seen it
                if group_id is None:
                    self.__getContactOrGroupInfo()
                    # not directly taking values from the above called function
                    # as if the number is not saved and chat is not initiated
                    # it is impossible to send msg in whatsapp
                    # so even after searching in chat, it would not have opened
                    # so getContactInfo will return the last open chat details
                    group_id = self.__getGroupIdInDB(ph_no_or_name)
                    # if group_id is obtained then means we are inside the
                    # intended chat as called in this function (group_name)
                    if group_id is None:
                        continue

                for msg in msgs:
                    if len(msg) != 2:
                        print('Msg must have 2 parameters. But provided', msg)
                        continue

                    if msg[0] == 'Text':
                        self.__goToTypeMessageBox()
                        self.__copyTextToClipBoard(msg[1])
                        self.__paste()
                        pag.leftClick(
                            self.__send_message_coordinates[0], self.__send_message_coordinates[1], self.__mouse_delay)
                        format_in_db = '%Y-%m-%d %H:%M'
                        date_time_object = datetime.now()
                        date_time_string = date_time_object.strftime(format_in_db)
                        self.__insertMessageWithoutCommit(
                            0, group_id, date_time_string, msg[1], 0)

                    elif msg[0] == 'Image':
                        self.__goToTypeMessageBox()
                        self.__copyImageToClipboard(msg[1])
                        self.__paste()
                        time.sleep(5 * self.__delay)
                        pag.leftClick(
                            self.__send_image_coordinates[0], self.__send_image_coordinates[1], self.__mouse_delay)
                        format_in_db = '%Y-%m-%d %H:%M'
                        date_time_object = datetime.now()
                        date_time_string = date_time_object.strftime(format_in_db)
                        msg_in_db = 'Sent image at location:' + msg[1]
                        self.__insertMessageWithoutCommit(0, group_id, date_time_string, msg_in_db, 0)

                    else:
                        print('msg[0] must be Image or Text, but provided', msg[0])

            else:
                print('Must be Personal Chat or Group Chat. But given', personal_or_grp)
        self.__commitDBChanges()
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def __send_to_clipboard(self, image):
        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

    def __copyImageToClipboard(self, img_location):
        if sys.platform == 'win32':
            image = Image.open(img_location)
            self.__send_to_clipboard(image)
        elif sys.platform == 'darwin':
            subprocess.run(["osascript", "-e",
                            "set the clipboard to (read (POSIX file \"" + img_location + "\") as JPEG picture)"])
        else:
            print('Send Image not supported in your platform. See documentation for more details')
            exit()

    def __sendImage(self, ph_no_or_name, img_location):
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        self.__openChat(ph_no_or_name)
        user_id = self.__getUserIdInDB(ph_no_or_name)
        # if it is none this chat is being initiated for first time
        # or this whatsappbot has not seen it
        if user_id is None:
            self.__getContactOrGroupInfo()
            # not directly taking values from the above called function
            # as if the number is not saved and chat is not initiated
            # it is impossible to send msg in whatsapp
            # so even after searching in chat, it would not have opened
            # so getContactInfo will return the last open chat details
            user_id = self.__getUserIdInDB(ph_no_or_name)
            # if user_id is obtained then means we are inside the
            # intended chat as called in this function (ph_no_or_name)
            if user_id is None:
                self.__goToDefaultGroup()
                self.__minimizeWhatsapp()
                print('No such contact in your whatsapp ->', ph_no_or_name)
                return
        self.__goToTypeMessageBox()
        # copy image to clipboard
        self.__copyImageToClipboard(img_location)
        # paste image and send
        self.__paste()
        time.sleep(5 * self.__delay)
        pag.leftClick(
            self.__send_image_coordinates[0], self.__send_image_coordinates[1], self.__mouse_delay)
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.now()
        date_time_string = date_time_object.strftime(format_in_db)
        msg = 'Sent image at location:' + img_location
        self.__insertMessageWithoutCommit(user_id, 0, date_time_string, msg, 0)
        self.__commitDBChanges()
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def __sendImageToGroup(self, group_name, img_location):
        self.__openWhatsApp()
        self.__turnOffUnreadChatFilter()
        self.__openChat(group_name)
        group_id = self.__getGroupIdInDB(group_name)
        # if it is none this chat is being initiated for first time
        # or this whatsappbot has not seen it
        if group_id is None:
            self.__getContactOrGroupInfo()
            # not directly taking values from the above called function
            # as if the number is not saved and chat is not initiated
            # it is impossible to send msg in whatsapp
            # so even after searching in chat, it would not have opened
            # so getContactInfo will return the last open chat details
            group_id = self.__getGroupIdInDB(group_name)
            # if group_id is obtained then means we are inside the
            # intended chat as called in this function (group_name)
            if group_id is None:
                self.__goToDefaultGroup()
                self.__minimizeWhatsapp()
                print('No such group in your whatsapp ->', group_name)
                return
        self.__goToTypeMessageBox()
        # copy image to clipboard
        self.__copyImageToClipboard(img_location)
        # paste image and send
        self.__paste()
        time.sleep(5 * self.__delay)
        pag.leftClick(
            self.__send_image_coordinates[0], self.__send_image_coordinates[1], self.__mouse_delay)
        format_in_db = '%Y-%m-%d %H:%M'
        date_time_object = datetime.now()
        date_time_string = date_time_object.strftime(format_in_db)
        msg = 'Sent image at location:' + img_location
        self.__insertMessageWithoutCommit(
            0, group_id, date_time_string, msg, 0)
        self.__commitDBChanges()
        self.__goToDefaultGroup()
        self.__minimizeWhatsapp()

    def sendMessage(self, personal_or_grp, message_to, message_type, text=None, image_location=None):
        if message_to is None:
            print('message_to not provided. It is None')
            return
        valid_personal_or_grp = {'Personal Chat', 'Group Chat'}
        if personal_or_grp not in valid_personal_or_grp:
            raise ValueError("sendMessage: personal_or_grp must be one of %r." % valid_personal_or_grp)

        valid_message_type = {'Text', 'Image'}
        if message_type not in valid_message_type:
            raise ValueError("sendMessage: message_type must be one of %r." % valid_message_type)

        if personal_or_grp == 'Personal Chat' and message_type == 'Text':
            if text is None:
                print('No text provided. It is None.')
                return
            return self.__sendText(message_to, text)

        if personal_or_grp == 'Group Chat' and message_type == 'Text':
            if text is None:
                print('No text provided. It is None.')
                return
            return self.__sendTextToGroup(message_to, text)

        if personal_or_grp == 'Personal Chat' and message_type == 'Image':
            if image_location is None:
                print('Image location not provided. It is None.')
                return
            return self.__sendImage(message_to, image_location)

        if personal_or_grp == 'Group Chat' and message_type == 'Image':
            if image_location is None:
                print('Image location not provided. It is None.')
                return
            return self.__sendImageToGroup(message_to, image_location)

    # code above complete
    # code below to be completed
    # must also make it empty list after that
    # do deep copy
    def getNewMessages(self):
        self.__lookForNewMessages()
        new_messages = copy.deepcopy(self.__new_messages)
        self.__new_messages = []
        return new_messages

    def getPreviousMessages(self, count=100, personal_or_grp=None, ph_no_or_name=None, message_type='Both',
                            start_date_time='1970-01-01 00:00', end_date_time='3000-01-01 00:00'):
        if not isinstance(count, int):
            print('getPreviousMessages: count should be int')
            return
        if count < 0:
            print('getPreviousMessages: count must be positive')
            return

        query = 'SELECT * FROM MESSAGES '
        where_clause = False
        if personal_or_grp is not None:
            valid_personal_or_grp = {'Personal Chat', 'Group Chat'}
            if personal_or_grp not in valid_personal_or_grp:
                raise ValueError("getPreviousMessages: personal_or_grp must be one of %r." % valid_personal_or_grp)
            if personal_or_grp == 'Personal Chat':
                query += 'WHERE group_id = 0 '
            else:
                query += 'WHERE group_id != 0 '
            where_clause = True

        if ph_no_or_name is not None:
            if personal_or_grp is None:
                print('Must specify personal or group chat, when filtering by contact name / group name.')
                return
            if personal_or_grp == 'Personal Chat':
                user_id = self.__getUserIdInDB(ph_no_or_name)
                if user_id is None:
                    print('No such contact exists or no messages from', ph_no_or_name)
                    return
                query += 'AND user_id = ' + str(user_id) + ' '
            else:
                group_id = self.__getGroupIdInDB(ph_no_or_name)
                if group_id is None:
                    print('No such group exists or no messages from', ph_no_or_name)
                    return
                query += 'AND group_id = ' + str(group_id) + ' '

        if message_type != 'Both':
            valid_message_type = {'Sent', 'Received', 'Both'}
            if message_type not in valid_message_type:
                raise ValueError("getPreviousMessages: message_type must be one of %r." % message_type)

            if message_type == 'Sent':
                if where_clause:
                    query += 'AND message_status_id = 0 '
                else:
                    query += 'WHERE message_status_id = 0 '

            elif message_type == 'Received':
                if where_clause:
                    query += 'AND message_status_id = 1 '
                else:
                    query += 'WHERE message_status_id = 1 '
            where_clause = True

        if not isinstance(start_date_time, str):
            print('start_date_time must be string in YYYY-MM-DD HH:MM format')
        if not isinstance(end_date_time, str):
            print('end_date_time must be string in YYYY-MM-DD HH:MM format')

        regex_time = re.compile(r"\d\d\d\d-\d\d-\d\d\s\d\d:\d\d")
        matched = regex_time.search(start_date_time)
        if matched is None:
            print('start_date_time must be string in YYYY-MM-DD HH:MM format')
        start_date_time = matched[0]

        matched = regex_time.search(end_date_time)
        if matched is None:
            print('end_date_time must be string in YYYY-MM-DD HH:MM format')
        end_date_time = matched[0]

        if where_clause:
            query += 'AND '
        else:
            query += 'WHERE '

        query += 'date >= "' + start_date_time + '" AND date <= "' + end_date_time + '" LIMIT ' + str(count)
        # print(query)

        self.__cur.execute(query)
        previous_messages = self.__cur.fetchall()
        previous_messages_to_user = []
        for previous_message in previous_messages:
            previous_message_to_user = []
            if previous_message[1] == 0:
                previous_message_to_user.append('Personal Chat')
            else:
                previous_message_to_user.append('Group Chat')

            if previous_message[4] == 0:
                previous_message_to_user.append('Sent')
            else:
                previous_message_to_user.append('Received')

            if previous_message_to_user[0] == 'Group Chat':
                group_name = self.__getGroupNameInDB(previous_message[1])
                previous_message_to_user.append(group_name)
            else:
                user_detail = self.__getUserDetailsInDBWithUserId(previous_message[0])
                previous_message_to_user.append(user_detail[2])
                previous_message_to_user.append(user_detail[1])

            previous_message_to_user.append(previous_message[2])
            if previous_message_to_user[0] == 'Group Chat' and previous_message[0] != 0:
                user_detail = self.__getUserDetailsInDBWithUserId(previous_message[0])
                previous_message_to_user.append(user_detail[2])
                previous_message_to_user.append(user_detail[1])

            previous_message_to_user.append(previous_message[3])
            previous_messages_to_user.append(previous_message_to_user)
        return previous_messages_to_user

    def changeTimeDelays(self, waiting_time_delay=None, mouse_delay=None, typing_delay=None):
        if waiting_time_delay is not None:
            if not isinstance(waiting_time_delay, float):
                print('waiting_time_delay must be float')
            else:
                self.__delay = waiting_time_delay
                self.__updateSetupField('delay', waiting_time_delay, self.__current_setup_name)

        if mouse_delay is not None:
            if not isinstance(mouse_delay, float):
                print('mouse_delay must be float')
            else:
                self.__mouse_delay = mouse_delay
                self.__updateSetupField('mouse_delay', mouse_delay, self.__current_setup_name)

        if typing_delay is not None:
            if not isinstance(typing_delay, float):
                print('typing_delay must be float')
            else:
                self.__type_delay = typing_delay
                self.__updateSetupField('type_delay', typing_delay, self.__current_setup_name)
        self.__commitDBChanges()

    def resetWhatsappBot(self):
        self.__cur.executescript('DELETE FROM MESSAGES; DELETE FROM GROUPS WHERE group_id!=0; DELETE FROM USERS WHERE user_id!=0;')
        self.__commitDBChanges()

    # below code logics is for setup
    def __callback(self, url):
        webbrowser.open_new_tab(url)

    def __insertSetupName(self, setup_name):
        self.__cur.execute(
            '''INSERT INTO SETUP (setup_name) VALUES (?)''', (setup_name,)
        )

    def __updateSetupField(self, column_name, value, setup_name):
        self.__cur.execute(
            '''UPDATE SETUP SET {}=? WHERE setup_name = ?;'''.format(column_name), (value, setup_name))

    # thread which keeps listening for mouse click
    # below function will be triggered when any mouse click happens
    def __on_click(self, x, y, button, pressed):
        if button == mouse.Button.right:
            if pressed:
                if self.__window_having_coordinates_or_color_or_input_field == 'coordinates' and self.__label_for_coordinates is not None:
                    position = pag.position()
                    self.__label_for_coordinates['text'] = str(position)
                    self.__label_for_coordinates['bg'] = 'green'
                    self.__x = position[0]
                    self.__y = position[1]
                # if self.__window_having_coordinates_or_color_or_input_field == 'color' and self.__label_for_coordinates is not None:
                #     pixel = pag.pixel(x, y)
                #     self.__label_for_coordinates['text'] = str(pixel)
                #     self.__r = pixel[0]
                #     self.__g = pixel[1]
                #     self.__b = pixel[2]

    def __clearScreen(self):
        for widget in self.__root.winfo_children():
            widget.destroy()
        self.__resetGridWeightConfig()

    def __resetGridWeightConfig(self):
        for counter in range(50):
            self.__root.grid_rowconfigure(counter, weight=0)
            self.__root.grid_columnconfigure(counter, weight=0)

    def __transitionUp(self, previous_screen_db_column, next_screen, flag_of_next_screen_field):
        if self.__window_having_coordinates_or_color_or_input_field == 'input_field':
            value = self.__input_field_for_text.get("1.0", 'end-1c')
            if value is None or value == '':
                messagebox.showerror('Field Empty', 'Please type in the field')
                return
            self.__input_field_for_text = None
            self.__updateSetupField(column_name=previous_screen_db_column, value=value,
                                    setup_name=self.__current_setup_name)

        if self.__window_having_coordinates_or_color_or_input_field == 'coordinates':
            value = self.__label_for_coordinates.cget('text')
            if value == 'Right click over point':
                messagebox.showerror('Coordinates not received', 'Right click on the specified point in your WhatApp')
                return
            self.__label_for_coordinates = None
            self.__updateSetupField(column_name=previous_screen_db_column + str(
                '_x'), value=self.__x, setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name=previous_screen_db_column + str('_y'), value=self.__y,
                                    setup_name=self.__current_setup_name)
            self.__x = None
            self.__y = None

        if self.__window_having_coordinates_or_color_or_input_field == 'color':
            value = self.__label_for_color.cget('text')
            if value == 'RGB (_,_,_)':
                messagebox.showerror('Color not received', 'Click "Get Color" button.')
                return
            self.__label_for_color = None
            self.__updateSetupField(column_name=previous_screen_db_column + str('_r'), value=self.__r,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name=previous_screen_db_column + str('_g'), value=self.__g,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name=previous_screen_db_column + str('_b'), value=self.__b,
                                    setup_name=self.__current_setup_name)
            self.__r = None
            self.__g = None
            self.__b = None

        self.__window_having_coordinates_or_color_or_input_field = flag_of_next_screen_field

        self.__clearScreen()
        self.__methods[next_screen]()

    def __instructionsScreen(self):
        def transitionFromInstruction():
            self.__clearScreen()
            self.__welcomeScreen()
            #self.__finish()

        self.__root = Tk()
        self.__listener = mouse.Listener(on_click=self.__on_click)
        self.__listener.start()
        self.__root.geometry("900x500")
        self.__root.attributes('-topmost', True)
        self.__root.title("WhatsAppBot Setup")

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)
        self.__root.grid_rowconfigure(5, weight=1)
        self.__root.grid_rowconfigure(6, weight=1)
        self.__root.grid_rowconfigure(7, weight=1)
        self.__root.grid_rowconfigure(8, weight=1)
        self.__root.grid_rowconfigure(9, weight=1)
        self.__root.grid_rowconfigure(10, weight=1)
        self.__root.grid_rowconfigure(11, weight=1)

        self.__root.grid_columnconfigure(0, weight=2)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=2)
        self.__root.grid_columnconfigure(3, weight=1)
        self.__root.grid_columnconfigure(4, weight=2)

        self.__root['bg'] = 'light blue'

        Label(self.__root, text='Our package automates the reading and sending of WhatsApp messages.', font=(
            'Aerial 10 bold'), bg="light blue", fg="red").grid(row=0, column=0, columnspan=5)

        documentation = Label(self.__root, text='Click to view Documentation',
                              font=('Aerial 10 bold'), bg="light blue", fg="green")
        documentation.grid(row=1, column=0, columnspan=5)

        documentation.bind("<Button-1>", lambda e: self.__callback("https://whatsappbotdocs.readthedocs.io/en/latest/"))

        Label(self.__root, text='We need a few co-ordinates of your WhatsApp screen.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=2, column=0, columnspan=5)

        Label(self.__root, text='Instructions are on top of each upcoming screen.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=3, column=0, columnspan=5)

        Label(self.__root, text='To view instructions, hover your mouse over the “Instructions”.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=4, column=0, columnspan=5)

        self.__instructions = 'This is a sample instruction'
        file = self.__DATA_PATH + 'instructions.png'
        instruction_image = Image.open(file)
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=5, column=0, columnspan=5)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        Label(self.__root, text='You have to RIGHT CLICK on specific locations as instructed.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=6, column=0, columnspan=5)

        Label(self.__root, text='On right click, you can notice the co-ordinates highlighted in green.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=7, column=0, columnspan=5)

        t2 = Label(self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        t2.grid(row=8, column=0)

        t3 = Label(self.__root, text='--->', fg='black', font=('Aerial', '10', 'bold'))
        t3.grid(row=8, column=1)

        file = self.__DATA_PATH + 'right_click_icon.jpg'
        right_click_image = Image.open(file)
        right_click_image = right_click_image.resize((50, 45), Image.ANTIALIAS)
        right_click_photo = ImageTk.PhotoImage(right_click_image)
        t = Label(self.__root, image=right_click_photo)
        t.grid(row=8, column=2)

        t4 = Label(self.__root, text='--->', fg='black', font=('Aerial', '10', 'bold'))
        t4.grid(row=8, column=3)

        t5 = Label(self.__root, text='Point(x=108, y=108)', bg='green', fg='white', font=('Aerial', '10', 'bold'))
        t5.grid(row=8, column=4)

        Label(self.__root, text='In case of multiple right-clicks, latest co-ordinates will be taken.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=9, column=0, columnspan=5)

        Label(self.__root, text='This way you can change the co-ordinates if you made any mistake.', font=(
            'Aerial 10'), bg='white', fg='black').grid(row=10, column=0, columnspan=5)

        next_button = Button(self.__root, text='Next', font='Aerial 10 bold', bg='blue', fg='white',
                             command=transitionFromInstruction)
        next_button.grid(row=11, column=0, columnspan=5)

        self.__root.mainloop()

    def __on_enter__for_instructions(self):
        if self.__root_for_instructions is None:
            self.__root_for_instructions = Tk()
            self.__root_for_instructions.attributes('-topmost', True)
            self.__root_for_instructions['bg'] = 'light blue'
            self.__root_for_instructions.title('Instructions')
            self.__root_for_instructions.columnconfigure(0, weight=1)
            if self.__instructions is not None:
                instructions = self.__instructions.split('\n')
                for instruction_cnt in range(0, len(instructions)):
                    if instruction_cnt % 2 == 0:
                        Label(self.__root_for_instructions, text=instructions[instruction_cnt], font=(
                            'Aerial', '10', 'bold'), fg="white", bg="blue").grid(row=instruction_cnt, column=0,
                                                                                 sticky='ew')
                    else:
                        Label(self.__root_for_instructions, text=instructions[instruction_cnt], font=(
                            'Aerial', '10', 'bold'), fg="blue", bg="light blue").grid(row=instruction_cnt, column=0,
                                                                                      sticky='ew')
            self.__root_for_instructions.mainloop()

    def __on_leave__for_instructions(self):
        if self.__root_for_instructions is not None:
            self.__root_for_instructions.destroy()
            self.__root_for_instructions = None

    def __welcomeScreen(self):
        global instruction_image, instruction_photo

        def transitionFromWelcome():
            setup_name_entered_by_user = setup_name.get("1.0", 'end-1c')
            if setup_name_entered_by_user == '' or setup_name_entered_by_user is None:
                messagebox.showerror('Setup Name Empty', 'Please enter a setup name')
                return
            if setup_name_entered_by_user.lower() == 'create a new setup':
                messagebox.showerror('Reserved', 'This name is reserved for creating a new setup')
                return
            if self.__setupNameExistsInDb(setup_name_entered_by_user):
                messagebox.showerror('Already defined', 'This setup name is already defined')
                return
            self.__insertSetupName(setup_name_entered_by_user)
            self.__current_setup_name = setup_name_entered_by_user
            # below code is for attributing next screen contents
            # next screen is for getting whatsapp path
            self.__window_having_coordinates_or_color_or_input_field = None
            self.__clearScreen()
            self.__whatsappVersionDropDown()

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=20)
        self.__root.grid_rowconfigure(3, weight=8)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)

        Label(self.__root, text="Hover below to view", font='Aerial 10 bold', bg='light blue').grid(row=0, column=0,
                                                                                                    columnspan=2)

        self.__instructions = "Enter a name that is easy for you to remember.\nAll the configuration that you will " \
                              "do from now will be stored against this name.\nUse this name while creating an " \
                              "instance of WhatsAppBot from its constructor.\n wt_object = WhatsAppBot('setup_name')"
        file = self.__DATA_PATH + 'instructions.png'
        instruction_image = Image.open(file)
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=1, column=0, columnspan=2)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        Label(self.__root, text="Enter a Setup Name", font='Aerial 10').grid(row=2, column=0)
        setup_name = Text(self.__root, width=30, height=2)
        setup_name.grid(row=2, column=1)

        next_button = Button(self.__root, text='Next', font=('Aerial', '10', 'bold'), bg='blue', fg='white',
                             command=transitionFromWelcome)
        next_button.grid(row=3, column=0, columnspan=2)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=2)
        progress_bar['value'] = 5

        # just to load tkvideo for better experience and faster loading time later
        kebab_video = Label(self.__root)
        kebab_player = tkvideo(r"KebabMenu.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

    def __whatsappVersionDropDown(self):

        global web_image, web_photo, wat_desktop_image, wat_desktop_photo
        global wat_desktop_microsoft_image, wat_desktop_microsoft_photo, mac_image, mac_photo

        def transitionFromVersion():
            version = clicked.get()
            if version == '-- Select your whatsapp version --':
                messagebox.showerror(
                    'Choose Version', 'Please select the version you are using')
                return

            if version == 'Whatsapp Desktop Windows from Microsoft Store':
                messagebox.showerror(
                    'Version Unavailable',
                    'Currently this latest windows version is not supported. Use Whatsapp Web for your windows instead')
                return

            self.__updateSetupField('wt_version', str(version), self.__current_setup_name)
            self.__window_having_coordinates_or_color_or_input_field = 'coordinates'
            self.__clearScreen()
            self.__version = version
            if version == 'Whatsapp Desktop Windows from Microsoft Store':
                self.__msStoreContactInfoCoordinates()
            else:
                self.__kebabMenuCoordinates()

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=3)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=3)
        self.__root.grid_rowconfigure(5, weight=1)
        self.__root.grid_rowconfigure(6, weight=1)
        self.__root.grid_rowconfigure(7, weight=1)

        Label(self.__root, text='Select WhatsApp Version you are using from the drop down below', bg='light blue',
              fg='black', font=('Aerial', '10', 'bold')).grid(row=0, column=0, columnspan=2)

        # Dropdown menu options
        options = [
            "-- Select your whatsapp version --",
            "Whatsapp Web",
            "Whatsapp Desktop Windows",
            "Whatsapp Desktop Windows from Microsoft Store",
            "Mac"
        ]

        # datatype of menu text
        clicked = StringVar()
        # initial menu text
        clicked.set("-- Select your whatsapp version --")

        helv36 = tkFont.Font(family='Helvetica', size=15)
        drop = OptionMenu(self.__root, clicked, *options)
        drop.grid(row=1, column=0, columnspan=2)
        drop.config(font=helv36)

        file = self.__DATA_PATH + 'whatsapp_web.jpeg'
        web_image = Image.open(file)
        web_image = web_image.resize(
            (260, 150), Image.ANTIALIAS)
        web_photo = ImageTk.PhotoImage(web_image)
        t = Label(self.__root, image=web_photo)
        t.grid(row=2, column=0)

        Label(self.__root, text='Whatsapp Web(Ubuntu also)', fg='black', font=('Aerial', '10', 'bold')).grid(row=3,
                                                                                                             column=0)

        file = self.__DATA_PATH + 'whatsapp_desktop.jpeg'
        wat_desktop_image = Image.open(file)
        wat_desktop_image = wat_desktop_image.resize(
            (260, 150), Image.ANTIALIAS)
        wat_desktop_photo = ImageTk.PhotoImage(wat_desktop_image)
        t = Label(self.__root, image=wat_desktop_photo)
        t.grid(row=2, column=1)

        Label(self.__root, text='Whatsapp Desktop Windows', fg='black', font=('Aerial', '10', 'bold')).grid(row=3,
                                                                                                            column=1)

        file = self.__DATA_PATH + 'whatsapp_microsoft.jpeg'
        wat_desktop_microsoft_image = Image.open(file)
        wat_desktop_microsoft_image = wat_desktop_microsoft_image.resize(
            (260, 150), Image.ANTIALIAS)
        wat_desktop_microsoft_photo = ImageTk.PhotoImage(wat_desktop_microsoft_image)
        t = Label(self.__root, image=wat_desktop_microsoft_photo)
        t.grid(row=4, column=0)

        Label(self.__root, text='Whatsapp Desktop(Microsoft Store)', fg='black', font=('Aerial', '10', 'bold')).grid(
            row=5, column=0)

        mac_image = Image.open(self.__DATA_PATH + 'apple.jpg')
        mac_image = mac_image.resize(
            (150, 150), Image.ANTIALIAS)
        mac_photo = ImageTk.PhotoImage(mac_image)
        t = Label(self.__root, image=mac_photo)
        t.grid(row=4, column=1)

        Label(self.__root, text='Mac', fg='black', font=('Aerial', '10', 'bold')).grid(row=5, column=1)

        next_button = Button(self.__root, text='Next', font=('Aerial', '10', 'bold'), bg='blue', fg='white',
                             command=transitionFromVersion)
        next_button.grid(row=6, column=0, columnspan=2)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=7, column=0, columnspan=2)
        progress_bar['value'] = 10

    def __kebabMenuCoordinates(self):
        global instruction_image, instruction_photo
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        self.__instructions = "Open WhatsApp. Open any chat which is a saved contact.\nRight-click on the kebab menu " \
                              "(3-dot icon) on the top right corner which you use to open the dropdown as shown " \
                              "below.\nNOTE: Right-click won’t open the dropdown. It is only to get the " \
                              "co-ordinates.\nAfter right-clicking on 3 dot kebab menu, you can the see the " \
                              "co-ordinates being displayed in green in the setup.\nDon’t accidentally right-click " \
                              "anywhere else. If so, right-click on kebab menu again.\nAfter right " \
                              "clicking, you are good to go, left-click next. "
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize(
            (192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        please_wait = Label(self.__root, text="Please wait...      loading ...", bg='light blue', font='Aerial 10')
        please_wait.grid(row=2, column=0)
        kebab_video = Label(self.__root)
        kebab_player = tkvideo(self.__DATA_PATH + "KebabMenu.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()
        kebab_video.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='kebab_menu_coordinates',
                                                                 next_screen='__contactInfoCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 15

    def __contactInfoCoordinates(self):
        global instruction_image, instruction_photo
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        self.__instructions = 'Now, left-click the 3-dot icon to open the dropdown menu in WhatsApp.\nThen, ' \
                              'right-click the “Contact Info” option in the dropdown menu.\nMake sure the ' \
                              'co-ordinates are displayed in green.\nNOTE: Right-click won’t open the contact info. ' \
                              'It is only for co-ordinates.\nDon’t accidentally right-click anywhere else. If so, ' \
                              'you can right-click again on “Contact Info” option again.\nLeft-click next. '
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize(
            (192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        please_wait = Label(self.__root, text="Please wait...      loading ...", bg='light blue', font='Aerial 10')
        please_wait.grid(row=2, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "ContactInfo.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='contact_info_coordinates',
                                                                 next_screen='__contactInfoField1Coordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 20

    def __contactInfoField1Coordinates(self):
        global instruction_image, instruction_photo
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        self.__instructions = 'Open Contact Info (Left-click on the “Contact Info” to open it).\nRight-click on the ' \
                              'middle of the contact name to get the co-ordinates.\nClick next. '
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize(
            (192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        please_wait = Label(self.__root, text="Please wait...      loading ...", bg='light blue', font='Aerial 10')
        please_wait.grid(row=2, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "ContactInfoField1.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field1_coordinates',
                                 next_screen='__contactInfoField2Coordinates',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 25

    def __contactInfoField2Coordinates(self):
        global instruction_image, instruction_photo
        global field2_photo, field2_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on the position highlighted by green dot in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)

        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        field2_image = Image.open(self.__DATA_PATH + 'field2.png')
        field2_image = field2_image.resize((240, 350), Image.ANTIALIAS)
        field2_photo = ImageTk.PhotoImage(field2_image)
        t = Label(self.__root, image=field2_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field2_coordinates',
                                 next_screen='__contactInfoField2CoordinatesForGroup',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 30

    def __contactInfoField2CoordinatesForGroup(self):
        global field2group_photo, field2group_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on the position highlighted by green dot in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        field2group_image = Image.open(self.__DATA_PATH + 'field2group.png')
        field2group_image = field2group_image.resize(
            (240, 350), Image.ANTIALIAS)
        field2group_photo = ImageTk.PhotoImage(field2group_image)
        t = Label(self.__root, image=field2group_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field2_coordinates_for_group',
                                 next_screen='__closeContactInfoField',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 35

    def __closeContactInfoField(self):
        global close_photo, close_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on the close contact info icon in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        close_image = Image.open(self.__DATA_PATH + 'close_contact.jpg')
        close_image = close_image.resize((240, 350), Image.ANTIALIAS)
        close_photo = ImageTk.PhotoImage(close_image)
        t = Label(self.__root, image=close_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='close_contact_info_coordinates',
                                 next_screen='__topLeftInChat',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 40

    def __msStoreContactInfoCoordinates(self):
        Label(self.__root, text="__msStoreContactInfoCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(previous_screen_db_column='contact_info_coordinates',
                                                                 next_screen='__msStoreContactInfoField1Coordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __msStoreContactInfoField1Coordinates(self):
        Label(self.__root, text="__msStoreContactInfoField1Coordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field1_coordinates',
                                 next_screen='__msStoreContactInfoField2Coordinates',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __msStoreContactInfoField2Coordinates(self):
        Label(self.__root, text="__msStoreContactInfoField2Coordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field2_coordinates',
                                 next_screen='__msStoreContactInfoField2CoordinatesForUnsaved',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __msStoreContactInfoField2CoordinatesForUnsaved(self):
        Label(self.__root, text="__msStoreContactInfoField2CoordinatesForUnsaved").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='contact_info_field2_coordinates_for_unsaved',
                                 next_screen='__msStoreCloseContactInfoField',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __msStoreCloseContactInfoField(self):
        Label(self.__root, text="__msStoreCloseContactInfoField").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='close_contact_info_coordinates',
                                 next_screen='__latestMessageCoordinates',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __latestMessageCoordinates(self):
        Label(self.__root, text="__latestMessageCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(previous_screen_db_column='latest_message_coordinates',
                                                                 next_screen='__copyAfterLatestMessageCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __copyAfterLatestMessageCoordinates(self):
        Label(self.__root, text="__copyAfterLatestMessageCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='copy_latest_message_coordinates',
                                 next_screen='__topLeftInChat',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __topLeftInChat(self):
        global topleft_photo, topleft_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Close Contact Info and then, Right click on the top right corner of the chat.",
              font=('Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        topleft_image = Image.open(self.__DATA_PATH + 'topleft.png')
        topleft_image = topleft_image.resize((640, 360), Image.ANTIALIAS)
        topleft_photo = ImageTk.PhotoImage(topleft_image)
        t = Label(self.__root, image=topleft_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='top_left_in_chat',
                                                                 next_screen='__bottomRightInChat',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 45

    def __bottomRightInChat(self):
        global bottomleft_photo, bottomleft_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on the bottom most part of chat, parallel to the highlighted line", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        bottomleft_image = Image.open(self.__DATA_PATH + 'bottomleft.png')
        bottomleft_image = bottomleft_image.resize((640, 360), Image.ANTIALIAS)
        bottomleft_photo = ImageTk.PhotoImage(bottomleft_image)
        t = Label(self.__root, image=bottomleft_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='bottom_right_in_chat',
                                                                 next_screen='__typeMessageCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 50

    def __typeMessageCoordinates(self):
        global type_msg_photo, type_msg_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on the type message box in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        type_msg_image = Image.open(self.__DATA_PATH + 'type_message.png')
        type_msg_image = type_msg_image.resize((640, 360), Image.ANTIALIAS)
        type_msg_photo = ImageTk.PhotoImage(type_msg_image)
        t = Label(self.__root, image=type_msg_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='type_message_coordinates',
                                                                 next_screen='__sendMessageCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 55

    def __sendMessageCoordinates(self):
        global send_msg_photo, send_msg_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on send message in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        send_msg_image = Image.open(self.__DATA_PATH + 'send_message.png')
        send_msg_image = send_msg_image.resize((640, 360), Image.ANTIALIAS)
        send_msg_photo = ImageTk.PhotoImage(send_msg_image)
        t = Label(self.__root, image=send_msg_photo)
        t.grid(row=2, column=0)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='send_message_coordinates',
                                                                 next_screen='__sendImageCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 60

    def __sendImageCoordinates(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Copy and paste some image. Then RIGHT CLICK on the send image button.", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        please_wait = Label(self.__root, text="Please wait...      loading ...", bg='light blue', font='Aerial 10')
        please_wait.grid(row=2, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "SendImage.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='send_image_coordinates',
                                                                 next_screen='__searchBarCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 65

    def __searchBarCoordinates(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root,
              text="Right click on the Right-most part of search bar where the mouse cursor turns to an I-cursor.",
              font=('Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        please_wait = Label(self.__root, text="Please wait...      loading ...", bg='light blue', font='Aerial 10')
        please_wait.grid(row=2, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "SearchBar.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        if self.__version == 'Whatsapp Desktop Windows from Microsoft Store':
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(previous_screen_db_column='search_bar_coordinates',
                                                                     next_screen='__kebabMenuFilterCoordinates',
                                                                     flag_of_next_screen_field='coordinates'))
        else:
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(previous_screen_db_column='search_bar_coordinates',
                                                                     next_screen='__unreadChatCoordinates',
                                                                     flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)
        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 70

    def __unreadChatCoordinates(self):

        global instruction_image, instruction_photo
        global unread_big_image, unread_big_photo, unread_crct_image, unread_crct_photo
        global unread_wrong1_image, unread_wrong1_photo, unread_wrong2_image, unread_wrong2_photo

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)
        self.__root.grid_rowconfigure(5, weight=1)
        self.__root.grid_rowconfigure(6, weight=1)

        self.__root.grid_columnconfigure(0, weight=8)
        self.__root.grid_columnconfigure(1, weight=3)

        Label(self.__root, text="Right click on the position highlighted by green dot in your WhatsApp", font=(
            'Aerial', '10', 'bold'), bg='white', fg='blue').grid(row=0, column=0, columnspan=2)

        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0, columnspan=2)

        unread_big_image = Image.open(self.__DATA_PATH + 'unreadbig.png')
        unread_big_image = unread_big_image.resize((660, 360), Image.ANTIALIAS)
        unread_big_photo = ImageTk.PhotoImage(unread_big_image)
        t = Label(self.__root, image=unread_big_photo)
        t.grid(row=2, column=0, rowspan=3)

        unread_crct_image = Image.open(self.__DATA_PATH + 'unread_correct.png')
        unread_crct_image = unread_crct_image.resize(
            (100, 100), Image.ANTIALIAS)
        unread_crct_photo = ImageTk.PhotoImage(unread_crct_image)
        t = Label(self.__root, image=unread_crct_photo)
        t.grid(row=2, column=1)

        unread_wrong1_image = Image.open(self.__DATA_PATH + 'unread_wrong1.png')
        unread_wrong1_image = unread_wrong1_image.resize(
            (100, 100), Image.ANTIALIAS)
        unread_wrong1_photo = ImageTk.PhotoImage(unread_wrong1_image)
        t = Label(self.__root, image=unread_wrong1_photo)
        t.grid(row=3, column=1)

        unread_wrong2_image = Image.open(self.__DATA_PATH + 'unread_wrong2.png')
        unread_wrong2_image = unread_wrong2_image.resize(
            (100, 100), Image.ANTIALIAS)
        unread_wrong2_photo = ImageTk.PhotoImage(unread_wrong2_image)
        t = Label(self.__root, image=unread_wrong2_photo)
        t.grid(row=4, column=1)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='unread_chat_filter_coordinates',
                                 next_screen='__unreadOn',
                                 flag_of_next_screen_field='color'))
        next_button.grid(row=5, column=0, columnspan=2)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=6, column=0, columnspan=2)
        progress_bar['value'] = 75

    def __getUnreadCoordinates(self, setup_name):
        self.__cur.execute(
            'SELECT unread_chat_filter_coordinates_x,unread_chat_filter_coordinates_y FROM SETUP WHERE setup_name=?',
            (setup_name,))
        return self.__cur.fetchone()

    def __rgb_to_hex(self, rgb):
        # translates an rgb tuple of int to a tkinter friendly color code
        return "#%02x%02x%02x" % rgb

    def __unreadOn(self):

        global instruction_image, instruction_photo
        global chosen_color

        def transitionToOff():
            value = self.__label_for_color.cget('text')
            if value == 'RGB (_,_,_)':
                messagebox.showerror('Color not received', 'Click "Get Color" button after turning on unread chat '
                                                           'filter. Make sure the filter is visible on screen')
                return
            self.__label_for_color = None
            self.__clearScreen()
            self.__unreadOff()

        def getPixel():
            x, y = self.__getUnreadCoordinates(self.__current_setup_name)
            r, g, b = pag.pixel(x, y)
            self.__updateSetupField(column_name='unread_chat_filter_on_r', value=r,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='unread_chat_filter_on_g', value=g,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='unread_chat_filter_on_b', value=b,
                                    setup_name=self.__current_setup_name)

            self.__label_for_color['text'] = str(r) + ',' + str(g) + ',' + str(b)
            chosen_color['fg'] = self.__rgb_to_hex((r, g, b))
            chosen_color['bg'] = self.__rgb_to_hex((r, g, b))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=4)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=4)

        self.__instructions = "Open WhatsApp and keep this setup application on top.\nTurn on the unread chat " \
                              "filter.\nNote: The setup application should not be over the unread chat filter.\nThen " \
                              "click on the 'Get Color' button.\nMost likely you will green color on the setup " \
                              "field.\nMake a note of the RGB values.\nClick Next."
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0, columnspan=3)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_color = Label(self.__root, text='RGB (_,_,_)', font=('Aerial', '10'))
        self.__label_for_color.grid(row=1, column=0, sticky='e')
        chosen_color = Label(self.__root, fg='black', text='No color selected', borderwidth=1, relief='solid')
        chosen_color.grid(row=1, column=1)
        get_pixel_button = Button(self.__root, text="Get Color", bg='red', fg='white', font=('Aerial', '10'),
                                  command=getPixel)
        get_pixel_button.grid(row=1, column=2, sticky='w')

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0, columnspan=3)
        kebab_player = tkvideo(self.__DATA_PATH + "unread_cordinate_on.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=transitionToOff)
        next_button.grid(row=3, column=0, columnspan=3)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 78

    def __unreadOff(self):
        global instruction_image, instruction_photo
        global chosen_color

        def transitionToFirstUnderFilter():
            value = self.__label_for_color.cget('text')
            if value == 'RGB (_,_,_)':
                messagebox.showerror('Color not received', 'Click "Get Color" button after turning off unread chat '
                                                           'filter. Make sure the filter is visible on screen')
                return

            self.__label_for_color = None
            self.__clearScreen()
            self.__window_having_coordinates_or_color_or_input_field = 'coordinates'
            self.__firstChatUnderFilterCoordinates()

        def getPixel():
            x, y = self.__getUnreadCoordinates(self.__current_setup_name)
            r, g, b = pag.pixel(x, y)
            self.__updateSetupField(column_name='unread_chat_filter_off_r', value=r,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='unread_chat_filter_off_g', value=g,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='unread_chat_filter_off_b', value=b,
                                    setup_name=self.__current_setup_name)

            self.__label_for_color['text'] = str(r) + ',' + str(g) + ',' + str(b)
            chosen_color['fg'] = self.__rgb_to_hex((r, g, b))
            chosen_color['bg'] = self.__rgb_to_hex((r, g, b))

        def transitionToUnreadFilter():
            self.__clearScreen()
            self.__label_for_color = None
            self.__r = None
            self.__g = None
            self.__b = None
            self.__window_having_coordinates_or_color_or_input_field = 'coordinates'
            self.__unreadChatCoordinates()

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=4)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=4)

        self.__instructions = "Now turn off the unread chat filter.\nClick on the 'Get Color' button.\nCompare this " \
                              "color with the previous color taken with unread chat filter on.\nIt should be " \
                              "different.\nIf it is not different and of the same color, click on the 'Try Again' " \
                              "button.\nThis means that you have not properly taken the unread coordinates.\nIf it " \
                              "is different as expected, click Next. "
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0, columnspan=3)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_color = Label(self.__root, text='RGB (_,_,_)', font=('Aerial', '10'))
        self.__label_for_color.grid(row=1, column=0, sticky='e')
        chosen_color = Label(self.__root, fg='black', text='No color selected', borderwidth=1, relief='solid')
        chosen_color.grid(row=1, column=1)
        get_pixel_button = Button(self.__root, text="Get Color", bg='red', fg='white', font=('Aerial', '10'),
                                  command=getPixel)
        get_pixel_button.grid(row=1, column=2, sticky='w')

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0, columnspan=3)
        kebab_player = tkvideo(self.__DATA_PATH + "unread_cordinate_off.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        button_to_unread = Button(self.__root, text='Try again (same color)', bg='red', fg='white',
                                  font=('Aerial', '10', 'bold'), command=transitionToUnreadFilter)
        button_to_unread.grid(row=3, column=0, sticky='e')

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=transitionToFirstUnderFilter)
        next_button.grid(row=3, column=2, sticky='w')

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 80

    def __firstChatUnderFilterCoordinates(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Turn on the unread chat filter. Now right-click on the first chat under the filter.",
              bg='white', fg='blue', font=('Aerial', '10', 'bold')).grid(row=0, column=0)
        self.__label_for_coordinates = Label(self.__root, text='Right click over point', bg='red', fg='white',
                                             font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "FirstChatUnread.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        if self.__version == "Whatsapp Web":
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(
                                     previous_screen_db_column='first_chat_under_filter_coordinates',
                                     next_screen='__whatsappCoordinates',
                                     flag_of_next_screen_field='coordinates'))
        elif self.__version == "Whatsapp Desktop Windows" or self.__version == "Mac":
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(
                                     previous_screen_db_column='first_chat_under_filter_coordinates',
                                     next_screen='__whatsappPathScreen',
                                     flag_of_next_screen_field='input_field'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 82

    def __kebabMenuFilterCoordinates(self):
        Label(self.__root, text="__kebabMenuFilterCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='kebab_menu_for_filter_coordinates',
                                 next_screen='__filterByCoordinates',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __filterByCoordinates(self):
        Label(self.__root, text="__filterByCoordinates").grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(previous_screen_db_column='filter_by_coordinates',
                                                                 next_screen='__unreadCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __unreadCoordinates(self):
        Label(self.__root, text="__unreadCoordinates").grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(previous_screen_db_column='unread_coordinates',
                                                                 next_screen='__closeFilterCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __closeFilterCoordinates(self):
        Label(self.__root, text="__closeFilterCoordinates").grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(previous_screen_db_column='close_filter_coordinates',
                                                                 next_screen='__firstChatUnderCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __firstChatUnderCoordinates(self):
        # for windows latest
        Label(self.__root, text="__firstChatUnderFilterCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='first_chat_under_filter_coordinates',
                                 next_screen='__secondChatUnderCoordinates',
                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=2, column=0)

    def __secondChatUnderCoordinates(self):
        # for windows latest
        Label(self.__root, text="__secondChatUnderCoordinates").grid(
            row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point')
        self.__label_for_coordinates.grid(row=0, column=1)

        next_button = Button(self.__root, text='Next',
                             command=lambda: self.__transitionUp(
                                 previous_screen_db_column='second_chat_under_filter_coordinates',
                                 next_screen='__whatsappPathScreen',
                                 flag_of_next_screen_field='input_field'))
        next_button.grid(row=2, column=0)

    def __whatsappPathScreen(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Please paste the WhatsApp path. A sample for Windows is shown below.",
              font=('Aerial', '10', 'bold'), fg='blue', bg='white').grid(row=0, column=0)
        self.__input_field_for_text = Text(self.__root, width=30, height=2)
        self.__input_field_for_text.grid(row=1, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "whatsappPath.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='whatsapp_path',
                                                                 next_screen='__whatsappCoordinates',
                                                                 flag_of_next_screen_field='coordinates'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 83

    def __whatsappCoordinates(self):
        global instruction_image, instruction_photo
        global new_msg_wrong_image, new_msg_wrong_photo
        global new_msg_correct_image, new_msg_correct_photo, new_msg_correct_image2, new_msg_correct_photo2
        if self.__version == "Whatsapp Desktop Windows" or self.__version == "Mac":
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_rowconfigure(1, weight=1)
            self.__root.grid_rowconfigure(2, weight=1)
            self.__root.grid_rowconfigure(3, weight=1)
            self.__root.grid_rowconfigure(4, weight=1)
            self.__root.grid_rowconfigure(5, weight=1)
            self.__root.grid_rowconfigure(6, weight=1)

            self.__root.grid_columnconfigure(0, weight=8)
            self.__root.grid_columnconfigure(1, weight=3)

            if self.__version == 'Mac':
                self.__instructions = "Open System Preferences and navigate into 'Dock & Menu Bar'.\nCheck mark the " \
                                      "'Minimise windows into application icon' if not checked already.\nOpen " \
                                      "WhatsApp and make sure you have unread messages.\nIf you don't have unread " \
                                      "messages, send one from your friend's number.\nMake sure you have the red dot " \
                                      "with number of unread messages in the whatsapp icon.\nThen right click on the " \
                                      "outer most part of the red circle in WhatsApp icon in taskbar.\nClick Next."

            if self.__version == 'Whatsapp Desktop Windows':
                self.__instructions = "Open WhatsApp and make sure you have unread messages.\nIf you don't have " \
                                      "unread messages, send one from your friend's number.\nMake sure you have the " \
                                      "red dot with number of unread messages in the whatsapp icon.\nMove WhatsApp to " \
                                      "left-most part as shown in video.\nWhenever you are running WhatsAppBot with " \
                                      "this setup, make sure WhatsApp is in the left-most part.\nThen right click on " \
                                      "the outer most part of the red circle in WhatsApp icon in taskbar.\nClick Next."

            instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
            instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
            instruction_photo = ImageTk.PhotoImage(instruction_image)
            t = Label(self.__root, image=instruction_photo)
            t.grid(row=0, column=0, columnspan=2)
            t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
            t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

            self.__label_for_coordinates = Label(self.__root, text='Right click over point', bg='red', fg='white',
                                                 font=('Aerial', '10', 'bold'))
            self.__label_for_coordinates.grid(row=1, column=0, columnspan=2)

            kebab_video = Label(self.__root)
            kebab_video.grid(row=2, column=0, rowspan=3)
            if self.__version == 'Mac':
                kebab_player = tkvideo(self.__DATA_PATH + "mac_whatsapp_squared.mp4", kebab_video, loop=1, size=(354, 360))
                kebab_player.play()

            if self.__version == 'Whatsapp Desktop Windows':
                kebab_player = tkvideo(self.__DATA_PATH + "MoveWhatsappIconToLeft.mp4", kebab_video, loop=1, size=(640, 360))
                kebab_player.play()

            new_msg_wrong_image = Image.open(self.__DATA_PATH + 'wt_icon_wrong.png')
            new_msg_wrong_image = new_msg_wrong_image.resize((114, 94), Image.ANTIALIAS)
            new_msg_wrong_photo = ImageTk.PhotoImage(new_msg_wrong_image)
            t = Label(self.__root, image=new_msg_wrong_photo)
            t.grid(row=2, column=1)

            new_msg_correct_image = Image.open(self.__DATA_PATH + 'wt_icon_crt2.png')
            new_msg_correct_image = new_msg_correct_image.resize((114, 94), Image.ANTIALIAS)
            new_msg_correct_photo = ImageTk.PhotoImage(new_msg_correct_image)
            t = Label(self.__root, image=new_msg_correct_photo)
            t.grid(row=3, column=1)

            new_msg_correct_image2 = Image.open(self.__DATA_PATH + 'wt_icon_crt.png')
            new_msg_correct_image2 = new_msg_correct_image2.resize((114, 94), Image.ANTIALIAS)
            new_msg_correct_photo2 = ImageTk.PhotoImage(new_msg_correct_image2)
            t = Label(self.__root, image=new_msg_correct_photo2)
            t.grid(row=4, column=1)

            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(previous_screen_db_column='whatsapp_coordinates',
                                                                     next_screen='__whatsappNewMsgs',
                                                                     flag_of_next_screen_field='color'))
            next_button.grid(row=5, column=0, columnspan=2)

            progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
            progress_bar.grid(row=6, column=0, columnspan=2)
            progress_bar['value'] = 84

        elif self.__version == 'Whatsapp Web':
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_rowconfigure(1, weight=1)
            self.__root.grid_rowconfigure(2, weight=1)
            self.__root.grid_rowconfigure(3, weight=1)

            self.__root.grid_columnconfigure(0, weight=1)

            self.__instructions = "Move Chrome (or the brower in which WhatsApp Web is running) to left-most part as shown in video.\nWhenever you are running WhatsAppBot with this setup, make sure the browser is in the left-most part.\nThen right click on the brower to get its coordinates.\nClick Next. "
            instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
            instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
            instruction_photo = ImageTk.PhotoImage(instruction_image)
            t = Label(self.__root, image=instruction_photo)
            t.grid(row=0, column=0)
            t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
            t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

            self.__label_for_coordinates = Label(self.__root, text='Right click over point', bg='red', fg='white',
                                                 font=('Aerial', '10', 'bold'))
            self.__label_for_coordinates.grid(row=1, column=0)

            kebab_video = Label(self.__root)
            kebab_video.grid(row=2, column=0)
            kebab_player = tkvideo(self.__DATA_PATH + "whatsapp_web_move.mp4", kebab_video, loop=1, size=(640, 360))
            kebab_player.play()

            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(previous_screen_db_column='whatsapp_coordinates',
                                                                     next_screen='__minimizeWhatsappCoordinates',
                                                                     flag_of_next_screen_field='coordinates'))
            next_button.grid(row=3, column=0)

            progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
            progress_bar.grid(row=4, column=0)
            progress_bar['value'] = 84

    def __getWhatsappCoordinates(self, setup_name):
        self.__cur.execute(
            'SELECT whatsapp_coordinates_x,whatsapp_coordinates_y FROM SETUP WHERE setup_name=?', (setup_name,))
        return self.__cur.fetchone()

    def __whatsappNewMsgs(self):
        global instruction_image, instruction_photo
        global chosen_color

        def transitionToOff():
            value = self.__label_for_color.cget('text')
            if value == 'RGB (_,_,_)':
                messagebox.showerror('Color not received', 'Click "Get Color" button. Make sure there are unread '
                                                           'messages.')
                return

            self.__label_for_color = None
            self.__clearScreen()
            self.__whatsappNoNewMsgs()

        def getPixel():
            x, y = self.__getWhatsappCoordinates(self.__current_setup_name)
            r, g, b = pag.pixel(x, y)
            self.__updateSetupField(column_name='whatsapp_new_msg_r', value=r,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='whatsapp_new_msg_g', value=g,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='whatsapp_new_msg_b', value=b,
                                    setup_name=self.__current_setup_name)
            self.__label_for_color['text'] = str(r) + ',' + str(g) + ',' + str(b)
            chosen_color['fg'] = self.__rgb_to_hex((r, g, b))
            chosen_color['bg'] = self.__rgb_to_hex((r, g, b))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=4)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=4)

        self.__instructions = "Open WhatsApp and make sure you have unread messages.\nIf you don't have unread " \
                              "messages, send one from your friend's number.\n Make sure you have the red dot with " \
                              "number of unread messages in the whatsapp icon.\nThen click on the 'Get Color' " \
                              "button.\nMost likely you will get red color on the setup field.\nMake a note of the " \
                              "RGB values.\nClick Next. "
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0, columnspan=3)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_color = Label(self.__root, text='RGB (_,_,_)', font=('Aerial', '10'))
        self.__label_for_color.grid(row=1, column=0, sticky='e')
        chosen_color = Label(self.__root, fg='black', text='No color selected', borderwidth=1, relief='solid')
        chosen_color.grid(row=1, column=1)
        get_pixel_button = Button(self.__root, text="Get Color", bg='red', fg='white', font=('Aerial', '10'),
                                  command=getPixel)
        get_pixel_button.grid(row=1, column=2, sticky='w')

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0, columnspan=3)
        kebab_player = tkvideo(self.__DATA_PATH + "wt_new_msg.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=transitionToOff)
        next_button.grid(row=3, column=0, columnspan=3)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 85

    def __whatsappNoNewMsgs(self):
        global instruction_image, instruction_photo
        global chosen_color

        def transitionToMinimize():
            value = self.__label_for_color.cget('text')
            if value == 'RGB (_,_,_)':
                messagebox.showerror('Color not received', 'Click "Get Color" button after reading all messages.')
                return
            self.__label_for_color = None
            self.__clearScreen()
            self.__window_having_coordinates_or_color_or_input_field = 'coordinates'
            self.__minimizeWhatsappCoordinates()

        def getPixel():
            x, y = self.__getWhatsappCoordinates(self.__current_setup_name)
            r, g, b = pag.pixel(x, y)
            self.__updateSetupField(column_name='whatsapp_no_new_msg_r', value=r,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='whatsapp_no_new_msg_g', value=g,
                                    setup_name=self.__current_setup_name)
            self.__updateSetupField(column_name='whatsapp_no_new_msg_b', value=b,
                                    setup_name=self.__current_setup_name)

            self.__label_for_color['text'] = str(r) + ',' + str(g) + ',' + str(b)
            chosen_color['fg'] = self.__rgb_to_hex((r, g, b))
            chosen_color['bg'] = self.__rgb_to_hex((r, g, b))

        def transitionToWhatsAppCoordinates():
            self.__clearScreen()
            self.__label_for_color = None
            self.__r = None
            self.__g = None
            self.__b = None
            self.__window_having_coordinates_or_color_or_input_field = 'coordinates'
            self.__whatsappCoordinates()

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=4)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=4)

        self.__instructions = "Open WhatsApp and read all the messages.\nMake sure you don't have the red dot with " \
                              "number of unread messages in the whatsapp icon.\nClick on the 'Get Color' " \
                              "button.\nCompare this color with the previous color taken with unread messages.\nIt " \
                              "should be different.\nIt is usually green in color or white.\nIf it is not different " \
                              "and of the same color, click on the 'Try Again' button.\nThis means that you have not " \
                              "properly taken the WhatsApp icon coordinates.\nIf it is different as expected, " \
                              "click Next. "

        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0, columnspan=3)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        self.__label_for_color = Label(self.__root, text='RGB (_,_,_)', font=('Aerial', '10'))
        self.__label_for_color.grid(row=1, column=0, sticky='e')
        chosen_color = Label(self.__root, fg='black', text='No color selected', borderwidth=1, relief='solid')
        chosen_color.grid(row=1, column=1)
        get_pixel_button = Button(self.__root, text="Get Color", bg='red', fg='white', font=('Aerial', '10'),
                                  command=getPixel)
        get_pixel_button.grid(row=1, column=2, sticky='w')

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0, columnspan=3)
        kebab_player = tkvideo(self.__DATA_PATH + "wt_no_new_msg.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        button_to_wt_cor = Button(self.__root, text='Try again (same color)', bg='red', fg='white',
                                  font=('Aerial', '10', 'bold'), command=transitionToWhatsAppCoordinates)
        button_to_wt_cor.grid(row=3, column=0, sticky='e')

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=transitionToMinimize)
        next_button.grid(row=3, column=2, sticky='w')

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 86

    def __minimizeWhatsappCoordinates(self):
        global minimize_photo, minimize_image
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on minimize WhatsApp ", bg='white', fg='blue',
              font=('Aerial', '10', 'bold')).grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        minimize_image = Image.open(self.__DATA_PATH + 'minimize.png')
        minimize_image = minimize_image.resize((640, 360), Image.ANTIALIAS)
        minimize_photo = ImageTk.PhotoImage(minimize_image)
        t = Label(self.__root, image=minimize_photo)
        t.grid(row=2, column=0)

        if self.__version == 'Whatsapp Desktop Windows':
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(
                                     previous_screen_db_column='minimize_whatsapp_coordinates',
                                     next_screen='__showDesktopCoordinates',
                                     flag_of_next_screen_field='coordinates'))
        else:
            next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                                 command=lambda: self.__transitionUp(
                                     previous_screen_db_column='minimize_whatsapp_coordinates',
                                     next_screen='__timeDelay',
                                     flag_of_next_screen_field=None))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 87

    def __showDesktopCoordinates(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root, text="Right click on Show Desktop.", bg='white', fg='blue',
              font=('Aerial', '10', 'bold')).grid(row=0, column=0)
        self.__label_for_coordinates = Label(
            self.__root, text='Right click over point', bg='red', fg='white', font=('Aerial', '10', 'bold'))
        self.__label_for_coordinates.grid(row=1, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "showDesktop.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='show_desktop_coordinates',
                                                                 next_screen='__timeDelay',
                                                                 flag_of_next_screen_field=None))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 89

    def __timeDelay(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)
        self.__root.grid_rowconfigure(5, weight=1)
        self.__root.grid_rowconfigure(6, weight=1)
        self.__root.grid_rowconfigure(7, weight=1)
        self.__root.grid_rowconfigure(8, weight=1)
        self.__root.grid_rowconfigure(9, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=1)
        self.__root.grid_columnconfigure(3, weight=1)

        def transitionFromTimeDelay():
            delay = clicked_delay.get()
            mouse_delay = clicked_mouse_delay.get()
            type_delay = clicked_type_delay.get()

            self.__updateSetupField('delay', float(delay), self.__current_setup_name)
            self.__updateSetupField('mouse_delay', float(mouse_delay), self.__current_setup_name)
            self.__updateSetupField('type_delay', float(type_delay), self.__current_setup_name)
            self.__window_having_coordinates_or_color_or_input_field = None
            self.__clearScreen()
            self.__timeFormat()

        options_for_delay = [
            '0.25', '0.5', '0.75', '1.0', '1.5', '2.0'
        ]

        options_for_mouse_delay = [
            '0.25', '0.5', '0.75', '1.0', '1.5', '2.0'
        ]

        options_for_type_delay = [
            '0.01', '0.05', '0.1', '0.25', '0.5', '0.75'
        ]

        clicked_delay = StringVar()
        clicked_mouse_delay = StringVar()
        clicked_type_delay = StringVar()

        clicked_delay.set('1.0')
        clicked_mouse_delay.set('0.75')
        clicked_type_delay.set('0.25')

        Label(self.__root,
              text="Choose time delay between\n operations, mouse moving\n speed and typing speed \nbased on your system\n performance.",
              bg='white', fg='blue',
              font=('Aerial', '11', 'bold')).grid(row=1, column=0, rowspan=2)

        helv36 = tkFont.Font(family='Helvetica', size=15)

        Label(self.__root, text="Time Delay", bg='white', fg='blue', font='Aerial 11 bold').grid(row=1, column=1)
        drop_delay = OptionMenu(self.__root, clicked_delay, *options_for_delay)
        drop_delay.grid(row=2, column=1)
        drop_delay.config(font=helv36)

        Label(self.__root, text="Mouse Speed", bg='white', fg='blue', font='Aerial 11 bold').grid(row=1, column=2)
        drop_mouse_delay = OptionMenu(self.__root, clicked_mouse_delay, *options_for_mouse_delay)
        drop_mouse_delay.grid(row=2, column=2)
        drop_mouse_delay.config(font=helv36)

        Label(self.__root, text="Typing Speed", bg='white', fg='blue', font='Aerial 11 bold').grid(row=1, column=3)
        drop_type_delay = OptionMenu(self.__root, clicked_type_delay, *options_for_type_delay)
        drop_type_delay.grid(row=2, column=3)
        drop_type_delay.config(font=helv36)

        Label(self.__root, text="Recommended specifications",
              bg='light blue', fg='red', font=('Aerial', '11', 'bold')).grid(row=3, column=0, columnspan=4)

        Label(self.__root, text="i3 4GB RAM", borderwidth='3', relief='solid',
              bg='lawn green', fg='red', font=('Aerial', '9', 'bold')).grid(row=4, column=0, sticky='nsew')
        Label(self.__root, text="1.5", borderwidth='3', relief='solid',
              bg='lawn green', fg='black', font=('Aerial', '9', 'bold')).grid(row=4, column=1, sticky='nsew')
        Label(self.__root, text="1.5", borderwidth='3', relief='solid',
              bg='lawn green', fg='black', font=('Aerial', '9', 'bold')).grid(row=4, column=2, sticky='nsew')
        Label(self.__root, text="0.5", borderwidth='3', relief='solid',
              bg='lawn green', fg='black', font=('Aerial', '9', 'bold')).grid(row=4, column=3, sticky='nsew')

        Label(self.__root, text="i5 8GB RAM", borderwidth='3', relief='solid',
              bg='yellow', fg='red', font=('Aerial', '9', 'bold')).grid(row=5, column=0, sticky='nsew')
        Label(self.__root, text="1.0", borderwidth='3', relief='solid',
              bg='yellow', fg='black', font=('Aerial', '9', 'bold')).grid(row=5, column=1, sticky='nsew')
        Label(self.__root, text="1.0", borderwidth='3', relief='solid',
              bg='yellow', fg='black', font=('Aerial', '9', 'bold')).grid(row=5, column=2, sticky='nsew')
        Label(self.__root, text="0.25", borderwidth='3', relief='solid',
              bg='yellow', fg='black', font=('Aerial', '9', 'bold')).grid(row=5, column=3, sticky='nsew')

        Label(self.__root, text="i7 16GB RAM", borderwidth='3', relief='solid',
              bg='orange', fg='red', font=('Aerial', '9', 'bold')).grid(row=6, column=0, sticky='nsew')
        Label(self.__root, text="0.5", borderwidth='3', relief='solid',
              bg='orange', fg='black', font=('Aerial', '9', 'bold')).grid(row=6, column=1, sticky='nsew')
        Label(self.__root, text="0.5", borderwidth='3', relief='solid',
              bg='orange', fg='black', font=('Aerial', '9', 'bold')).grid(row=6, column=2, sticky='nsew')
        Label(self.__root, text="0.1", borderwidth='3', relief='solid',
              bg='orange', fg='black', font=('Aerial', '9', 'bold')).grid(row=6, column=3, sticky='nsew')

        Label(self.__root,
              text="Note: You can set custom speed later using \nself.changeTimeDelays(waiting_time_delay=?, mouse_delay=?, typing_delay=?)",
              bg='light blue', fg='black', font=('Aerial', '11', 'bold')).grid(row=7, column=0, columnspan=4)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '11', 'bold'),
                             command=transitionFromTimeDelay)
        next_button.grid(row=8, column=0, columnspan=4)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=9, column=0, columnspan=4)
        progress_bar['value'] = 93

    def __timeFormat(self):
        global instruction_image, instruction_photo

        def transitionFromTimeFormat():
            selected = clicked.get()
            if selected == '-- Select your time-date format --':
                messagebox.showerror(
                    'Select Time Format', 'Please select your whatsapp time format of copied messages')
                return

            time_format = dict_time_format[selected]
            self.__updateSetupField(
                'time_format', time_format, self.__current_setup_name)
            self.__window_having_coordinates_or_color_or_input_field = 'input_field'
            self.__clearScreen()
            self.__userNameOfWtBot()

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        self.__instructions = "Open any chat in your WhatsApp and select multiple messages.\nCopy it and paste it " \
                              "somewhere.\nYou will see the WhatsApp messages with time annotated.\nCompare this and " \
                              "choose the time format of your WhatsApp.\nNote: The time in WhatsApp may be different " \
                              "that your system time.\nSo please check once and select.\nThe time in dropdown : Day " \
                              "- 18, Month - 05, Year - 2002. "
        instruction_image = Image.open(self.__DATA_PATH + 'instructions.png')
        instruction_image = instruction_image.resize((192, 37), Image.ANTIALIAS)
        instruction_photo = ImageTk.PhotoImage(instruction_image)
        t = Label(self.__root, image=instruction_photo)
        t.grid(row=0, column=0)
        t.bind("<Enter>", lambda event: self.__on_enter__for_instructions())
        t.bind("<Leave>", lambda event: self.__on_leave__for_instructions())

        # Dropdown menu options
        options = [
            "-- Select your time-date format --",
            "05:30 PM, 18/05/2002",
            "05:30 PM, 18/2002/05",
            "05:30 PM, 05/18/2002",
            "05:30 PM, 05/2002/18",
            "05:30 PM, 2002/18/05",
            "05:30 PM, 2002/05/18",
            "17:30, 18/05/2002",
            "17:30, 18/2002/05",
            "17:30, 05/18/2002",
            "17:30, 05/2002/18",
            "17:30, 2002/18/05",
            "17:30, 2002/05/18"
        ]

        dict_time_format = {
            "05:30 PM, 18/05/2002": '%I:%M %p, %d/%m/%Y',
            "05:30 PM, 18/2002/05": '%I:%M %p, %d/%Y/%m',
            "05:30 PM, 05/18/2002": '%I:%M %p, %m/%d/%Y',
            "05:30 PM, 05/2002/18": '%I:%M %p, %m/%Y/%d',
            "05:30 PM, 2002/18/05": '%I:%M %p, %Y/%d/%m',
            "05:30 PM, 2002/05/18": '%I:%M %p, %Y/%m/%d',
            "17:30, 18/05/2002": '%H:%M, %d/%m/%Y',
            "17:30, 18/2002/05": '%H:%M, %d/%Y/%m',
            "17:30, 05/18/2002": '%H:%M, %m/%d/%Y',
            "17:30, 05/2002/18": '%H:%M, %m/%Y/%d',
            "17:30, 2002/18/05": '%H:%M, %Y/%d/%m',
            "17:30, 2002/05/18": '%H:%M, %Y/%m/%d'
        }
        # datatype of menu text
        clicked = StringVar()
        # initial menu text
        clicked.set("-- Select your time-date format --")

        helv36 = tkFont.Font(family='Helvetica', size=15)
        drop = OptionMenu(self.__root, clicked, *options)
        drop.grid(row=1, column=0)
        drop.config(font=helv36)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "DateTimeFormat.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=transitionFromTimeFormat)
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0, columnspan=3)
        progress_bar['value'] = 96

    def __userNameOfWtBot(self):
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)

        Label(self.__root,
              text="Type the username of your WhatsApp account. You can find this under the Profile section",
              bg='white', fg='blue', font=('Aerial', '10', 'bold')).grid(row=0, column=0)
        self.__input_field_for_text = Text(self.__root, width=30, height=2)
        self.__input_field_for_text.grid(row=1, column=0)

        kebab_video = Label(self.__root)
        kebab_video.grid(row=2, column=0)
        kebab_player = tkvideo(self.__DATA_PATH + "username.mp4", kebab_video, loop=1, size=(640, 360))
        kebab_player.play()

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='user_name_of_wt_bot',
                                                                 next_screen='__defaultGroup',
                                                                 flag_of_next_screen_field='input_field'))
        next_button.grid(row=3, column=0)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=4, column=0)
        progress_bar['value'] = 98

    def __defaultGroup(self):
        global new_grp_image, new_grp_photo
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)

        Label(self.__root, text="Group Name", bg='white', fg='blue', font='Aerial 10 bold').grid(row=0, column=0)
        self.__input_field_for_text = Text(self.__root, width=40, height=2)
        self.__input_field_for_text.grid(row=0, column=1, sticky='w')

        Label(self.__root,
              text="Create a new group with any name.\n\nYou can be the only member in the group too.\n\nMessages from this group won't be read by bot.\n\nSo it is recommended to make the group as \nonly admins can message (if there are participants).\n\nType the group name in the text box.",
              bg='white', fg='blue',
              font=('Aerial', '11', 'bold')).grid(row=1, column=0)
        new_grp_image = Image.open(self.__DATA_PATH + 'new_group.jpeg')
        new_grp_image = new_grp_image.resize((265, 360), Image.ANTIALIAS)
        new_grp_photo = ImageTk.PhotoImage(new_grp_image)
        t = Label(self.__root, image=new_grp_photo)
        t.grid(row=1, column=1)

        next_button = Button(self.__root, text='Next', bg='blue', fg='white', font=('Aerial', '10', 'bold'),
                             command=lambda: self.__transitionUp(previous_screen_db_column='default_group',
                                                                 next_screen='__finish',
                                                                 flag_of_next_screen_field=None))
        next_button.grid(row=2, column=0, columnspan=2)

        progress_bar = ttk.Progressbar(self.__root, orient='horizontal', mode='determinate', length=890)
        progress_bar.grid(row=3, column=0, columnspan=2)
        progress_bar['value'] = 100

    def __finish(self):
        self.__commitDBChanges()
        # working fine even without stopping thread

        global add_bg, github_photo, linked_in, instagram, email, phone, arvind, niresh
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_rowconfigure(1, weight=1)
        self.__root.grid_rowconfigure(2, weight=1)
        self.__root.grid_rowconfigure(3, weight=1)
        self.__root.grid_rowconfigure(4, weight=1)
        self.__root.grid_rowconfigure(5, weight=1)
        self.__root.grid_rowconfigure(6, weight=8)
        self.__root.grid_rowconfigure(7, weight=2)

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=4)
        self.__root.grid_columnconfigure(2, weight=4)
        self.__root.grid_columnconfigure(3, weight=10)

        self.__root.geometry('836x627')

        original = Image.open(self.__DATA_PATH + 'nanda.jpg')
        resized = original.resize((836, 627), Image.ANTIALIAS)
        add_bg = ImageTk.PhotoImage(resized)  # Keep a reference, prevent GC
        Label(self.__root, image=add_bg).place(x=0, y=0)

        Label(self.__root, text="Nanda Kishore B", bg='white', fg='red', font='Aerial 20 bold').grid(row=0, column=0,
                                                                                                     columnspan=4)

        github_photo = Image.open(self.__DATA_PATH + 'github.png')
        github_photo = github_photo.resize((50, 50), Image.ANTIALIAS)
        github_photo = ImageTk.PhotoImage(github_photo)
        git1 = Label(self.__root, image=github_photo)
        git1.grid(row=1, column=0, sticky='e')
        git2 = Label(self.__root, text="nandakishfast", bg='white', fg='black', font='Aerial 15 bold')
        git2.grid(row=1, column=1, sticky='w', columnspan=2)
        git1.bind("<Button-1>", lambda e: self.__callback("https://github.com/nandakishfast"))
        git2.bind("<Button-1>", lambda e: self.__callback("https://github.com/nandakishfast"))

        linked_in = Image.open(self.__DATA_PATH + 'linkedin.png')
        linked_in = linked_in.resize((50, 50), Image.ANTIALIAS)
        linked_in = ImageTk.PhotoImage(linked_in)
        link1 = Label(self.__root, image=linked_in)
        link1.grid(row=2, column=0, sticky='e')
        link2 = Label(self.__root, text="nanda-kishore-899848204", bg='white', fg='blue', font='Aerial 15 bold')
        link2.grid(row=2,column=1,sticky='w',columnspan=2)
        link1.bind("<Button-1>", lambda e: self.__callback("https://www.linkedin.com/in/nanda-kishore-899848204/"))
        link2.bind("<Button-1>", lambda e: self.__callback("https://www.linkedin.com/in/nanda-kishore-899848204/"))

        instagram = Image.open(self.__DATA_PATH + 'instagram.png')
        instagram = instagram.resize((50, 50), Image.ANTIALIAS)
        instagram = ImageTk.PhotoImage(instagram)
        insta1 = Label(self.__root, image=instagram)
        insta1.grid(row=3, column=0, sticky='e')
        insta2 = Label(self.__root, text="nanda_kishore_b7", bg='white', fg='purple', font='Aerial 15 bold')
        insta2.grid(row=3,column=1,sticky='w',columnspan=2)
        insta1.bind("<Button-1>", lambda e: self.__callback("https://www.instagram.com/nanda_kishore_b7/"))
        insta2.bind("<Button-1>", lambda e: self.__callback("https://www.instagram.com/nanda_kishore_b7/"))

        email = Image.open(self.__DATA_PATH + 'gmail.png')
        email = email.resize((50, 50), Image.ANTIALIAS)
        email = ImageTk.PhotoImage(email)
        Label(self.__root, image=email).grid(row=4, column=0, sticky='e')
        Label(self.__root, text="pgsbssnk@gmail.com", bg='white', fg='brown', font='Aerial 15 bold').grid(row=4, column=1,
                                                                                                       sticky='w',
                                                                                                       columnspan=2)

        phone = Image.open(self.__DATA_PATH + 'phone.png')
        phone = phone.resize((50, 50), Image.ANTIALIAS)
        phone = ImageTk.PhotoImage(phone)
        Label(self.__root, image=phone).grid(row=5, column=0, sticky='e')
        Label(self.__root, text="+91 99524 02150", bg='white', fg='green', font='Aerial 15 bold').grid(row=5, column=1,
                                                                                                       sticky='w',
                                                                                                       columnspan=2)

        arvind = Image.open(self.__DATA_PATH + 'arvind.jpeg')
        arvind = arvind.resize((104, 150), Image.ANTIALIAS)
        arvind = ImageTk.PhotoImage(arvind)
        Label(self.__root, image=arvind).grid(row=6, column=1, sticky='sw')
        Label(self.__root, text="Arvind K", bg='white', fg='red', font='Aerial 15 bold').grid(row=7, column=1,
                                                                                              sticky='nw')

        niresh = Image.open(self.__DATA_PATH + 'niresh.jpeg')
        niresh = niresh.resize((108, 150), Image.ANTIALIAS)
        niresh = ImageTk.PhotoImage(niresh)
        Label(self.__root, image=niresh).grid(row=6, column=2, sticky='sw')
        Label(self.__root, text="Niresh K", bg='white', fg='red', font='Aerial 15 bold').grid(row=7, column=2,
                                                                                              sticky='nw')
