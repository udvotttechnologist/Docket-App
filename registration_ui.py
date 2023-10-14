from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget,QCheckBox)

import docket_applications as docket
import psycopg2

host = "db.zchhatbxymoarixuwoqn.supabase.co"
port = 5432
database = "postgres"
user = "postgres"
password = "Docket+Access+Database+*2345#"
class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(537, 610)
        Register.setMaximumSize(QSize(590, 610))
        Register.setStyleSheet(u"")
        self.centralwidget = QWidget(Register)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.password_line_edit = QLineEdit(self.frame)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


        self.gridLayout.addWidget(self.password_line_edit, 2, 1, 1, 1)

        self.name_label = QLabel(self.frame)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.otp_label = QLabel(self.frame)
        self.otp_label.setObjectName(u"otp_label")

        self.gridLayout.addWidget(self.otp_label, 3, 0, 1, 1)

        self.email_line_edit = QLineEdit(self.frame)
        self.email_line_edit.setObjectName(u"email_line_edit")

        self.gridLayout.addWidget(self.email_line_edit, 1, 1, 1, 1)

        self.pass_label = QLabel(self.frame)
        self.pass_label.setObjectName(u"pass_label")

        self.gridLayout.addWidget(self.pass_label, 2, 0, 1, 1)

        self.name_line_edit = QLineEdit(self.frame)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.gridLayout.addWidget(self.name_line_edit, 0, 1, 1, 1)

        self.register_button = QPushButton(self.frame)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_button.setStyleSheet(u"")

        self.gridLayout.addWidget(self.register_button, 4, 1, 1, 1)
        self.verify_button = QPushButton(self.frame)
        self.verify_button.setObjectName(u"verify_button")
        self.verify_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.verify_button.setStyleSheet(u"")

        self.gridLayout.addWidget(self.verify_button, 5, 1, 1, 1)

        self.email_label = QLabel(self.frame)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 1, 0, 1, 1)

        self.otp_line_edit = QLineEdit(self.frame)
        self.otp_line_edit.setObjectName(u"otp_line_edit")
        self.otp_line_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.otp_line_edit, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(570, 200))
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.docket_logo = QLabel(self.frame_2)
        self.docket_logo.setObjectName(u"docket_logo")
        self.docket_logo.setGeometry(QRect(240, 30, 80, 40))
        self.docket_logo.setMaximumSize(QSize(250, 250))
        self.docket_logo.setCursor(QCursor(Qt.WhatsThisCursor))
        self.status = QLabel(self.frame_2)
        self.status.setObjectName(u"status")
        self.status.setText("")
        self.status.setGeometry(QRect(20, 71, 471, 120))
        self.status.setMaximumSize(471,120)

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        Register.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Register)
        self.statusbar.setObjectName(u"statusbar")
        Register.setStatusBar(self.statusbar)

        self.otp_line_edit.setVisible(False)
        self.otp_label.setVisible(False)
        self.verify_button.setVisible(False)
        self.register_button.clicked.connect(self.call_register)

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Register", None))
        self.name_label.setText(QCoreApplication.translate("Register", u"Name", None))
        self.otp_label.setText(QCoreApplication.translate("Register", u"OTP", None))
        self.pass_label.setText(QCoreApplication.translate("Register", u"Password", None))
        self.register_button.setText(QCoreApplication.translate("Register", u"Register", None))
        self.email_label.setText(QCoreApplication.translate("Register", u"Email", None))
#if QT_CONFIG(whatsthis)
        self.frame_2.setWhatsThis(QCoreApplication.translate("Register", u"Docket Logo", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.docket_logo.setWhatsThis(QCoreApplication.translate("Register", u"Docket", None))
#endif // QT_CONFIG(whatsthis)
        self.docket_logo.setText(QCoreApplication.translate("Register", u"<html><h2>Docket</h2></html>", None))
    # retranslateUi
    def call_register(self):
        email_id = self.email_line_edit.text()
        password_id = self.password_line_edit.text()
        name_id = self.name_line_edit.text()
        exist = docket.check_exist(email_id)
        otp = docket.security_key(8)

        if exist == 0:
            sub = 'User Verification'
            message = message = """"<h2>Welcome to DOCKET - A daily planner</h2> 
            <h3>Here is your One Time Password, <b>OTP::</b></h3>
            <h2>
            """ + otp + """</h2><br><br>
            <p>Use it for user verification.</p>
            <p><br><b>Are you not "User"?</b> Then simply ignore this mail or complain to us.</p>
            <br>Thanks in Advanced!</br>
            """
            send = docket.mail_send(sub, email_id, message)
            self.status.setText("<html><body><p>An email sent to "+email_id+"<br> Check your email ASAP</body></html>")
            self.otp_label.setVisible(True)
            self.otp_line_edit.setVisible(True)

            self.register_button.setVisible(False)
            self.verify_button.setVisible(True)
            self.verify_button.setText('Verify')

            self.verify_button.clicked.connect(lambda: self.cross_check(otp, name_id, email_id, password_id))

        else:
            self.status.setText("<html>The same email already exist in our database, <br>try with another email</html>")


    def cross_check(self,otp,name,email,psswrd):
        check_otp = self.otp_line_edit.text()
        exist = docket.check_exist(email)
        if exist == 0:
            if otp == check_otp:
                uid = docket.security_key(30)
                connect = psycopg2.connect(
                    host=host,
                    port=port,
                    database=database,
                    user=user,
                    password=password
                )
                cursor = connect.cursor()

                query = """
                INSERT INTO user_list (name, email, pass, uid,status)
                VALUES (%s, %s, %s, %s, %s);"""
                val = (name, email, psswrd, uid,"New_User")
                cursor.execute(query, val)
                connect.commit()

                return_value = ["User created!", "Your user id(UID) authentication code is: " + uid,
                                "Save it for future purpose"]

                confirmation_sub = "Welcome to Docket - A Daily Planner"
                confirmation_mail = """<h2 style = "color:blue">Hello """ + name + """</h>
                            <br><br><h2>Your account has been created successfully. Your Docket user id(UID) authentication code is: """ + uid + """</h2>
                            <br><h2>Save it for further uses.<br> </h2>
                            <br> <h2 style="color:red">it may be necessary during the security purpose.</h2> 
                            <br><h2>Thanks for using Docket! </h2>"""

                docket.mail_send(confirmation_sub, email, confirmation_mail)

                self.status.setText(
                    "<html><body>User created!<br>Your user id(UID): <b>" + uid + "</b><br>Save it for future purpose<br>Now close this window and Login</body></html>")
                #docket.set_new_user_log(email)
            elif check_otp != otp:
                self.status.setText('Authentication Failed! Please try again!')

        else:
            self.status.setText("<html>The same email already exist in our database, <br>try with another email</html>")
