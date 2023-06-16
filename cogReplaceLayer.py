from arcgis.gis import GIS
from arcgis.mapping import WebMap
import arcpy

# sign into the active portal of the ArcGIS Pro Project this script is run from
gis = GIS('pro')

def main():
    # signs into the active portal of the ArcGIS Pro Project this script is run from

    print("Logged into {} as {}".format(arcpy.GetActivePortalURL(), gis.properties['user']['username']))

    # creates variable for user input services

    # inputs services to web map search function
    wm_search()

    # inputs services to app search function
    #app_search(services)

# returns Web Map title and url where the input service matches a layer
def wm_search():
    print('Searching' + ' webmaps in ' + arcpy.GetActivePortalURL())
    web_maps = gis.content.search(query="", item_type="Web Map", max_items=10000)
    for item in web_maps:
        wm = WebMap(item)
        layers = wm.layers
        for lyr in layers:
            if lyr.layerType == 'ArcGISImageServiceLayer':
                if  'url_2_replace' in lyr.url:
                    print(item)
                    lyr.url = lyr.url.replace('url_2_replace', 'updated_layer_url')
                    wm.update()
                    print(lyr.url)

if __name__ == '__main__':
    main()