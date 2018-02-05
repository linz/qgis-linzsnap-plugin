from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os.path

from . import Resources

helpText = """
Load a SNAP adjustment into QGIS.  The SNAP command file must include
a command

output_csv all wkt_shape no_tab_delimited
"""

class Plugin:

    Name = "LinzSnap"
    LongName="SNAP data loader plugin"
    Version="1.0"
    QgisMinimumVersion="2.0"
    Author="ccrook@linz.govt.nz <Chris Crook>"
    #PluginUrl="http://pygqgis.org/repo/contributed"
    Description="Tools for use with LINZ SNAP data"

    def __init__( self, iface ):
        self._iface = iface
        self._jobs = []
        self._watchers = []

    def initGui(self):
        from .LinzSnap import LinzSnap

        self._loader = LinzSnap(self._iface)

        toolbar = self._iface.addToolBar('SNAP tools')
        self._toolbar = toolbar

        self._loadaction = QAction(QIcon(":/plugins/LinzSnap/LinzSnap.png"), 
            "Load SNAP output csv files", self._iface.mainWindow())
        self._loadaction.setWhatsThis("Loads a SNAP output CSV files")
        self._loadaction.triggered.connect( self.loadSnapJob )

        self._refreshaction = QAction(QIcon(":/plugins/LinzSnap/LinzSnapRefresh.png"), 
            "Update SNAP job", self._iface.mainWindow())
        self._refreshaction.setWhatsThis("Refreshes data after a SNAP job has been rerun")
        self._refreshaction.setEnabled(False)
        self._refreshaction.triggered.connect(self.refreshCurrentLayer)

        self._infoaction = QAction(QIcon(":/plugins/LinzSnap/LinzSnapInfo.png"), 
            "SNAP job info", self._iface.mainWindow())
        self._infoaction.setWhatsThis("Display info about the SNAP job")
        self._infoaction.setEnabled(False)
        self._infoaction.triggered.connect(self.showJobInfo)

        self._iface.currentLayerChanged[QgsMapLayer].connect(self.activeLayerChanged)

        QApplication.instance().focusChanged[QWidget, QWidget].connect(self.focusChanged)

        toolbar.addAction(self._loadaction)
        toolbar.addAction(self._infoaction)
        toolbar.addAction(self._refreshaction)
        self._iface.addPluginToMenu("&SNAP tools", self._loadaction)
        self._iface.addPluginToMenu("&SNAP tools", self._infoaction)
        self._iface.addPluginToMenu("&SNAP tools", self._refreshaction)


    def unload(self):      
        self._iface.currentLayerChanged[QgsMapLayer].disconnect(self.activeLayerChanged)
        QApplication.instance().focusChanged[QWidget, QWidget].disconnect(self.focusChanged)
        self._iface.removePluginMenu("&SNAP tools",self._loadaction)
        self._iface.removePluginMenu("&SNAP tools",self._infoaction)
        self._iface.removePluginMenu("&SNAP tools",self._refreshaction)
        # self._iface.removeToolBar(self._toolbar) pass 

    def activeLayerChanged( self, layer ):
        self.enableActions()

    def addJob(self,job):
        if job in self._jobs:
            return
        self._jobs.append(job)
        file = job+"-metadata.csv"
        # Tried adding a QFileSystemWatcher on metadata file to enable 
        # buttons, but currently this doesn't recognise modification time
        # changed, only create/delete, on windows....
        # Using focusChanged instead

    def focusChanged( self, old, new ):
        # If focus is coming back to QGis from another application, then
        # check currency of SNAP files.
        if not old:
            self.enableActions()

    def enableActions(self):
        layer = self._iface.mapCanvas().currentLayer()
        issnap = False
        iscurrent = False
        job = self._loader.LayerSnapJob(layer) if layer else None
        if job:
            self.addJob(job)
            issnap = True
            iscurrent = self._loader.DatabaseIsCurrent(job)

        self._infoaction.setEnabled(issnap)
        self._refreshaction.setEnabled(issnap and not iscurrent)

    def loadSnapJob(self):
        job = self._loader.GetSnapJob()
        if job:
            self._loader.LoadSnapJob(job)

    def refreshCurrentLayer(self):
        layer = self._iface.mapCanvas().currentLayer()
        job = self._loader.LayerSnapJob(layer)
        if job:
            self._loader.RefreshSnapJob(job)
        self.enableActions()

    def showJobInfo(self):
        layer = self._iface.mapCanvas().currentLayer()
        job = self._loader.LayerSnapJob(layer)
        if not job:
            return
        info = self._loader.JobInfo(job)
        buttons = QMessageBox.Ok
        iscurrent = self._loader.DatabaseIsCurrent(job)
        if not iscurrent:
            info += ("\n\nThere is a more recent adjustment of this job\n" +
                    "Do you want to load it?")
            buttons |= QMessageBox.Cancel
        result = QMessageBox.information(self._iface.mainWindow(),
                    "Job information",
                    info,buttons,QMessageBox.Ok)
        if result == QMessageBox.Ok and not iscurrent:
            self.refreshCurrentLayer()

