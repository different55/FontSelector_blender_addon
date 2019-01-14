import bpy

from.preferences import get_addon_preferences


class FontSelectorPanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_category = "Font Selector"
    bl_context = "data"
    bl_label = "Font Selection"
    
    @classmethod
    def poll(cls, context):
        active=bpy.context.active_object
        if active is not None:
            active_type=active.type
        else:
            active_type=""
        return active_type=='FONT'

    def draw(self, context):
        layout = self.layout
        #get addon prefs
        addon_preferences = get_addon_preferences()
        rownumber=addon_preferences.row_number
        fplist = addon_preferences.font_folders
        activedata=bpy.context.active_object.data
        fonth=bpy.data.window_managers['WinMan']
        
        if len(fonth.fontselector_sub)>5:
            sub_row = 5
        else:
            try :
                sub_row=len(fonth.fontselector_sub)
            except IndexError :
                sub_row = 1
        
        if len(fplist)==0:
            layout.label('Add Font Folder in Addon Preference', icon='INFO')
        else:
            row=layout.row()
            row.operator("fontselector.refresh", icon='FILE_REFRESH')
            if fonth.fontselector_list==0:
                row=layout.row()
                row.label('Refresh to get List of available Fonts', icon='INFO')
            else: 
                row.operator("fontselector.remove_unused", icon='UNLINKED')
                row.prop(activedata, 'fontselector_use_sub', text='', icon='FILESEL')
                if activedata.fontselector_favs==True:
                    row.prop(activedata, 'fontselector_favs', text='', icon='SOLO_ON')
                elif activedata.fontselector_favs==False:
                    row.prop(activedata, 'fontselector_favs', text='', icon='SOLO_OFF')
                if len(fonth.fontselector_sub)!=0 and activedata.fontselector_use_sub==True:
                    row=layout.row()
                    row.template_list("SubdirUIList", "", fonth, "fontselector_sub", activedata, "fontselector_sub_index", rows=sub_row)
                row=layout.row()
                row.template_list("FontUIList", "", fonth, "fontselector_list", activedata, "fontselector_index", rows=rownumber)