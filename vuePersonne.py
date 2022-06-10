# -------------------------- Layout --------------------------
# import
import datetime
import sys
from PyQt6.QtWidgets import QWidget ,QLineEdit, QTextEdit,QDateEdit, QHBoxLayout, QComboBox, QVBoxLayout, QApplication, QLabel
from PyQt6.QtCore import pyqtSignal , QDate, Qt
import typing

import genre as g



# ---------------------------- GUI ---------------------------


class VuePersonne(QWidget):

    # signal
    personneChanged : pyqtSignal = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()

        self.reactive = True

        self.topLayout : QVBoxLayout = QVBoxLayout(); self.setLayout(self.topLayout)
        
        self.idLayout : QHBoxLayout = QHBoxLayout()
        self.dateLayout : QHBoxLayout = QHBoxLayout()
        self.textLayout : QHBoxLayout = QHBoxLayout()


        self.idContaineur : QWidget = QWidget() ; self.idContaineur.setLayout(self.idLayout)
        self.dateContaineur : QWidget = QWidget() ; self.dateContaineur.setLayout(self.dateLayout)
        self.textContaineur : QWidget = QWidget() ; self.textContaineur.setLayout(self.textLayout)


        self.topLayout.addWidget(self.idContaineur)
        self.topLayout.addWidget(self.dateContaineur)
        self.topLayout.addWidget(self.textContaineur)

        # -- Identité

        self.genre : QComboBox = QComboBox() ; self.genre.addItems(["M. ", "Mme. ", "_ "]) 
        self.idLayout.addWidget(self.genre)
        self.prenom : QLineEdit = QLineEdit("Prenom"); self.idLayout.addWidget(self.prenom)
        self.nom : QLineEdit = QLineEdit("Nom"); self.idLayout.addWidget(self.nom)

        # -- Date
        self.dateLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nee : QLabel = QLabel("Né le :") ; self.dateLayout.addWidget(self.nee)
        self.dateNaissance : QDateEdit = QDateEdit(); self.dateNaissance.setDateRange(QDate(1,1,1),QDate.currentDate()) 
        self.dateLayout.addWidget(self.dateNaissance)
        self.mort : QLabel = QLabel("Mort le :") ; self.dateLayout.addWidget(self.mort)
        self.dateMort : (QDateEdit | None) = QDateEdit();  self.dateMort.setDateRange(QDate(1,1,1),QDate.currentDate()) 
        self.dateLayout.addWidget(self.dateMort)

        # -- Biographie
    
        self.bio : QTextEdit = QTextEdit('"Biographie"'); self.textLayout.addWidget(self.bio)

        # -- Connexion 
        self.genre.currentIndexChanged.connect(self.changeGenre)
        self.prenom.editingFinished.connect(self.changePrenom)
        self.nom.editingFinished.connect(self.changeNom)
        self.bio.textChanged.connect(self.changeBiographie)
        self.dateNaissance.dateChanged.connect(self.changeNaissance)
        self.dateMort.dateChanged.connect(self.changeMort)


    def updatePersonne(self, prenom: str, nom:str, genre: g.Genre, nee: datetime.date, mort: (datetime.date|None),bio: str) -> None:
        self.reactive = False
        self.prenom.setText(prenom)
        self.nom.setText(nom)
        self.bio.setPlainText(bio)
        self.dateNaissance.setDate(QDate(nee.year, nee.month, nee.day))
        if mort and self.dateMort:
            self.dateMort.setDate(QDate(mort.year, mort.month, mort.day))  
        else: 
            self.dateMort.setDate(QDate(0, 0, 0)) 
        self.genre.setCurrentIndex(genre.value-1)

        self.reactive = True

    # callback
    def changeGenre(self) -> None : 
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo())

    def changePrenom(self) -> None : 
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo())

    def changeNom(self) -> None : 
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo())

    def changeNaissance(self) -> None : 
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo()) 

    def changeMort(self) -> None : 
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo())

    def changeBiographie(self) -> None :
        if self.reactive:
            self.personneChanged.emit(self.getAllInfo())
    
    def getAllInfo(self) :
        if self.dateMort.date() != None: # type: ignore
            return { 
                "genre" : g.Genre(self.genre.currentIndex()+1).name, 
                "prenom" : self.prenom.text(), 
                "nom" : self.nom.text(), 
                "bio" : self.bio.toPlainText(), 
                "naissance" : str(self.dateNaissance.date().toPyDate()), 
                "mort" : str(self.dateMort.date().toPyDate()) #type: ignore
                }
        else :
            return { 
                "genre" : g.Genre(self.genre.currentIndex()+1).name, 
                "prenom" : self.prenom.text(), 
                "nom" : self.nom.text(), 
                "bio" : self.bio.toPlainText(), 
                "naissance" : self.dateNaissance.date().toPyDate(), 
                "mort" : self.dateMort.date().toPyDate() #type: ignore
                }
        



if __name__ == "__main__" :
    app : QApplication = QApplication(sys.argv)
    test : VuePersonne = VuePersonne()
    sys.exit(app.exec())