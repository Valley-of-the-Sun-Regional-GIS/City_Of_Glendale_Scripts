import json
from arcgis import gis
from arcgis.gis import GIS

def backupMaps2Json():
    #login to portal
    gis = GIS("pro")
    #declare what you are item you are searching for. 
    itemList = ['dashboards', 'Web Map', 'Web Mapping Application']
    #destination folder name.
    folderList = ['DashboardBackups', 'WebMapBackups', 'WebAppBackups']
    for a in range(len(itemList)):
        print('starting to find all the ' + itemList[a] + ' in your portal')
        #set max # of items returned from portal
        MAX_ITEMS_RETURNED = 1000
        #query all owners in portal, get itemid, limit search to integer stored in MAX_ITEMS_RETURNED .
        web_items = gis.content.search(query='owner:*', item_type=itemList[a], max_items = MAX_ITEMS_RETURNED)
        for b in range(len(web_items)):
            web_item_name = web_items[b]
            itemid= web_item_name.itemid
            #itemid = 'dbb11dbb464b4c81baea2c8fdbf0a1a6'
            item2json = gis.content.get(itemid) #Edit the item ID
            jsonData = item2json.get_data(try_json=True)

            with open (r'C:\Users\Username\Documents\YourADMINFOLDER\jsonBackups'+ '\\' + folderList[a] + '\\'+ web_item_name.title+'.json'.replace('\\\\','\\'), "w") as file_handle: #Edit the folder location
                file_handle.write(json.dumps(jsonData))
                #print("Completed")
backupMaps2Json()