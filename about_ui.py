from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, About_Docket):
        if not About_Docket.objectName():
            About_Docket.setObjectName(u"About_Docket")
        About_Docket.resize(751, 660)
        self.gridLayout = QGridLayout(About_Docket)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(About_Docket)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(About_Docket)

        QMetaObject.connectSlotsByName(About_Docket)
    # setupUi

    def retranslateUi(self, About_Docket):
        About_Docket.setWindowTitle(QCoreApplication.translate("About_Docket", u"About", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About_Docket", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><img src=\"https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBangladesh_Army_Unive"
                        "rsity_of_Engineering_%2526_Technology&amp;psig=AOvVaw3GOhZ-VyP8lTOhMqt4nmnJ&amp;ust=1696972167546000&amp;source=images&amp;cd=vfe&amp;opi=89978449&amp;ved=0CBEQjRxqFwoTCJib3ovw6YEDFQAAAAAdAAAAABAE\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:15pt; font-weight:700;\">Bangladesh Army University of Engineering &amp; Technology (BAUET)</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:13pt; font-weight:700;\">Qadirabad, Natore-6431</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-h"
                        "eight:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:16pt; font-weight:700;\">Department of Computer Science and Engineering (CSE)</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:26pt; font-weight:700; color:#000000;\">Project</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:18pt; font-weight:700; color:#000000;\">Course Code:</span><span style=\" font-family:'Times New Roman','serif'; font-size:18pt; color:#000000;\"> CSE-2218</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; background-color:transparent;\"><span style=\" font-family:'Times New Roman','serif'; font-size:18pt; font-weight:700; color:#000000;\">Course Title:</span><span style=\" font-family:'Times New Roman','serif'; font-size:18pt; color:#000000;\"> Advanced Programming Sessional</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:108%; font-family:'Times New Roman','serif'; font-size:18pt; color:#000000; background-color:transparent;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"></span><span style=\" font-family:'Times New Roman','serif'; font-size:18pt; font-weight:700; color:#000000;\">Proposed Title:</span><span style=\" font-family:'Times New Roman','serif'; font-size:18p"
                        "t; color:#000000;\"> Docket-A daily Planner</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\">Nazmine Nahar (</span><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; font-weight:700; color:#000000;\">ID:</span><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\"> 0812120105101009)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\">Nafisa Ahsan Mahi (</span><span style=\" font-family:'Times New Roman','serif'; fo"
                        "nt-size:22pt; font-weight:700; color:#000000;\">ID:</span><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\"> 0812120105101011)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\">Rhitwik Adhikary ( </span><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; font-weight:700; color:#000000;\">ID:</span><span style=\" font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\"> 0812120205101055)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700; color:#000000;\">Batch:</span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; color:#000000;\"> CSE-14</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700; color:#000000;\">Session: </span><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; color:#000000;\">2020-2021</span><br><br>Version:0.1.10</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Times New Roman','serif'; font-size:22pt; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"></span></p></body></html>", None))
    # retranslateUi


