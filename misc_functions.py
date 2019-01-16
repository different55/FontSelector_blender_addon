import bpy
import os

from .preferences import get_addon_preferences


# suppress filepath
def fontselector_suppress_fp(index) :
    #get addon prefs
    addon_preferences = get_addon_preferences()
    fplist = addon_preferences.font_folders
    
    fplist.remove(index)
    #operator refresh fonts if list created

# export menu
def menu_export_favorites(self, context) :
    self.layout.operator('fontselector.export_favorites', text="Favorite Fonts export", icon='FILE_FONT')

# clear collection
def clear_collection(collection) :
        if len(collection)>=1:
            for i in range(len(collection)-1,-1,-1):
                collection.remove(i)

# absolute path
def absolute_path(path) :
        apath = os.path.abspath(bpy.path.abspath(path))
        return apath

# get size of folder and subdir in bytes
def get_size(folderpath) :
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# create directory if doesn't exist
def create_dir(dir_path) :
        if os.path.isdir(dir_path) == False :
                os.makedirs(dir_path)