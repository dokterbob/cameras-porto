#!/usr/bin/env python3
import conflate

class Profile:

    # download_url = 'https://mipweb.cm-porto.pt/arcgis/rest/services/InfraestruturasMobilidade/MapServer/0/query?f=geojson&where=1%3D1&returnGeometry=true&outSR=4326'
    max_distance = 5
    dataset_id = 'porto_streetcameras'
    source = 'mipweb.cm-porto.pt'

    query = [
        ('man_made', 'surveillance')
    ]

    no_dataset_id = True

    def dataset(f):
        """ A function that should return a list of dicts with 'id', 'lat', 'lon' and 'tags' keys. It is provided with a file object for the first parameter, either an actual file or a wrapper to downloaded data. """
        import json, codecs

        reader = codecs.getreader('utf-8')
        json_src = json.load(reader(f))

        common_tags = {
            'man_made': 'surveillance',
            'surveillance': 'public',
            'surveillance:type': 'camera',
            'operator': 'Câmara Municipal do Porto',
            'surveillance:zone': 'traffic'
        }

        # Parse GeoJSON
        for item in json_src['features']:
            yield conflate.data.SourcePoint(
                item['geometry']['coordinates'],
                item['geometry']['coordinates'][1],
                item['geometry']['coordinates'][0],
                common_tags
            )

conflate.run(Profile)
