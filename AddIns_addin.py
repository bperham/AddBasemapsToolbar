import arcpy
import pythonaddins

class AddBingMaps(object):
    """Implementation for AddIns_addin.button_AddBingMaps (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\BingMaps.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
        
class AddTopoMaps(object):
    """Implementation for AddIns_addin.button_AddTopoMaps (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\TopoMaps.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass

class AddWorldImagery(object):
    """Implementation for AddIns_addin.button_AddWorldImagery (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\WorldImagery.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass

class AddParcelData(object):
    """Implementation for AddIns_addin.button_AddParcelData (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\PPLTD_Parcel_Data.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
        
class AddPLSS(object):
    """Implementation for AddIns_addin.button_AddPLSS (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\PLSS_National_WMS.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
