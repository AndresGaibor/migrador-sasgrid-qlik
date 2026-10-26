# Job `job_banking_formats`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Formats/banking_formats.sas` (sha256 `3d292f2a2243`)
- **Instrucciones:** 1 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

### 1. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s12` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Formats/banking_formats.sas:12`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/ts-sas-legacy-analytics/Formats/banking_formats.sas:12 · nombre oficial
  - `INTABLE` (Inline Table) = `ACCTTYPE | CHK | Checking
ACCTTYPE | SAV | Savings
ACCTTYPE | MMA | Money Market
ACCTTYPE | CD | Certificate of Deposit
ACCTTYPE | IRA | Individual Retirement
ACCTTYPE | LOC | Line of Credit
ACCTTYPE | MTG | Mortgage
ACCTTYPE | AUTO | Auto Loan
ACCTTYPE | PERS | Personal Loan
ACCTTYPE | CC | Credit Card
ACCTTYPE | HELC | Home Equity LOC
ACCTTYPE | OTHER | Unknown
ACCTSTAT | A | Active
ACCTSTAT | C | Closed
ACCTSTAT | D | Dormant
ACCTSTAT | F | Frozen
ACCTSTAT | R | Restricted
ACCTSTAT | S | Suspended
ACCTSTAT | P | Pending
ACCTSTAT | W | Written Off
ACCTSTAT | OTHER | Unknown
RISKRATE | 1 | Minimal Risk
RISKRATE | 2 | Low Risk
RISKRATE | 3 | Moderate Risk
RISKRATE | 4 | Elevated Risk
RISKRATE | 5 | High Risk
RISKRATE | 6 | Very High Risk
RISKRATE | 7 | Loss Expected
RISKRATE | OTHER | Not Rated
TXNCAT | DEP | Deposit
TXNCAT | WDR | Withdrawal
TXNCAT | TRF | Transfer
TXNCAT | PMT | Payment
TXNCAT | FEE | Fee
TXNCAT | INT | Interest
TXNCAT | ADJ | Adjustment
TXNCAT | REV | Reversal
TXNCAT | CHG | Charge
TXNCAT | REF | Refund
TXNCAT | OTHER | Other
DELQBKT | 0 | Current
DELQBKT | 1-29 | 1-29 Days
DELQBKT | 30-59 | 30-59 Days
DELQBKT | 60-89 | 60-89 Days
DELQBKT | 90-119 | 90-119 Days
DELQBKT | 120-179 | 120-179 Days
DELQBKT | 180-HIGH | 180+ Days
BALRANGE | LOW-<0 | Negative
BALRANGE | 0 | Zero
BALRANGE | 0<-<1000 | $0-$999
BALRANGE | 1000-<5000 | $1K-$4,999
BALRANGE | 5000-<25000 | $5K-$24,999
BALRANGE | 25000-<100000 | $25K-$99,999
BALRANGE | 100000-<500000 | $100K-$499,999
BALRANGE | 500000-HIGH | $500K+
REGION | NE | Northeast
REGION | SE | Southeast
REGION | MW | Midwest
REGION | SW | Southwest
REGION | W | West
REGION | NW | Northwest
REGION | HQ | Headquarters
REGION | OTHER | Unknown
CUSTSEG | RET | Retail
CUSTSEG | PREM | Premium
CUSTSEG | PB | Private Banking
CUSTSEG | SMB | Small Business
CUSTSEG | COMM | Commercial
CUSTSEG | CORP | Corporate
CUSTSEG | OTHER | Unclassified
LNPURP | PURCH | Purchase
LNPURP | REFI | Refinance
LNPURP | CASHOUT | Cash-Out Refinance
LNPURP | CONST | Construction
LNPURP | RENO | Renovation
LNPURP | CONSOL | Debt Consolidation
LNPURP | EDUC | Education
LNPURP | MEDIC | Medical
LNPURP | OTHER | Other` — SAS real/ts-sas-legacy-analytics/Formats/banking_formats.sas:12 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_12_format_definition_1_schema`

## Casos de validación

- `vc_op_12_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
