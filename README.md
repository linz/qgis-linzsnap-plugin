LinzSnap QGIS plugin
====================

Plugin for use with the Land Information New Zealand SNAP network adjustment program.

http://www.linz.govt.nz/data/geodetic-services/download-geodetic-software/snap-concord-downloads

This programs loads the output of survey network adjustments. The command file must include the 
lines 

```
  output_csv all wkt_shape no_tab_delimited
```

The plugin reads the output CSV files and uses them to populate and SQLite (+ spatialite)
database.  It then displays layers from the database to show nodes (stations), observations,
coordinate adjustments, and error ellipses.

The makefile is used to rebuild the LinzSnap.zip file, which can be uploaded to a QGIS plugin 
repository for installation into QGIS.

