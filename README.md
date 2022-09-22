# MDS7201-mineduc-desercion

## Matriz 1:

- **Notas de colegio**: Egresados Colegio, `PROM_NOTAS_ALU`. En matriz final: `prom_notas_ultimo_anio_col`
- **Región del colegio**: Egresados Colegio, `COD_REG_RBD`. En matriz final: `region_colegio`
- **Modalidad del colegio (científico humanista / técnico)**: Egresados Colegio, `COD_ENSE`. En matriz final: `tipo_ensenanza_colegio`
- **Tipo de establecimiento (particular, subvencionado, municipal)**: Establecimientos, `cod_depe`. En matriz final: `dependencia_colegio`
- **Género**: Matriculados, `gen_alu`.
- **Edad**: Matriculados, `fec_nac_alu`.
- **Área del conocimiento de la carrera**: Matriculados, `area_conocimiento`.
- **Región de la institución de educación superior**: Matriculados, `region_sede`.
- **Desertor**: Vector objetivo; Aquel que no se ha titulado ni se ha matriculado al año 2022. En matriz final: `desertor_1`

Ruta archivo: https://drive.google.com/file/d/1JABykXdUoRa_Y5cNaCip-OP1xBZNgtds/view?usp=sharing

Ruta notebook: https://github.com/GianniCatBug/MDS7201-mineduc-desercion/blob/main/notebooks/3-seleccion-atributos.ipynb

**NOTA 1**: Muchos nulos en `cod_depe` al hacer el cruce, solo tomé los colegios desde el 2004, se podría tomar anteriores.

**NOTA 2**: Solo tomé el último año de enseñanza, podrían tomarse los 4 años de enseñanza media y promediarse.

