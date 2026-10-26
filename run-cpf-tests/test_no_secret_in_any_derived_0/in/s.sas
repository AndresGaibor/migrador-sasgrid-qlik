libname ora oracle user=scott password="Tiger123" path=PRODDB;
libname d2 db2 user=u pw=Sekret9 database=S;
%let dbpass = TopSecret77;
%let anio = 2025;
proc sql;
  connect to oracle (user=scott password='Tiger123' path=PRODDB);
quit;
data work.y; set ora.t; if pw = 5 then x = 1; run;
