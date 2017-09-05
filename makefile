
LinzSnap.zip: LinzSnap/SnapSqliteLoader.csys.db always_build
	rm LinzSnap.zip
	zip -r LinzSnap LinzSnap -x *.db -x *.pyc

always_build:

LinzSnap/SnapSqliteLoader.csys.db: LinzSnap/SnapSqliteLoader.csys.sql
	sqlite3 $@ < $<
