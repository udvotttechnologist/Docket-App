from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget,QMainWindow)

import docket_applications as docket
import offline_file_handling as ofh
import database_handling
import os

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if not SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.resize(595, 572)
        SignIn.setMaximumSize(QSize(850, 700))
        central_widget = QWidget(SignIn)
        SignIn.setCentralWidget(central_widget)  # Set the central widget for the QMainWindow

        self.gridLayout = QGridLayout(central_widget)  # Use the central widget for the layout
        self.gridLayout.setObjectName(u"gridLayout")
        self.Docket_Label = QLabel(SignIn)
        self.Docket_Label.setObjectName(u"Docket_Label")

        self.gridLayout.addWidget(self.Docket_Label, 0, 0, 1, 1)

        self.User_Info = QFrame(SignIn)
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
        self.frame = QFrame(self.user_info_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.register_window = QPushButton(self.frame)
        self.register_window.setObjectName(u"register_window")
        self.register_window.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.register_window, 4, 1, 1, 1)

        self.email_line_edit = QLineEdit(self.frame)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.gridLayout_6.addWidget(self.email_line_edit, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.pushButton, 2, 1, 1, 1)

        self.email_label_2 = QLabel(self.frame)
        self.email_label_2.setObjectName(u"email_label_2")

        self.gridLayout_6.addWidget(self.email_label_2, 0, 0, 1, 1)

        self.password_line_edit = QLineEdit(self.frame)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout_6.addWidget(self.password_line_edit, 1, 1, 1, 1)

        self.pass_label = QLabel(self.frame)
        self.pass_label.setObjectName(u"pass_label")

        self.gridLayout_6.addWidget(self.pass_label, 1, 0, 1, 1)

        self.forget_pass = QPushButton(self.frame)
        self.forget_pass.setObjectName(u"forget_pass")

        self.gridLayout_6.addWidget(self.forget_pass, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.tabWidget.addTab(self.user_info_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
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

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.User_Info, 1, 0, 1, 1)

        self.status = QLabel(SignIn)
        self.status.setObjectName(u"status")

        self.gridLayout.addWidget(self.status, 2, 0, 1, 1)

        self.pushButton.clicked.connect(self.call_sign_in)
        self.register_window.clicked.connect(self.call_register_ui)

        self.retranslateUi(SignIn)

        if docket.check_internet() == False:
            error_message = "<html><h3 style='color:red'><b>Your Internet Connection is not available! <br>Please Re-Open the window and try again</h3></html>"
            self.status.setText(error_message)
            self.pushButton.setVisible(False)
            self.forget_pass.setVisible(False)
            self.register_window.setVisible(False)

        self.closed_tabs = []
        # Make tabs closable
        self.tabWidget.setTabsClosable(True)

        # Connect the tabCloseRequested signal to the slot that closes tabs
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.setTabEnabled(1, False)
        #self.tabWidget.removeTab(1)
        self.tabWidget.isTabVisible(0)
        self.tabWidget.setCurrentIndex(1)

        self.change_password_box.setVisible(False)
        self.otp_label.setVisible(False)
        self.otp_lineEdit_2.setVisible(False)
        self.otp_verify_button_2.setVisible(False)
        self.otp = ''
        self.email_text = ''

        self.forget_pass.clicked.connect(self.call_password_reset)
        self.closeTab()

        self.check_button_2.clicked.connect(self.uid_email_verify)
        self.otp_verify_button_2.clicked.connect(self.otp_verify)
        self.change_password_button_2.clicked.connect(self.password_change)

        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.Docket_Label.setText(QCoreApplication.translate("SignIn", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Docket</span></p></body></html>", None))
        self.register_window.setText(QCoreApplication.translate("SignIn", u"Not User? Register", None))
        self.pushButton.setText(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.email_label_2.setText(QCoreApplication.translate("SignIn", u"Email", None))
        self.pass_label.setText(QCoreApplication.translate("SignIn", u"Password", None))
        self.forget_pass.setText(QCoreApplication.translate("SignIn", u"Forget Password?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_info_tab), QCoreApplication.translate("SignIn", u"Sign In", None))
        self.change_password_box.setTitle(QCoreApplication.translate("SignIn", u"Change Password", None))
        self.change_password_button_2.setText(QCoreApplication.translate("SignIn", u"Change Password", None))
        self.password_reset_label.setText(QCoreApplication.translate("SignIn", u"<html><head/><body><h3>Enter the new password</h3></body></html>", None))
        self.verify_box.setTitle(QCoreApplication.translate("SignIn", u"Verification", None))
        self.uid_label_2.setText(QCoreApplication.translate("SignIn", u"Enter UID", None))
        self.email_label.setText(QCoreApplication.translate("SignIn", u"Enter Email", None))
        self.check_button_2.setText(QCoreApplication.translate("SignIn", u"Check", None))
        self.otp_label.setText(QCoreApplication.translate("SignIn", u"Enter the OTP", None))
        self.otp_verify_button_2.setText(QCoreApplication.translate("SignIn", u"Verify", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SignIn", u"Reset Password", None))
        self.status.setText("")
    # retranslateUi

    def closeTab(self):
        # Get the current index of the tab to close
        index = self.tabWidget.currentIndex()

        # Store the removed tab content and its title
        tab_content = self.tabWidget.currentWidget()
        tab_title = self.tabWidget.tabText(index)
        self.closed_tabs.append((tab_title, tab_content))

        # Remove the tab
        self.tabWidget.removeTab(index)

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
                self.status.setText("<p style='color:red'>An Verification Code send to {}. <br> Check Your Email for verification.</p>".format(self.email_text))
                sub = 'User Verification'
                message = """"<h2>Welcome to DOCKET - A daily planner</h2>
                    <h3>Here is your One Time Password, <b>OTP::</b></h3>
                    <h2>
                    """ + self.otp + """</h2><br><br><p style='color:red'>
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
        docket.change_password(self.email_text, new_pass)
        self.status.setText("<h3 style='color:green'>Password changed Successfully! <br>Now You can login with your New Passowrd.</h3>")
        sub = 'Password Change Notification'
        message = """"<h2>Welcome to DOCKET - A daily planner</h2>
                            <h2>Your password has been succesfully changed.</h2>
                             <br><h3>Thanks in Advanced!</h3></br>
                            """
        docket.mail_send(sub, self.email_text, message)

    def call_sign_in(self):
        email_id = self.email_line_edit.text()
        password_id = self.password_line_edit.text()

        docket.push_device_info(email_id)
        user_data = docket.fetch_user_data(email_id)
        ofh.create_and_insert_file(user_data)

        return_value = docket.login_user(email_id, password_id)
        self.status.setText(return_value)

        if return_value == 'Succesfully logged in':
            n_user = docket.check_new_user(email_id)  # checks if the user is new. if the user is new then creates new databse for the user
            if n_user == 'New_User':
                database_handling.append_db()
                database_handling.append_table_for_notification()
                file_name = ofh.read_uid() + '.db'
                docket.sign_in_status(email_id)
                docket.sync_online(file_name)
            else:  # if the user is not new then downloads the database from the server
                file_name = ofh.read_uid() + '.db'
                docket.download_online(file_name)
                docket.sign_in_status(email_id)


            self.call_main_window()

    def call_register_ui(self):
        from registration_ui import Ui_Register
        self.window = QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window)
        self.window.show()

    def call_main_window(self):
        import mainwindow
        # Create an instance of the MainWindow class
        self.main_window = QMainWindow()

        # Create an instance of the Ui_MainWindow class from the mainwindow module
        self.ui_main_window = mainwindow.Ui_MainWindow()

        # Set up the main window UI
        self.ui_main_window.setupUi(self.main_window)

        # Show the main window and close the sign-in window
        self.main_window.show()


