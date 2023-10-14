from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
from sign_in_ui import Ui_SignIn
import sys
import database_handling as dh
import offline_file_handling as ofh

# Create the QApplication instance here
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Sign_In_Window(QMainWindow):  # Use QMainWindow, not QApplication
    def __init__(self):
        super().__init__()
        self.ui = Ui_SignIn()
        self.ui.setupUi(self)

if ofh.check_error() == "exist":
    if ofh.check_db_error() == "exist":
        dh.append_db()
        window = MainWindow()
        window.show()
    elif ofh.check_db_error() == "error":
        window = Sign_In_Window()
        window.show()

elif ofh.check_error() == "error":
    window = Sign_In_Window()
    window.show()

sys.exit(app.exec())  # Start the application event loop
