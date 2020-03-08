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

## Code License
WTFPL. Do what the fuck you want! \o/

## Data License
This is rather unclear. Input gladly appreciated, the author himself does not feel called into legal debate (hence the 'anti-legalistic' code license. 
