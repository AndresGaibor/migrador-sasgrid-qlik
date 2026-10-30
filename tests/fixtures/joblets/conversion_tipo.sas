/* Recorte de Cod2: conversión de tipo repetida (data temporal / data original / proc delete). */
data work.temporal;
format NRO_CTA 30.;
set WORK.DBIFTCD;
NRO_CTA=input(left(VAR7), 30.);
run;

data WORK.DBIFTCD;
set work.temporal;
run;

proc delete data=work.temporal;
run;

data work.temporal;
format LLAVE_NOMBRE 30.;
set WORK.DBIFTCD;
LLAVE_NOMBRE=input(left(VAR8), 30.);
run;

data WORK.DBIFTCD;
set work.temporal;
run;

proc delete data=work.temporal;
run;

data work.temporal;
format TIPO_DOC 8.;
set WORK.DBIFTCD;
TIPO_DOC=input(left(VAR9), 8.);
run;

data WORK.DBIFTCD;
set work.temporal;
run;

proc delete data=work.temporal;
run;

data work.temporal;
format NRO_DOC 30.;
set WORK.DBIFTCD;
NRO_DOC=input(left(VAR10), 30.);
run;

data WORK.DBIFTCD;
set work.temporal;
run;

proc delete data=work.temporal;
run;

data work.temporal;
format GMF 3.;
set WORK.DBIFTCD;
GMF=input(left(VAR11), 3.);
run;

data WORK.DBIFTCD;
set work.temporal;
run;

proc delete data=work.temporal;
run;

