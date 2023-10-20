CREATE TABLE Clients(
   idClient VARCHAR(100),
   prenom VARCHAR(50),
   nom VARCHAR(50),
   email VARCHAR(50),
   telephone VARCHAR(100),
   dateNaissance DATE,
   mdp VARCHAR(16),
   ville VARCHAR(50),
   pays VARCHAR(50),
   PRIMARY KEY(idClient)
);


CREATE TABLE Commandes(
   idCommande VARCHAR(100),
   dateCommande DATE,
   statut boolean,
   idClient VARCHAR(100) NOT NULL,
   PRIMARY KEY(idCommande),
   FOREIGN KEY(idClient) REFERENCES Clients(idClient)
);

CREATE TABLE Categories(
   idCategorie VARCHAR(100),
   nomCategorie VARCHAR(200),
   idCategorieMere VARCHAR(100) NOT NULL,
   PRIMARY KEY(idCategorie),
   FOREIGN KEY(idCategorieMere) REFERENCES Categories(idCategorie)
);

CREATE TABLE Produits(
   idProduit VARCHAR(100),
   nomproduit VARCHAR(200),
   prix INT,
   poids DECIMAL(15,2),
   idCategorie VARCHAR(100) NOT NULL,
   PRIMARY KEY(idProduit),
   FOREIGN KEY(idCategorie) REFERENCES Categories(idCategorie)
);

CREATE TABLE LignesCommandes(
   noligne VARCHAR(100),
   quantite VARCHAR(50),
   idProduit VARCHAR(100) NOT NULL,
   idCommande VARCHAR(100) NOT NULL,
   PRIMARY KEY(noligne,idCommande),
   FOREIGN KEY(idProduit) REFERENCES Produits(idProduit),
   FOREIGN KEY(idCommande) REFERENCES Commandes(idCommande)
);
