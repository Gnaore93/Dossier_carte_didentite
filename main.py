import sys
from PyQt5.QtWidgets import QApplication
from Widget.app import AccountPage



def main():
    app = QApplication(sys.argv)
    home = AccountPage()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
