PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE spatial_ref_sys (
srid INTEGER NOT NULL PRIMARY KEY,
auth_name VARCHAR(256) NOT NULL,
auth_srid INTEGER NOT NULL,
ref_sys_name VARCHAR(256),
proj4text VARCHAR(2048) NOT NULL);
INSERT INTO "spatial_ref_sys" VALUES(2105,'epsg',2105,'NZGD2000 / Mount Eden 2000','+proj=tmerc +lat_0=-36.87972222222222 +lon_0=174.7641666666667 +k=0.9999 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2106,'epsg',2106,'NZGD2000 / Bay of Plenty 2000','+proj=tmerc +lat_0=-37.76111111111111 +lon_0=176.4661111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2107,'epsg',2107,'NZGD2000 / Poverty Bay 2000','+proj=tmerc +lat_0=-38.62444444444444 +lon_0=177.8855555555556 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2108,'epsg',2108,'NZGD2000 / Hawkes Bay 2000','+proj=tmerc +lat_0=-39.65083333333333 +lon_0=176.6736111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2109,'epsg',2109,'NZGD2000 / Taranaki 2000','+proj=tmerc +lat_0=-39.13555555555556 +lon_0=174.2277777777778 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2110,'epsg',2110,'NZGD2000 / Tuhirangi 2000','+proj=tmerc +lat_0=-39.51222222222222 +lon_0=175.64 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2111,'epsg',2111,'NZGD2000 / Wanganui 2000','+proj=tmerc +lat_0=-40.24194444444444 +lon_0=175.4880555555555 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2112,'epsg',2112,'NZGD2000 / Wairarapa 2000','+proj=tmerc +lat_0=-40.92527777777777 +lon_0=175.6472222222222 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2113,'epsg',2113,'NZGD2000 / Wellington 2000','+proj=tmerc +lat_0=-41.3011111111111 +lon_0=174.7763888888889 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2114,'epsg',2114,'NZGD2000 / Collingwood 2000','+proj=tmerc +lat_0=-40.71472222222223 +lon_0=172.6719444444444 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2115,'epsg',2115,'NZGD2000 / Nelson 2000','+proj=tmerc +lat_0=-41.27444444444444 +lon_0=173.2991666666667 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2116,'epsg',2116,'NZGD2000 / Karamea 2000','+proj=tmerc +lat_0=-41.28972222222222 +lon_0=172.1088888888889 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2117,'epsg',2117,'NZGD2000 / Buller 2000','+proj=tmerc +lat_0=-41.81055555555555 +lon_0=171.5811111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2118,'epsg',2118,'NZGD2000 / Grey 2000','+proj=tmerc +lat_0=-42.33361111111111 +lon_0=171.5497222222222 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2119,'epsg',2119,'NZGD2000 / Amuri 2000','+proj=tmerc +lat_0=-42.68888888888888 +lon_0=173.01 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2120,'epsg',2120,'NZGD2000 / Marlborough 2000','+proj=tmerc +lat_0=-41.54444444444444 +lon_0=173.8019444444444 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2121,'epsg',2121,'NZGD2000 / Hokitika 2000','+proj=tmerc +lat_0=-42.88611111111111 +lon_0=170.9797222222222 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2122,'epsg',2122,'NZGD2000 / Okarito 2000','+proj=tmerc +lat_0=-43.11 +lon_0=170.2608333333333 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2123,'epsg',2123,'NZGD2000 / Jacksons Bay 2000','+proj=tmerc +lat_0=-43.97777777777778 +lon_0=168.6061111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2124,'epsg',2124,'NZGD2000 / Mount Pleasant 2000','+proj=tmerc +lat_0=-43.59055555555556 +lon_0=172.7269444444445 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2125,'epsg',2125,'NZGD2000 / Gawler 2000','+proj=tmerc +lat_0=-43.74861111111111 +lon_0=171.3605555555555 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2126,'epsg',2126,'NZGD2000 / Timaru 2000','+proj=tmerc +lat_0=-44.40194444444445 +lon_0=171.0572222222222 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2127,'epsg',2127,'NZGD2000 / Lindis Peak 2000','+proj=tmerc +lat_0=-44.735 +lon_0=169.4675 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2128,'epsg',2128,'NZGD2000 / Mount Nicholas 2000','+proj=tmerc +lat_0=-45.13277777777778 +lon_0=168.3986111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2129,'epsg',2129,'NZGD2000 / Mount York 2000','+proj=tmerc +lat_0=-45.56361111111111 +lon_0=167.7386111111111 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2130,'epsg',2130,'NZGD2000 / Observation Point 2000','+proj=tmerc +lat_0=-45.81611111111111 +lon_0=170.6283333333333 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2131,'epsg',2131,'NZGD2000 / North Taieri 2000','+proj=tmerc +lat_0=-45.86138888888889 +lon_0=170.2825 +k=0.99996 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2132,'epsg',2132,'NZGD2000 / Bluff 2000','+proj=tmerc +lat_0=-46.6 +lon_0=168.3427777777778 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(2193,'epsg',2193,'NZGD2000 / New Zealand Transverse Mercator 2000','+proj=tmerc +lat_0=0 +lon_0=173 +k=0.9996 +x_0=1600000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3764,'epsg',3764,'NZGD2000 / Chatham Island Circuit 2000','+proj=tmerc +lat_0=-44 +lon_0=-176.5 +k=1 +x_0=400000 +y_0=800000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3788,'epsg',3788,'NZGD2000 / Auckland Islands TM 2000','+proj=tmerc +lat_0=0 +lon_0=166 +k=1 +x_0=3500000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3789,'epsg',3789,'NZGD2000 / Campbell Island TM 2000','+proj=tmerc +lat_0=0 +lon_0=169 +k=1 +x_0=3500000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3790,'epsg',3790,'NZGD2000 / Antipodes Islands TM 2000','+proj=tmerc +lat_0=0 +lon_0=179 +k=1 +x_0=3500000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3791,'epsg',3791,'NZGD2000 / Raoul Island TM 2000','+proj=tmerc +lat_0=0 +lon_0=-178 +k=1 +x_0=3500000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3793,'epsg',3793,'NZGD2000 / Chatham Islands TM 2000','+proj=tmerc +lat_0=0 +lon_0=-176.5 +k=1 +x_0=3500000 +y_0=10000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(3852,'epsg',3852,'RSRGD2000 / DGLC2000','+proj=lcc +lat_1=-76.66666666666667 +lat_2=-79.33333333333333 +lat_0=-90 +lon_0=157 +x_0=500000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4167,'epsg',4167,'NZGD2000','+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4272,'epsg',4272,'NZGD49','+proj=longlat +ellps=intl +datum=nzgd49 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4322,'epsg',4322,'WGS 72','+proj=longlat +ellps=WGS72 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4326,'epsg',4326,'WGS 84','+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4673,'epsg',4673,'Chatham Islands 1979','+proj=longlat +ellps=intl +towgs84=174.05,-25.49,112.57,-0,-0,0.554,0.2263 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4715,'epsg',4715,'Camp Area Astro','+proj=longlat +ellps=intl +towgs84=-104,-129,239,0,0,0,0 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(4764,'epsg',4764,'RSRGD2000','+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27200,'epsg',27200,'NZGD49 / New Zealand Map Grid','+proj=nzmg +lat_0=-41 +lon_0=173 +x_0=2510000 +y_0=6023150 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27205,'epsg',27205,'NZGD49 / Mount Eden Circuit','+proj=tmerc +lat_0=-36.87986527777778 +lon_0=174.7643393611111 +k=0.9999 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27206,'epsg',27206,'NZGD49 / Bay of Plenty Circuit','+proj=tmerc +lat_0=-37.76124980555556 +lon_0=176.46619725 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27207,'epsg',27207,'NZGD49 / Poverty Bay Circuit','+proj=tmerc +lat_0=-38.62470277777778 +lon_0=177.8856362777778 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27208,'epsg',27208,'NZGD49 / Hawkes Bay Circuit','+proj=tmerc +lat_0=-39.65092930555556 +lon_0=176.6736805277778 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27209,'epsg',27209,'NZGD49 / Taranaki Circuit','+proj=tmerc +lat_0=-39.13575830555556 +lon_0=174.22801175 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27210,'epsg',27210,'NZGD49 / Tuhirangi Circuit','+proj=tmerc +lat_0=-39.51247038888889 +lon_0=175.6400368055556 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27211,'epsg',27211,'NZGD49 / Wanganui Circuit','+proj=tmerc +lat_0=-40.24194713888889 +lon_0=175.4880996111111 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27212,'epsg',27212,'NZGD49 / Wairarapa Circuit','+proj=tmerc +lat_0=-40.92553263888889 +lon_0=175.6473496666667 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27213,'epsg',27213,'NZGD49 / Wellington Circuit','+proj=tmerc +lat_0=-41.30131963888888 +lon_0=174.7766231111111 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27214,'epsg',27214,'NZGD49 / Collingwood Circuit','+proj=tmerc +lat_0=-40.71475905555556 +lon_0=172.6720465 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27215,'epsg',27215,'NZGD49 / Nelson Circuit','+proj=tmerc +lat_0=-41.27454472222222 +lon_0=173.2993168055555 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27216,'epsg',27216,'NZGD49 / Karamea Circuit','+proj=tmerc +lat_0=-41.28991152777778 +lon_0=172.1090281944444 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27217,'epsg',27217,'NZGD49 / Buller Circuit','+proj=tmerc +lat_0=-41.81080286111111 +lon_0=171.5812600555556 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27218,'epsg',27218,'NZGD49 / Grey Circuit','+proj=tmerc +lat_0=-42.33369427777778 +lon_0=171.5497713055556 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27219,'epsg',27219,'NZGD49 / Amuri Circuit','+proj=tmerc +lat_0=-42.68911658333333 +lon_0=173.0101333888889 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27220,'epsg',27220,'NZGD49 / Marlborough Circuit','+proj=tmerc +lat_0=-41.54448666666666 +lon_0=173.8020741111111 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27221,'epsg',27221,'NZGD49 / Hokitika Circuit','+proj=tmerc +lat_0=-42.88632236111111 +lon_0=170.9799935 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27222,'epsg',27222,'NZGD49 / Okarito Circuit','+proj=tmerc +lat_0=-43.11012813888889 +lon_0=170.2609258333333 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27223,'epsg',27223,'NZGD49 / Jacksons Bay Circuit','+proj=tmerc +lat_0=-43.97780288888889 +lon_0=168.606267 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27224,'epsg',27224,'NZGD49 / Mount Pleasant Circuit','+proj=tmerc +lat_0=-43.59063758333333 +lon_0=172.7271935833333 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27225,'epsg',27225,'NZGD49 / Gawler Circuit','+proj=tmerc +lat_0=-43.74871155555556 +lon_0=171.3607484722222 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27226,'epsg',27226,'NZGD49 / Timaru Circuit','+proj=tmerc +lat_0=-44.40222036111111 +lon_0=171.0572508333333 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27227,'epsg',27227,'NZGD49 / Lindis Peak Circuit','+proj=tmerc +lat_0=-44.73526797222222 +lon_0=169.4677550833333 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27228,'epsg',27228,'NZGD49 / Mount Nicholas Circuit','+proj=tmerc +lat_0=-45.13290258333333 +lon_0=168.3986411944444 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27229,'epsg',27229,'NZGD49 / Mount York Circuit','+proj=tmerc +lat_0=-45.56372616666666 +lon_0=167.7388617777778 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27230,'epsg',27230,'NZGD49 / Observation Point Circuit','+proj=tmerc +lat_0=-45.81619661111111 +lon_0=170.6285951666667 +k=1 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27231,'epsg',27231,'NZGD49 / North Taieri Circuit','+proj=tmerc +lat_0=-45.86151336111111 +lon_0=170.2825891111111 +k=0.99996 +x_0=300000 +y_0=700000 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27232,'epsg',27232,'NZGD49 / Bluff Circuit','+proj=tmerc +lat_0=-46.60000961111111 +lon_0=168.342872 +k=1 +x_0=300002.66 +y_0=699999.58 +ellps=intl +datum=nzgd49 +units=m +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27291,'epsg',27291,'NZGD49 / North Island Grid','+proj=tmerc +lat_0=-39 +lon_0=175.5 +k=1 +x_0=274319.5243848086 +y_0=365759.3658464114 +ellps=intl +datum=nzgd49 +to_meter=0.9143984146160287 +no_defs ');
INSERT INTO "spatial_ref_sys" VALUES(27292,'epsg',27292,'NZGD49 / South Island Grid','+proj=tmerc +lat_0=-44 +lon_0=171.5 +k=1 +x_0=457199.2073080143 +y_0=457199.2073080143 +ellps=intl +datum=nzgd49 +to_meter=0.9143984146160287 +no_defs ');
CREATE TABLE geometry_columns (
f_table_name VARCHAR(256) NOT NULL,
f_geometry_column VARCHAR(256) NOT NULL,
type VARCHAR(30) NOT NULL,
coord_dimension INTEGER NOT NULL,
srid INTEGER,
spatial_index_enabled INTEGER NOT NULL);
CREATE TABLE crs_epsg_srid_mapping (
    cos_id integer NOT NULL primary key,
    srid integer NOT NULL,
    code varchar(20) NOT NULL
);
INSERT INTO "crs_epsg_srid_mapping" VALUES(1,27219,'AMURTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(2,2119,'AMURTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(4,27206,'PLENTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(5,2106,'PLENTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(7,27232,'BLUFTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(8,2132,'BLUFTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(10,27217,'BULLTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(11,2117,'BULLTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(15,3764,'CHATTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(17,27214,'COLLTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(18,2114,'COLLTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20,27225,'GAWLTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(21,2125,'GAWLTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(23,27218,'GREYTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(24,2118,'GREYTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(27,27208,'HAWKTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(28,2108,'HAWKTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(29,27221,'HOKITM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(30,2121,'HOKITM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(32,27223,'JACKTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(33,2123,'JACKTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(35,27216,'KARATM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(36,2116,'KARATM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(38,27227,'LINDTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(39,2127,'LINDTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(41,27220,'MARLTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(42,2120,'MARLTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(44,27205,'EDENTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(45,2105,'EDENTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(47,27224,'PLEATM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(48,2124,'PLEATM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(50,27229,'YORKTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(51,2129,'YORKTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(53,27228,'NICHTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(54,2128,'NICHTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(56,27215,'NELSTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(57,2115,'NELSTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(59,27200,'NZMG');
INSERT INTO "crs_epsg_srid_mapping" VALUES(60,27291,'NNAT');
INSERT INTO "crs_epsg_srid_mapping" VALUES(61,27231,'TAIETM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(62,2131,'TAIETM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(64,27230,'OBSETM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(65,2130,'OBSETM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(67,27222,'OKARTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(68,2122,'OKARTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(86,2107,'POVETM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(87,27207,'POVETM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(89,27292,'SNAT');
INSERT INTO "crs_epsg_srid_mapping" VALUES(90,27209,'TARATM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(91,2109,'TARATM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(93,27226,'TIMATM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(94,2126,'TIMATM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(96,27210,'TUHITM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(97,2110,'TUHITM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(99,27212,'WAIRTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(100,2112,'WAIRTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(102,27211,'WANGTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(103,2111,'WANGTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(105,27213,'WELLTM1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(106,2113,'WELLTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(108,4272,'NZGD1949');
INSERT INTO "crs_epsg_srid_mapping" VALUES(109,4167,'NZGD2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(139,4673,'CHAT1979');
INSERT INTO "crs_epsg_srid_mapping" VALUES(141,4715,'CAMPAREA');
INSERT INTO "crs_epsg_srid_mapping" VALUES(142,4764,'RSRGD2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(144,4322,'WGS72');
INSERT INTO "crs_epsg_srid_mapping" VALUES(145,4326,'WGS84');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20298,2193,'NZTM');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20301,3793,'CITM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20302,3788,'AKTM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20303,3789,'CATM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20304,3790,'AITM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20305,3791,'RITM2000');
INSERT INTO "crs_epsg_srid_mapping" VALUES(20307,3852,'DGLC2000');
ANALYZE sqlite_master;
INSERT INTO "sqlite_stat1" VALUES('crs_epsg_srid_mapping',NULL,'74');
INSERT INTO "sqlite_stat1" VALUES('spatial_ref_sys',NULL,'74');
CREATE UNIQUE INDEX idx_geocols ON geometry_columns
(f_table_name, f_geometry_column);
CREATE TRIGGER fkd_refsys_geocols BEFORE DELETE ON spatial_ref_sys
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'delete on table ''spatial_ref_sys'' violates constraint: ''geometry_columns.srid''')
WHERE (SELECT srid FROM geometry_columns WHERE srid = OLD.srid) IS NOT NULL;
END;
CREATE TRIGGER fki_geocols_refsys BEFORE INSERT ON geometry_columns
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'insert on table ''geometry_columns'' violates constraint: ''spatial_ref_sys.srid''')
WHERE  NEW."srid" IS NOT NULL
AND (SELECT srid FROM spatial_ref_sys WHERE srid = NEW.srid) IS NULL;
END;
CREATE TRIGGER fku_geocols_refsys BEFORE UPDATE ON geometry_columns
FOR EACH ROW BEGIN
SELECT RAISE(ROLLBACK, 'update on table ''geometry_columns'' violates constraint: ''spatial_ref_sys.srid''')
WHERE  NEW.srid IS NOT NULL
AND (SELECT srid FROM spatial_ref_sys WHERE srid = NEW.srid) IS NULL;
END;
CREATE VIEW geom_cols_ref_sys AS
SELECT  f_table_name, f_geometry_column, type,
coord_dimension, spatial_ref_sys.srid AS srid,
auth_name, auth_srid, ref_sys_name, proj4text
FROM geometry_columns, spatial_ref_sys
WHERE geometry_columns.srid = spatial_ref_sys.srid;
COMMIT;
