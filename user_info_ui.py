from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

import docket_applications as docket
import offline_file_handling as ofh
import os

class Ui_User(object):
    def setupUi(self, User):
        if not User.objectName():
            User.setObjectName(u"User")
        User.resize(595, 648)
        User.setMaximumSize(QSize(850, 700))
        self.gridLayout = QGridLayout(User)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Docket_Label = QLabel(User)
        self.Docket_Label.setObjectName(u"Docket_Label")

        self.gridLayout.addWidget(self.Docket_Label, 0, 0, 1, 1)

        self.User_Info = QFrame(User)
        self.User_Info.setObjectName(u"User_Info")
        self.User_Info.setFrameShape(QFrame.StyledPanel)
        self.User_Info.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.User_Info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.User_Info)
        self.tabWidget.setObjectName(u"tabWidget")
        self.user_info_tab = QWidget()
        self.user_info_tab.setObjectName(u"user_info_tab")
        self.gridLayout_3 = QGridLayout(self.user_info_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sign_out_button = QPushButton(self.user_info_tab)
        self.sign_out_button.setObjectName(u"sign_out_button")

        self.gridLayout_3.addWidget(self.sign_out_button, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.user_info_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 91, 31))
        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(120, 30, 351, 31))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 70, 91, 31))
        self.uid_label = QLabel(self.groupBox)
        self.uid_label.setObjectName(u"uid_label")
        self.uid_label.setGeometry(QRect(120, 70, 361, 31))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 120, 141, 31))
        self.login_status = QLabel(self.groupBox)
        self.login_status.setObjectName(u"login_status")
        self.login_status.setGeometry(QRect(150, 120, 321, 31))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 160, 81, 31))
        self.device_info = QLabel(self.groupBox)
        self.device_info.setObjectName(u"device_info")
        self.device_info.setGeometry(QRect(30, 190, 481, 201))

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)

        self.reset_password_button = QPushButton(self.user_info_tab)
        self.reset_password_button.setObjectName(u"reset_password_button")

        self.gridLayout_3.addWidget(self.reset_password_button, 1, 1, 1, 1)

        self.tabWidget.addTab(self.user_info_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verify_box = QGroupBox(self.tab)
        self.verify_box.setObjectName(u"verify_box")
        self.gridLayout_4 = QGridLayout(self.verify_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.uid_label_2 = QLabel(self.verify_box)
        self.uid_label_2.setObjectName(u"uid_label_2")

        self.gridLayout_4.addWidget(self.uid_label_2, 0, 0, 1, 1)

        self.uid_lineEdit_2 = QLineEdit(self.verify_box)
        self.uid_lineEdit_2.setObjectName(u"uid_lineEdit_2")

        self.gridLayout_4.addWidget(self.uid_lineEdit_2, 0, 1, 1, 1)

        self.email_label = QLabel(self.verify_box)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout_4.addWidget(self.email_label, 1, 0, 1, 1)

        self.email_lineEdit = QLineEdit(self.verify_box)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.gridLayout_4.addWidget(self.email_lineEdit, 1, 1, 1, 1)

        self.check_button_2 = QPushButton(self.verify_box)
        self.check_button_2.setObjectName(u"check_button_2")

        self.gridLayout_4.addWidget(self.check_button_2, 2, 1, 1, 1)

        self.otp_label = QLabel(self.verify_box)
        self.otp_label.setObjectName(u"otp_label")

        self.gridLayout_4.addWidget(self.otp_label, 3, 0, 1, 1)

        self.otp_lineEdit_2 = QLineEdit(self.verify_box)
        self.otp_lineEdit_2.setObjectName(u"otp_lineEdit_2")

        self.gridLayout_4.addWidget(self.otp_lineEdit_2, 3, 1, 1, 1)

        self.otp_verify_button_2 = QPushButton(self.verify_box)
        self.otp_verify_button_2.setObjectName(u"otp_verify_button_2")

        self.gridLayout_4.addWidget(self.otp_verify_button_2, 3, 2, 1, 1)


        self.gridLayout_5.addWidget(self.verify_box, 0, 0, 1, 1)

        self.change_password_box = QGroupBox(self.tab)
        self.change_password_box.setObjectName(u"change_password_box")
        self.password_change_edit_2 = QLineEdit(self.change_password_box)
        self.password_change_edit_2.setObjectName(u"password_change_edit_2")
        self.password_change_edit_2.setGeometry(QRect(90, 120, 341, 31))
        self.change_password_button_2 = QPushButton(self.change_password_box)
        self.change_password_button_2.setObjectName(u"change_password_button_2")
        self.change_password_button_2.setGeometry(QRect(200, 180, 141, 31))
        self.password_reset_label = QLabel(self.change_password_box)
        self.password_reset_label.setObjectName(u"password_reset_label")
        self.password_reset_label.setGeometry(QRect(160, 50, 221, 41))

        self.gridLayout_5.addWidget(self.change_password_box, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.User_Info, 1, 0, 1, 1)


        self.retranslateUi(User)

        self.closed_tabs = []
        # Make tabs closable
        self.tabWidget.setTabsClosable(True)

        # Connect the tabCloseRequested signal to the slot that closes tabs
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.isTabVisible(0)
        self.tabWidget.setCurrentIndex(1)
        self.fetch_info()

        self.change_password_box.setVisible(False)
        self.otp_label.setVisible(False)
        self.otp_lineEdit_2.setVisible(False)
        self.otp_verify_button_2.setVisible(False)
        self.otp = ''
        self.email_text = ''

        self.tabWidget.setCurrentIndex(1)

        self.reset_password_button.clicked.connect(self.call_password_reset)
        self.check_button_2.clicked.connect(self.uid_email_verify)
        self.otp_verify_button_2.clicked.connect(self.otp_verify)
        self.change_password_button_2.clicked.connect(self.password_change)
        self.sign_out_button.clicked.connect(self.sign_out_function)
        QMetaObject.connectSlotsByName(User)
    # setupUi

    def retranslateUi(self, User):
        User.setWindowTitle(QCoreApplication.translate("User", u"Docket Settings", None))
        self.Docket_Label.setText(QCoreApplication.translate("User", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Docket</span></p></body></html>", None))
        self.sign_out_button.setText(QCoreApplication.translate("User", u"Sign Out", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("User", u"Name:", None))
        self.name_label.setText("")
        self.label_3.setText(QCoreApplication.translate("User", u"UID:", None))
        self.uid_label.setText("")
        self.label_6.setText(QCoreApplication.translate("User", u"Last Logged In:", None))
        self.login_status.setText("")
        self.label_8.setText(QCoreApplication.translate("User", u"Device Info", None))
        self.device_info.setText(QCoreApplication.translate("User", u"Device Info", None))
        self.reset_password_button.setText(QCoreApplication.translate("User", u"Reset Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_info_tab), QCoreApplication.translate("User", u"User Info", None))
        self.verify_box.setTitle(QCoreApplication.translate("User", u"Verification", None))
        self.uid_label_2.setText(QCoreApplication.translate("User", u"Enter UID", None))
        self.email_label.setText(QCoreApplication.translate("User", u"Enter Email", None))
        self.check_button_2.setText(QCoreApplication.translate("User", u"Check", None))
        self.otp_label.setText(QCoreApplication.translate("User", u"Enter the OTP", None))
        self.otp_verify_button_2.setText(QCoreApplication.translate("User", u"Verify", None))
        self.change_password_box.setTitle(QCoreApplication.translate("User", u"Change Password", None))
        self.change_password_button_2.setText(QCoreApplication.translate("User", u"Change Password", None))
        self.password_reset_label.setText(QCoreApplication.translate("User", u"<html><head/><body><h3>Enter the new password</h3></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("User", u"Page", None))
    # retranslateUi

    def closeTab(self):

        #Get the current index of the tab to close
        index = self.tabWidget.currentIndex()

        # Store the removed tab content and its title
        tab_content = self.tabWidget.currentWidget()
        tab_title = self.tabWidget.tabText(index)
        self.closed_tabs.append((tab_title, tab_content))

        # Remove the tab
        self.tabWidget.removeTab(index)
    def fetch_info(self):
        uid = ofh.read_uid()
        username = ofh.read_uname()
        self.name_label.setText(username)
        self.uid_label.setText(uid)

        file_name = "user_device"  # Replace with the path to your CSV file
        try:
            with open(file_name, mode='r') as file:
                self.device_info.setText(file.read())
        except:
            self.device_info.setText("Fetch Error")

        self.closeTab()

    def call_password_reset(self):
        index = self.tabWidget.indexOf(self.tabWidget.widget(1))
        if index <= 0:
            self.reopenTab()
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setCurrentIndex(1)
            self.tabWidget.setTabText(1, "Reset Password")
        else:
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setCurrentIndex(1)
            self.tabWidget.setTabText(1, "Reset Password")

    def reopenTab(self):
        if self.closed_tabs:
            # Get the last closed tab and its content
            tab_title, tab_content = self.closed_tabs.pop()

            # Add the tab with its content back to the tab widget
            self.tabWidget.addTab(tab_content, tab_title)

    def uid_email_verify(self):
        uid_text = self.uid_lineEdit_2.text()
        self.email_text = self.email_lineEdit.text()
        if docket.check_exist_uid(uid_text) == 1:
            if docket.check_exist(self.email_text) == 1:

                self.otp_label.setVisible(True)
                self.otp_lineEdit_2.setVisible(True)
                self.otp_verify_button_2.setVisible(True)
                self.otp = docket.security_key(10)

                sub = 'User Verification'
                message = """"<h2>Welcome to DOCKET - A daily planner</h2>
                    <h3>Here is your One Time Password, <b>OTP::</b></h3>
                    <h2>
                    """ + self.otp + """</h2><br><br>
                    <p>Use it for user verification.</p>
                    <p><br><b>Are you not "User"?</b> Then simply ignore this mail or complain to us.</p>
                    <br>Thanks in Advanced!</br>
                    """
                docket.mail_send(sub, self.email_text, message)
            else:
                self.email_lineEdit.setText("Email Error! Try again")
        else:
            self.uid_lineEdit_2.setText("UID Error! Try again")

    def otp_verify(self):
        inputted_otp = self.otp_lineEdit_2.text()
        if docket.security_check(inputted_otp, self.otp) == 'succeed':
            self.change_password_box.setVisible(True)
        else:
            self.otp_lineEdit_2.setText("Wrong OTP, Try again!")
    
    def password_change(self):
        new_pass = self.password_change_edit_2.text()
        docket.change_password(self.email_text,new_pass)
        self.change_password_box.setTitle("Password Changed Successfully")
        sub = 'Password Change Notification'
        message = """"<h2>Welcome to DOCKET - A daily planner</h2>
                            <h2>Your password has been succesfully changed.</h2>
                             <br><h3>Thanks in Advanced!</h3></br>
                            """
        docket.mail_send(sub, self.email_text, message)


    def sign_out_function(self):
        path = ofh.read_uid()
        file_path = path + ".db"
        docket.sign_out_status(path)

        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists("user_data"):
            os.remove("user_data")

        if os.path.exists("user_name"):
            os.remove("user_name")

        if os.path.exists("user_device"):
            os.remove("user_device")

        docket.sign_out_status(path)

        QApplication.quit()