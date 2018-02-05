#!/usr/bin/python
#from __future__ import unicode_literals

import re
import os
import os.path
import csv
import sys
import inspect
from pyspatialite import dbapi2 as sqlite3
from datetime import datetime

class SnapCsvFile:

    class cleanFile( object ):

        def __init__(self,filename):
            self._f=open(filename)

        def next(self):
            line=self._f.next()
            line=re.sub(r'[\x80-\xff]','.',line)
            return line

        def __iter__(self):
            return self

    def __init__(self,filename):
        self._filename = filename
        self._csv = csv.reader(self.cleanFile(filename))
        self._fields = self._csv.next()

    def reset(self):
        self._csv = csv.reader(open(self._filename))
        self._csv.next()

    def fields(self):
        return self._fields

    def __iter__(self):
        return self._csv


class SnapSqliteLoader:

    '''
    Class to import data from SNAP CSV files into an SQLite database, 
    with spatial objects in tables stations, point_obs, line_obs.
    Also creates a table 'metadata' with the metadata info.
    '''


    jobmetacache = dict()

    csvfiletypes = ('metadata','stn','obs')

    numfields="""
        adj_e
        adj_h
        adj_n
        corr12
        corr13
        corr23
        errell_bmax
        errell_max
        errell_min
        errhgt
        error
        error1
        error2
        error3
        fromhgt
        height
        latitude
        length
        longitude
        rescorr12
        rescorr13
        rescorr23
        reserror
        reserror1
        reserror2
        reserror3
        residual
        residual1
        residual2
        residual3
        stdres
        stdres1
        stdres2
        stdres3
        tohgt
        value
        value1
        value2
        value3
        """.split()

    intfields="""
        id
        obsset
        sourcelineno
        """.split()

    sqliteext = ".sqlite"

    def _files( self, job ):
        csvfiles = dict()
        for c in SnapSqliteLoader.csvfiletypes:
            f = job + "-" + c + ".csv"
            if not os.path.isfile(f):
                raise Exception("The " + c + " csv file is missing")
            csv = SnapCsvFile(f)
            if c in ('stations','obs'):
                if 'shape' not in csv.fields():
                    raise Exception("The " + c + " csv file doesn't contain shapes")
            csvfiles[c] = csv
        return csvfiles

    def _fieldType( self, field ):
        return ('real' if field in SnapSqliteLoader.numfields else
               'integer' if field in SnapSqliteLoader.intfields else
               'blob' if field == 'shape' else
               'string')

    def _buildSql( self, table, fields, type, srid=0 ):
        types = (self._fieldType(f) if type != 'metadata' 
                 else 'string'
                 for f in fields)

        create = ('create table ' + table + '('
            'uid INTEGER PRIMARY KEY, '
            + ', '.join(
            [f+" "+t for f,t in zip(fields,types)]) +
            ')')

        index='CREATE INDEX idx_{0}_{1} ON {0} ( {1} )'.format(table,fields[0])

        insert = ('insert into ' + table 
            + ' (' + ','.join(fields)+')'
            + ' values ('
            + ', '.join(
            '?' if f != 'shape' else
            'GeomFromText(?,'+str(srid)+')'
            for f in fields) + ')')

        return create, index, insert
    
    def _executeSql( self, db, sql, *values ):
        try:
            return db.execute( sql, values )
        except:
            message = "SQL exception: " + str(sys.exc_info()[1])
            message += "\n" + "SQL statement: " + sql
            if len(values) > 0: 
                message += "\n" + "SQL values: " + ', '.join(map(str,values))
            raise Exception(message)

    def _createMetadataTable( self, job, db, csv ):
        create, index, insert = self._buildSql('metadata',csv.fields(),'metadata')
        self._executeSql(db,create)
        self._executeSql(db,index)
        for row in csv:
            self._executeSql(db,insert,*row)
        self._setCsvMtime(job, db)

    def _setCsvMtime( self, job, db ):
        mtime = self._snapCsvMtime( job )
        self._executeSql(db,"delete from metadata where code='CSVMTIME'")
        self._executeSql(db,"insert into metadata (code,value,comment) values ('CSVMTIME',?,'SNAP metadata csv modification time')",
                         mtime)
    
    def _createStationTable( self, db, csv, srid ):
        create, index, insert = self._buildSql('stations',csv.fields(),'stn',srid)
        self._executeSql(db,create)
        self._executeSql(db,index)
        for row in csv:
            self._executeSql(db,insert,*row)
    
    def _createObsTables( self, db, csv, srid ):
        fields = csv.fields()[:]
        fields.insert(0,'_csvid')
        shapeid = fields.index('shape')

        create, index, insert = self._buildSql('line_obs',fields,'obs',srid)
        self._executeSql(db,create)
        self._executeSql(db,index)
        csv.reset()
        csvid = 0
        for row in csv:
            csvid += 1
            row.insert(0,csvid)
            if 'LINE' in row[shapeid].upper(): self._executeSql(db,insert,*row)

        create, index, insert = self._buildSql('point_obs',fields,'obs',srid)
        self._executeSql(db,create)
        self._executeSql(db,index)
        csv.reset()
        csvid = 0
        for row in csv:
            csvid += 1
            row.insert(0,str(csvid))
            if 'POINT' in row[shapeid].upper(): self._executeSql(db,insert,*row)

    # Test existing sqlite metadata against new data.  Return True if
    # if already loaded, False if not, raise exception if incompatible

    def _compareMetadata( self, db, filename):
        rows = self._executeSql( db, """
                    SELECT 
                       m1.code
                    FROM
                       metadata m1,
                       old.metadata m2
                    WHERE
                       m1.code = m2.code AND
                       m1.value = m2.value
                    """)
        same = []
        for r in rows: 
            same.append(r[0])

        result = False
        if "CRDSYS" not in same:
            raise Exception("Cannot reload SNAP job as the coordinate system is incompatible.\n" 
                            + "Delete the existing file "+filename+" first")
        if "VECFORMAT" not in same:
            raise Exception("Cannot reload SNAP job as the CSV vector format is incompatible.\n" 
                            + "Delete the existing file "+filename+" first")

        if "RUNTIME" in same:
            result = True

        return result

    def _saveDbMeta( self, job, db ):
        rows = self._executeSql( db, "SELECT code, value, comment from metadata")
        meta = dict()
        for code,value,description in rows: 
            meta[code] = { 'value':str(value), 'description':str(description) }

        SnapSqliteLoader.jobmetacache[job] = meta
        return meta

    def _snapCsvMtime( self, job ):
        file = job+'-metadata.csv'
        if not os.path.exists(file):
            return None
        mtime = os.path.getmtime(file)
        return datetime.fromtimestamp(mtime).isoformat().split('.')[0]

    def jobMetadata( self, job ):
        cache = SnapSqliteLoader.jobmetacache
        if job in cache: return cache[job]
        try:
            db = sqlite3.connect(job+SnapSqliteLoader.sqliteext)
            return self._saveDbMeta( job, db )
        except:
            return None

    def jobDatabaseIsCurrent( self, job ):
        meta = self.jobMetadata(job)
        if not meta: return False
        mtime = self._snapCsvMtime(job)
        if not mtime: return True
        if 'CSVMTIME' not in meta: return False
        return meta['CSVMTIME']['value'] == mtime

    def load( self, job ):
        try:
            csvfiles = self._files(job)
        except Exception:
            raise Exception(str(sys.exc_info()[1])+
                "\nThe SNAP command file must include \"output_csv all wkt_shape no_tab_delimited\"")

        sqlitefile = job+SnapSqliteLoader.sqliteext
        sqlitenew = sqlitefile
        if os.path.exists(sqlitefile):
            if self.jobDatabaseIsCurrent(job):
                return sqlitefile
            for i in range(100):
                sqlitenew = sqlitefile+'.'+str(i)+'.tmp'
                if not os.path.exists(sqlitenew): break

        if os.path.exists(sqlitenew):
            os.remove(sqlitefile)
            sqlitenew = sqlitefile

        if os.path.exists(sqlitenew):
            raise Exception("Cannot replace existing db " + sqlitefile)

        if job in SnapSqliteLoader.jobmetacache:
            del SnapSqliteLoader.jobmetacache[job]

        db = sqlite3.connect(sqlitenew)
        ok = False
        replacing = sqlitenew != sqlitefile
        try:
            db.isolation_level = "EXCLUSIVE"
            # Want to make this as fast as possible
            self._executeSql(db,'pragma journal_mode=OFF')
            self._executeSql(db,'pragma synchronous=OFF')
    
    
            self._createMetadataTable( job, db, csvfiles['metadata'] )
    
            if replacing:
                self._executeSql(db,"attach '" + sqlitefile + "' as old")
                if self._compareMetadata(db,sqlitefile):
                    db.close()
                    db = sqlite3.connect(sqlitefile)
                    self._setCsvMtime( job, db )
                    db.commit()
                    return sqlitefile
    
            # Find and attach the coordsys ref database
            csysdb = os.path.realpath(inspect.getmodule(self).__file__);
            print "module",inspect.getmodule(self).__file__;
            csysdb = re.sub(r'.[^\.]*$','.csys.db',csysdb)
            if not os.path.isfile(csysdb):
                raise Exception("Coordsys reference db "+csysdb+" doesn't exist")
            # srid = self._executeSQL
            self._executeSql(db,"attach database ? as csys",csysdb)
            row = self._executeSql(db,"""
                select s.srid 
                from csys.crs_epsg_srid_mapping c,
                     csys.spatial_ref_sys s,
                     metadata m
                where m.code = 'CRDSYS'
                and c.code=m.value
                and s.auth_name='epsg'
                and s.auth_srid=c.srid
                """).fetchone()
            if not row:
                row = self._executeSql(db,"select value from metadata where code='CRDSYS'").fetchone()
                csyscode = "undefined"
                if row:
                    csyscode = row[0]
                raise Exception("SNAP coordinate system %s not supported"%(csyscode,))
            srid=row[0]
            

            self._createStationTable( db, csvfiles['stn'], srid )
            self._createObsTables( db, csvfiles['obs'], srid )

            if replacing:
                self._executeSql(db,'delete from old.metadata')
                self._executeSql(db,'delete from old.stations')
                self._executeSql(db,'delete from old.line_obs')
                self._executeSql(db,'delete from old.point_obs')
                self._executeSql(db,'insert into old.metadata select * from metadata')
                self._executeSql(db,'insert into old.stations select * from stations')
                self._executeSql(db,'insert into old.line_obs select * from line_obs')
                self._executeSql(db,'insert into old.point_obs select * from point_obs')
            else:
                # Set up the spatial metadata
                self._executeSql(db,'select InitSpatialMetadata()')
                self._executeSql(db,"delete from spatial_ref_sys")
                self._executeSql(db,"""
                    insert into spatial_ref_sys (srid, auth_name, auth_srid, ref_sys_name, proj4text ) 
                    select distinct srid, auth_name, auth_srid, ref_sys_name, proj4text
                    from csys.spatial_ref_sys where srid=?""",srid)
                self._executeSql(db,"select RecoverGeometryColumn('stations','shape',?,'POINT',2)",srid)
                self._executeSql(db,"select RecoverGeometryColumn('point_obs','shape',?,'POINT',2)",srid)
                self._executeSql(db,"select RecoverGeometryColumn('line_obs','shape',?,'LINESTRING',2)",srid)
    
    
            db.commit()
            if replacing:
                db.close()
                db = sqlite3.connect(sqlitefile)

            self._executeSql(db,'vacuum')
            self._executeSql(db,'analyze')
            db.commit()
            ok = True
        finally:
            db.close()
            if not ok or replacing:
                os.remove(sqlitenew)
            if not ok: sqlitefile = ''

        return sqlitefile

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Syntax: snap2sqlite  snap_command_file_name (no extension)\n")
    try:
        loader = SnapSqliteLoader()
        sqlitefile = loader.load( sys.argv[1] )
        print "Data loaded successfully into ",sqlitefile
    except Exception:
        print str(sys.exc_info()[1]),"\n"
