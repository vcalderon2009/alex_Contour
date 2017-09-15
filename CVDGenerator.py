#!/usr/bin/env python

import os
import json
import wx
import GifTiffLoader as GTL
import ImageContour.SubContourTools as SCT

Data_path = os.path.abspath('./Segments/')

# app = wx.App()
# d = wx.DirSelector('Select a SWS results Directory (must contain a Segments folder)')

d=os.getcwd()
segDir     = os.path.join(d,'Segments')
outputFile = os.path.join(d,'cellularVoronoiDiagramList.json')
waterArr   = GTL.LoadFileSequence(segDir)
cvdList    = SCT.GetCVDListStatic( waterArr,
                                d,
                                True,
                                splitLength=None,
                                fixedNumInteriorPoints=0)
# Writing to file
with open(outputFile,'w') as fid:

    json.dump(cvdList,fid)

