# Public street camera's in Porto, Conflate OSM import

## Usage

1. `pip install conflate`
2. `python import.py -i cameras.json -o result.osm --osm existing_cameras.osm -c preview.json`

## TODO

After testing the importing process, you should follow the [import guidelines](https://wiki.openstreetmap.org/wiki/Import/Guidelines). At the least, you should post to your regional mailing list or regional forum, and/or to the imports@ mailing list:

* What are you planning to import.
* Why the license for the dataset is compatible with OSM contributor's terms (CC0 and PD sources are okay, CC-BY and more restrictive licenses would require a permission from an owner).
* How many relevant objects there are in OSM now, how many will be altered and how many will be updated (the conflator prints these numbers).
* Link to the profile you are using, if relevant.
* Link to a preview map. Go to geojson.io, open your json file and press "Share".
* A date for the final import, if there are no major objections. Give it a week or two, depending on an import size.

## Source
We're using the GeoJSON version of this dataset: https://mipweb.cm-porto.pt/MuniSIG/MuniSIGViewer/Index.html?configBase=https%3A%2F%2Fmipweb.cm-porto.pt%2FMuniSIG%2FREST%2Fsites%2FUrbanismo%2Fviewers%2FMipweb_-_Mobile%2Fvirtualdirectory%2FResources%2FConfig%2FDefault&layerTheme=1&scale=36111.909643&basemap=aWdfY2FydG9ncmFmaWFfdG90&center=-961296.5104906509%2C5035897.13304301&layers=0kWSNk1CXegz15BnDr2cXyeG3uffU40rAoxN0XkIKa1YUcwG21GugT3w6tVJ027sXX1OTEVz1TfrIx0lBkuh3d%2BblN1KVO201BcLnH283XLY3SpBUq

## Code License
WTFPL. Do what the fuck you want! \o/

## Data License
This is rather unclear. Input gladly appreciated, the author himself does not feel called into legal debate (hence the 'anti-legalistic' code license. On the web map (link above), no copyright is asserted and a copyright notice is also absent from exports made, we might (or might not) assume that this implies the data is public domain.
