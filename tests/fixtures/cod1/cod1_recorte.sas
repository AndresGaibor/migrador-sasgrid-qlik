​/* Etiqueta: Inicio_Timer */
/* Start timer */
%let _timer_start = %sysfunc(datetime());

/* Etiqueta: Programa */
libname GCIDLL01 "/data/GRID/GCIA_DLLO_SERVICIOS_DE_INFORMACION";

proc datasets lib=GCIDLL01 nolist;
delete cars_poc;
quit;

/* Etiqueta: Crea_Cars */
data WORK.cars_poc;
set sashelp.cars;
run;


/* Etiqueta: Ciclo_Append */
%macro append_all;
%do i=1 %to 15;
/* CREA UNA TABLA DE 2 GIGAS Y 14'024.704 DE REGISTROS */
proc append
base=WORK.cars_poc
data=WORK.cars_poc;
run;

%end;
%mend append_all;

%append_all;


%let clave=SecretoFicticio123;
%let pass_bd = ;
%global proceso lz_dsn libtmp tabdes pidexecution wprefix;

%macro ambiente;
%if &m_ambiente eq D %then
%do;

/* Desarrollo */
%let lz_dsn=IMPALA;
%end;
%else %if &m_ambiente eq C %then
%do;

/* Certi */
%let lz_dsn=IMPALAC;
%end;
%else %if &m_ambiente eq P %then
%do;

/* Produccion */
%let lz_dsn=IMPALAP;
%end;
%mend ambiente;


/* Etiqueta: Carga_Tablas */
%let dataset5  = $dataset5;
%let archivo_5  = $archivo_5;
data WORK.tabla_demo;
set WORK.cars_poc;
where Origin = "Asia";
run;
%ambiente;
