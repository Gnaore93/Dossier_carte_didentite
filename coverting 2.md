- for converting ui file to python3 file use that command
#etape 1
py -m PyQt5.uic.pyuic -x [ui file] -o [py file]
 install env et activé
- for converting qrc file to python3 file use that command
#etape 2
pyrcc5 -o [py file] [qrc file]

- run the application in the main file

----------------
 #etape 4
def main():
    app = QApplication(sys.argv)
    home = AccountPage()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()

----------------

- other py file in widget folder
#etape 3
class AccountPage(QtWidgets.QMainWindow, accueilInterface.Ui_Home):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)



