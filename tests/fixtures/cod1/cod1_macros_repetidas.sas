/* Recorte de Cod1: las mismas macros aparecen varias veces pegadas en el programa. */

%macro carga_tabla(tabla=, destino=);
data work.&destino.;
set &tabla.;
where edad > 18;
run;
%mend carga_tabla;

%macro split2(libreria, tabla_origen);
proc sort data=&libreria..&tabla_origen. out=work.ordenada;
by id;
run;
%mend split2;

%carga_tabla(tabla=work.clientes, destino=adultos);
%split2(work, clientes);

/* Segundo bloque: copia idéntica de las dos macros. */

%macro carga_tabla(tabla=, destino=);
data work.&destino.;
set &tabla.;
where edad > 18;
run;
%mend carga_tabla;

%macro split2(libreria, tabla_origen);
proc sort data=&libreria..&tabla_origen. out=work.ordenada;
by id;
run;
%mend split2;

/* Tercer bloque: carga_tabla con otro criterio (definición distinta, mismo nombre). */

%macro carga_tabla(tabla=, destino=);
data work.&destino.;
set &tabla.;
where edad > 30;
run;
%mend carga_tabla;

%carga_tabla(tabla=work.clientes, destino=mayores);
