import arcpy
import pythonaddins
import arcpy.mapping

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
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\Bing Maps.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
        
class AddTopoBasemap(object):
    """Implementation for AddIns_addin.button_AddTopoBasemap (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\Topo Maps.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
    class AddParcelCoverage(object):
    """Implementation for AddIns_addin.button_AddParcelCoverage (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # get the map document
        mxd = arcpy.mapping.MapDocument("CURRENT")

        # get the data frame
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        # specify the layer
        newlayer = arcpy.mapping.Layer(r"N:\GIS\Layer Files\PPLTD Parcel Coverage.lyr")

        # add the layer to the map at the bottom of the TOC in data frame 0
        arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

        # Refresh things
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        pass
