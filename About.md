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

  - [GET /api/v1/resources/messier?all](#get-objects)
  - [GET /api/v1/resources/messier?N_messier={id}](#get-objectsid)
  - [GET /api/v1/resources/messier?magnitude={id}&constellation_FR={id}&Year={id}](#get-objectsidparameter)
  
 ### GET /objects

Example: https://messier-123.herokuapp.com/api/v1/resources/messier/all

Response body:
```
{
    "Constellation": "Com", 
    "Constellation_EN": "Hair of Berenice", 
    "Constellation_FR": "Chevelure de B\u00e9r\u00e9nice", 
    "Constellation_Latin": "Coma Berenices", 
    "Dec (Declinaison)": "+18:11:29.4", 
    "Discoverer": "M\u00e9chain", 
    "Distance (l.y / a. l.)": "41000000", 
    "Image": "http://www.lasam.ca/messier/M085.JPG", 
    "Magnitude": "9", 
    "Messier": "M85", 
    "NGC": "NGC 4382", 
    "Object type / Type d'objet": "Galaxy / Galaxie", 
    "RA (Right Ascension)": "12:25:24.11", 
    "Season / Saison": "Spring / Printemps", 
    "Size / Dimensions": "7,1' x 5,2'", 
    "URL de l'image": "https://www.datastro.eu/api/v2/catalog/datasets/catalogue-de-messier/files/6f5ba5b373b9d98409c648eccca69991", 
    "Year": "1781"
  }, 
  ...
  {
    "Constellation": "CVn", 
    "Constellation_EN": "Hound Dogs", 
    "Constellation_FR": "Les\u00a0Chiens de chasse", 
    "Constellation_Latin": "Canes Venatici", 
    "Dec (Declinaison)": "+42:01:45.4", 
    "Discoverer": "M\u00e9chain", 
    "Distance (l.y / a. l.)": "23800000", 
    "Image": "http://www.lasam.ca/messier/M063.JPG", 
    "Magnitude": "8", 
    "Messier": "M63", 
    "NGC": "NGC 5055", 
    "Object type / Type d'objet": "Galaxy / Galaxie", 
    "RA (Right Ascension)": "13:15:49.33", 
    "Season / Saison": "Spring / Printemps", 
    "Size / Dimensions": "12,0' x 7,6'", 
    "URL de l'image": "https://www.datastro.eu/api/v2/catalog/datasets/catalogue-de-messier/files/6cc3be477870d7c2a23c13181ba4ce0c", 
    "Year": "1779"
  }
```

### GET /objects/{id}

Example: https://messier-123.herokuapp.com/api/v1/resources/messier?N_messier=M1

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
### GET /objects/{parameter}
Example: http://messier-123.herokuapp.com/api/v1/resources/messier?magnitude=3&constellation_FR=Cancer

Response body:
```
[
  {
    "Constellation": "Cnc", 
    "Constellation_EN": "Crab", 
    "Constellation_FR": "Cancer", 
    "Constellation_Latin": "Cancer", 
    "Dec (Declinaison)": "+19:40:19.4", 
    "Discoverer": "", 
    "Distance (l.y / a. l.)": "520", 
    "Image": "http://www.lasam.ca/messier/M044.JPG", 
    "Magnitude": "3", 
    "Messier": "M44", 
    "NGC": "NGC 2632", 
    "Object type / Type d'objet": "Open Cluster / Amas Ouvert", 
    "RA (Right Ascension)": "08:40:22.20", 
    "Season / Saison": "Spring / Printemps", 
    "Size / Dimensions": "70,0'", 
    "URL de l'image": "https://www.datastro.eu/api/v2/catalog/datasets/catalogue-de-messier/files/d4caf3578fb228161b3065e9d37cc2b2", 
    "Year": ""
  }
]
```



### Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |




