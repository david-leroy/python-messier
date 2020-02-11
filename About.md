# Projet Python : Catalogue de Messier

David Leroy
Yves Trang
Baptiste Dhuicque

# Projet Messier

Mise en place d'un catalogue de Messier dans le cadre du cours de Python du Mastère data à Hétic.

> Charles Messier, astronome français du XVIIIème siècle spécialiste des comètes a élaboré ce catalogue des objets diffus. En cherchant de nouvelles comètes dans le ciel, il était perturbé par de nombreuses taches laiteuses et diffuses. Afin de se débarasser de ces objets parasites, il décida de les lister ... Autrefois inconnus, ces objets diffus sont des galaxies, des nébuleuses planétaires, des amas globulaires ou des amas ouverts, tous visibles dans l'hémisphère nord. Aujourd'hui, ce catalogue de 110 objets fait autorité en France parmi la communauté des astronomes amateurs. Dans le catalogue Messier, vous trouverez les coordonnées ainsi que les principales caractéristiques de ces objets.

Source [astropolis.fr](https://www.astropolis.fr/catalogue-Messier/page-de-garde/astronomie-accueil-catalogue-Messier.html)



## 1/ les données (Messier amélioré)

Detail du é le furet des comètes :
* Numero Messier : de 1 à 103
* Numero NGC : 
* Image : photographie de l'objet astronomique
* Type :
* Declinaison : Distance angulaire d'un astre au plan équatorial.
* Constellation : Nom de la constellation
* A.D. : l'équivalent sur la sphère céleste de la longitude terrestre en degré
* Taille : Année-lumière
* Magnitude : Grandeur qui caractérise l'éclat des astres visibles.
* Repérage : qualité du Repearge (Très bonne qualité - Bonne - Moyene - Mediocre)
* Visibilité : type d'outils d'observation
* Photographiable : Oui ou Non
* Observation : texte 

## 2/ l'intérêt scientifique de ces données et de votre catalogue

Le Catalogue de Messier est le premier catalogue des objets extragalactiques, il a ainsi pu classer un ensemble d'objet spatial immobile pour les différeciers à des comètes.

## 3/ les fonctionnalités minimales de votre outil de consultation
* Recherche
* Affichage des resultats
## 4/ les fonctionnalités idéales de votre outil

## 5/ Technologies utilisées
* [Python] - Langage utilisé pour la création de l'API
* [Flask] - Framework permettant la création de l'API
* [SQLite] - Base de données relationnelle (très légère)
* [HEROKU] - Utilisé pour déployé le code en serverless et hébergement du front

## Request & Response Examples

### API Resources

  - [GET api/v1/resources/messier?N_messier=all](#get-objects)
  - [GET api/v1/resources/messier?N_messier={id}](#get-objectsid)
  - [GET /api/v1/objects/{id}/{parameter}](#get-objectsidparameter)
  - [POST /api/v1](#post-objects)
  
 ### GET /objects

Example: http://example.gov/api/v1/resources/messier?N_messier=M1

Response body:
```
[
  {
    "Constellation": "Tau", 
    "Constellation_EN": "Bull", 
    "Constellation_FR": "Taureau", 
    "Constellation_Latin": "Taurus", 
    "Dec (Declinaison)": "+22:00:52.1", 
    "Discoverer": "B\u00e9vis", 
    "Distance (l.y / a. l.)": "6500", 
    "Image": "http://www.lasam.ca/messier/M001.JPG", 
    "Magnitude": "8", 
    "Messier": "M1", 
    "NGC": "NGC 1952", 
    "Object type / Type d'objet": "Supernova remnant / Reste de Supernova", 
    "RA (Right Ascension)": "05:34:31.97", 
    "Season / Saison": "Winter / Hiver", 
    "Size / Dimensions": "6,0' x 4,0'", 
    "URL de l'image": "https://www.datastro.eu/api/v2/catalog/datasets/catalogue-de-messier/files/9e2732e960c78804a2ee3fa059c69231", 
    "Year": "1731"
  }
]
```

### GET /objects/{id}

Example: http://example.gov/api/v1/objects/1.json

Response body:
```
{
    "result": {
        "id": "1",
        "messier_number": "M1",
        "name": "Crab Nebula",
        "ngc": "NGC 1952",
        "constellation": "Taurus",
        "type": "Supernova remnant",
        "dimension": "6'×4'",
        "distance": {
            "value": "6.3",
            "unit": "kly"
        },
        "magnitude": "8.4",
        "ascension": "05h 34m 31.94s",
        "discovery_date": "03/05/1731",
        "discoverer": "John Bevis",
        "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg"
    }
}
```

### GET /objects/{id}/{parameter}

Example: http://example.gov/api/v1/objects/1/name.json

Response body:
```
{
    "result": {
        "name": "Crab Nebula"
    }
}
```


### Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Liens annexes de données
* [HyperLeda](http://leda.univ-lyon1.fr/)
* [CDS Portal](http://cdsportal.u-strasbg.fr/)

### Installation

> __TODO :__ Compléter les instructions d'installation et de déploiement

### Todos

 - Compléter le fichier about.md
 - Documenter les routes utilisées
 - Initialiser Django Rest Framework
 - Mettre en place l'infrastructure Azure
 - Développer les Az function requises
 - Mettre en place un FrontEnd ludique et interactif


