/* Fixture recortado de Cod1: dos cargas a Impala idénticas salvo la tabla origen. */
%let _timer_start = %sysfunc(datetime());

/* Etiqueta: Programa */
libname GCIDLL01 "/data/GRID/GCIA_DLLO_SERVICIOS_DE_INFORMACION";

data WORK.cars_poc;
set sashelp.cars;
run;

/* Etiqueta: ACURA */
PROC SQL;
CREATE TABLE WORK.ACURA AS
SELECT CARS_POC.Make, CARS_POC.Model, CARS_POC.MSRP
FROM WORK.CARS_POC CARS_POC
WHERE ( CARS_POC.Make = 'Acura' );
QUIT;

/* Etiqueta: BMW */
PROC SQL;
CREATE TABLE WORK.BMW AS
SELECT CARS_POC.Make, CARS_POC.Model, CARS_POC.MSRP
FROM WORK.CARS_POC CARS_POC
WHERE ( CARS_POC.Make = 'BMW' );
QUIT;

%let libdes=PROCESO;
%let libtmp=proceso;
%let wsplit=3500000;
%let wprefix=grdtare_%substr(&pidexecution, 1, 5)_&sysuserid.;
%let wpgmbl=bulkload_generic.sh;
%let wf_errslz=/data/Programas_SAS/source/grid_errors_write_lz.txt;
%let wt_errslz=param_err_lz;

/* Etiqueta: Carga ACURA */
%macro mainProgram;
options nosymbolgen nomlogic nomprint nosource nosource2 nonotes;
%showMessage(msg=Inicio del programa principal de escritura);

%if %sysfunc(fileexist("&wf_errslz.")) %then
%do;
proc import datafile="&wf_errslz." out=&wt_errslz. dbms=DLM replace;
delimiter=',';
getnames=no;
run;
%end;

filename ex_pcs pipe "ps -eo pid,euser,cmd | tr -s ' ' | grep -i &wpgmbl.";

%capturaCampos;
%split3(tabla_origen=WORK.ACURA, registros_por_chunk=&wsplit, prefix=&wprefix);
%create_commands;
%deleteTableLZ(&libdes., ACURA);
x "&wpgmbl.";
%waitForBulkLoads;
%checkForErrors(&pidexecution.);
%delProcessTables;
%comparaRegistros;
%tiempos(&hi);
%mend mainProgram;

%mainProgram;

/* Etiqueta: Carga BMW */
%macro mainProgram;
options nosymbolgen nomlogic nomprint nosource nosource2 nonotes;
%showMessage(msg=Inicio del programa principal de escritura);

%if %sysfunc(fileexist("&wf_errslz.")) %then
%do;
proc import datafile="&wf_errslz." out=&wt_errslz. dbms=DLM replace;
delimiter=',';
getnames=no;
run;
%end;

filename ex_pcs pipe "ps -eo pid,euser,cmd | tr -s ' ' | grep -i &wpgmbl.";

%capturaCampos;
%split3(tabla_origen=WORK.BMW, registros_por_chunk=&wsplit, prefix=&wprefix);
%create_commands;
%deleteTableLZ(&libdes., BMW);
x "&wpgmbl.";
%waitForBulkLoads;
%checkForErrors(&pidexecution.);
%delProcessTables;
%comparaRegistros;
%tiempos(&hi);
%mend mainProgram;

%mainProgram;

/* Etiqueta: Final_Timer */
data _null_;
  dur = datetime() - &_timer_start;
  put 30*'-' / ' TOTAL DURATION:' dur time13.2 / 30*'-';
run;
