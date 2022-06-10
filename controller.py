import annuaire, vueAnnuaire, personne, vuePersonne, sys
from PyQt6.QtWidgets import QApplication


class Controller:
    # constructor
    def __init__(self) -> None:
        # attrbut
        self.modele = annuaire.Annuaire('anphi.json')
        self.vue = vueAnnuaire.VueAnnuaire()
        p = self.modele.getPersonne()
        if isinstance(p, personne.Personne): self.vue.updatePersonne(p)  # type: ignore
        # slots ie callback
        self.vue.nextClicked.connect(self.next)
        self.vue.previousClicked.connect(self.previous)
        self.vue.openFileClicked.connect(self.openFile)
        self.vue.newClicked.connect(self.new)
        self.vue.personneChanged.connect(self.update)
        self.vue.saveAsClicked.connect(self.saveAs)
    
    def update(self,d) -> None :
        self.modele.update
        if isinstance(d, personne.Personne):
            self.vue.updatePersonne(d.prenom, d.nom, d.genre, d.naissance, d.mort, d.bio)  # type: ignore

    def next(self) -> None:
        self.modele.next()
        self.vue.updatePersonne(self.modele.getPersonne())  # type: ignore

    def previous(self) -> None: 
        self.modele.previous()
        self.vue.updatePersonne(self.modele.getPersonne())  # type: ignore
    
    def new(self) -> None: 
        self.modele.addPersonne(personne.Personne.new())
        self.vue.updatePersonne(self.modele.getPersonne())  # type: ignore

    def openFile(self, fname : str) -> None:
        self.modele = annuaire.Annuaire(fname)
        self.update(self.modele.getPersonne)

    def saveAs(self, fname: str) -> None:
        self.modele.save(fname)

if __name__ == "__main__":
    app : QApplication = QApplication(sys.argv)
    test : Controller = Controller()
    sys.exit(app.exec())
