# MDS7201-mineduc-desercion

## Matriz 1:

- **Notas de colegio**: Egresados Colegio, `PROM_NOTAS_ALU`. En matriz final: `prom_notas_media`
- **Región del colegio**: Egresados Colegio, `COD_REG_RBD`. En matriz final: `region_colegio`
- **Modalidad del colegio (científico humanista / técnico)**: Egresados Colegio, `COD_ENSE`. En matriz final: `tipo_ensenanza_colegio`
- **Tipo de establecimiento (particular, subvencionado, municipal)**: Establecimientos, `cod_depe`. En matriz final: `dependencia_colegio`
- **Género**: Matriculados, `gen_alu`.
- **Edad**: Matriculados, `fec_nac_alu`.
- **Área del conocimiento de la carrera**: Matriculados, `area_conocimiento`.
- **Región de la institución de educación superior**: Matriculados, `region_sede`.
- **Desertor**: Vector objetivo; Aquel que no se ha titulado ni se ha matriculado al año 2022. En matriz final: `desertor_1`

Ruta archivo: https://drive.google.com/file/d/1qVsWgYH5GiEEwxxgRtKal6Ge7safzni8/view?usp=sharing

Ruta notebook: https://github.com/GianniCatBug/MDS7201-mineduc-desercion/blob/main/notebooks/3-seleccion-atributos.ipynb

## Matriz 2:
- **Valor Arancel**: Matriculados, `valor_arancel` (Matriz 2).
- **Estado acreditación carrera**: Matriculados, `acreditada_carr` (Matriz 2).
- **Estado acreditación institución**: Matriculados, `acreditada_inst` (Matriz 2).
- **Cantidad de becas**: Becas y créditos, `BENEFICIO_BECA_FSCU` (Matriz 2).

Ruta archivo: https://drive.google.com/file/d/1TWj9DgtmFG72g547Uoro_jBCKAhqNbbn/view?usp=sharing

## Matriz 3:
- **FSCU**: Tiene fondo solidario, `BENEFICIO_BECA_FSCU` (Matriz 3).
- **gratuidad**: Tiene gratuidad, `BENEFICIO_BECA_FSCU` (Matriz 3).
- **beca**: Tiene beca, `BENEFICIO_BECA_FSCU` (Matriz 3).

Ruta archivo: https://drive.google.com/file/d/1anNyWcUCDUqndFgZTFL4GJmD3hpF4a7w/view?usp=sharing

## Matriz 4:
- **Jornada**: Diurno o vespertino (Matriz 4).
- **Duración carrera**: Duración en semestres de la carrera (Matriz 4).
- **Duración titulación**: Duración en semestres del proceso de titulación (Matriz 4).

Se corrige además el valor del arancel, para lo cual se tiene que consultar el formato del valor.

Ruta archivo: https://drive.google.com/file/d/1itpZ3CrdcqBqaoDDHjLpBGfftfKOt_lP/view?usp=sharing

## Matrices de trabajo:

Agrega atributo **Sub tipo de institución**: CFT Privado, CFT Estatal, IP Privado con presencia nacional, IP Privado

- No dummy: https://drive.google.com/file/d/1r5VsqBJuXqlLxflkQQmHFav8v99FeAlF/view?usp=sharing
- Dummy con drop: https://drive.google.com/file/d/1BbGXKMFgSFzs_mdYAXAvHntXAzGG7tha/view?usp=sharing
- Dummy sin drop: https://drive.google.com/file/d/1O0NdyfwdhWEA9s4Xvuo10ZWUd7bLam3F/view?usp=sharing
- Matriz solo 2015 y mejores atributos: https://drive.google.com/file/d/1y_4OMs2PIljSpHu8o1J15yHnSJN0052u/view?usp=sharing

## Otros

Ruta geojson regiones: https://drive.google.com/file/d/1dwzVGss_7v8xRUk7AEIpUT_tCGZH8gOc/view?usp=sharing

Modelo grilla XGB: https://drive.google.com/file/d/1uf2Bi9srohSl5QmAj6AMl8CWduc43aur/view?usp=sharing
