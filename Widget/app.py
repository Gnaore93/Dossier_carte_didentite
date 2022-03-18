from tkinter import END
from unittest import result
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox,QDialog,QFileDialog,QTableWidgetItem
from PyQt5.QtGui import QPixmap
from Widget.identite import Ui_MainWindow
from PyQt5.uic import loadUi
import sqlite3


class AccountPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_enregistrer.clicked.connect(self.valider_donner)
        self.btn_browser.clicked.connect(self.browser_files)
        self.btn_recherche_bar.clicked.connect(self.seach_bar)
    def browser_files(self):
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac_33/Desktop/PHOTO')
        self.label_photo1.setPixmap(QPixmap(file_name[0]))
        self.label_photo2.setPixmap(QPixmap(file_name[0])) 
        self.entry_browser.setText(file_name[0])
        print(file_name) 
    def valider_donner(self): 
        
        d={
            "Nom": self.entry_nom.text(),
            "Prenom":self.entry_prenom.text(),
            "Sexe":self.comboBox_sexe.currentText(),
            "Date_naissance":self.combobox_date_nais.text(),
            "Lieu_naissance":self.entry_lieu_naissance.text(),
            "Profession":self.entry_profession.text(),
            "Domicile":self.entry_domicile.text(),
            "Date_enregistrement":self.combobox_date_enr.text(),
            "Nationnalite":self.entry_nationnalite.text(),
            
        }

       
        conn=sqlite3.connect('myBD_ajout_donnes.db')

        """if self.entry_nom.text() == "" or self.entry_prenom.text() == "" or self.comboBox_sexe.currentText() == "" or self.combobox_date_nais.text() == "" or self.entry_lieu_naissance.text() == "" or self.entry_profession.text()=="" or self.entry_domicile.text()==""or self.combobox_date_enr.text()=="" or self.entry_nationnalite.text()=="":
            QMessageBox.information(self,'erreur','veuillez renseigner tous les champs svp',QMessageBox.ok)
        else:
            QMessageBox.information(self,'succes','Enregistrer avec succes',QMessageBox.ok)"""

        cur =conn.cursor()

        
        cur.execute("""CREATE TABLE IF NOT EXISTS ajout_donnes(
                Nom text,
                Prenom text,
                Sexe text,
                Date_naissance text,
                Lieu_naissance text,
                Profession text,
                Domicile text,
                Date_enregistrement text,
                Nationnalite text    
            )""")

        cur.execute("INSERT INTO ajout_donnes VALUES(:Nom, :Prenom, :Sexe, :Date_naissance, :Lieu_naissance,:Profession,:Domicile,:Date_enregistrement,:Nationnalite)",d)
        
        con = sqlite3.connect('myBD_ajout_donnes.db')
        cur = con.cursor()
        command = '''SELECT * FROM ajout_donnes'''
        result=cur.execute(command)

        self.entry_nom1.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.entry_nom1.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.entry_nom1.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

        conn.commit()
        conn.close()

    def seach_bar(self): 
        conn=sqlite3.connect('myBD_ajout_donnes.db')
        cursor = conn.cursor()
        nom = self.entry_recherche_bar.text()

        command = ''' SELECT * FROM ajout_donnes WHERE Prenom=? '''
        result=cursor.execute(command,[nom])
        self.entry_nom1.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.entry_nom1.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.entry_nom1.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        
        
        
                
        
    
        
    