/* Dos copias idénticas de una macro de negocio (filtrar clientes activos). No es fontanería: debe
   contar como dos apariciones del mismo joblet. */

%macro filtra_activos(tabla=, destino=);
data work.&destino.;
set &tabla.;
where estado = 'A';
run;
%mend filtra_activos;

%filtra_activos(tabla=work.clientes, destino=clientes_activos);

%macro filtra_activos(tabla=, destino=);
data work.&destino.;
set &tabla.;
where estado = 'A';
run;
%mend filtra_activos;

%filtra_activos(tabla=work.pedidos, destino=pedidos_activos);
