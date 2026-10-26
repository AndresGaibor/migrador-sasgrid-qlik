# Job `job_insurance_formats`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Formats/insurance_formats.sas` (sha256 `3051af02bbc5`)
- **Instrucciones:** 1 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

### 1. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s11` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Formats/insurance_formats.sas:11`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/ts-sas-legacy-analytics/Formats/insurance_formats.sas:11 · nombre oficial
  - `INTABLE` (Inline Table) = `POLTYPE | WL | Whole Life
POLTYPE | TL | Term Life
POLTYPE | UL | Universal Life
POLTYPE | VL | Variable Life
POLTYPE | AUTO | Auto Insurance
POLTYPE | HOME | Homeowners
POLTYPE | RENT | Renters
POLTYPE | UMBR | Umbrella
POLTYPE | HLTH | Health
POLTYPE | DNTL | Dental
POLTYPE | VIS | Vision
POLTYPE | DISAB | Disability
POLTYPE | LTCI | Long-Term Care
POLTYPE | OTHER | Unknown
CLMSTAT | NEW | New
CLMSTAT | OPEN | Open
CLMSTAT | INV | Under Investigation
CLMSTAT | ADJ | Adjusting
CLMSTAT | PEND | Pending Approval
CLMSTAT | APPR | Approved
CLMSTAT | DENY | Denied
CLMSTAT | PAID | Paid
CLMSTAT | CLOS | Closed
CLMSTAT | REOP | Reopened
CLMSTAT | SUSP | Suspended
CLMSTAT | LITI | In Litigation
CLMSTAT | OTHER | Unknown
RISKCAT | STD | Standard
RISKCAT | PREF | Preferred
RISKCAT | SPRM | Super Preferred
RISKCAT | SUB | Substandard
RISKCAT | DEC | Declined
RISKCAT | OTHER | Unrated
COVTYPE | COMP | Comprehensive
COVTYPE | COLL | Collision
COVTYPE | LIAB | Liability
COVTYPE | PIP | Personal Injury Protection
COVTYPE | UMBI | Uninsured Motorist BI
COVTYPE | UMPD | Uninsured Motorist PD
COVTYPE | MED | Medical Payments
COVTYPE | TOW | Towing
COVTYPE | RENT | Rental Reimbursement
COVTYPE | OTHER | Other
LOSSRANGE | LOW-<0 | Recovery
LOSSRANGE | 0 | No Loss
LOSSRANGE | 0<-<5000 | $0-$4,999
LOSSRANGE | 5000-<25000 | $5K-$24,999
LOSSRANGE | 25000-<100000 | $25K-$99,999
LOSSRANGE | 100000-<500000 | $100K-$499,999
LOSSRANGE | 500000-HIGH | $500K+` — SAS real/ts-sas-legacy-analytics/Formats/insurance_formats.sas:11 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_11_format_definition_1_schema`

## Casos de validación

- `vc_op_11_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
