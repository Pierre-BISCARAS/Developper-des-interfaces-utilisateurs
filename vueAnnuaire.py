import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSignal
from personne import Personne
from vuePersonne import VuePersonne

class VueAnnuaire(QWidget):
    # signal
    nextClicked = pyqtSignal()
    previousClicked = pyqtSignal()
    openFileClicked = pyqtSignal(str)
    newClicked = pyqtSignal()
    personneChanged = pyqtSignal(dict)
    saveAsClicked =pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.topLayout : QVBoxLayout = QVBoxLayout(); self.setLayout(self.topLayout)

        self.pers = VuePersonne()
        self.topLayout.addWidget(self.pers)

        self.footerLayout : QHBoxLayout = QHBoxLayout()

        self.footerContaineur : QWidget = QWidget() ; self.footerContaineur.setLayout(self.footerLayout)
        self.topLayout.addWidget(self.footerContaineur)

        self.precedent : QPushButton = QPushButton("<< précedent") ; self.footerLayout.addWidget(self.precedent)
        self.load : QPushButton = QPushButton("load") ; self.footerLayout.addWidget(self.load)
        self.new : QPushButton = QPushButton("new") ; self.footerLayout.addWidget(self.new)
        self.saveAs : QPushButton = QPushButton("save as") ; self.footerLayout.addWidget(self.saveAs)
        self.suivant : QPushButton = QPushButton("suivant >>") ; self.footerLayout.addWidget(self.suivant)

        self.pers.personneChanged.connect(self.changepersonne)
        self.suivant.clicked.connect(self.next)
        self.precedent.clicked.connect(self.previous)
        self.new.clicked.connect(self.neww)
        self.saveAs.clicked.connect(self.save)
        self.load.clicked.connect(self.open)

        self.show()


    def changepersonne(self, dict : dict):
        self.personneChanged.emit(dict)

    def next(self):
        self.nextClicked.emit()

    def previous(self):
        self.previousClicked.emit()

    def neww(self):
        self.newClicked.emit()

    def save(self):
        self.saveAsClicked.emit("anphi.json")

    def open(self):
        self.openFileClicked.emit("anphi.json")


    def updatePersonne(self, p : Personne):
        self.pers.updatePersonne(p.nom,p.prenom,p.genre,p.naissance,p.mort,p.bio)
        

if __name__ == "__main__" :
    app : QApplication = QApplication(sys.argv)
    test : VueAnnuaire = VueAnnuaire()
    sys.exit(app.exec())
