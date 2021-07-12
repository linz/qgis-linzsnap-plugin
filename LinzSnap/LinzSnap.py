from builtins import str
from builtins import object

from qgis.PyQt.QtCore import QFileInfo, QSettings
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.core import Qgis, QgsDataSourceUri, QgsProject, QgsVectorLayer

from random import randint
import sys
import os.path
import re
import math
import sqlite3

from .SnapSqliteLoader import SnapSqliteLoader;

try:
    from VectorFieldLayerManager.VectorFieldLayerManager import VectorFieldLayerManager
    haveVFR=True
except ImportError:
    haveVFR=False

class LinzSnap(object):

    _stnColor = QColor("red")
    _obsColor = QColor.fromRgb(127,127,127)
    _hadjColor = QColor("red")
    _vadjColor = QColor("blue")
    _dbext = ".sqlite"
    
    def __init__( self, iface ):
        self._iface = iface
        self._loader = SnapSqliteLoader()

    def LayerSnapJob(self,layer):
        props = self._snapLayerProperties(layer)
        if props:
            return props['job']
        return ''

    def _snapFileJob( self, filename ):
        job = re.sub(r'(?:\-(?:stn|obs|metadata)\.csv|\.[^\.]*)$','',str(filename))
        return job

    def GetSnapJob( self ):
        job = ''
        s = QSettings()
        setting = "/Plugin/LinzSnap/snapdir"
        path = s.value(setting,"./",str)
        filename, __ = QFileDialog.getOpenFileName(
            self._iface.mainWindow(),
            "SNAP command file", path, 
            "Command files (*.cmd *.snp *.snap);;All files (*.*)")
        if filename:
            s.setValue(setting,QFileInfo(filename).absolutePath())
            job = self._snapFileJob( filename )
        return job

    def _snapLayers( self, job=None ):
        for layer in QgsProject.instance().mapLayers().values():
            props = self._snapLayerProperties(layer)
            if props and (not job or props['job'] == job):
                yield layer, props

    def _providerJob( self, layer ):
        if layer.type() != layer.VectorLayer or layer.dataProvider().name() != "spatialite":
            return None
        uri = QgsDataSourceUri(layer.dataProvider().dataSourceUri())
        db = str(uri.database())
        if db.lower().endswith(self._dbext):
            db = db[0:len(db)-len(self._dbext)]
        return db

    def _snapLayerProperties( self, layer ):
        job = self._providerJob( layer )
        if not job:
            return None
        isSnap = layer.customProperty("SNAPLoader.isSnapJob")
        if not isSnap:
            return None
        return {'job':job }

    def _setSnapLayerProperties( self, layer ):
        job = self._providerJob( layer )
        if not job:
            return
        layer.setCustomProperty("SNAPLoader.isSnapJob","Y")
        return {'job': job }

    def _groupId( self, job ):
        legend = self._iface.legendInterface()
        for layer, props in self._snapLayers(job):
            groupids = [i 
                    for i,x in enumerate(legend.groupLayerRelationship()) 
                    if layer.id() in x[1]]
            if len(groupids) > 0 and legend.groupExists(groupids[0]): 
                return groupids[0]

        groupname = re.sub(".*[\\\/]","",job)
        return legend.addGroup(groupname)

    def _installLayer( self, layer, adjgroup=None ):
        if layer.featureCount() == 0:
            return groupid
        lprops = self._setSnapLayerProperties( layer )
        QgsProject.instance().addMapLayer(layer,adjgroup is None)
        if adjgroup:
            adjgroup.insertLayer(0,layer)

    def _layerUri( self, job, table ):
        uri = QgsDataSourceUri()
        uri.setDatabase(job+self._dbext)
        uri.setDataSource('',table, 'shape')
        return uri.uri()

    def _setLayerColor( self, layer, color ):
        symbol=layer.renderer().symbol().clone()
        symbol.setColor(color)
        layer.renderer().setSymbol(symbol)

    def CreateStationLayer( self, job, adjgroup=None ):
        uri = self._layerUri(job,'stations');
        layer = QgsVectorLayer(uri, 'Stations', 'spatialite')
        self._setLayerColor(layer,self._stnColor)
        self._installLayer( layer, adjgroup )
        return layer

    def CreateLineObsLayer( self, job, adjgroup=None ):
        uri = self._layerUri(job,'line_obs');
        layer = QgsVectorLayer(uri, 'Line observations', 'spatialite')
        self._setLayerColor(layer,self._obsColor)
        self._installLayer( layer, adjgroup )
        return layer

    def CreatePointObsLayer( self, job, adjgroup=None ):
        uri = self._layerUri(job,'point_obs');
        layer = QgsVectorLayer(uri, 'Point observations', 'spatialite')
        self._setLayerColor(layer,self._obsColor)
        self._installLayer( layer, adjgroup )
        return layer

    def CreateAdjustmentLayer( self, job, adjgroup=None ):
        if not haveVFR:
            print("Vector field layer manager not found")
            return adjgroup

        db = sqlite3.connect(job+self._dbext)
        count,maxadjh,maxadjv = db.cursor().execute("""
             select count(*),sum(adj_e*adj_e+adj_n*adj_n), sum(adj_h*adj_h)
             from stations
             where abs(adj_e) > 0 or abs(adj_n) > 0 or abs(adj_h) > 0
             """).fetchone()
        if count == 0:
            print("No vectors to plot")
            return
        maxvec = max(maxadjh,maxadjv)

        uri = self._layerUri(job,'stations')
        vfm=VectorFieldLayerManager(self._iface)
        scale_layer=None
        if maxadjv > 0.0:
            adj_layer = QgsVectorLayer(uri, 'Vertical adjustments', 'spatialite')
            scale_layer=adj_layer
            vfm.renderLayerAsVectorField(
                adj_layer,
                color=self._vadjColor,
                baseBorderColor="#000000",
                heightField='adj_h',
                heightErrorField='errhgt',
                scaleGroup='adjustment',
                ellipseScale=1.96
            )

            # r.setLegendText('')
            # r.setScaleBoxText('m vrt adj (95% conf)')

            # adj_layer.setRenderer(r)
            self._installLayer( adj_layer, adjgroup );
            #legend.refreshLayerSymbology(adj_layer)

        if maxadjh > 0.0:
            adj_layer = QgsVectorLayer(uri, 'Horizontal adjustments', 'spatialite')
            #if scale < 0:
            #    scale = self._calcAdjustmentLayerScale( adj_layer, maxvec, count )
            scale_layer=adj_layer

            vfm.renderLayerAsVectorField(
                adj_layer,
                color=self._hadjColor,
                baseBorderColor="#000000",
                dxField='adj_e',
                dyField='adj_n',
                emaxField='errell_max',
                eminField='errell_min',
                emaxAzimuthField='errell_bmax',
                # scale=scale,
                scaleGroup='adjustment',
                ellipseScale=2.45,
                # autoscale=True
            )

            # r.setLegendText('')
            # r.setScaleBoxText('m hor adj (95% conf)')

            self._installLayer( adj_layer, adjgroup );
            #legend.refreshLayerSymbology(adj_layer)

        if scale_layer:
            vfm.autoscaleVectorLayer(scale_layer)
        return scale_layer

    def RefreshSnapLayers(self, job):
        for layer, props in self._snapLayers(job):
            layer.triggerRepaint()

    def JobName( self, job ):
        job=re.sub(r'.*[\\\/]','',job)
        return job

    def LoadSnapFiles(self,job):
        # Convert the SNAP data to an sqlite database
        try:
            sqlitedb = self._loader.load(job)
            return True
        except:
            errmsg=str(sys.exc_info()[1])
            job=self.JobName(job)
            self._iface.messageBar().pushMessage(
                "SNAP error",
                "Error loading job " + job + ": " + errmsg,
                level=Qgis.Warning,
                duration=20)
            return False

    def RefreshSnapJob( self, job ):
        self.LoadSnapFiles( job )
        self.RefreshSnapLayers( job )

    def LoadSnapJob( self, job ):
        if not self.LoadSnapFiles(job):
            return
        initialLoad=len(QgsProject.instance().mapLayers()) == 0
        rootNode=QgsProject.instance().layerTreeRoot()
        jobname=self.JobName(job)
        adjgroup=rootNode.insertGroup(0, f"Adjustment {jobname}")
        linobslayer=self.CreateLineObsLayer(job,adjgroup)
        pntobslayer=self.CreatePointObsLayer(job,adjgroup)
        stnlayer=self.CreateStationLayer(job,adjgroup)
        # Need to set the map extent if loading to empty map 
        # else 
        if initialLoad:
            extent=stnlayer.extent()
            extent.scale(1.1)
            self._iface.mapCanvas().setExtent(extent)
        adjlayer=self.CreateAdjustmentLayer(job,adjgroup)

    def DatabaseIsCurrent( self, job ):
        return self._loader.jobDatabaseIsCurrent( job )

    def JobInfo( self, job ):
        meta = self._loader.jobMetadata( job )
        info = []
        for item in "TITLE RUNTIME NOBS NPRM NIMP NCON NDOF SSR SEU".split():
            if item not in meta:
                continue
            value = str(meta[item]['value'])
            comment = str(meta[item]['description'])
            if item in "NIMP NCON" and value == "0":
                continue
            info.append(comment + ": " + value)

        if 'CONVERGED' in meta and meta['CONVERGED'] != 'Y':
            info.append("\nNOTE: this adjustment did not converge")

        return "\n".join(info)

