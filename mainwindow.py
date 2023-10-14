from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFrame,
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget,QDialog,QAbstractItemView,QMessageBox,QGraphicsView,QGraphicsScene, QGraphicsPixmapItem)
import os, sys
import database_handling
import docket_applications
import sqlite3
import offline_file_handling as ofh
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 746)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        # defining the icons
        if getattr(sys, 'frozen', False):
            # Running as a standalone executable
            base_path = sys._MEIPASS
        else:
            # Running in a development environment
            base_path = os.path.abspath(".")
        # Construct the path to your PNG file
        docket_icon = os.path.join(base_path, "resources", "docket.png")
        register_icon = os.path.join(base_path, "resources", "register.png")
        sign_in_icon = os.path.join(base_path, "resources", "sign_in.png")
        sign_out_icon = os.path.join(base_path, "resources", "sign_out.png")
        refresh_icon = os.path.join(base_path, "resources", "refresh.png")
        save_icon = os.path.join(base_path, "resources", "save_icon.jpg")
        cross_icon = os.path.join(base_path, "resources", "cross.png")
        delete_icon = os.path.join(base_path, "resources", "delete.png")
        export_icon = os.path.join(base_path, "resources", "export.png")
        add_icon = os.path.join(base_path, "resources", "add.png")
        edit_icon = os.path.join(base_path, "resources", "edit.png")

        icon = QIcon()
        icon.addFile(docket_icon, QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.actionSign_In = QAction(MainWindow)
        self.actionSign_In.setObjectName(u"actionSign_In")
        icon1 = QIcon()
        icon1.addFile(sign_in_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionSign_In.setIcon(icon1)
        self.actionRegister = QAction(MainWindow)
        self.actionRegister.setObjectName(u"actionRegister")
        icon2 = QIcon()
        icon2.addFile(register_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionRegister.setIcon(icon2)
        self.actionSign_Out = QAction(MainWindow)
        self.actionSign_Out.setObjectName(u"actionSign_Out")
        icon3 = QIcon()
        icon3.addFile(sign_out_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionSign_Out.setIcon(icon3)
        font1 = QFont()
        self.actionSign_Out.setFont(font1)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon4 = QIcon()
        icon4.addFile(refresh_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon4)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon5 = QIcon()
        icon5.addFile(save_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionClear_All = QAction(MainWindow)
        self.actionClear_All.setObjectName(u"actionClear_All")
        icon6 = QIcon()
        icon6.addFile(cross_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear_All.setIcon(icon6)
        self.actionDelete_Database = QAction(MainWindow)
        self.actionDelete_Database.setObjectName(u"actionDelete_Database")
        icon7 = QIcon()
        icon7.addFile(delete_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_Database.setIcon(icon7)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon8 = QIcon()
        icon8.addFile(export_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon8)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Insert_Box = QFrame(self.centralwidget)
        self.Insert_Box.setObjectName(u"Insert_Box")
        self.Insert_Box.setMinimumSize(QSize(771, 150))
        self.Insert_Box.setFrameShape(QFrame.StyledPanel)
        self.Insert_Box.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.Insert_Box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.priority_checkbox = QCheckBox(self.Insert_Box)
        self.priority_checkbox.setObjectName(u"priority_checkbox")

        self.gridLayout_2.addWidget(self.priority_checkbox, 1, 2, 1, 1)

        self.Notifier_checkbox = QCheckBox(self.Insert_Box)
        self.Notifier_checkbox.setObjectName(u"Notifier_checkbox")

        self.gridLayout_2.addWidget(self.Notifier_checkbox, 2, 2, 1, 1)

        self.text_editor = QTextEdit(self.Insert_Box)
        self.text_editor.setObjectName(u"text_editor")

        self.gridLayout_2.addWidget(self.text_editor, 0, 0, 5, 1)

        self.dateTimeEdit = QDateTimeEdit(self.Insert_Box)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout_2.addWidget(self.dateTimeEdit, 0, 2, 1, 1)

        self.add_item = QPushButton(self.Insert_Box)
        self.add_item.setObjectName(u"add_item")
        self.add_item.setMinimumSize(QSize(150, 40))
        self.add_item.setMaximumSize(QSize(160, 45))
        self.add_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_item.setStyleSheet(u"QPushButton{\n"
"			\n"
"			color: rgb(46, 194, 126);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	font: bold;\n"
"	background-color: rgb(161, 247, 150);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(add_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.add_item.setIcon(icon9)

        self.gridLayout_2.addWidget(self.add_item, 3, 2, 1, 1)


        self.gridLayout_3.addWidget(self.Insert_Box, 3, 0, 2, 2)

        self.View_Box = QFrame(self.centralwidget)
        self.View_Box.setObjectName(u"View_Box")
        self.View_Box.setMinimumSize(QSize(500, 511))
        self.View_Box.setStyleSheet("""
        QFrame {
        border-radius: 10px;  /* Adjust the value to control the rounding */
        border: 1px solid #000; /* Optional border styling */
        background-color: #fec89a;
        }
        """)
        self.View_Box.setFrameShape(QFrame.StyledPanel)
        self.View_Box.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.View_Box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.todo_list = QListWidget(self.View_Box)
        self.todo_list.setObjectName(u"todo_list")
        self.todo_list.setMinimumSize(QSize(500, 440))
        self.todo_list.setStyleSheet("""
    QListWidget {
        border-radius: 10px;  /* Adjust the value to control the rounding */
        border: 1px solid #000; /* Optional border styling */
        background-color: #f8edeb;
    }
    QListWidget::Item {
        background-color: #fcd5ce;
        border: 1px solid gray;
        border-radius: 10px;
        padding: 5px;
        margin-top: 7px;      /* Top margin */
        margin-bottom: 7px;   /* Bottom margin */
        margin-left: 10px;    /* Left margin */
        margin-right: 10px;   /* Right margin */
    }

    QListWidget::Item:selected {
        background-color: lightblue;
    }
""")

        self.gridLayout.addWidget(self.todo_list, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.View_Box, 0, 0, 2, 1)

        self.Editorial_Box = QFrame(self.centralwidget)
        self.Editorial_Box.setObjectName(u"Editorial_Box")
        self.Editorial_Box.setMinimumSize(QSize(211, 221))
        self.Editorial_Box.setFrameShape(QFrame.StyledPanel)
        self.Editorial_Box.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Editorial_Box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.edit_item = QPushButton(self.Editorial_Box)
        self.edit_item.setObjectName(u"edit_item")
        self.edit_item.setMinimumSize(QSize(150, 40))
        self.edit_item.setMaximumSize(QSize(160, 45))
        self.edit_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_item.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: bold;\n"
"	background-color: rgb(153, 198, 245);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(edit_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.edit_item.setIcon(icon10)

        self.gridLayout_4.addWidget(self.edit_item, 1, 0, 1, 1)

        self.delete_item = QPushButton(self.Editorial_Box)
        self.delete_item.setObjectName(u"delete_item")
        self.delete_item.setMinimumSize(QSize(150, 40))
        self.delete_item.setMaximumSize(QSize(160, 45))
        self.delete_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_item.setStyleSheet(u"QPushButton{\n"
"color:rgb(237, 51, 59);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: bold;\n"
"	background-color: rgb(248, 170, 170);\n"
"}")
        self.delete_item.setIcon(icon7)

        self.gridLayout_4.addWidget(self.delete_item, 2, 0, 1, 1)

        self.clear_item = QPushButton(self.Editorial_Box)
        self.clear_item.setObjectName(u"clear_item")
        self.clear_item.setMinimumSize(QSize(0, 40))
        self.clear_item.setMaximumSize(QSize(160, 45))
        self.clear_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_item.setStyleSheet(u"QPushButton{\n"
"color:rgb(237, 51, 59);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: bold;\n"
"	background-color: rgb(248, 170, 170);\n"
"}")
        self.clear_item.setIcon(icon6)

        self.gridLayout_4.addWidget(self.clear_item, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.Editorial_Box, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(210, 270))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Status_icon_label = QGraphicsView(self.frame_4)
        self.Status_icon_label.setObjectName(u"Status_icon_label")
        self.Status_icon_label.setStyleSheet(
            "background-color: transparent;"  # Make the background transparent
        )
        self.Status_icon_label.setGeometry(QRect(50, 10, 110, 110))

        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1)

        self.Status_notify_label = QLabel(self.frame_4)
        self.Status_notify_label.setObjectName(u"Status_notify_label")
        self.Status_notify_label.setGeometry(QRect(20, 130, 171, 111))

        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1)


        self.user_info_button = QPushButton(self.centralwidget)
        self.user_info_button.setObjectName(u"user_info_button")
        self.user_info_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_info_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	font: bold;\n"
"	background-color: rgb(153, 198, 245);\n"
"}")

        # Sets timer to the status
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_status_message)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.check_notifications)
        self.timer2.start(1000)

        self.gridLayout_3.addWidget(self.user_info_button, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 789, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAuthentication = QMenu(self.menubar)
        self.menuAuthentication.setObjectName(u"menuAuthentication")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAuthentication.menuAction())
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionAbout)
        self.menuAuthentication.addAction(self.actionSign_In)
        self.menuAuthentication.addAction(self.actionRegister)
        self.menuAuthentication.addAction(self.actionSign_Out)
        self.menuEdit.addAction(self.actionClear_All)
        self.menuEdit.addAction(self.actionDelete_Database)

        # Button calls
        self.clear_item.clicked.connect(self.clear_items)
        self.delete_item.clicked.connect(self.delete_items)
        self.edit_item.clicked.connect(self.edit_items)
        self.add_item.clicked.connect(self.add_items)
        self.user_info_button.clicked.connect(self.call_user_info_ui)

        # Menu Bar actions
        self.actionSign_Out.triggered.connect(self.sign_out_function)
        self.actionSign_In.triggered.connect(self.call_sign_in_ui)
        self.actionRegister.triggered.connect(self.call_register_ui)
        self.actionSave.triggered.connect(self.save_all)
        self.actionRefresh.triggered.connect(lambda: self.refresh_all("Refreshed"))
        self.actionDelete_Database.triggered.connect(self.clear_database_function)
        self.actionClear_All.triggered.connect(self.clear_items)
        self.actionPrint.triggered.connect(self.export_data)
        self.actionAbout.triggered.connect(self.call_about_ui)

        # Set timer for clearing status messages
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_status_message)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.check_notifications)
        self.timer2.start(1000)

        self.load_all()
        uname = ofh.read_uname()
        self.user_info_button.setText(uname)
        self.todo_list.clearSelection()
        self.load_status_icon_label()
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Docket", None))
        self.actionSign_In.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.actionRegister.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.actionSign_Out.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClear_All.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionDelete_Database.setText(QCoreApplication.translate("MainWindow", u"Delete Database", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.priority_checkbox.setText(QCoreApplication.translate("MainWindow", u"Set Priority", None))
        self.Notifier_checkbox.setText(QCoreApplication.translate("MainWindow", u"Notify", None))
        self.add_item.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.edit_item.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_item.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.clear_item.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))

        self.Status_notify_label.setText("")
        self.previous = ""
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAuthentication.setTitle(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

    def add_items(self):
        select = self.Status_notify_label.text()

        # Get the text from the text editor
        item_text = self.text_editor.toPlainText()

        # Determine priority based on the checkbox state
        is_priority = self.priority_checkbox.isChecked()

        if select == 'Edit item':
            selected = self.todo_list.currentRow()

            if selected >= 0:
                edited_item = self.todo_list.item(selected)
                edited_item.setText(item_text)
                edited_item.setCheckState(Qt.CheckState.Checked if is_priority else Qt.CheckState.Unchecked)

                if self.Notifier_checkbox.isChecked():
                    notifier_datetime = self.dateTimeEdit.dateTime().toString(Qt.ISODate)
                    self.edit_notifier(self.previous, item_text, notifier_datetime)

                self.Status_notify_label.setText("Edited")
                self.fetch_all()
                self.timer.start(3000)
                self.todo_list.clearSelection()
        else:
            new_item = QListWidgetItem(item_text)
            new_item.setCheckState(Qt.CheckState.Checked if is_priority else Qt.CheckState.Unchecked)
            self.todo_list.addItem(new_item)

            if self.Notifier_checkbox.isChecked():
                notifier_datetime = self.dateTimeEdit.dateTime().toString(Qt.ISODate)
                self.append_notifier(item_text, notifier_datetime)

            self.Status_notify_label.setText("Added")
            self.fetch_all()
            self.timer.start(3000)
            self.todo_list.clearSelection()

        self.text_editor.setText("")
        self.refresh_all("Added")# Delete items from ToDO List
    def delete_items(self):
        # Grab the selected row/item

        selected = self.todo_list.currentRow()
        self.previous = self.todo_list.item(selected).text()
        # delete selected item
        self.todo_list.takeItem(selected)
        self.fetch_all()
        self.Status_notify_label.setText("Deleted")
        self.timer.start(3000)
        exist = database_handling.check_exist(self.previous)
        if exist[0]>=1:
            database_handling.remove_notification2(self.previous)


    # Clear all items from ToDo List
    def clear_items(self):
        self.todo_list.clear()
        self.fetch_all()
        self.Status_notify_label.setText("Cleared All")
        self.timer.start(3000)

        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("DROP TABLE notifier")
        conn.commit()
        conn.close()
        database_handling.append_table_for_notification()

    # Edit the selected items
    def edit_items(self):
        selected = self.todo_list.currentRow()
        current_text = self.todo_list.item(selected).text()
        self.text_editor.setText(current_text)
        self.previous = current_text
        self.Status_notify_label.setText("Edit item")
        self.timer.start(100000)


    def load_all(self):

        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("SELECT list_item, priority FROM todo_list")
        records = cursor.fetchall()

        conn.commit()
        conn.close()

        # Set the selection mode to NoSelection to hide checkboxes
        self.todo_list.setSelectionMode(QAbstractItemView.NoSelection)

        # Store priority and non-priority items separately
        priority_items = []
        non_priority_items = []

        for record in records:
            item_text = record[0]
            priority = record[1]

            item = QListWidgetItem(item_text)
            if priority == 1:
                item.setForeground(QColor(255, 0, 0))  # Red color for priority items
                priority_items.append(item)  # Add to the list of priority items
            else:
                non_priority_items.append(item)  # Add to the list of non-priority items

        # Clear the existing items in the QListWidget
        self.todo_list.clear()

        # Add priority items first, maintaining their order
        for item in priority_items:
            self.todo_list.addItem(item)

        # Add non-priority items after priority items
        for item in non_priority_items:
            self.todo_list.addItem(item)

        self.Status_notify_label.setText("Loaded")
        self.timer.start(3000)

    def fetch_all(self):
        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM todo_list;", )

        items = []
        for index in range(self.todo_list.count()):
            item = self.todo_list.item(index)
            item_text = item.text()
            priority = 1 if item.checkState() == Qt.Checked else 0
            cursor.execute("INSERT INTO todo_list(list_item, priority) VALUES (:item, :priority)",
                           {
                               'item': item_text,
                               'priority': priority,
                           })
        conn.commit()
        conn.close()
        if self.todo_list.itemChanged:
            if docket_applications.check_internet():
                path = ofh.read_uid() + '.db'
                docket_applications.sync_online(path)
            else:
                pass

    def update_item_order(self, item):
        # Get the current item's index
        index = self.todo_list.indexFromItem(item).row()

        # Check if the item's checkbox is checked
        priority = 1 if item.checkState() == Qt.Checked else 0

        # Remove the item from the list
        self.todo_list.takeItem(index)

        # Find the index to insert the item based on its priority
        insert_index = 0
        for i in range(self.todo_list.count()):
            current_item = self.todo_list.item(i)
            current_priority = 1 if current_item.checkState() == Qt.Checked else 0
            if priority >= current_priority:
                insert_index = i + 1

        # Insert the item at the correct position
        self.todo_list.insertItem(insert_index, item)
    def refresh_all(self, text):
        self.todo_list.clear()
        self.load_all()
        self.Status_notify_label.setText(text)
        self.timer.start(3000)
        self.todo_list.clearSelection()

    def save_all(self):
        self.fetch_all()
        path = ofh.read_uid() + '.db'

        if docket_applications.check_internet():
            docket_applications.sync_online(path)
            self.Status_notify_label.setText("Saved")
            self.timer.start(3000)
        else:
            self.Status_notify_label.setText("Internet Error!")
            self.timer.start(3000)

    def auto_save(self):
        self.save_all()

    def clear_database_function(self):
        path = ofh.read_uid()
        file_path = path + ".db"
        docket_applications.sign_out_status(path)
        if os.path.exists(file_path):
            os.remove(file_path)
        database_handling.append_db()
        self.todo_list.clear()
        self.fetch_all()
        self.Status_notify_label.setText("Cleared Local Database.")
        self.timer.start(3000)

    def sign_out_function(self):
        path = ofh.read_uid()
        file_path = path + ".db"
        docket_applications.sign_out_status(path)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists("user_data"):
            os.remove("user_data")
        if os.path.exists("user_name"):
            os.remove("user_name")
        docket_applications.sign_out_status(path)
        self.todo_list.clear()

        QApplication.quit()

    def call_sign_in_ui(self):
        from sign_in_ui import Ui_SignIn
        self.window = QMainWindow()
        self.ui = Ui_SignIn()
        self.ui.setupUi(self.window)
        self.window.show()

    def call_register_ui(self):
        from registration_ui import Ui_Register
        self.window = QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        self.window.show()

    def call_about_ui(self):
        from about_ui import Ui_Form
        self.window = QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def call_user_info_ui(self):
        from user_info_ui import Ui_User
        self.window = QDialog()
        self.ui = Ui_User()
        self.ui.setupUi(self.window)
        self.window.show()

    def clear_status_message(self):
        self.Status_notify_label.setText("")

    def append_notifier(self, item, notifier_datetime):
        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO notifier (list_item, notification_datetime) VALUES (?, ?)", (item, notifier_datetime))

        conn.commit()
        conn.close()
    def edit_notifier(self,previoustext,item,notifier_datetime):
        exist = database_handling.check_exist(previoustext)
        print(exist[0])
        if exist[0]==1:
            database_handling.remove_notification2(previoustext)
            self.append_notifier(item, notifier_datetime)
        else:
            self.append_notifier(item,notifier_datetime)

    def check_notifications(self):
        current_datetime = QDateTime.currentDateTime().toString(Qt.ISODate)
        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("SELECT list_item, notification_datetime FROM notifier WHERE notification_datetime <= ?", (current_datetime,))
        notifications = cursor.fetchall()

        conn.commit()
        conn.close()

        for notification in notifications:
            item, datetime = notification
            self.show_notification(item, datetime)
            self.remove_notification(item, datetime)

    def show_notification(self, item, datetime):
        title = "Notification"

        message = f"<h2>{item}</h2>\n\n\n\nDatetime: {datetime}"

        # Create a QMessageBox and set the title and message
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Add an "OK" button to close the message box
        msg_box.addButton(QMessageBox.Ok)

        # Show the message box as a modal dialog
        msg_box.exec()

    def remove_notification(self, item, datetime):
        file = ofh.read_uid()
        conn = sqlite3.connect(file + ".db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM notifier WHERE list_item = ? AND notification_datetime = ?", (item, datetime))

        conn.commit()
        conn.close()

    def export_data(self):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        path = ofh.read_uid()
        file_path = path + ".db"
        # Connect to the SQLite database
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()

        # Execute an SQL query to fetch the data
        cursor.execute('SELECT * FROM todo_list;')

        # Fetch all the data and remove lines with 0 (integer) values
        data = [row for row in cursor.fetchall() if any(item != 0 for item in row)]

        # Close the database connection
        conn.close()

        # Create a PDF file
        pdf_filename = 'exported_data.pdf'
        c = canvas.Canvas(pdf_filename, pagesize=letter)

        # Define the PDF content format
        y = 700  # Initial vertical position
        item_number = 1  # Initialize item numbering

        for row in data:
            for item in row:
                if item != 0:  # Only add items that are not 0
                    c.drawString(100, y, f"{item_number}. {item}")  # Include the item number
                    y -= 20  # Adjust vertical spacing
                    item_number += 1  # Increment the item number
            y -= 20  # Add additional spacing between rows

        # Save the PDF file
        c.save()

        self.Status_notify_label.setText(f'Data \nexported \nto {pdf_filename}')
        self.timer.start(3000)

    def load_status_icon_label(self):
        if docket_applications.check_internet():
            image_url = "https://firebasestorage.googleapis.com/v0/b/docket-d857d.appspot.com/o/docket.png?alt=media&token=a6e81b85-5328-4d09-ac44-c9b7a9316c7a&_gl=1*1n6dbpo*_ga*MTUxMzkyMjY4NC4xNjk1MjM2ODY1*_ga_CW55HF8NVT*MTY5NTk0MTYyMy4zLjEuMTY5NTk0MTY5NC42MC4wLjA."

            # Download the image from the web using requests
            response = requests.get(image_url)

            if response.status_code == 200:
                # Create a QPixmap from the image data
                image_data = response.content
                status_icon_pixmap = QPixmap()
                status_icon_pixmap.loadFromData(image_data)
            # Load the image using QPixmap
            # status_icon_pixmap = QPixmap("docket.png")  # Replace with the actual path to your image

            # Get the dimensions of the QGraphicsView
            view_width = self.Status_icon_label.width()
            view_height = self.Status_icon_label.height()

            # Calculate the scaling factors to fit the image within the view
            scale_factor_width = view_width / status_icon_pixmap.width()
            scale_factor_height = view_height / status_icon_pixmap.height()

            # Use the minimum scaling factor to maintain the aspect ratio and fit the image
            scale_factor = min(scale_factor_width, scale_factor_height)

            # Scale the pixmap using the calculated scale factor
            status_icon_pixmap = status_icon_pixmap.scaled(
                status_icon_pixmap.width() * scale_factor,
                status_icon_pixmap.height() * scale_factor,
                Qt.KeepAspectRatio
            )

            # Create a QGraphicsPixmapItem to hold the image
            status_icon_pixmap_item = QGraphicsPixmapItem(status_icon_pixmap)

            # Create a QGraphicsScene
            scene = QGraphicsScene()

            # Set the scene's dimensions to match the scaled image
            scene.setSceneRect(0, 0, status_icon_pixmap.width(), status_icon_pixmap.height())

            # Add the pixmap item to the scene
            scene.addItem(status_icon_pixmap_item)

            # Set the QGraphicsScene for your QGraphicsView
            self.Status_icon_label.setScene(scene)

            # Disable scroll bars
            self.Status_icon_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.Status_icon_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

            # Show the image
            self.Status_icon_label.show()
