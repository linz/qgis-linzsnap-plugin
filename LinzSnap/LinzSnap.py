from __future__ import absolute_import
from builtins import str
from builtins import object

from qgis.PyQt.QtCore import QFileInfo, QSettings
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.core import QgsDataSourceURI, QgsMapLayerRegistry, QgsVectorLayer
from qgis.gui import QgsMessageBar

from random import randint
import sys
import os.path
import re
import math
from pyspatialite import dbapi2 as sqlite3

from .SnapSqliteLoader import SnapSqliteLoader;

try:
    from VectorFieldLayerManager import VectorFieldLayerManager
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
        filename, __, __ = QFileDialog.getOpenFileName(
            self._iface.mainWindow(),
            "SNAP command file", path, 
            "Command files (*.cmd *.snp *.snap);;All files (*.*)")
        if filename:
            s.setValue(setting,QFileInfo(filename).absolutePath())
            job = self._snapFileJob( filename )
        return job

    def _snapLayers( self, job=None ):
        for layer in self._iface.mapCanvas().layers():
            props = self._snapLayerProperties(layer)
            if props and (not job or props['job'] == job):
                yield layer, props

    def _providerJob( self, layer ):
        if layer.type() != layer.VectorLayer or layer.dataProvider().name() != "spatialite":
            return None
        uri = QgsDataSourceURI(layer.dataProvider().dataSourceUri())
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

    def _installLayer( self, layer, groupid=None ):
        if layer.featureCount() == 0:
            return groupid
        legend = self._iface.legendInterface()
        lprops = self._setSnapLayerProperties( layer )
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        if groupid is None:
            groupid = self._groupId( lprops['job'])
        legend.moveLayer(layer,groupid)
        return groupid

    def _layerUri( self, job, table ):
        uri = QgsDataSourceURI()
        uri.setDatabase(job+self._dbext)
        uri.setDataSource('',table, 'shape')
        return uri.uri()

    def CreateStationLayer( self, job, groupid=None ):
        uri = self._layerUri(job,'stations');
        layer = QgsVectorLayer(uri, 'Stations', 'spatialite')
        layer.rendererV2().symbol().setColor(self._stnColor);
        return self._installLayer( layer, groupid )

    def CreateLineObsLayer( self, job, groupid=None ):
        uri = self._layerUri(job,'line_obs');
        layer = QgsVectorLayer(uri, 'Line observations', 'spatialite')
        layer.rendererV2().symbol().setColor(self._obsColor);
        return self._installLayer( layer, groupid )

    def CreatePointObsLayer( self, job, groupid=None ):
        uri = self._layerUri(job,'point_obs');
        layer = QgsVectorLayer(uri, 'Point observations', 'spatialite')
        layer.rendererV2().symbol().setColor(self._obsColor);
        return self._installLayer( layer, groupid )

    def _calcAdjustmentLayerScale( self, layer, maxvec, count ):

        scale = 1.0
        arrlen = math.sqrt(maxvec/count)
        arrlen *= min(1+count/20,2) 

        maprenderer = self._iface.mapCanvas().mapRenderer()
        extent = maprenderer.layerExtentToOutputExtent(layer,layer.extent())

        mapsize = math.sqrt(abs(extent.width()*extent.height()))
        maplen = mapsize/math.sqrt(16.0+count)
        maplen = max(min(maplen,mapsize/10),mapsize/100)
        scale = maplen

        if arrlen > 0: scale /= arrlen
        return scale

    def CreateAdjustmentLayer( self, job, groupid=None ):
        if not haveVFR:
            return groupid

        db = sqlite3.connect(job+self._dbext)
        count,maxadjh,maxadjv = db.execute("""
             select count(*),sum(adj_e*adj_e+adj_n*adj_n), sum(adj_h*adj_h)
             from stations
             where abs(adj_e) > 0 or abs(adj_n) > 0 or abs(adj_h) > 0
             """).fetchone()
        if count == 0:
            return
        maxvec = max(maxadjh,maxadjv)

        uri = self._layerUri(job,'stations')
        scale = -1
        vfm=VectorFieldLayerManager(self._iface)
        legend = self._iface.legendInterface()
        if maxadjv > 0.0:
            adj_layer = QgsVectorLayer(uri, 'Vertical adjustments', 'spatialite')
            scale = self._calcAdjustmentLayerScale( adj_layer, maxvec, count )
            
            vfm.renderLayerAsVectorField(
                adj_layer,
                color=self._vadjColor,
                baseBorderColor="#000000",
                heightField='adj_h',
                heightErrorField='errhgt',
                scale=scale,
                scaleGroup='adjustment',
                ellipseScale=1.96
            )

            # r.setLegendText('')
            # r.setScaleBoxText('m vrt adj (95% conf)')

            # adj_layer.setRendererV2(r)
            groupid=self._installLayer( adj_layer, groupid );
            legend.refreshLayerSymbology(adj_layer)

        if maxadjh > 0.0:
            adj_layer = QgsVectorLayer(uri, 'Horizontal adjustments', 'spatialite')
            if scale < 0:
                scale = self._calcAdjustmentLayerScale( adj_layer, maxvec, count )

            vfm.renderLayerAsVectorField(
                adj_layer,
                color=self._hadjColor,
                baseBorderColor="#000000",
                dxField='adj_e',
                dyField='adh_n',
                emaxField='errell_max',
                eminField='errell_min',
                emaxAzimuthField='errell_bmax',
                scale=scale,
                scaleGroup='adjustment',
                ellipseScale=2.45
            )

            # r.setLegendText('')
            # r.setScaleBoxText('m hor adj (95% conf)')

            groupid=self._installLayer( adj_layer, groupid );
            legend.refreshLayerSymbology(adj_layer)

        return groupid

    def RefreshSnapLayers(self, job):
        refresh = False
        for layer, props in self._snapLayers(job):
            layer.setCacheImage(None)
            refresh = True
        if refresh:
            self._iface.mapCanvas().refresh()

    def LoadSnapFiles(self,job):
        # Convert the SNAP data to an sqlite database
        try:
            sqlitedb = self._loader.load(job)
            return True
        except:
            errmsg=str(sys.exc_info()[1])
            job=re.sub(r'.*[\\\/]','',job)
            self._iface.messageBar().pushMessage(
                "SNAP error",
                "Error loading job " + job + ": " + errmsg,
                level=QgsMessageBar.WARNING,
                duration=20)
            return False

    def RefreshSnapJob( self, job ):
        self.LoadSnapFiles( job )
        self.RefreshSnapLayers( job )

    def LoadSnapJob( self, job ):
        if not self.LoadSnapFiles(job):
            return
        groupid=None
        groupid=self.CreateLineObsLayer(job,groupid)
        groupid=self.CreatePointObsLayer(job,groupid)
        groupid=self.CreateStationLayer(job,groupid)
        groupid=self.CreateAdjustmentLayer(job,groupid)

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

