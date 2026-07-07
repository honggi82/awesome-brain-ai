[Figure 1]

# Implementacio´n de modelos lineales mixtos flexibles a datos de crecimiento craneofacial en la cohorte CESLPH-Damasco

Mariluz Trilleras Mota

# Implementacio´n de modelos lineales mixtos flexibles a datos de crecimiento craneofacial en la cohorte CESLPH Damasco

### Mariluz Trilleras Mota

Tesis o trabajo de grado presentada(o) como requisito parcial para optar al tı´tulo de: Magister en Estad´ıstica

Director: Juan Carlos Salazar Uribe, Ph.D. University of Kentucky Profesor Titular, Universidad Nacional de Colombia, Sede Medellı´n.

Codirector: Mauricio Alejandro Mazo Lopera, Ph.D. Universidad Nacional De Colombia Profesor Asociado, Universidad Nacional de Colombia, Sede Medellı´n.

Grupo de Investigaci´n en Estadı´stica, Universidad Nacional de Colombia, Sede Medellı´n y Grupo Labio y Paladar Hendido, Fisiologı´a Oral y Crecimiento CESLPH Universidad CES

###### (Dedicatoria)

“La cosa m´s bella que podemos experimentar es lo misterioso. Es la fuente de toda verdad y ciencia. Aquel para quien esa emoci´n es ajena, aquel que ya no puede maravillarse y extasiarse ante el miedo, vale tanto como un muerto: sus ojos est´n cerrados...”

Albert Einstein

## Agradecimientos

Gracias a Dios y a mi familia, de manera especial a mis padres e hijo por la motivacio´n y el apoyo que siempre me dieron para la realizaci´on de este proyecto.

Mi gratitud infinita, a mi director el Doctor Juan Carlos Salazar Uribe por su continua guı´a, sus orientaciones y lineamientos durante el desarrollo de la investigaci´on.

Gracias tambi´en al Doctor Mauricio Alejandro Mazo Lopera, codirector de este trabajo de grado, por su ayuda y orientacio´n con el progreso de la investigaci´on.

Al grupo de investigacio´n Labio y paladar hendido, fisiologı´a oral y crecimiento craneofacial CESLPH mis agradecimientos por hacer posible la realizaci´on de este estudio.

A mi jurado, Doctor Freddy Herna´ndez Barajas y Mario Ce´sar Jaramillo Elorza mis agradecimientos por los comentarios y sugerencias al presente trabajo.

A los docentes que con su soporte cientı´fico y humano contribuyeron a mi formaci´on acade´mica.

A la Universidad Nacional de Colombia sede Medellı´n por ser parte integral de mi proceso profesional, acad´emico y laboral.

A todos aquellos vinculados a este trabajo de una u otra forma.

ix

## Resumen

###### Implementacio´n de modelos lineales mixtos flexibles a datos de crecimiento craneofacial en la cohorte CESLPH Damasco

Entender el crecimiento craneofacial en humanos es importante en muchas a´reas del conocimiento y del quehacer humano, como la antropologı´a, la biolog´ıa, la cirugı´a y la ortodoncia entre otros. Usualmente, las mediciones con caracter´ısticas craneofaciales se registran de manera longitudinal en determinados intervalos de tiempo. Factores predictores tales como la direccio´n, velocidad y la aceleraci´on de crecimiento son esenciales para comprender la naturaleza del crecimiento craneofacial y su posible comportamiento de acuerdo con el ge´nero y la edad. Desde hace algunas de´cadas, en la literatura se pueden encontrar recomendaciones del uso de modelos lineales mixtos cuando los datos son de tipo longitudinal ya que ellos son herramientas precisas y u´tiles para generar conocimiento de calidad a partir de este tipo de datos como se hace notar en el libro titulado Applied Longitudinal Analysis [Fitzmaurice et al., 2012]. Este conocimiento de calidad es relevante para la toma de decisiones, especialmente en los campos de la ortodoncia, cirug´ıa maxilofacial y la oclusio´n dental donde se quieren obtener resultados o´ptimos durante un tratamiento. En particular, los polinomios de segundo orden con coeficientes aleatorios han demostrado un muy buen desempen˜o en la modelacio´n de datos de crecimiento craneofacial en poblacio´n anglosajona. Por estas razones, en este trabajo se ilustran resultados de la implementacio´n de modelos a medidas de crecimiento facial conocidas como altura facial anterior (AFH), altura facial posterior (PFH), ´angulo plano mandibular (S-N/PM) y a´ngulo goniaco (Ar-Go-Me), que han sido recopiladas en el estudio CES-Damasco durante ma´s de 24 an˜os, constituye´ndose en uno de los estudios de crecimiento craneofacial m´as largos del mundo y el ma´s largo llevado a cabo en poblacio´n de mestizos [Jim´enez et al., 2020]. Especı´ficamente, se ajustan modelos lineales mixtos con coeficientes aleatorios, modelos lineales mixtos basados en coeficientes aleatorios y funciones splines, modelos lineales mixtos con intercepto aleatorios, modelos lineales mixtos con intercepto aleatorio. Se vera´ que el desempe˜no de estos u´ltimos modelos basados en funciones spline generan una mayor plausibilidad y un mejor poder predictivo [Chvatal et al., 2005].

Palabras claves: Crecimiento craneofacial, estad´ıstica, ortodoncia, modelos mixtos, splines.

## Abstract

Implementation of flexible mixed linear models to craniofacial growth data in the CESLPH Damasco cohort

x

Understanding craniofacial growth in humans is important in many areas of human knowledge and endeavor, such as anthropology, biology, surgery and orthodontics, among others. Usually, measurements with craniofacial characteristics are recorded longitudinally at certain time intervals. Predictors such as direction, speed and acceleration of growth are essential to understand the nature of craniofacial growth and its possible behavior according to gender and age. For some decades, recommendations for the use of linear mixed models can be found in the literature when the data are of longitudinal type since they are accurate and useful tools to generate quality knowledge from this type of data as noted in the book entitled Applied Longitudinal Analysis [Fitzmaurice et al., 2012]. This quality knowledge is relevant for decision making, especially in the fields of orthodontics, maxillofacial surgery and dental occlusion where optimal results are desired during a treatment. In particular, second order polynomials with random coefficients have shown a very good performance in the modeling of craniofacial growth data in Anglo-Saxon population [Jime´nez et al., 2020]. For these reasons, this paper illustrates results from the implementation of models to facial growth measures known as anterior facial height (AFH), posterior facial height (PFH), mandibular plane angle (S-N/PM) and goniac angle (Ar-Go-Me), which have been collected in the CES-Damascus study for more than 24 years, constituting one of the longest craniofacial growth studies in the world and the longest carried out in mestizo population. Specifically, linear mixed models with random coefficients, linear mixed models based on random coefficients and spline functions, linear mixed models with random intercept, linear mixed models with random intercept, fixed spline and random spline are fitted. It will be shown that the performance of the latter models based on spline functions generates higher plausibility and better predictive power.[Chvatal et al., 2005]

Keywords: Craniofacial growth, statistics, orthodontics, mixed models, splines.

# Contenido

Agradecimientos VII

Resumen IX

Lista de figuras XIII

Lista de tablas XVII

- 1 Introducci´n 2
- 2 Revisio´n de Literatura: Antecedentes y Marco Te´rico 5

- 2.1 Antecedentes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.2 Estado del arte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.3 Modelos lineales mixtos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

- 2.3.1 Estimaci´on en Modelos Lineales Mixtos . . . . . . . . . . . . . . . . . 9
- 2.3.2 Estimaci´on de m´axima verosimilitud (MLE) . . . . . . . . . . . . . . 9
- 2.3.3 Caso especial θ es conocido . . . . . . . . . . . . . . . . . . . . . . . 10
- 2.3.4 Caso general θ es desconocido . . . . . . . . . . . . . . . . . . . . . . 11
- 2.3.5 Estimaci´on REML . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

- 2.4 Modelos lineales mixtos con splines . . . . . . . . . . . . . . . . . . . . . . . 12

- 2.4.1 Bases y nodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 2.4.2 Selecci´on del par´ametro de suavizado . . . . . . . . . . . . . . . . . . 14

- 3 Modelos propuestos para las medidas craneofaciales consideradas 17

- 3.1 Modelos lineales mixtos para el a´ngulo del plano mandibular . . . . . . . . . 19
- 3.2 Ana´lisis exploratorio de datos . . . . . . . . . . . . . . . . . . . . . . . . . . 19

- 3.2.1 Poblaci´on de estudio y variables consideradas . . . . . . . . . . . . . 20
- 3.2.2 Angulo´ del plano mandibular . . . . . . . . . . . . . . . . . . . . . . 21
- 3.2.3 An´alisis descriptivo de los datos . . . . . . . . . . . . . . . . . . . . . 22

- 3.3 Resultados para SN-MP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 3.3.1 Interpretacio´n de los resultados . . . . . . . . . . . . . . . . . . . . . 25
- 3.4 Evaluaci´on de la precisio´n de los modelos ajustados . . . . . . . . . . . . . . 28
- 3.5 Discusio´n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

xii Contenido

- 4 Angulo´ Goniaco (ArGoMe) 30

- 4.1 Puntos de referencia ´angulo goniaco (ArGoMe) . . . . . . . . . . . . . . . . . 30
- 4.2 Ana´lisis descriptivo de los datos . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 4.3 Resultados para ArGoMe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- 4.4 Evaluaci´on de la precisio´n de los modelos ajustados . . . . . . . . . . . . . . 36
- 4.5 Discusio´n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

- 5 Modelos lineales mixtos para la altura facial anterior 38

- 5.1 Altura Facial Anterior (AFH) . . . . . . . . . . . . . . . . . . . . . . . . . . 38
- 5.2 Ana´lisis exploratorio de datos . . . . . . . . . . . . . . . . . . . . . . . . . . 39
- 5.3 Resultados AFH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 5.4 Evaluaci´on de precisi´on de los modelos ajustados . . . . . . . . . . . . . . . 47
- 5.5 Discusio´n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

- 6 Modelos lineales mixtos para la altura facial posterior 49

- 6.1 Altura Facial Posterior (PFH) . . . . . . . . . . . . . . . . . . . . . . . . . . 49
- 6.2 Ana´lisis exploratorio de datos . . . . . . . . . . . . . . . . . . . . . . . . . . 50
- 6.3 Resultados PFH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
- 6.4 Evaluaci´on de la precisio´n de los modelos ajustados . . . . . . . . . . . . . . 56
- 6.5 Discusio´n . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

- 7 Comparaci´n de resultados 58
- 8 Conclusiones y recomendaciones 60

- 8.1 Conclusiones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
- 8.2 Recomendaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61 Bibliografı´a 62

# Lista de Figuras

- 3-1 Gra´ficos de densidad de algunas de las medidas de inter´es en el estudio de caracterizacio´n demogr´afica de la corte CESLPH-DAMASCO. . . . . . . . . 21
- 3-2 Angulo´ SN-MP formado por los planos mandibular (Go-Me) y de Frankfort (Po-Or). Define el patr´n de crecimiento facial. Fuente: [Ricketts, 1981] . . . . . . . . . . . 22
- 3-3 Gr´fica de perfiles de acuerdo al ge´nero en funci´n de la medida SN-MP. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . 23
- 3-4 Diagramas de boxplot global y longitudinales del ´ngulo del plano mandibular. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . 23
- 3-5 Diagrama de Boxplot longitudinal y gr´fico de lineas promedio de acuerdo a la edad y al g´enero del ´ngulo del plano mandibular. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 3-6 Gr´fico de lineas del modelo con intercepto aleatorio (izq.) versus el modelo ajustado de intercepto aleatorio y funciones splines (der.). Lı´nea punteada corresponde a los valores observados y la lı´nea s´lida corresponde a los modelos ajustados por g´enero. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . 27
- 3-7 Perfiles observados y predichos del ´ngulo del plano mandibular basado en splines de 4 individuos de ambos g´eneros. Las lı´neas s´lidas corresponden al modelo individual ajustado y las lı´neas punteadas corresponden a las observaciones del sujeto. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . 28

- 4-1 La distancia desde los puntos Gonion (Gn), Gonion (Gn) y Menton (Me) representan la magnitud del Angulo´ Goniaco (ArGoMe). . . . . . . . . . . . . . . . . . . 30
- 4-2 Gra´fica de perfiles de acuerdo a la edad y al g´enero en funci´on de la medida del a´ngulo goniaco (ArGoMe). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 4-3 Diagramas de boxplot global y longitudinales del ´ngulo Goniaco (ArGoMe). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . 32
- 4-4 Diagrama de Boxplot longitudinal y gr´fico de lineas promedio de acuerdo a la edad y al g´enero del ´ngulo goniaco (ArGoMe). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
- 4-5 Gr´fico de lineas para la medida del ´ngulo gonion (ArGoMe) del modelo con intercepto aleatorio (izq.) versus el modelo ajustado de intercepto aleatorio y funciones splines (der.). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . 35

###### xiv Lista de Figuras

- 4-6 Perfiles observados y predichos del angulo del ´ngulo goniaco (ArGoMe) basado en splines de 4 individuos de ambos ge´neros. Las lı´neas s´lidas corresponden al modelo individual ajustado y las lı´neas punteadas corresponden a las observaciones del sujeto. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . 35
- 5-1 Puntos de referencia cefalome´tricas y trazado cefalom´etrico altura facial anterior (AFH). Fuente: [Lee et al., 2021] . . . . . . . . . . . . . . . . . . . . . . . . . 39

- 5-2 Gra´fica de perfiles de acuerdo a la edad y al g´enero en funci´on de la medida de la medida altura facial Anterior (AFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
- 5-3 Diagrama de Boxplot global que ignora la longitudinalidad de acuerdo al ge´nero de la altura facial anterior (AFH). Fuente: Creaci´on propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
- 5-4 Diagramas de boxplot global y longitudinales de la medida altura facial anterior (AFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH . . . 41
- 5-5 Diagrama de Boxplot longitudinal y gra´fico de lineas promedio de acuerdo a la edad y al g´enero de la medida altura facial anterior (AFH). Fuente: Creaci´on propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . 42
- 5-6 Modelos ajustados con intercepto, pendiente y te´rmino cuadr´tico aleatorio y modelo ajustado con intercepto, pendiente y t´ermino cuadr´tico aleatorio y funciones spline. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . 46
- 5-7 Perfiles observados y predichos de la altura facial anterior (AFH) basado en splines de 4 individuos de ambos g´eneros. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

- 6-1 Puntos de referencia cefalome´tricas y trazado cefalom´etrico Altura Facial Posterior. Fuente: [Ricketts, 1981] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

- 6-2 Gra´fica de perfiles de acuerdo a la edad y al g´enero en funcio´n de la medida altura facial posterior (PFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
- 6-3 Diagramas de boxplot global y longitudinal de la medida altura facial posterior (PFH). Fuente: Creacio´n propia y Grupo de Investigaci´on CESLPH . . . . . 51
- 6-4 Diagrama de Boxplot longitudinal y gra´fico de lineas promedio de acuerdo a la edad y al g´enero de la medid Altura Facial Posterior (PFH). Fuente: Creaci´on propia y Grupo de Investigacio´n CESLPH . . . . . . . . . . . . . . . . . . . 52
- 6-5 Modelo ajustados con intercepto aleatorio y modelo ajustado con intercepto aleatorio y funciones spline para la medida altura facial posterior. Fuente: Creacio´n propia y Grupo de Investigaci´on CESLPH . . . . . . . . . . . . . . 55

###### Lista de Figuras xv

6-6 Perfiles observados y predichos de la altura facial posterior basado en splines de 4 individuos de ambos g´eneros para PFH. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

# Lista de Tablas

- 3-1 Caracterizacio´n demogr´afica y medidas craneofaciales de 49 mestizos de la cohorte CESLPH-DAMASCO . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 3-2 Tiempo promedio de seguimiento y evoluci´on o cambio en SN-MP de la cohorte desde la lı´nea base de acuerdo al ge´nero. . . . . . . . . . . . . . . . . . 22
- 3-3 Coeficientes de regresi´on estimados (efectos fijos) y errores esta´ndar y componentes de varianza para el modelo del a´ngulo del plano mandibular . . . . 25
- 3-4 Estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio y funciones spline para la medida del ´angulo del plano mandibular . 26
- 3-5 Valores para la selecci´on de modelo basados en el AIC y BIC respectivamente 28
- 3-6 Criterios para la selecci´on de modelo mediante el coeficiente de correlaci´on intraclase (ICC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
- 3-7 R2 de Nakagawa para modelos mixtos . . . . . . . . . . . . . . . . . . . . . . 29

- 4-1 Tiempo promedio de seguimiento y evolucio´n o cambio en ArGoMe de la cohorte desde la lı´nea base de acuerdo al ge´nero. . . . . . . . . . . . . . . . . 31
- 4-2 Coeficientes de regresi´on estimados (efectos fijos) y errores esta´ndar y componentes de varianza para los datos del a´ngulo goniaco . . . . . . . . . . . . 33
- 4-3 Estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio y splines fijos y aleatorios para la medida a´ngulo goniaco . . . . . . 34
- 4-4 Criterios para la seleccio´n del mejor modelo. . . . . . . . . . . . . . . . . . . 36
- 4-5 Criterios para la selecci´on de modelo mediante el coeficiente de correlaci´on intraclase (ICC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 4-6 R2 de Nakagawa para modelos mixtos . . . . . . . . . . . . . . . . . . . . . . 36

- 5-1 Tiempo promedio de seguimiento y evolucio´n o cambio en AFH de la cohorte desde la lı´nea base de acuerdo al g´enero. . . . . . . . . . . . . . . . . . . . . 39
- 5-2 Coeficientes de regresi´on estimados (efectos fijos) y errores esta´ndar y componentes de varianza para los datos de la altura facial anterior (AFH) . . . . 43
- 5-3 Estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio y splines fijos para la medida altura facial anterior (AFH). . . . . . 45
- 5-4 Criterios para la seleccio´n de modelo mediante el Criterio de informacio´n de Akaike y BIC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
- 5-5 Criterios para la selecci´on de modelo mediante el coeficiente de correlaci´on intraclase (ICC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

Lista de Tablas 1

- 5-6 R2 de Nakagawa para modelos mixtos . . . . . . . . . . . . . . . . . . . . . . 47
- 6-1 Tiempo promedio de seguimiento y evoluci´on o cambio en PFH de la cohorte desde la lı´nea base de acuerdo al g´enero. . . . . . . . . . . . . . . . . . . . . 50

- 6-2 Coeficientes de regresi´on estimados (efectos fijos) y errores esta´ndar y componentes de varianza para los datos de la altura facial posterior (PFH). . . . 53
- 6-3 Estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio, splines fijos y aleatorios para la altura facial posterior (PFH). . . . 54
- 6-4 Criterios para la seleccio´n de modelo mediante el Criterio de informacio´n Akaike 56
- 6-5 Criterios para la selecci´on de modelo mediante el coeficiente de correlaci´on intraclase (ICC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
- 6-6 R2 de Nakagawa para modelos mixtos . . . . . . . . . . . . . . . . . . . . . . 56

- 7-1 Comparacio´n modelos ajustados para las medidas de a´ngulos . . . . . . . . . 58 7-2 Comparacio´n modelos ajustados para las medidas . . . . . . . . . . . . . . . 59

# 1 Introducci´n

En los datos longitudinales el resultado se observa repetidamente en diferentes momentos para cada sujeto en estudio. Los sujetos no se observan necesariamente ni al mismo tiempo ni el mismo n´umero de veces (datos desbalanceados). Las covariables tambie´n pueden ser diferentes para cada sujeto. Este tipo de datos tiene varias caracterı´sticas, una de ellas es que cada sujeto tiene una tendencia (o trayectoria) particular y no son necesariamente lı´neas rectas. Del mismo modo, si se obtiene la media de todas las observaciones se obtiene una estimacio´n del perfil medio de la poblaci´on. Para este tipo de datos longitudinales se formulan los llamados modelos especı´ficos de sujetos o modelos de poblaci´on media y dependiendo de los objetivos del estudio uno puede estar interesado en uno u otro. En los dise˜nos de medidas repetidas se registran varias covariables relacionadas con el individuo y el inter´es se centra en co´mo la respuesta depende de las covariables a lo largo del tiempo. Cuando la variable de respuesta es continua, los modelos de regresi´on lineal cla´sicos pueden ampliarse para manejar los resultados correlacionados que son tı´picos en los datos longitudinales. Esta correlacio´n entre medidas repetidas puede modelarse explı´citamente (por ejemplo, mediante modelos de patrones de covarianza) o impl´ıcitamente (mediante la introduccio´n de efectos aleatorios). Este u´ltimo enfoque da lugar a una clase versa´til de modelos de regresi´on para datos longitudinales conocidos como modelos lineales de efectos mixtos [Fitzmaurice et al., 2012]. De este modo surge el por qu´e utilizar modelos lineales mixtos para modelar datos de tipo longitudinal. Estos modelos podemos definirlos como una herramienta flexible para modelar datos correlacionados, su estimacio´n se basa en la funci´on de verosimilitud, se da lugar a pruebas va´lidas en disen˜os complejos con datos desbalanceados y permite la inferencia de efectos aleatorios. Finalmente, los modelos lineales mixtos permiten la estimacio´n REML ( Ma´xima verosimilitud restringida) de los componentes de la varianza. Los modelos lineales mixtos (LMM) son una extensi´on de los modelos lineales simples para tener en cuenta tanto los efectos fijos como los efectos aleatorios y se aplican ampliamente cuando hay dependencia en los datos. Los casos ma´s comunes en los que aparece esta dependencia es cuando se toman varias medidas de un mismo individuo e implica una variaci´on intra-sujeto que se incluye en el modelo lineal mixto a trav´es de un t´ermino de error. La variaci´on entre sujetos tambi´en se incluye en el MLE por medio de un t´ermino de efecto aleatorio. El supuesto teo´rico para estas dos fuentes de variacio´n es que son variables aleatorias multivariantes independientes y normalmente distribuidas con vectores de media cero y matrices de covarianza estructuradas. [Laird and Ware, 1982] propusieron estimar los para´metros de estas matrices de covarianza utilizando la Ma´xima Verosimilitud (MLE) y Ma´xima Verosimilitud Restringida (REML) y

3

afirman que tanto MLE como REML son bastante sensibles a la selecci´on de las estructuras de covarianza siendo en general ma´s recomendable el me´todo REML.

De acuerdo a esto es razonable creer que la respuesta de cada individuo tiene varios componentes: un efecto fijo, que es una funcio´n de las covariables; un efecto aleatorio, que expresa la variaci´on entre individuos y un error, que se debe a mediciones o variables no registradas [Faraway, 2016]. Cuando la relacio´n entre las variables es compleja o no lineal, es posible obtener un ajuste de los datos mediante modelos polino´micos puesto que a mayor grado del polinomio el ajuste de los datos mejora, no obstante tener un modelo polino´mico de grado elevado puede aumentar la complejidad del modelo, disminuir su precisio´n y dificultar su interpretacio´n y dicho modelo se puede sobreajustar, obteniendo un modelo con predileccio´n por el ruido y no por la sen˜al oculta de los datos. En estos escenarios es posible usar me´todos de suavizamiento basados en modelos de regresio´n por splines, los cuales permiten ajustar modelos ma´s flexibles. Estos modelos se fundamentan en bases de polinomios que se calculan por tramos y se unen en unos extremos denominados nodos. Estos modelos, de acuerdo con [Fitzmaurice et al., 2012] se pueden formular dentro de un marco de modelos lineales mixtos. El crecimiento craneofacial en nin˜os y adolescentes ha sido ampliamente estudiado, en la medida que diferentes investigadores han manifestado su inter´es de argumentar sus postulados. El intere´s de este estudio viene dado a que en algunos de los trabajos que se han revisado se evidencia el uso de modelos lineales mixtos segu´n [Chvatal et al., 2005] y [Buschang et al., 1988]. En estos trabajos los modelos que se seleccionaron tienen plausibilidad, interpretabilidad y generacio´n de conocimientos respecto a algunas medidas craneofaciales. Pero, el uso de polinomios cuadr´aticos podr´ıa ser inadecuado debido a que estos modelos a largo plazo dan curvaturas que indican que algunas medidas pueden decrecer lo cual podrı´a no ser biolo´gicamente plausible, como podr´ıa ser por ejemplo el caso de la altura facial anterior. Este problema se puede resolver utilizando modelos mixtos flexibles, por ejemplo, modelos basados en funciones spline, como los expuestos en el libro de [Fitzmaurice et al., 2012]. La idea de estos modelos es que expliquen el crecimiento craneofacial a partir de algunas medidas sin los problemas que se est´an discutiendo en relaci´on con el modelo cuadra´tico. Concretamente, se han de ajustar modelos lineales mixtos con coeficientes aleatorios, modelos lineales mixtos basados en coeficientes aleatorios y funciones splines, modelos lineales mixtos con intercepto aleatorios, spline fijos y aleatorios. Se vera´ que el desempe˜no de los modelos lineales mixtos con splines generan mayor plausibilidad y un mejor poder predictivo proporcionando resultados analı´ticos, potentes y flexibles como dice [Verbeke and Molenberghs, 2012] para la toma de decisiones, especialmente en los campos de la ortodoncia, la cirugı´a y la oclusi´on dental donde se quiere lograr resultados o´ptimos durante un tratamiento.

El trabajo consta de 5 capı´tulos distribuidos de la siguiente forma: en el capı´tulo 1, se da un enfoque general de lo que se quiere proponer y su contextualizaci´on. Luego en el capı´tulo

4 1 Introduccio´n

- 2, se hace una revisio´n de la literatura referente a los antecedentes y al marco teo´rico. En los antecedentes se mencionan algunos de los trabajos publicados sobre modelos mixtos y su aplicaci´on en la ortodoncia, en el marco teo´rico se definen algunos conceptos en cuanto a modelos lineales mixtos, estimaci´on de ma´xima verosimilitud, modelos lineales mixtos con splines y selecci´on del para´metro de suavizamiento, conceptos que son necesarios para el desarrollo del trabajo. En el cap´ıtulo 3 se discute la metodolog´ıa, en donde se presentan los modelos lineales mixtos para las medidas craneofaciales correspondientes a a´ngulos tales como ´angulo plano mandibular y a´ngulo goniaco (ArGoMe). Se consideran modelos lineales mixtos con intercepto aleatorios y con splines fijos y aleatorios. Posteriormente en el capı´tulo 4, se tienen en cuenta las medidas craneofaciales, altura facial anterior y altura facial posterior. Se proponen modelos lineales mixtos con coeficientes aleatorios y modelos lineales mixtos basados en coeficientes aleatorios y funciones splines. Luego en el capı´tulo 5, se realiza la comparaci´on de los resultados de los modelos ajustados. Se discuten los resultados de los modelos lineales mixtos propuestos y se define cu´ales son los de mejor desempen˜o. Finalmente, en el capı´tulo 6, se mencionan algunas conclusiones y recomendaciones respecto al uso de modelos mixtos basados en splines en el ´area de crecimiento craneofacial.

# 2 Revisio´n de Literatura: Antecedentes y Marco Te´rico

### 2.1. Antecedentes

Desde hace 29 an˜os, en el corregimiento Damasco del municipio de Santa Ba´rbara, Antioquia, se inici´o un estudio donde investigadores de la Facultad de Odontolog´ıa de la Universidad CES y la Universidad Nacional de Colombia, Sede Medellı´n, buscaban conocer mediante una muestra de 54 nin˜os y nin˜as de 6 a 8 an˜os con rasgos faciales normales y sin historia de tratamiento de ortodoncia como es el crecimiento y desarrollo facial con el pasar del tiempo. El seguimiento au´n es liderado, desde 1992, por el odont´ologo de la Universidad CES e investigador, Dr. Iv´an Dar´ıo Jime´nez Vargas, ahora director de la lı´nea de investigaci´on de crecimiento y desarrollo facial del grupo de investigacio´n CESLPH. Con el an´alisis y sus principales conclusiones se podra´ obtener una referencia para ejecutar los controles y tener en cuenta en otras investigaciones, las cuales servira´n para la toma de decisiones, especialmente en los campos de la ortodoncia, cirug´ıa maxilofacial y la oclusio´n dental donde se quieren obtener resultados o´ptimos durante un tratamiento [Jim´enez et al., 2020]. El estudio de estas mediciones conduce a la bu´squeda de nuevas formas de acercamiento a conceptos y procedimientos estadı´stico-matem´aticos relacionados con la construccio´n de modelos estadı´sticos en funcio´n del grado de complejidad que se han de presentar en ciertas medidas craneofaciales tales como altura facial anterior (AFH), altura facial posterior (PFH), a´ngulo plano mandibular (SN-MP) y a´ngulo goniaco (ArGoMe).

### 2.2. Estado del arte

Se realiza una revisi´on de la literatura donde se presentan avances relacionados con modelos lineales mixtos basados en coeficientes aleatorios, coeficientes aleatorios y funciones splines, intercepto aleatorios e intercepto aleatorios, spline fijos y aleatorios. A continuaci´on, se hace una revisi´on de algunos de estos trabajos.

[Preece and Heinrich, 1981] Establecen m´etodos estadı´sticos capaces de revelar las tendencias esenciales de una curva de crecimiento, utilizando pocos para´metros. De este modo plantean dos enfoques, uno es un enfoque no estructural donde utilizaron funciones de spline cu´bicas para suavizar las curvas de crecimiento y el segundo enfoque

implica un enfoque estructural, en el que desarrollan un modelo matem´atico determinado, donde ajustan los datos de medidas craneofaciales individuales mediante me´todos estadı´sticos apropiados. Los autores se centraron m´as por el enfoque estructural donde combinaron modelos como son los modelos de doble logı´stica, modelo simple, modelos mu´ltiples logı´sticos, modelo de Preece-Baines, con algunas funciones como la funcio´n logı´stica para el periodo pre-adolescente, funci´on de Gompertz hasta la adolescencia y funcio´n de Richards la cual se derivan de una ecuacio´n diferencial que vincula la tasa de crecimiento con el tiempo.

[Pan and Goldstein, 1998] Proponen la adaptacio´n de modelos de niveles mu´ltiples a datos de crecimiento en un amplio rango de edad usando una nueva clase de modelos spline extendidos. Restringe la discusio´n a modelos lineales.

[Brumback and Rice, 1998] Introducen una clase de modelos para una descomposicio´n aditiva de grupos de curvas estratificados por factores cruzados y anidados, generalizando splines suavizados a tales muestras asocia´ndolos con un modelo de efectos mixtos correspondiente. Asimismo, demuestran que los mejores predictores lineales insesgados (BLUP) del modelo extendido de efectos mixtos corresponden a soluciones de una regresio´n penalizada generalizada donde los para´metros de suavizado est´an directamente relacionados con los componentes de la varianza, y muestran que estas soluciones son splines c´ubicos.

[Chvatal et al., 2005] Desarrollaron modelos que permitieron obtener curvas de crecimiento longitudinal para modelar con precisi´on las variaciones individuales y usaron estos modelos para predecir cambios de crecimiento craneofacial en ni˜nos con datos longitudinales disponibles.

[Jime´nez et al., 2013] Desde 1992 el Grupo de Investigacio´n de Labio y Paladar Hendido, Fisiologı´a Oral y Crecimiento Craneofacial, CESLPH, est´a llevando a cabo un estudio longitudinal del crecimiento facial, que empez´o con 54 mestizos colombianos sin tratamiento con una muestra de 373 radiograf´ıas cef´alicas laterales obtenidas durante 18 an˜os de seguimiento, y en la actualidad hay 49 pacientes bajo estudio. La muestra disminuyo´ debido a abandonos.

[Bejarano et al., 2014] En este trabajo describen en detalle la muestra y los me´todos usados. Hacen uso de modelos longitudinales de efectos mixtos, caracterizando los patrones de crecimiento evaluando el patro´n individual de crecimiento y controlando la variabilidad entre sujetos del perı´metro cefa´lico en nin˜os de 0 a 3 an˜os.

[Guevara, 2015] Implement´o an´alisis univariados y multivariados para los estudios de variaciones morfol´ogicas de componentes craneofaciales para clasificar relaciones esquele´ticas I, II y III mediante variables como distancias, ´angulos y planos referenciales.

[Bavia and Garcia, 2016] Investigaron la asociaci´on entre la morfologı´a craneofacial y los trastornos temporomandibulares en adultos. Tambie´n evaluaron la influencia de diferentes morfologı´as craneofaciales en los trastornos temporomandibulares dolorosos. Los datos fueron analizados mediante las pruebas de Tukey-Kramer y Chi-cuadrado.

[Jime´nez et al., 2020] Implementaron a medidas de crecimiento facial, que han sido recopiladas en el estudio CES-Damasco durante ma´s de 24 an˜os, constituy´endose en uno de los estudios de crecimiento craneofacial m´as largos del mundo y el m´as largo llevado a cabo en poblaci´on de mestizos. Los resultados han permitido comprender mejor la dina´mica de crecimiento craneofacial en nin˜as y nin˜os mestizos colombianos.

[Correa Morales et al., 2016] En este libro se presenta en detalle conceptos b´asicos y la implementacio´n del uso de modelos lineales mixtos a situaciones pra´cticas y propias del quehacer cotidiano o como apoyo en la soluci´on de problemas de investigaci´on en diversas ´areas del conocimiento.

### 2.3. Modelos lineales mixtos

El nombre de modelos lineales mixtos proviene del hecho de que estos modelos son lineales en los para´metros y que las covariables o variables independientes, pueden involucrar efectos fijos y efectos aleatorios.

)⊤ al vector de respuestas del i-e´simo individuo, donde ni es el respectivo nu´mero de observaciones tomadas en dicho sujeto. El modelo lineal mixto individual est´a dado por.

Considere una muestra aleatoria de tama˜no n y denote por Yi = (Yi1,...,Yin

i

Yi = Xiβ + Zibi + εi bi ∼ N(0,D) εi ∼ N(0,Ri)

donde Xi y Zi son las matrices de dise˜no para los efectos fijos y efectos aleatorios, respectivamente y que acompa˜nan a los vectores β y bi, i = 1,...,n y bi y εi son independientes. Xi es una matriz (ni × p) de dise˜no, que representa los valores conocidos de la p covariables X(1),...,X(p), para cada uno de los ni observaciones del i-e´simo sujeto.





X1(1)i X1(2)i ··· X1(pi) X2(1)i X2(2)i ··· X2(pi)

Xi =

... . Xn(1)

 

 

. .

ii Xn(2)

ii ··· Xn(p)

ii

En un modelo que incluye un t´ermino intercepto, la primera columna ser´ıa simplemente igual

a 1 para todas las observaciones [West et al., 2014]. El vector β = (β1,β2,...,βp) es un vector de p coeficientes de regresio´n desconocidos (o para´metros de efectos fijos) asociado con las p covariables utilizadas en la construccio´n de la matriz Xi. La matriz Zi es una matriz (ni×p) de disen˜o, que representa los valores conocidos de las q covariables Z(1),...,Z(q) para el i-e´simo sujeto. Esta matriz es muy parecida a la matriz Xi en que representa los valores observados de covariables; sin embargo, generalmente tiene menos columnas que la matriz Xi.





- Z1(1)i Z1(2)i ··· Z1(qi)
- Z2(1)i Z2(2)i ··· Z2(qi)

Zi =

... . Zn(1)

 

 

. .

ii Zn(2)

ii ··· Zn(q)

ii

Las columnas en la matriz Zi representan los valores observados para las variables predictoras para el i-e´simo sujeto, que tiene efectos sobre la variable de respuesta continua que varı´a aleatoriamente entre sujetos. En muchos casos, los predictores con efectos que varı´an aleatoriamente entre sujetos esta´n representados tanto en la matriz Xi y la matriz Zi. En un modelo lineal mixto, en el que solo se supone que los interceptos varı´an aleatoriamente de sujeto a sujeto, la matriz Zi tendrı´a la primera columna de 1’s. El vector bi = (bi1,bi2,...,biq) para el i-e´simo sujeto representa un vector de orden q de efectos aleatorios asociado con las q covariables de la matriz Zi. Suponemos que los efectos de orden aleatorio en el vector bi siguen una distribucio´n normal multivariada, con vector de medias 0 y una matriz de varianzas-covarianzas denotada por D.

Los elementos a lo largo de la diagonal principal de la matriz D representan las variaciones de cada efecto aleatorio en bi y los elementos fuera de la diagonal representan las covarianzas entre dos efectos aleatorios correspondientes. Debido a que hay q efectos aleatorios en el modelo asociado con el i-e´simo sujeto, D es una matriz (q × q) es sime´trica y positiva. Los elementos de esta matriz se muestran a continuaci´on:





V ar(b1i) cov(b1i,b2i) ··· cov(b1i,bqi) cov(b1i,b2i) V ar(b2i) ··· cov(b2i,bqi)

D = V ar(bi) =

 

 

... . cov(b1i,bqi) cov(b2i,bqi) ··· V ar(bqi)

. .

Los elementos (varianzas y covarianzas) de la matriz D se definen como funciones de un conjunto pequen˜o de para´metros de covarianza almacenados en un vector denotado por θD. Finalmente, el vector εi es un vector de ni residuales con cada elemento en εi que denota el residuo asociado con una respuesta observada en t o en ni ocasiones para el i-e´simo sujeto. Debido a que algunos sujetos pueden tener m´as observaciones que otras, el vector

εi = (εi1,εi2,...,εin

) puede tener un n´umero diferente de elementos. Supo´ngase que los errores ni en el vector εi para un sujeto dado, i, son variables aleatorias que siguen una distribucio´n normal multivariada, con un vector de medias 0 y una matriz de varianzacovarianza definida positiva Ri:

i

εi ∼ N(0,Ri) Se asume que los errores asociados a diferentes sujetos son independientes entre si, y que los vectores de errores ε1,...,εm, y los efectos aleatorios b1,...,bm, son independientes el uno del otro. La forma general de la matriz Ri es:





V ar(ε1i) cov(ε1i,ε2i) ··· cov(ε1i,εin

) cov(ε1i,ε2i) V ar(ε2i) ··· cov(ε2i,εin

i

)

i

D = V ar(εi) =

 

 

... . cov(ε1i,εin

. .

) ··· V ar(εin

) cov(ε2i,εin

)

i

i

i

Los elementos (varianzas y covarianzas) de la matriz Ri se definen como funciones de otro conjunto de para´metros de covarianzas en un vector denotado por θR. Al completar la notacio´n para el modelo lineal mixto, el vector θ combina todos los para´metros de covarianza contenida en los vectores θD y θR. Estos par´ametros se conocen con el nombre t´ecnico de componentes de varianza y covarianza [Correa Morales et al., 2016].

#### 2.3.1. Estimaci´n en Modelos Lineales Mixtos

En el modelo lineal mixto, estimamos los par´ametros de efectos fijos, β, y los para´metros de covarianza, θ (i.e., θD y θR para la matriz D y Ri, respectivamente). Usualmente,esto se hace por medio de la estimaci´on de m´axima verosimilitud (MLE) y ma´xima verosimilitud restringida (REML).

#### 2.3.2. Estimaci´n de ma´xima verosimilitud (MLE)

En general, la estimacio´n de m´axima verosimilitud (MLE) es un m´etodo para obtener estimaciones de para´metros desconocidos mediante la optimizacio´n de una funci´on de verosimilitud. Para aplicar la estimacio´n de MLE, primero construimos la probabilidad como una funcio´n de los par´ametros en el modelo especificado, basado en supuestos de distribucio´n. Las estimaciones de ma´xima verosimilitud (MLEs) de los par´ametros son los valores de los argumentos que maximizan la funcio´n de probabilidad (i.e., los valores de los para´metros que hacen que los valores observados de la variable dependiente sean m´as probables, dados los supuestos de distribuci´on). Ver [Casella and Berger, 2002]. En el contexto de los LMM, construimos la funci´on de probabilidad de β y θ haciendo referencia a la distribucio´n marginal de la variable dependiente Yi. La funci´on de densidad

###### de probabilidad normal multivariada correspondiente, f(Yi|β,θ), es:

- 1

- 2

−ni

−1

(Yi − Xiβ)τVi−1(Yi − Xiβ)

2 exp −

f(Yi|β,θ) = (2π)

2 det(Vi)

Donde det se define como el determinante de la matriz y los elementos de la matriz Vi como funciones de los para´metros de covarianza en θ.

Basado en la funcio´n de densidad de probabilidad y dado los datos observados Yi = yi, la contribucio´n de la funci´on de verosimilitud para el i-e´simo sujeto se define de la siguiente manera:

Li(β,θ;yi) = (2π)

−ni

−1

2 exp −

2 det(Vi)

- 1

- 2

(yi − Xiβ)τVi−1(yi − Xiβ)

Escribimos la funci´on de verosimilitud, L(β,θ) como el producto de las n contribuciones independientes para los individuos (i = 1,...,n).

n

n

- 1

- 2

−ni

−1

(yi − Xiβ)τVi−1(yi − Xiβ) La funci´on correspondiente a la log-verosimilitud l(β,θ), se define como

2 exp −

L(β,θ) =

Li(β,θ) =

(2π)

2 det(Vi)

i=1

i=1

n

n

- 1

- 2

- 1

- 2 ×

- 1

- 2 ×

(yi −Xiβ)τVi−1(yi −Xiβ)

l(β,θ) = lnL(β,θ) = −

n×ln(2π)−

ln(det(Vi))−

i=1

i=1

n

Donde n =

ni es el nu´mero de observaciones (filas) en el conjunto de datos, y ”ln” se refiere al logaritmo natural.

i=1

#### 2.3.3. Caso especial θ es conocido

Consideramos un caso especial de estimacio´n de ML para LMM, en el que asumimos que θ, y como resultado la matriz Vi, son conocidos. Como suponemos que θ es conocido, los ´unicos para´metros que estimamos son los efectos fijos, β. La funci´on log-verosimilitud, l(β,θ), por lo tanto, se convierte en una funci´on β y su optimizaci´on es equivalente a encontrar un mı´nimo de una funcio´n objetivo q(θ)

- 1

- 2 ×

q(θ) =

i

(yi − Xiβ)τVi−1(yi − Xiβ)

Tenga en cuenta que la optimizaci´on de q(θ) con respecto a β puede llevarse a cabo aplicando el m´etodo de mı´nimos cuadrados generalizados (GLS). El valor de β se puede obtener analı´ticamente:

−1

Xiτ Vi−1yi

Xiτ Vi−1Xi

β =

i

i

β tiene la propiedad estadı´stica de ser el mejor estimador lineal insesgado BLUE [Correa Morales et al., 2016].

#### 2.3.4. Caso general θ es desconocido

Se considera la estimacio´n de ML de los par´ametros de covarianza, θ, y el valor de efectos fijo, β, suponiendo que θ es desconocido. Primero, para obtener estimaciones para los para´metros de covarianza en θ, construimos una funcio´n de log-verosimilitud lML(θ). La funcio´n lML(θ) se deriva de l(β,θ) reemplazando el para´metro β por la expresio´n que define β. La funcio´n resultante es

- 1

- 2

- 1

- 2 ×

- 1

- 2 ×

riτVi−1ri Donde,

lML(θ) = −

n × ln(2π) −

ln(det(Vi)) −

i

i



 

−1

 i

XiτVi−1Xi

XiτVi−1yi

ri = yi − Xi

i

Despue´s de las estimaciones de ML de los par´ametros de covarianza en θ (y, en consecuencia, las estimaciones de las varianzas y covarianzas en r y Ri) calculamos β. Primero, reemplazamos las matrices D y Ri por sus estimaciones de ML D y Ri, para calcular Vi, una estimaci´on de Vi

Vi = Zi DZiτ + Ri

Luego, usamos la fo´rmula generalizada de mı´nimos cuadrados para β, con Vi reemplazado por su estimacio´n para obtener β:

β =

i

Xiτ Vi−1Xi

−1

i

Xiτ Vi−1yi

Reemplazamos Vi por su estimacio´n Vi, decimos que β es el mejor estimador lineal insesgado empı´rico EBLUE de β. La varianza de β, V ar( β), es una matriz de varianza-covarianza p × p calculada de la siguiente manera:

V ar( β) =

i

XiτVi−1Xi

−1

Las estimaciones de ML de θ esta´n sesgadas porque no tienen en cuenta la p´erdida de grados de libertad que resultan de estimar los para´metros de efectos fijos en β [Verbeke, 1997]. Una forma alternativa del me´todo de ma´xima verosimilitud conocido como estimacio´n REML se usa con frecuencia para eliminar el sesgo en las estimaciones de ML de los par´ametros de covarianza. Discutimos la estimacio´n REML en la siguiente subseccio´n.

#### 2.3.5. Estimaci´n REML

La estimacio´n REML es una forma alterna de estimar los par´ametros de covarianza en θ. [Patterson and Thompson, 1971], propusieron un me´todo alternativo llamado Estimacio´n por Ma´xima Verosimilitud Restringida (REML) que tambi´en se conoce co´mo Ma´xima verosimilitud residual. Este procedimiento utiliza te´cnicas de estimaci´on por ma´xima verosimilitud a una funcio´n de verosimilitud asociada a un conjunto de errores de contraste en vez de aquella asociada a las observaciones originales. Este procedimiento compensa la p´erdida de grados de libertad que resulta de la estimaci´on de los efectos fijos en β y produce estimaciones menos sesgadas de las componentes de varianza. El asunto relacionado con este sesgo es importante cuando el nu´mero de para´metros no es pequen˜o en relacio´n al nu´mero total de observaciones [Correa Morales et al., 2016]. Las derivaciones ma´s generales de REML esta´n dadas por [Harville, 1977], [Cooper and Thompson, 1977], y [Verbyla, 1990]. Las estimaciones REML de θ se basa en la optimizaci´on de la siguiente funci´on de verosimilitud REML:

- 1

- 2 × (n − p) × ln(2π) −

1 2 ×

lREML(θ) = −

- 1

- 2 ×

−

i

ln(det(XiτVi−1Xi))

i

- 1

- 2 ×

ln(det(Vi)) −

i

riτVi−1ri

### 2.4. Modelos lineales mixtos con splines

Los modelos de regresio´n parame´trica tienen como objetivo analizar la posible relacio´n estadı´stica entre una respuesta Y y un conjunto de covariables especificadas en un vector X y parten de una funcio´n de distribuci´on conocida que facilita la estimacio´n de los par´ametros que mejor se ajustan al comportamiento de los datos. Cuando la relacio´n entre las variables es compleja o no lineal, el enfoque parame´trico no provee las herramientas para que el ajuste del modelo sea adecuado, sin embargo es posible obtener un ajuste de los datos mediante modelos polino´micos (param´etricos), puesto que a mayor grado del polinomio el ajuste de los datos mejora, no obstante tener un modelo polino´mico de grado elevado puede aumentar la complejidad del modelo, disminuir su precisi´on y dificultar su interpretacio´n, adem´as, se corre el riesgo de sobre-parametrizarlo. En estos escenarios es factible que los modelos no par´ametricos sean la mejor opci´on para dar soluci´on a esta limitante, dado que su principal ventaja es la flexibilidad que poseen para el ajuste de los datos, lo cual se debe a que la relaci´on entre las variables es determinada por los datos, mientras que en un marco parame´trico la relaci´on es definida por el modelo considerado. Actualmente existen diversos modelos de regresio´n no para´metricos que permiten modelar dos variables que presenten una relaci´on compleja o no lineal, entre los cuales est´an los m´etodos kernel, regresiones spline, regresiones spline penalizadas, entre otros [Toquica Vargas, 2017]. Estos me´todos de suavizamiento y ajuste de

datos tienen un papel importante en la actualidad [Wand and Jones, 1994]. Supongamos que disponemos de pares de datos (xi,yi), un modelo suavizado (para datos normales) vendra´ dado por:

yi = f(xi) + εi, εi ∼ N(0,σ2), donde f(·) es una funcio´n suave de los datos. Las t´ecnicas de suavizado est´an basados en splines. [Racine, 2014], define un spline como construcciones matema´ticas hechas de piezas de funciones polinomiales que se unen para formar una curva suave. Los puntos donde se unen estas piezas se denominan “nodos”. Los desafı´os en el uso de splines de suavizado son, primero, seleccionar la ubicaci´on de los nodos, y segundo, encontrar un conjunto ´optimo de polinomios para modelar la relacio´n estadı´stica [Moore, 2016]. Hay dos grandes familias dentro de los modelos de suavizado con splines:

- 1. Splines de regresio´n (regression splines). En estos modelos es necesario seleccionar el nu´mero y la localizaci´on de los nodos (para controlar la suavidad de la funci´on ajustada) e imponer restricciones para que los trozos de polinomio se unan de forma suave. Una vez hecha la elecci´on, el modelo se ajusta por mı´nimos cuadrados.
- 2. Splines de suavizado (smoothing splines). Aparecen como la solucio´n al siguiente problema de regresio´n no-param´etrica: encontrar la funcio´n que minimiza la suma de cuadrados penalizada (SCP) [Durb´an, 2009]

SCP =

n

(yi − f(xi))2 + λ

i=1

(f′′(x))2dx,

y

donde el u´ltimo te´rmino es una penalizacio´n en la segunda derivada de la curva y λ es el para´metro de suavizado que controla la suavidad de la misma, de modo que si λ = 0 estaremos sobre-ajustando los datos, y si λ → ∞ tendremos un ajuste lineal [Green and Silverman, 1993]. Los splines con penalizaciones (B-splines) combinan lo mejor de ambos enfoques: utilizan menos par´ametros que los splines de suavizado y la seleccio´n de los nodos no es tan determinante como en los splines de regresi´on, pero sı´ lo es, la eleccio´n del grado de suavizaci´on del spline. [Eilers and Marx, 1996] Por u´ltimo, la correspondencia entre los P-splines y el BLUP (Best Linear Unbiased Predictor) en un modelo mixto, permite en algunos casos, utilizar la metodologı´a existente en el campo de los modelos mixtos y el uso de software R, a trav´es de la funci´on lme() de la librerı´a lme4.

#### 2.4.1. Bases y nodos

La base para la regresio´n se puede calcular de muchas maneras, y de hecho hay dos grandes grupos dentro de los estadı´sticos que utilizan los P-splines: los que utilizan las bases polino-

mios truncados y los que utilizan las bases de B-splines [Ruppert et al., 2003].

Polinomios truncados Supongamos que tenemos pares (xi,yi), i = 1,··· ,n. Para simplificar, vamos a suponer que x esta en [0,1]. Tomamos k nodos equidistantes en ese intervalo

tj = (j−k1) j = 2,··· ,k + 1. Una base de polinomios truncados de grado p viene dada de acuerdo a la siguiente regla:

1,x,x2,··· ,xp,{(x − t1)+}p ,··· ,{(x − tk)p+}p donde x+ = max(0,x) (por eso son truncados, ya que a partir de un cierto punto valen 0). La funcio´n {(x − tk)p+}p tienen p − 1 derivadas continuas, de modo que cuanto mayor sea p, ma´s suave son las funciones en la base.

Bases de B-splines. Una B-spline de orden n es una funcio´n polinomial, continua a trozos de grado n − 1 en una variable x. Se define sobre 1 + n ubicaciones tj, llamados nodos, que deben estar en orden no descendente tj ≤ tj+1. El B-spline contribuye solo en el rango entre el primero y el ´ultimo de estos nudos y es cero en otros lugares.

#### 2.4.2. Selecci´n del par´ametro de suavizado

Una herramienta ´util en la selecci´on de modelos son los criterios de informaci´on. Los criterios de informaci´on (a veces denominados criterios de ajuste) proporcionan una forma de evaluar el ajuste de un modelo con base en la funci´on de log-verosimilitud y la complejidad a partir del nu´mero de par´ametros. Una caracterı´stica clave de los criterios de informacio´n es que proporcionan una manera de comparar cualquiera de los dos modelos ajustados al mismo conjunto de observaciones; i.e., los modelos no necesitan estar anidados. Un valor menor del criterio indica un modelo m´as recomendable.

Criterio de informacio´n de Akaike (AIC) El AIC no es una prueba de hipo´tesis sobre el ajuste del modelo, sino m´as bien un criterio parame´trico comparativo entre modelos y representa por esto una herramienta para selecci´on de modelos. Dado un conjunto de datos, es posible encontrar varios modelos que se ajustan a ellos. La idea es ranquearlos de acuerdo al AIC. Se define como:

AIC = 2k − 2logLik

, donde k es el nu´mero de para´metros estimados y logLik es una medida del ajuste del modelo. El modelo asociado al menor AIC se considera mejor entre aquellos que se ajustan. El AIC solo dice cu´al de los modelos comparados es el mejor, pero no puede decir cua´l es el mejor modelo para explicar los datos. El AIC no requiere que los modelos est´en anidados.

Criterio de informaci´on bayesiano de Schwarz (BIC) El BIC al igual que el AIC, es un criterio param´etrico para selecci´on de modelos. El BIC no requiere que los modelos este´n anidados. El modelo asociado al menor BIC se considera mejor que los otros. El BIC solo dice cu´al de los modelos comparados es el mejor, pero no puede decir cu´al es el mejor modelo para explicar los datos. Se define como:

BIC = −2logLik + k ln(n)

donde k nu´mero de para´metros estimados, n el nu´mero de observaciones que fueron usadas en el proceso de estimacio´n y logLik es una medida del ajuste del modelo. [Correa Morales et al., 2016].

Coeficiente de correlaci´on intraclase (ICC) Me´todo para evaluar la precisi´on de un modelo. Se basa en el modelo de an´alisis de la varianza con medidas repetidas o intrasujeto. Este coeficiente se puede interpretar como un coeficiente de correlaci´on como lo afirma [Bartko, 1966]

σs2 σs2 + σ,.2j

ρ

=

ICC

+ σε2 donde,

- • σs Variabilidad intersujeto (atribuible a las diferencias entre los sujetos, s)
- • σj2 Variabilidad intrasujeto (se refiere a las diferencias de las mediciones de un mismo sujeto, j).
- • σε2 Variabilidad residual (variabilidad aleatoria asociada a los errores de medicio´n, e).

R2 de Nakagawa para modelos mixtos Corresponde a los valores marginales y condicionales de R2 para los modelos mixtos [Stoffel et al., 2017]. El RGLMM2 (m) marginal representa la proporci´on de la varianza total explicada por los efectos fijos, mientras que el RGLMM2 (c) condicional es la proporcio´n de la varianza explicada por efectos fijos y aleatorios y σf2 es la varianza explicada por efectos fijos. Las varianzas de los efectos aleatorios son en realidad las varianzas medias de los efectos aleatorios, por lo que el valor de r-cuadrado tambi´en es apropiado para los modelos mixtos con pendientes aleatorias o efectos aleatorios anidados.

R2

σ2

f σ2

GLMM(m)=

α+σ2′ϵ

+σ2

f

y

###### R2

σ2 f

+σ2

α σ2

GLMM(c)=

α+σ2′ϵ

+σ2

f

σf2 = var

h

k

βhXhij

donde,

- • Xhij es el j -e´simo valor del i -´esimo individuo para el h -´esimo de k predictores de efectos fijos.
- • βh es el coeficiente de regresi´on para el h -e´simo predictor.

# 3 Modelos propuestos para las medidas craneofaciales consideradas

Esta seccio´n describe los modelos considerados para realizar el ana´lisis de cada una de las medidas craneofaciales usadas en este trabajo. Los datos para cada una de las medidas craneofaciales son de tipo longitudinal de la cohorte CES-LPH de Damasco [Jime´nez et al., 2020]. Cada nivel del factor aleatorio (individuos) es analizado y provienen de determinadas ocasiones a lo largo del tiempo. Se asume que la variable objetivo puede describirse mediante un patr´on de evolucio´n poblacional (efectos fijos) y un patr´on individualizado (efectos aleatorios). Este supuesto se puede verificar al observar los gra´ficos de perfiles de cada medida, los cuales se presentan ma´s adelante. Los modelos que se consideran son de la siguiente forma

yij = β0 + β1Ageij + β2Genderi + β3Ageij × Genderi + θ(Ageij) + f(Ageij) + εij, do´nde

yij denota la respuesta del individuo i-´esimo en el tiempo tj

El sujeto esta´ representado por i: i = 1,2,...,n

Observaciones por sujeto j: j = 1,2,...,ni

- β0 es el intercepto del modelo promedio poblacional.

- β1 es el efecto de la edad.

- β2 es el efecto del g´enero, M=hombre y F=mujer. El nivel de referencia es F.

- β3 es el efecto de la interacci´on entre edad y ge´nero.

εij son variables aleatorias independientes con εij ∼ N(0,σe2) θ(Ageij) puede tener por ejemplo, las siguientes estructuras:

θ(Ageij) = b0i intercepto aleatorio.

θ(Ageij) = b0i + b1iAgeij intercepto y pendiente aleatorios.

θ(Ageij) = b0i + b1iAgeij + b2iAge2ij intercepto, pendiente y te´rmino cuadra´tico aleatorios.

donde

- b0i ∼ N1(0,σb2

0i

) para el modelo de intercepto aleatorio,

- b1i =

- b0i
- b1i ∼ N2(0,D2×2)

para el modelo de intercepto y pendiente aleatorios,

- b2i =

  ∼ N3(0,D3×3)

 

- b0i
- b1i
- b2i

para el modelo de intercepto, pendiente y te´rmino cuadr´atico aleatorios.

Para la funci´on f(Ageij) se plantea la siguiente estructura:

M

am(Ageij − km)+,

f(Ageij) =

m=1

donde km, representa los nodos de la parte poblacional respectivamente, am (m = 1,...,M) son para´metros comunes a todos los sujetos a ser estimados con media cero y varianza σk2. De acuerdo a la estructura de θ(Ageij) se obtiene el siguiente modelo:

Modelo lineal mixto con intercepto y spline fijos y aleatorios:

yij = β0 + β1Ageij + β2Genderi + β3Ageij × Genderi +

M

M

am(Ageij − km)+ + εij,

+b0i +

m=1

β1m(Ageij − km)+

m=1

donde

am ∼ N(0,σa2) b0i ∼ N(0,σb2) εij ∼ N(0,σe2)

son los respectivos efectos aleatorios. Tambi´en, am, b0i y εij son independientes.

3.1 Modelos lineales mixtos para el a´ngulo del plano mandibular 19

### 3.1. Modelos lineales mixtos para el a´ngulo del plano mandibular

Los patrones de crecimiento craneofacial en nin˜os y ni˜nas son particularmente activos durante la primera infancia y la adolescencia do´nde se observa un alto grado de heterogeneidad en los individuos, independiente del g´enero y de la etnia. Por esto es importante entenderlos y predecirlos con un alto grado de precisio´n de manera que, por ejemplo, los ortodoncistas puedan enfocar mejor sus tratamientos de acuerdo a las caracterı´sticas particulares de los individuos. En la literatura se evidencia que los patrones de crecimiento individuales pueden ser extremadamente variables [Bishara et al., 1985]. Este hecho justifica el uso de modelos estadı´sticos que tengan en cuenta esta heterogeneidad propia de los sujetos, por ejemplo los Modelos Lineales Mixtos (LMM, siglas en ingl´es). En este sentido los modelos de regresio´n lineal mixtos son particularmente apropiados para estudiar el crecimiento craneofacial ya que ellos tienen en cuenta variabilidad intra y entre individuos [Jime´nez et al., 2020]. Adem´as, el uso y la comprensio´n de herramientas estadı´sticas para generar conocimiento de calidad con base en datos, debe ser una parte fundamental de las competencias de profesionales de las ciencias de la salud y tambi´en debe contribuir al desarrollo de las buenas pra´cticas clı´nicas. Usar modelos o instrumentos consolidados y reportados en la literatura puede ayudar a ahorrar recursos y tiempo. Sin embargo, su uso se debe hacer con cuidado, ya que estos pueden haber sido construidos con datos de otras poblaciones o con esta´ndares diferentes, que no necesariamente se acercan a la realidad de la poblaci´on donde se quieren usar. Por esto, es fundamental evaluar antes su desempen˜o para decidir si es o no satisfactorio y plausible. Por lo tanto, en este cap´ıtulo se ilustra la implementaci´on de dos modelos mixtos con caracter´ısticas muy propias al llamado ´angulo del plano mandibular (SN-MP). Entender la din´amica de SN-MP permite anticiparse a posibles problemas de maloclusio´n y enfocar de mejor manera los tratamientos de ortodoncia en la adolescencia. Especı´ficamente, se ajustan dos modelos: un modelo lineal mixto con intercepto aleatorio y otro modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios.

### 3.2. An´alisis exploratorio de datos

En general, se realiza el ana´lisis exploratorio de datos para descripci´on de los datos que se van a analizar, para descubrir patrones y tendencias que contribuyan a la elaboracio´n y visualizacio´n de modelos estadı´sticos. De este modo, se presentan los ana´lisis de los datos correspondientes a la medida de crecimiento craneofacial del a´ngulo del plano mandibular, que ha sido recopilada en el estudio CES-Damasco durante ma´s de 24 an˜os. A lo largo del documento, la medida del a´ngulo plano mandibular se representa como SN-MP.

#### 3.2.1. Poblaci´n de estudio y variables consideradas

Se hace uso de los resultados del estudio correspondiente a la medida de crecimiento craneofacial del Angulo´ del plano mandibular, datos que han sido recopilados en el estudio CES-Damasco. El estudio consta de 54 sujetos, el cual se redujo a 49, 30 nin˜as y 19 ni˜nos por abandono del estudio de 5 sujetos, cada uno de ellos con distintas cantidades de medidas repetidas, para un resultado de 449 observaciones. Se registran edades pares entre los 6 a 24 an˜os [Jime´nez et al., 2020].

|Caracterı´sticas|Mujeres n=30 (61%)| |Hombres n=19 (39%)| |
|---|---|---|---|---|
| |Media<br><br>|Desv. Est.<br><br>|Media<br><br>|Desv. Est.|
|Tiempo de seguimiento SN-MP ArGoMe AFA AFP<br><br>|16.86 2.38 32.81 5.21<br><br>123.09 5.89 112.79 9.47<br><br>71.62 7.80| |15.47 3.64 33.28 4.85<br><br>121.93 7.37 117.70 12.01<br><br>74.57 10.30| |

- Tabla 3-1: Caracterizaci´on demogr´afica y medidas craneofaciales de 49 mestizos de la cohorte CESLPH-DAMASCO

- La figura 3-1 visualiza los gra´ficos de densidad de algunas de las medidas craneofaciales de inter´es en el estudio de caracterizacio´n demogr´afica de la cohorte CESLPH-DAMASCO.

[Figure 2]

[AGE]

[Figure 3]

[Figure 4]

[SN-MP] [ArGoMe]

[Figure 5]

[Figure 6]

[AFH] [PFH]

Figura 3-1: Gr´aficos de densidad de algunas de las medidas de inter´es en el estudio de

caracterizacio´n demogr´afica de la corte CESLPH-DAMASCO.

#### 3.2.2. Angulo´ del plano mandibular

De acuerdo a Ricketts [Ricketts, 1981], es el ´angulo formado entre el plano mandibular y el plano horizontal de Frankfurt. Su valor normal es de 14 a 32º ± 4º a los 9 an˜os y disminuye 0,3º por an˜o hasta el final del crecimiento. Un valor superior al normal revela la existencia de un tramo mandibular corto, caracterı´stica del tipo dolicofacial. Un valor bajo generalmente esta´ relacionado con pacientes que presentan un buen crecimiento y corresponden al biotipo braquifacial.[Ricketts, 1981]

[Figure 7]

- Figura 3-2: Angulo´ SN-MP formado por los planos mandibular (Go-Me) y de Frankfort (Po-Or). Define el patr´n de crecimiento facial. Fuente: [Ricketts, 1981]

#### 3.2.3. An´alisis descriptivo de los datos

- La tabla 3-2 presenta un ana´lisis exploratorio de los datos involucrando medidas de resumen de la medida ´angulo plano mandibular con el fin de describir algunas caracter´ısticas relevantes asociadas al proceso.

|VARIABLES<br><br>|MUJERES n = 30 (61%)| | | |HOMBRES n = 19 (39%)| | | |
|---|---|---|---|---|---|---|---|---|
| |Media|Desv. Est.<br><br>|Mı`n.|Ma`x.<br><br>|Media<br><br>|Desv. Est.|Mı`n.|Ma`x.|
|SEGUIMIENTO<br><br>|16.86|2.38<br><br>|10.00|18.00<br><br>|15.47<br><br>|3.64|4.00|18.00|
|EVOLUCION´<br><br>|-3.93<br><br>|3.26|-9.00<br><br>|2.00<br><br>|-6.10|3.92<br><br>|-16.00|0.00|

- Tabla 3-2: Tiempo promedio de seguimiento y evolucio´n o cambio en SN-MP de la cohorte desde la lı´nea base de acuerdo al g´enero.

- La figura 3-3 correspondiente a la gr´afica de perfiles evidencia la trayectoria del crecimiento para cada uno de los sujetos de acuerdo a la edad y al g´enero, las lineas de crecimiento de los datos no son lineales, sino que presentan un crecimiento curvil´ıneo en el tiempo, con un intercepto aleatorio asociado a cada sujeto do´nde tienen un cierto grado de similitud en sus pendientes debido a que el conjunto de datos es altamente desbalanceado pues la longitud de los perfiles son distintos.

[Figure 8]

###### Figura 3-3: Gr´fica de perfiles de acuerdo al ge´nero en funci´n de la medida SN-MP. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

- La figura 3-4 muestra la descripcio´n del comportamiento longitudinal de los datos para la medida del a´ngulo del plano mandibular. Se observa, en general, como el trazado para los nin˜os es mayor que el de las nin˜as en cada uno de los boxplot generados.

[Figure 9]

Figura 3-4: Diagramas de boxplot global y longitudinales del ´ngulo del plano mandibular. Fuen-

te: Creaci´n propia y Grupo de Investigaci´n CESLPH

- La figura 3-5 muestra el boxplot longitudinal, en la lı´nea azul de promedios observados, los nin˜os entre los 6 a 16 an˜os tenı´an valores del ´angulo del plano mandibular ma´s grandes que las nin˜as. El cambio de crecimiento en ellos comenzo´ a nivelarse a edades m´as avanzadas,

pero continuo aumentando a partir de los 16 an˜os para las nin˜as como se evidencia en la linea roja de promedios observados.

[Figure 10]

- Figura 3-5: Diagrama de Boxplot longitudinal y gr´fico de lineas promedio de acuerdo a la edad y al g´enero del ´ngulo del plano mandibular. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

### 3.3. Resultados para SN-MP

En el modelo lineal mixto, a cada sujeto se le ha de registrar una medida o respuesta de inter´es que se ha de denotar como yij donde el subı´ndice i indica que se registra dicha medida al sujeto y el subı´ndice j indica que la medicio´n se hizo al tiempo j.

El primer modelo lineal mixto se puede representar matema´ticamente por medio de la siguiente ecuacio´n:

Yij = β0 + β1Genderi + β2Ageij + β3Genderi ∗ Ageij + bi0 + εij, donde

El sub´ındice i = 1,2,...,n representa cada uno de los sujetos considerados mientras que el subı´ndice j = 1,2,...,ni indica las observaciones intra sujeto.

#### 3.3.1. Interpretaci´n de los resultados

La tabla 3-3, presenta los coeficientes de regresi´on estimados para los efectos fijos y los errores para la medida del a´ngulo del plano mandibular.

Intercepto estimado βˆ0 =36.029 indica el promedio de la medida del ´angulo del plano mandibular.

- La estimacio´n βˆ1 correspondiente al efecto ge´nero masculino Gender : M = 2.926 significa que la medida del ´angulo del plano mandibular es mayor en hombres que en mujeres por esta raz´on se evidencia un valor positivo.
- La estimacio´n βˆ2 correspondiente al efecto de la edad. El a´ngulo del plano mandibular tiende a disminuir su valor dado el signo de la estimaci´on es negativo, AGE = -0.224. Esta medida disminuye 0.3◦ cada an˜o hasta el final del crecimiento [Ricketts, 1981]. Un ´angulo mayor implica que una mordida abierta puede ser debida a caracterı´sticas de la mandı´bula [Cubillo and Smith, 2006].

Para´metro Estimacio´n SE T P-Valor β0 36.029 0.878 41.034 <0.001 βGENDER 2.926 1.412 2.070 0.043 βAGE -0.224 0.016 -13.731 <0.001 βGENDER∗AGE -0.186 0.027 -6.747 <0.001 V (b0i) 20.153 V (εij) 2.289

Tabla 3-3: Coeficientes de regresio´n estimados (efectos fijos) y errores esta´ndar y componentes de varianza para el modelo del a´ngulo del plano mandibular

A partir del modelo anterior se construyo´ un segundo modelo:

Modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios. En los modelos ajustados, se har´a uso de la siguiente funcio´n:

f(x) = (x − k)+ f(x) =

x − k, si x > k 0 si x < k

El modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios se caracteriza por tener dos nodos correspondiente a la edad de 16 y 22 (estos nodos se seleccionaron de manera arbitraria a partir de la visualizaci´on de las curvas promedio). De este modo, el modelo es:

Yij = β0 + β1Genderi + β2Ageij + β3Genderi ∗ Ageij + β4(Ageij − 16)+

+β5(Ageij − 22)+ + bi0 + a1(Ageij − 16)+ + a2(Ageij − 22)+ + εij,

donde

Los sujetos esta´n representados por i: i = 1,2,...,N.

Observaciones para el sujeto j: j = 1,2,...,ni

b0i ∼ N(0,σb2). εij ∼ N(0,σe2). bi0 indep de εij

- La tabla 3-4, muestra las estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio y splines fijos y aleatorios para la medida del ´angulo del plano mandibular. Por consiguiente, se tienen los resultados correspondientes a los valores de las componentes de varianza de los efectos fijos, Las funciones lineales truncadas para el modelo spline lineal

denotadas por β4, β5, β6 y β7, el valor de las varianzas y la correlacio´n. Una caracter´ıstica de este modelo es que permite que las salidas especı´ficas del sujeto sean funciones no lineales del tiempo.

Para´metro Estimacio´n SE T P-Valor β0 36.944 0.880 41.941 <0.001 βGENDER(M) 2.661 1.394 1.908 0.062 βAGE -0.314 0.025 -12.308 <0.001 βGENDER∗AGE -0.162 0.032 -4.955 <0.001

- β4 0.256 0.134 1.909 0.056
- β5 -0.136 0.229 -0.596 0.551
- β6 0.089 0.249 0.356 0.721
- β7 -0.001 0.268 -0.005 0.995 σbf 0.050

σb

###### 20.153 σε

0i

1.640 Corr(b0i,b1i) -0.327

ij

- Tabla 3-4: Estimaciones de m´axima verosimilitud para el modelo mixto con intercepto aleatorio y funciones spline para la medida del ´angulo del plano mandibular

- La figura 3-6, muestra los gra´ficos correspondientes a los dos modelos ajustados. De acuerdo a los resultados de los modelos se observa una leve mejora del comportamiento de los datos con el modelo ajustado de intercepto aleatorio y funciones spline.

[Figure 11]

Figura 3-6: Gr´fico de lineas del modelo con intercepto aleatorio (izq.) versus el modelo ajustado de intercepto aleatorio y funciones splines (der.). Lı´nea punteada corresponde a los valores observados y la lı´nea s´lida corresponde a los modelos ajustados por g´enero. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

###### La figura 3-7, muestra el comportamiento de cuatro sujetos al ajustar el nuevo modelo aplicando splines con nodos entre los 16 y 22 an˜os de edad. Resaltar que se tiene un mejor ajuste basado en lo que se observa en la gra´fica respecto a los datos observados. Por lo tanto, se argumenta que nuestro modelo podrı´a ser u´til para realizar prono´stico a largo plazo, lo cual no es conveniente ni plausible con el modelo anterior.

[Figure 12]

- Figura 3-7: Perfiles observados y predichos del ´ngulo del plano mandibular basado en splines de 4 individuos de ambos g´eneros. Las lı´neas s´lidas corresponden al modelo individual ajustado y las lı´neas punteadas corresponden a las observaciones del sujeto. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

### 3.4. Evaluaci´n de la precisi´n de los modelos ajustados

En esta seccio´n se presentan dos me´todos para medir la precisi´on del modelo lineal mixto. Se muestran los modelos ajustados que se obtuvieron para explicar el a´ngulo del plano mandibular, en funci´on de la variable edad (Age) y g´enero (Gender).

De acuerdo al Criterio de informacio´n de Akaike se observa, con base en los resultados de la tabla 3-5 que el modelo 2 (el que esta´ basado en splines) es el ma´s adecuado de los dos.

Modelo DF AIC BIC Mod1 6 1875.04 1899.68 Mod2 11 1816.41 1861.59

- Tabla 3-5: Valores para la seleccio´n de modelo basados en el AIC y BIC respectivamente

De la tabla 3-6, se ha de determinar cu´al de los dos modelos ajustados tiene mejor poder predictivo. De acuerdo al ICC se concluye que el proceso de estimaci´on para los dos modelos ajustados fueron de excelente fiabilidad.

###### 3.5 Discusi´on 29

Modelo ICC Mod1 0.95 Mod2 0.95

Tabla 3-6: Criterios para la seleccio´n de modelo mediante el coeficiente de correlaci´on in-

traclase (ICC)

La tabla 3-7 muestra los resultados de RGLMM2 propuesto por Nakagawa’s, donde representa la proporci´on de la varianza total explicada por los efectos fijos .

##### Modelo R2GLMM Mod1 0.912 Mod2 0.935

Tabla 3-7: R2 de Nakagawa para modelos mixtos

### 3.5. Discusi´n

En este capı´tulo se mostraron caracter´ısticas importantes y muy propias al llamado a´ngulo del plano mandibular. Se evidenci´o una alta variabilidad en los datos. Se plantearon dos tipos de modelos lineales mixtos, un primer modelo, modelo lineal mixto con intercepto aleatorio y un segundo modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios. Se establecieron m´etodos que pueden resultar ´utiles para decantarse por uno u otro modelo, partiendo de m´etodos de precisio´n dentro del modelo lineal mixto con el fin de reconocer el modelo con mejor fiabilidad y plausibilidad. De ahı´, que el segundo modelo result´o siendo el modelo con mejor desempe˜no.

# 4 Angulo´ Goniaco (ArGoMe)

Para la medida ´angulo goniaco (ArGoMe) se tiene el mismo nu´mero de individuos, respectivamente. Es decir, 49 individuos, 30 ni˜nas y 19 nin˜os do´nde cada sujeto tiene distintas cantidades de medidas repetidas, para un resultado de 449 observaciones. Los sujetos no son necesariamente observados ni al mismo tiempo ni el mismo nu´mero de veces (datos no balanceados). El objetivo principal de este capı´tulo es comparar los resultados de dos modelos, un primer modelo lineal mixto con intercepto aleatorio y un segundo modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios para caracterizar los cambios en la respuesta a lo largo del tiempo.

### 4.1. Puntos de referencia ´angulo goniaco (ArGoMe)

Este a´ngulo representa la morfologı´a mandibular al describir la forma en que la rama y el cuerpo mandibular se relacionan entre sı´. Esta´ representado por la uni´on de la tangente al borde posterior de la rama y el plano mandibular, a trave´s de la uni´on de los puntos Ar, Go y Me. [Ramos-Montiel, 2019]

Punto Articular (Ar): Es un punto que se forma por la intersecci´on del borde posterior de la rama con la ap´ofisis basilar del occipital.

Punto Gonion (Gn): Se forma por la interseccio´n de dos planos imaginarios: plano ramal(borde posterior de la rama) y el mandibular (borde inferior del cuerpo mandibular).

Punto Menton (Me): Es la unio´n del borde inferior de la sı´nfisis con el borde inferior del cuerpo mandibular.

[Figure 13]

- Figura 4-1: La distancia desde los puntos Gonion (Gn), Gonion (Gn) y Menton (Me) representan la magnitud del Angulo´ Goniaco (ArGoMe).

4.2 An´alisis descriptivo de los datos 31

### 4.2. An´alisis descriptivo de los datos

El An´alisis descriptivo para la medida ´angulo goniaco, se basa en medidas num´ericas de acuerdo al tiempo (media, mediana, desviaci´on esta´ndar), gra´ficos de lı´neas y boxplots. Este tipo de an´alisis es implementado en R usando distintas funciones como se ilustra a continuaci´on:

La tabla 4-1 muestra una descripcio´n estadı´stica de los datos correspondientes al a´ngulo goniaco, este tipo de ejercicio proporciona un enfoque por el que se elabora un resumen de informacio´n que dan los datos de una muestra.

|VARIABLES<br><br>|MUJERES n = 30 (61%)<br><br>| | | |HOMBRES n = 19 (39%)| | | |
|---|---|---|---|---|---|---|---|---|
| |Media|Desv. Est.<br><br>|Mı`n.|Ma`x.<br><br>|Media|Desv. Est.<br><br>|Mı`n.|Ma`x.|
|SEGUIMIENTO|16.86|2.38<br><br>|10.00|18.00|15.47<br><br>|3.64|4.00|18.00|
|EVOLUCION´<br><br>|-6.83<br><br>|4.96|-17.00<br><br>|1.00<br><br>|-6.10|6.79<br><br>|-30.00|0.00|

Tabla 4-1: Tiempo promedio de seguimiento y evolucio´n o cambio en ArGoMe de la cohorte

desde la lı´nea base de acuerdo al g´enero.

La figura 4-2 muestra el gra´fico de perfiles para la medida del a´ngulo Gonion (ArGoMe). Se observa un decrecimiento no lineal a lo largo del tiempo con un intercepto aleatorio (parece que cada sujeto tiene su propio intercepto y su propia pendiente).

[Figure 14]

Figura 4-2: Gr´afica de perfiles de acuerdo a la edad y al g´enero en funci´on de la medida del a´ngulo goniaco (ArGoMe). Fuente: Creaci´on propia y Grupo de Investigaci´on CESLPH

###### La figura 4-3 muestran tres gr´aficos u´tiles para chequear la descripci´on del comportamiento longitudinal de los datos a nivel global para el ´angulo goniaco. En los gra´ficos se observan como las mujeres presentan mayor promedio que los hombres a lo largo del tiempo.

[Figure 15]

- Figura 4-3: Diagramas de boxplot global y longitudinales del ´ngulo Goniaco (ArGoMe). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

###### La figura 4-4 muestra el gra´fico boxplot y el crecimiento por ge´nero con el gra´fico de perfiles a lo largo del tiempo. La figura permite ver como antes de los 12 an˜os las lineas promedios para ambos ge´neros esta nivelada. A partir, de esta edad se observa un decrecimiento en la medida del a´ngulo goniaco en los ni˜nos (lı´nea azul) con respecto a las ni˜nas.

[Figure 16]

- Figura 4-4: Diagrama de Boxplot longitudinal y gr´fico de lineas promedio de acuerdo a la edad y al g´enero del ´ngulo goniaco (ArGoMe). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

### 4.3. Resultados para ArGoMe

Para llevar a cabo el desarrollo de esta seccio´n se hizo uso de los datos para la medida de crecimiento craneofacial a´ngulo goniaco (ArGoMe) con una muestra de 30 nin˜as y 19 nin˜os entre los 6 y 24 a˜nos. Se asume que Yij es la variable respuesta dada para la medida del crecimiento a´ngulo goniaco para i-´esimo sujeto (i = 1,...,N) en el tiempo j-e´simo (j = 1,...,ni). Se ajustan dos modelos:

Un primer modelo, modelo lineal mixto con intercepto aleatorio.

Yij = β0 + β1Genderi + β2Ageij + β3Genderi ∗ Ageij + bi0 + εij El subı´ndice i = 1,2,...,N es el valor que representa cada uno de los sujetos considerados mientras que el subı´ndice j = 1,2,...,ni indica las observaciones.

La tabla 4-2, muestra los coeficientes de regresio´n estimados para los efectos fijos y los errores esta´ndar para los datos de la medida a´ngulo goniaco (ArGoMe). Interpretacio´n de los para´metro del modelo de acuerdo a los resultados de la tabla 4-2:

Intercepto estimado βˆ0 =128.773 muestra el promedio para la medida del a´ngulo goniaco. Su valor promedio es menor a 130◦, de este modo el valor dado es un valor promedio admisible. Un a´ngulo aumentado da se˜nal de un menor desarrollo de la rama mandibular en relacio´n al cuerpo, caracterı´stico de los pacientes dolicofaciales (cara alargada, arcadas dentarias angostas) y por el contrario un a´ngulo disminuido es t´ıpico de los individuos braquifaciales (mand´ıbulas con ramas potentes, caras anchas, arcadas dentarias bien desarrolladas, existe un mayor desarrollo muscular, direccio´n de crecimiento horizontal), en los cuales se encuentra una equivalencia entre el cuerpo y la rama mandibular.

- La estimacio´n βˆ1= 2.787 hace referencia al efecto del g´enero masculino muestra que la medida del ´angulo ArGoMe tiende a ser mayor en hombres que en las mujeres, ya que se evidencia un valor positivo.

- La estimacio´n βˆ2 correspondiente al efecto de que la edad tiende a disminuir en 0.394 por cada incremento de un an˜o.

Para´metro Estimacio´n SE T P-Valor β0 128.773 1.079 119.304 <0.001 βGENDER 2.787 1.738 1.603 0.115 βAGE -0.394 0.024 -16.353 <0.001 βGENDER∗AGE -0.315 0.040 -7.731 <0.001 V (b0i) 30.496 V (εij) 4.992

Tabla 4-2: Coeficientes de regresio´n estimados (efectos fijos) y errores esta´ndar y compo-

nentes de varianza para los datos del a´ngulo goniaco

El segundo modelo, modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios.

Se definen dos nodos correspondiente a la edad de 16 y 22, de manera que:

Yij = β0 + β1Genderi + β2Ageij + β3Genderi ∗ Ageij + β4(Ageij − 16)+

+β5(Ageij − 22)+ + bi0 + a1(Ageij − 16)+ + a2(Ageij − 22)+ + εij donde

Los sujetos esta´n representados por i: i = 1,2,...,n.

Observaciones para el sujeto j: j = 1,2,...,ni

b0i ∼ N(0,σb2). εij ∼ N(0,σe2). bi0 indep de εij

- La tabla 4-3, muestra las estimaciones de ma´xima verosimilitud para el modelo mixto con intercepto aleatorio y splines fijos y aleatorios para la medida a´ngulo goniaco. Se presentan los valores de las componentes de varianza correspondientes a los efectos fijos, funciones

lineales truncadas para el modelo spline lineal denotadas por β4, β5, β6 y β7, el valor de las varianzas y finalmente la correlaci´on.

Para´metro Estimacio´n SE T P-Valor β0 130.002 1.064 122.09 <0.001 βGENDER(M) 2.733 1.682 1.625 0.110 βAGE -0.313 0.025 -12.308 <0.001 βGENDER∗AGE -0.312 0.047 -6.605 <0.001

- β4 0.152 0.187 0.809 0.418
- β5 0.317 0.317 1.001 0.317
- β6 -0.154 0.347 -0.445 0.656
- β7 -0.073 0.372 -0.197 0.843 σbf 0.144

σb

###### 28.190 σε

0i

3.109 Corr(b0i,b1i) -0.376

ij

- Tabla 4-3: Estimaciones de m´axima verosimilitud para el modelo mixto con intercepto aleatorio y splines fijos y aleatorios para la medida a´ngulo goniaco

- La figura 4-5, muestra los gra´ficos correspondientes al modelo ajustado con intercepto aleatorio y al modelo con intercepto aleatorio y funciones spline. De acuerdo a los resultados de los dos modelos ajustados, se deduce que el segundo modelo sirve para realizar prono´stico a largo plazo mientras que el primer modelo no, ya que es lineal en todo el rango admisible de valores. Por lo tanto, el segundo modelo demuestra tener una estructura plausible y adecuada que permite hacer del modelamiento de los datos de la mejor manera posible.

[Figure 17]

Figura 4-5: Gr´fico de lineas para la medida del ´ngulo gonion (ArGoMe) del modelo con intercepto aleatorio (izq.) versus el modelo ajustado de intercepto aleatorio y funciones splines (der.). Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

###### La figura 4-6, al aplicar el segundo modelo a cuatro sujetos, con splines en los nodos entre 16 y 22 an˜os de edad. Se evidencia la gr´afica con el mejor ajuste respecto a los datos observados.

[Figure 18]

Figura 4-6: Perfiles observados y predichos del angulo del ´ngulo goniaco (ArGoMe) basado en splines de 4 individuos de ambos g´eneros. Las lı´neas s´lidas corresponden al modelo individual ajustado y las lı´neas punteadas corresponden a las observaciones del sujeto. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

### 4.4. Evaluaci´n de la precisi´n de los modelos ajustados

En esta parte del capı´tulo se tiene en cuenta los dos me´todos para medir la precisi´on de los modelos ajustados que se obtuvieron para explicar el a´ngulo goniaco, en funci´on de las variables edad (Age) y ge´nero (Gender).

La tabla 4-4, indica la comparacio´n de los resultados de acuerdo al Criterio de informacio´n Akaike con el BIC. Ası´ se observa, al segundo modelo como el modelo ma´s recomendable por presentar un menor valor AIC y BIC para la medida del ´angulo goniaco

Modelo DF AIC BIC Mod1 6 2205.35 2229.99 Mod2 11 2105.20 2150.37

Tabla 4-4: Criterios para la selecci´on del mejor modelo.

De acuerdo a la tabla 4-5, mediante la f´ormula del coeficiente de correlaci´on intraclase (ICC), se puede decidir que el proceso de estimaci´on de los dos modelos ajustados son relevantes.

Modelo ICC Mod1 0.93 Mod2 0.95

Tabla 4-5: Criterios para la seleccio´n de modelo mediante el coeficiente de correlaci´on in-

traclase (ICC)

- La tabla 4-6 presenta el resultado de RGLMM2 de la medida craneofacial ArGoMe propuestos por Nakagawa’s, allı´ se obtiene la varianza explicada tanto por factores fijos como aleatorios (es decir, para todo el modelo).

Modelo R2GLMM Mod1 0.888 Mod2 0.927

Tabla 4-6: R2 de Nakagawa para modelos mixtos

### 4.5. Discusi´n

En este apartado, correspondiente al a´ngulo goniaco se evidenciaron caracterı´sticas importantes entre ellas una alta variabilidad en los datos, similar a las dem´as medidas, la longitud

4.5 Discusi´on 37

de cada uno de los sujetos por ser distintos implic´o mucho desbalance en ellos, motivo por el cual se determina que no existe una tendencia lineal sino curvilı´nea, se presentan estrategias de modelamiento basadas en estadı´sticas de resumen, se discutieron dos modelos. Un primer modelo, modelo lineal mixto con intercepto aleatorio y un segundo modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios. Se establecen m´etodos que pueden resultar u´tiles para decantarse por uno u otro modelo, partiendo de m´etodos de precisio´n dentro del modelo lineal mixto con el fin de reconocer el modelo con mejor ajuste y plausibilidad. Finalmente, se llega a la conclusio´n que el segundo modelo resulta ser el modelo con el mejor desempen˜o para futuras predicciones.

# 5 Modelos lineales mixtos para la altura facial anterior

Con el transcurrir del tiempo, se ha demostrado que los polinomios de segundo orden con coeficientes aleatorios tienen un muy buen desempen˜o para la modelacio´n de datos de crecimiento craneofacial. Motivo por el cual en este capı´tulo se busca poder divulgar los resultados obtenidos de la implementaci´on de dos modelos a la medida de crecimiento craneofacial conocida como altura facial anterior. En particular, se han de ajustar dos modelos: un modelo basado en polinomios de segundo orden con coeficientes aleatorios y un segundo modelo basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. Se ha de justificar cual de los dos modelos anteriormente mencionados ha de generar resultados o´ptimos a largo plazo.

### 5.1. Altura Facial Anterior (AFH)

Altura Facial Anterior (AFH): est´a formada por la uni´on de Nasion (Na) y Menton (Me).

Punto Nasion (N): Es el punto ma´s anterior de la sutura fronto-nasal, ubicado sobre el planosagital medio.[Faraway, 2016]

Punto Menton (Me): Es la unio´n del borde inferior de la sı´nfisis con el borde inferior del cuerpo mandibular. [Cubillo and Smith, 2006]

[Figure 19]

Figura 5-1: Puntos de referencia cefalom´etricas y trazado cefalom´etrico altura facial anterior

(AFH). Fuente: [Lee et al., 2021]

### 5.2. An´alisis exploratorio de datos

Se presentan los resultados de los datos correspondientes a una medida de crecimiento craneofacial llamada altura facial anterior (AFH). Los datos constan de 49 individuos, 30 ni˜nas y 19 nin˜os con distintas cantidades de medidas repetidas por sujeto, para un resultado de 449 observaciones. La medida craneofacial altura facial anterior se registra en edades pares entre los 6 a 24 an˜os, agregando a lo anterior. El an´alisis de los datos esta´ basado en estadı´sticos de resumen y gr´aficos para datos longitudinales que han sido realizados con el software RStudio. La tabla 5-1 observando la tabla vemos, para la medida altura facial anterior el valor promedio para los nin˜os (27.89) es superior que la que le corresponde a las nin˜as (20.50). Ası´ mismo la evolucio´n para la medida es superior en los nin˜os alcanzando un valor ma´ximo de 43.00. Finalmente, los nin˜os tuvieron mayores aumentos tanto en el seguimiento como en la evolucio´n que las nin˜as.

|VARIABLES|MUJERES n = 30 (61%)| | | |HOMBRES n = 19 (39%)| | | |
|---|---|---|---|---|---|---|---|---|
| |Media|Desv. Est.<br><br>|Mı`n.|Ma`x.<br><br>|Media<br><br>|Desv. Est.|Mı`n.|Ma`x.|
|SEGUIMIENTO<br><br>|16.86<br><br>|2.38|10.00<br><br>|18.00<br><br>|15.47<br><br>|3.64|4.00<br><br>|18.00|
|EVOLUCION´|20.50<br><br>|3.54|13.00<br><br>|28.00<br><br>|27.89|6.23<br><br>|12.00<br><br>|43.00|

Tabla 5-1: Tiempo promedio de seguimiento y evolucio´n o cambio en AFH de la cohorte

desde la lı´nea base de acuerdo al g´enero.

En la figura 5-2, se encuentran todos los perfiles para la medida de AFH, entre hombres y

mujeres y las edades que fueron registradas para cada uno de los sujetos. Se muestra co´mo la trayectoria de crecimiento de cada uno de los sujetos no siguen una linea recta, algunos var´ıan alrededor de la curva promedio lo que permite evidenciar un alto grado de heterogeneidad. Sin embargo, se puede observar que sus pendientes parecen tener la misma tendencia.

[Figure 20]

- Figura 5-2: Gr´afica de perfiles de acuerdo a la edad y al ge´nero en funci´on de la medida de la medida altura facial Anterior (AFH). Fuente: Creaci´on propia y Grupo de Investigaci´on CESLPH

- La figura 5-3 muestra el diagrama de boxplot d´onde se ignora la longitudinalidad. Allı´ se ilustra como el promedio global de la medida correspondiente a la altura facial anterior tiende a ser mayor en los hombres que en las mujeres.

[Figure 21]

- Figura 5-3: Diagrama de Boxplot global que ignora la longitudinalidad de acuerdo al g´enero de la altura facial anterior (AFH). Fuente: Creaci´on propia y Grupo de Investigacio´n CESLPH

###### La figura 5-4 muestra la descripci´on del comportamiento longitudinal de la medida altura facial anterior (AFH). La figura evidencia en los nin˜os un mayor promedio a partir de los 18 an˜os que las ni˜nas. Es decir, con el transcurrir de los a˜nos el promedio tiende a incrementar. De este modo, hombres y mujeres evolucionan de manera creciente a trave´s del tiempo hasta lograr estabilizarse.

[Figure 22]

Figura 5-4: Diagramas de boxplot global y longitudinales de la medida altura facial anterior

(AFH). Fuente: Creacio´n propia y Grupo de Investigaci´on CESLPH

###### La figura 5-5 muestra el gra´fico boxplot y el crecimiento de acuerdo al ge´nero con el gra´fico de perfiles a trav´es del tiempo. La figura evidencia como las lineas promedios para ambos ge´neros tienden a crecer con el pasar de los an˜os. Sin embargo la tasa de crecimiento en las nin˜as es m´as lenta comparada con la tasa de crecimiento de los nin˜os. Luego se determina que este comportamiento es biolo´gicamente plausible.

[Figure 23]

- Figura 5-5: Diagrama de Boxplot longitudinal y gra´fico de lineas promedio de acuerdo a la edad y al g´enero de la medida altura facial anterior (AFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH

### 5.3. Resultados AFH

El modelo lineal mixto ajustado se basa en un polinomio de segundo orden con coeficientes aleatorios donde Yi son las observaciones del sujeto i. El subı´ndice i = 1,2,...,49 representa el vector de observaciones considerados mientras que el subı´ndice j = 1,2,...,ni indica las observaciones repetidas para cada individuo. Se tiene que:

Modelo basado en polinomios de segundo orden con coeficientes aleatorios.

Yij = β0 +β1Genderi +β2Ageij +β3Age2ij +β4Genderi ∗Ageij +b0i +b1iAgeij +b2iAge2ij +ϵij donde,

Yij Altura facial anterior del i − esimo´ sujeto en la j − esima´ observaci´on.

Xij Edad del i − esimo´ sujeto en la j − esima´ observaci´on.

Xij2 Edad al cuadrado del i − esimo´ sujeto en la j − esima´ observaci´on.

bi vector de efectos aleatorios, el cual varı´a independientemente entre observaciones, con bi ∼ N3(0,Σi)

ϵij errores que varı´an independientemente entre los sujetos. (dentro de una misma observaci´on), con ϵij ∼ N(0,σϵ2)

###### Consideremos los resultados de la tabla 5-2, donde se muestra el modelo de efectos fijos con interaccio´n para la medida de crecimiento craneofacial AFH.

Para´metro Estimaci´on SE T P-Valor β0 81.262 1.047 77.593 <0.001

- β1GENDER : M -0.452 1.663 -0.271 0.786
- β2AGE 3.230 0.110 29.219 <0.001
- β3AGE2 -0.067 0.003 -18.934 <0.001 β4(GENDER)M : AGE 0.596 0.090 6.563 <0.001

- V (b0i) 17.003
- V (b1i) 0.145
- V (b2i) 1.609 V (εij) 2.929

Tabla 5-2: Coeficientes de regresio´n estimados (efectos fijos) y errores esta´ndar y componentes de varianza para los datos de la altura facial anterior (AFH)

Sea yij=AFHij donde,

yij = 81.262 − 0.452Genderi + 3.230Ageij − 0.07Age2ij + 0.596Genderi × Ageij Si Gender=0 (Femenino), el modelo queda: yij = 81.262 + 3.230Ageij − 0.07Age2ij Si Gender =1 (Masculino), el modelo queda: yij = 81.262 − 0.452 + (3.230 + 0.596)Ageij − 0.07Age2ij

= 80.809 + 3.827Ageij − 0.07Age2ij

Como la pendiente para hombres es mayor que para mujeres, la curva estar´a por encima de la de mujeres, pues

3.827 > 3.230 El segundo modelo considerado corresponde al:

Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline.

Un modelo de regresio´n spline consiste en un ajuste por partes, donde cada una de ellas es una regio´n del campo de variacio´n de la variable explicativa en la que se ajusta un modelo de regresio´n polino´mica (en general de bajo orden) y que est´an unidos en los extremos (“nodos”) para dar continuidad a la curva [Isern and Cuesta, 2013]. La expresio´n del modelo spline resulta:

Yi = f(xi) + ϵi = β0 + β1xi +

k

β1k(xi − Nk)+ + ϵi

k=1

donde las expresiones de la forma (xi−Nk)+ se conocen como funciones de “bases truncadas”; las mismas toman el valor (xi−Nk)+ si xi > Nk y cero en otro caso.[Isern and Cuesta, 2013].

La selecci´on de la cantidad y ubicacio´n de los nodos es una problema´tica que ha sido ampliamente abordada por diversos autores como [Wu and Zhang, 2006] quienes han sugerido que puede resolverse a trave´s del conocimiento profundo de los datos o bien recurriendo a alguna forma de selecci´on automa´tica de los mismos. Un buen ajuste depende en gran medida de la ubicacio´n de los nodos ma´s que de su cantidad.

Para simplificar se establece un segundo modelo lineal mixto basados en polinomios de segundo orden con coeficientes aleatorios y funciones splines para la medida altura facial anterior (AFH); el modelo se presenta a continuaci´on:

Yij = β0 + β1Genderi + β2Ageij + β3Age2ij + β4Genderi ∗ Ageij + b0i + b1iAgeij + b2iAge2ij

+ai(Ageij − 12)+ + a2(Ageij − 15)+ + a3(Ageij − 18)+ + a4(Ageij − 20)+ + ϵij

De acuerdo a lo anterior el modelo se caracteriza por tener cuatro nodos (m=4) donde los cambios en las pendientes se dan en las edades de 12, 15, 18 y 22, allı´se concentrara el ajuste generando por cuatro (4) funciones truncadas y obteniendo los par´ametros fijos y aleatorios.

- La tabla 5-3 muestra las estimaciones para el modelo basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline para la medida altura facial anterior. Por consiguiente, se tienen los resultados.

Para´metro Estimaci´on SE T P-Valor β0 87.784 2.154 40.739 <0.001

- β1GENDER(M) -1.595 1.664 -0.958 0.342
- β2AGE 2.128 0.447 4.750 <0.001
- β3AGE2 -0.018 0.024 -0.758 0.448 β3(GENDER)M : AGE 0.410 0.097 4.200 <0.001
- β4 0.404 0.295 1.370 0.171
- β5 -0.584 0.346 -1.684 0.093
- β6 -0.738 0.376 -1.961 0.050
- β7 -0.258 0.256 -1.009 0.313 σbf 0.075

σb

- 0i 26.965 σb
- 1i 0.070 σε

0.000

ij

- Corr(b0i,b1i) -0.888
- Corr(b0i,b2i) 0.865 Corr(b1i,b2i) -0.003 V (εij) 2.073

Tabla 5-3: Estimaciones de m´axima verosimilitud para el modelo mixto con intercepto alea-

torio y splines fijos para la medida altura facial anterior (AFH).

Sea yij=AFHij donde,

yij = 87.784 − 1.595Genderi + 2.128Ageij − 0.018Age2ij + 0.410Genderi × Ageij

Si Gender = 0 (Femenino), el modelo queda:

yij = 87.784 + 2.128Ageij − 0.018Age2ij

Si Gender =1 (Masculino), el modelo queda:

yij = 87.784 − 1.595 + (2.128 + 0.410)Ageij − 0.018Age2ij

= 86.189 + 2.538Ageij − 0.018Age2ij

Como la pendiente para hombres es mayor que para mujeres, la curva estar´a por encima de la de mujeres, pues

2.538 > 2.128

La figura 5-6, se observan los gr´aficos correspondientes a los modelos ajustados con intercepto, pendiente y te´rmino cuadra´tico aleatorio y al modelo ajustado con intercepto, pendiente y t´ermino cuadra´tico aleatorio y funciones spline.

[Figure 24]

###### Figura 5-6: Modelos ajustados con intercepto, pendiente y t´ermino cuadr´tico aleatorio y modelo ajustado con intercepto, pendiente y t´ermino cuadr´tico aleatorio y funciones spline. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

La figura 5-7, muestra al mejor modelo aplicando Splines con los nodos entre 12, 15 , 18 y 20 an˜os a cuatro sujetos para ambos ge´neros. Se evidencia el buen ajuste del modelo basados en splines. Por lo tanto se concluye que el modelo propuesto con splines es mucho ma´s recomendable al momento de realizar predicciones.

[Figure 25]

###### Figura 5-7: Perfiles observados y predichos de la altura facial anterior (AFH) basado en splines de 4 individuos de ambos g´eneros. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

5.4 Evaluacio´n de precisio´n de los modelos ajustados 47

### 5.4. Evaluaci´n de precisi´n de los modelos ajustados

En esta parte del capı´tulo se ha de mostrar dos formas para medir la precisi´on del modelo lineal mixto. Los resultados de los modelos ajustados han de explicar la medida de la altura facial anterior, en funcio´n de la variable edad (Age) y g´enero (Gender).

El criterio de informacio´n de Akaike y el BIC, la tabla 5-4 permiten seleccionar al modelo cuyo valor del criterio de informacio´n sea m´as pequen˜o. De acuerdo a los resultados presentados se recomienda al segundo modelo, modelo lineal mixto con intercepto, pendiente, t´ermino cuadra´tico aleatorio y funciones spline.

Modelo DF AIC BIC Mod1 8 2107.25 2156.53 Mod2 12 2048.27 2118.09

- Tabla 5-4: Criterios para la seleccio´n de modelo mediante el Criterio de informacio´n de Akaike y BIC

Ası´ mismo, mediante el coeficiente de correlacio´n intraclase (ICC) se determina cu´al de los dos modelos ajustados pronostica mejor. De acuerdo a los resultados arrojados de la tabla 5-5, se concluye que el proceso de estimacio´n que mejor pronostica es el modelo 1.

Modelo ICC Mod1 0.95 Mod2 0.79

- Tabla 5-5: Criterios para la seleccio´n de modelo mediante el coeficiente de correlaci´on intraclase (ICC)

La tabla 5-6 muestra los resultados de RGLMM2 , para la medida craneofacial altura facial anterior (AFH) propuestos por Nakagawa’s.

##### Modelo R2GLMM Mod1 0.975 Mod2 0.982

Tabla 5-6: R2 de Nakagawa para modelos mixtos

### 5.5. Discusi´n

En esta parte del capı´tulo se describe el comportamiento de los datos de la altura facial anterior a trave´s del tiempo. Se evidenci´o gran inestabilidad en los datos, se presentan estrategias de modelamiento basadas en dos modelos. Un primer modelo, modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios. y un segundo Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. Finalmente, se verifica el mejor ajuste mediante m´etodos de precisi´on aplicados en los modelos lineales mixtos. De acuerdo a los resultados se obtiene que el segundo modelo resulta ser el modelo con mejor resultado para futuras predicciones.

# 6 Modelos lineales mixtos para la altura facial posterior

La aplicacio´n de los modelos lineales mixtos permiten analizar de manera eficientemente los datos de experimentos con medidas repetidas. Este conocimiento es importante al momento de tomar decisiones, especialmente en los campos de ortodoncia donde se quiere obtener excelentes resultados durante cierto tratamiento. De acuerdo a ello en este capı´tulo se busca poder ilustrar resultados de la implementacio´n de dos modelos a una medida de crecimiento facial llamada altura facial posterior. Se establecen dos modelos: un modelo basado en polinomios de segundo orden con coeficientes aleatorios y un segundo modelo basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. Se ha de indicar cual de los dos modelos propuestos ha de generar resultados importantes.

### 6.1. Altura Facial Posterior (PFH)

Representada por la distancia lineal entre el punto gonion (Go) y el punto CF Su valor normal es de 55 mm +/- 3,3 mm a los 8 an˜os y medio de edad y aumentando 1 mm por a˜no hasta la finalizacio´n del crecimiento facial. Expresa la longitud de la rama mandibular. Ramas cortas son caracterı´sticas del tipo dolicofacial, debido al crecimiento vertical predominante, con giro de la mandı´bula en sentido horario. Por otro lado, ramas m´as anchas y con m´as longitud corresponden al tipo braquifacial, debido al crecimiento predominantemente horizontal y al giro de la mandı´bula en sentido antihorario. [Ricketts, 1981]

[Figure 26]

Figura 6-1: Puntos de referencia cefalom´etricas y trazado cefalom´etrico Altura Facial Posterior.

Fuente: [Ricketts, 1981]

### 6.2. An´alisis exploratorio de datos

Para la realizacio´n de esta seccio´n se hizo uso de los resultados del estudio correspondiente a la medida de crecimiento craneofacial Altura Facial Posterior que ha sido recopilada en el estudio CES-Damasco.

Los datos de igual forma constan de 49 individuos, 30 nin˜as y 19 nin˜os, cada sujeto con cantidades de medidas repetidas, para un resultado total de 449 observaciones. Para la medida de crecimiento craneofacial altura facial posterior se han tomado las edades disponibles pares entre los 6 a 24 an˜os.

- La tabla 6-1 muestra un corto ana´lisis descriptivo, etapa preliminar para el tratamiento de datos, el cual consiste en recopilar los datos en busca de obtener informacio´n para realizar el an´alisis correspondiente a la medida de crecimiento craneofacial altura facial posterior.

|VARIABLES|MUJERES n = 30 (61%)<br><br>| | | |HOMBRES n = 19 (39%)| | | |
|---|---|---|---|---|---|---|---|---|
| |Media|Desv. Est.|Mı`n.<br><br>|Ma`x.|Media|Desv. Est.<br><br>|Mı`n.<br><br>|Ma`x.|
|SEGUIMIENTO|16.86|2.38|10.00<br><br>|18.00|15.47<br><br>|3.64|4.00<br><br>|18.00|
|EVOLUCION´<br><br>|17.50|3.14<br><br>|11.00|25.00<br><br>|25.31|5.01<br><br>|12.00|37.00|

Tabla 6-1: Tiempo promedio de seguimiento y evolucio´n o cambio en PFH de la cohorte

desde la lı´nea base de acuerdo al g´enero.

En la figura 6-2, se encuentran los perfiles para la medida de altura facial posterior, fueron obtenidos con las mediciones registradas para cada uno de los sujetos. Se presenta la trayectoria de crecimiento que cada sujeto y se verifica que el comportamiento a trav´es de los an˜os no siguen una linea recta.

6.2 An´alisis exploratorio de datos 51

[Figure 27]

Figura 6-2: Gr´afica de perfiles de acuerdo a la edad y al g´enero en funci´on de la medida altura facial posterior (PFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH

- La figura 6-3 muestra la descripci´on del comportamiento longitudinal de la medida altura facial posterior(PFH) por medio del diagrama de boxplot. Se observa, a trave´s del tiempo hombres y mujeres evolucionan de manera creciente pero a partir de los 18 an˜os el valor de la medida tiende a estabilizarse.

[Figure 28]

Figura 6-3: Diagramas de boxplot global y longitudinal de la medida altura facial posterior

(PFH). Fuente: Creacio´n propia y Grupo de Investigaci´on CESLPH

- La figura 6-4. Muestra la gra´fica boxplot y la evolucio´n por g´enero con el gr´afico de lineas.

La curva promedio para los hombres comparado con las mujeres tiende a ir aumentando a partir de los 8 an˜os hasta la finalizacio´n del crecimiento facial .

[Figure 29]

- Figura 6-4: Diagrama de Boxplot longitudinal y gra´fico de lineas promedio de acuerdo a la edad y al ge´nero de la medid Altura Facial Posterior (PFH). Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH

### 6.3. Resultados PFH

El modelo lineal mixto propuesto como un polinomio de segundo orden con coeficientes aleatorios indica al subı´ndice i = 1,2,...,49 como cada uno de los sujetos considerados mientras que el sub´ındice j = 1,2,...,ni indica las observaciones repetidas para cada sujeto.

Modelo basado en polinomios de segundo orden con coeficientes aleatorios.

Yij = β0 +β1Genderi +β2Ageij +β3Age2ij +β1Genderi ∗Ageij +b0i +b1iAgeij +b2iAge2ij +ϵij donde,

Yij corresponde a la altura facial posterior del i − esimo´ sujeto en la j − esima´ observacio´n.

bi Efecto aleatorio la cual varı´a independientemente entre observaciones, con bi ∼ N(0,σb2)

ϵij errores que varı´an independientemente entre los sujetos. (dentro de una misma observaci´on), con ϵij ∼ N(0,σϵ2)

###### La tabla 6-2 evidencia los resultados de las estimaciones correspondientes al primer modelo de la altura facial posterior:

Para´metro Estimaci´on SE T P-Valor β0 45.171 0.864 52.280 <0.001 β1GENDER : M -4.0401 1.164 -3.470 0.001 β2AGE 2.702 0.121 22.284 <0.001 β3AGE2 -0.055 0.003 -15.732 <0.001 β4(GENDER)M : AGE 0.674 0.063 10.583 <0.001 V (b0i) 13.301 V (b1i) 0.378 V (b2i) 0.000 V (εij) 2.300

Tabla 6-2: Coeficientes de regresio´n estimados (efectos fijos) y errores esta´ndar y compo-

nentes de varianza para los datos de la altura facial posterior (PFH).

Sea yij=PFHij donde,

yij = 45.171 − 4.0401Genderi + 2.702Ageij + 0.055Age2ij + 0.674Genderi × Ageij Si Gender = 0 (Femenino), el modelo queda:

yij = 45.171 + 2.7402Ageij − 0.055Age2ij Si Gender =1 (Masculino), el modelo queda:

yij = 45.171 − 4.040 + (2.702 + 0.674)Ageij + 0.055Age2ij

= 41.130 + 3.376Ageij + 0.055Age2ij

Como la pendiente para hombres es mayor que para mujeres, la curva estar´a por encima de la de mujeres, pues

3.376 > 2.7402

De la misma forma que se consideraron modelos con splines en capı´tulos anteriores, aquı´ tambie´n se hara´ con el fin de ilustrar una mayor flexibilidad de la curva ajustada.

Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline.

Yij = β0 + β1Genderi + β2Ageij + β3Age2ij + β4Genderi ∗ Ageij + b0i + b1iAgeij + b2iAge2ij

+ai(Ageij − 12)+ + a2(Ageij − 15)+ + a3(Ageij − 18)+ + a4(Ageij − 20)+ + ϵij

De acuerdo a lo anterior el modelo de igual forma se caracteriza por tener cuatro nodos (m=4), donde los cambios en las pendientes se dan en las edades de 12, 15, 18 y 20, allı´ el ajuste genera cuatro (4) funciones truncadas, pues entre m´as nodos se incluyan en la funci´on lineal a trozos, mayor sera´ la flexibilidad de la curva ajustada.

- La tabla 6-3 indica las estimaciones para el modelo basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline para la medida altura facial posterior. De esta manera, se obtienen los resultados.

Para´metro Estimaci´on SE T P-Valor β0 52.471 1.638 32.030 <0.001

- β1GENDER(M) -2.216 1.244 -1.780 0.081
- β2AGE 1.211 0.345 3.509 <0.001
- β3AGE2 0.019 0.018 1.022 0.306 β3(GENDER)M : AGE 0.287 0.103 2.775 0.005
- β4 0.197 0.216 0.912 0.362
- β5 -1.031 0.201 -5.120 <0.001
- β6 -0.771 0.202 -3.813 <0.001
- β7 -0.130 0.210 -0.618 0.536 σbf 0.148

- σb0i 14.339
- σb1i 0.089
- σb2i 0.000

- Corr(b0i,b1i) -0.909
- Corr(b0i,b2i) 0.873 Corr(b1i,b2i) 0.159 σ(εij) 1.212

- Tabla 6-3: Estimaciones de m´axima verosimilitud para el modelo mixto con intercepto aleatorio, splines fijos y aleatorios para la altura facial posterior (PFH).

Sea yij=PFHij

donde,

yij = 52.471 − 2.216Genderi + 1.211Ageij + 0.019Age2ij + 0.287Genderi × Ageij Si Gender = 0 (Femenino), el modelo queda:

yij = 52.471 + 1.211Ageij + 0.019Age2ij Si Gender =1 (Masculino), el modelo queda: yij = 52.471 − 2.216 + (1.211 + 0.287)Ageij + 0.019Age2ij

= 50.255 + 1.498Ageij + 0.019Age2ij Como la pendiente para hombres es mayor que para mujeres, la curva estar´a por encima de la de mujeres, pues

1.498 > 1.211

- La figura 6-5, muestra los gra´ficos del modelo ajustado con intercepto aleatorio y al modelo ajustado con intercepto aleatorio y funciones spline. Existe un mejor ajuste en el segundo

modelo propuesto. Este modelo resulta ser ´util al momento de querer realizar importantes predicciones.

[Figure 30]

- Figura 6-5: Modelo ajustados con intercepto aleatorio y modelo ajustado con intercepto aleatorio y funciones spline para la medida altura facial posterior. Fuente: Creacio´n propia y Grupo de Investigacio´n CESLPH

La figura 6-6, muestra cuatro individuos seleccionados para demostrar de mejor forma el ajuste del nuevo modelo aplicando Splines en los nodos entre las edades de 12, 15, 18 y 20 an˜os.

[Figure 31]

- Figura 6-6: Perfiles observados y predichos de la altura facial posterior basado en splines de 4 individuos de ambos ge´neros para PFH. Fuente: Creaci´n propia y Grupo de Investigaci´n CESLPH

### 6.4. Evaluaci´n de la precisi´n de los modelos ajustados

En este ´ultimo capı´tulo se presentan las dos formas para medir la precisio´n del modelo. A continuaci´on, se observan los modelos ajustados que lograron explicar la altura facial posterior, en funcio´n de la variable edad (Age) y g´enero (Gender).

De acuerdo al Criterio de informacio´n Akaike y al BIC se observa, los resultados de la tabla

- 6-4 d´onde se selecciona el mejor modelo. De este modo se llega a la conclusio´n que el modelo con mejor ajuste es el segundo modelo.

Modelo DF AIC BIC Mod1 12 1966.15 2015.43 Mod2 17 1887.15 1956.97

- Tabla 6-4: Criterios para la seleccio´n de modelo mediante el Criterio de informaci´on Akaike

Mediante el coeficiente de correlacio´n intraclase (ICC) se ha de determinar cua´l de los dos modelos tiene mayor plausibilidad. De acuerdo a los resultados de la tabla 6-5, se llega concluye que el proceso de estimaci´on para los dos modelos propuestos son muy buenos.

Modelo ICC Modelo 1 0.98 Modelo 2 0.84

- Tabla 6-5: Criterios para la seleccio´n de modelo mediante el coeficiente de correlaci´on intraclase (ICC)

- La tabla 6-6 muestra los resultados de RGLMM2 para la medida craneofacial altura facial posterior (PFH) propuestos por Nakagawa’s.

##### Modelo R2GLMM Mod1 0.973 Mod2 0.986

Tabla 6-6: R2 de Nakagawa para modelos mixtos

### 6.5. Discusi´n

Al finalizar el cap´ıtulo correspondiente a la altura facial posterior se evidencia mucha inestabilidad en los datos para cada sujeto causando desbalanceo, se plantean dos modelos. Un

6.5 Discusi´on 57

primer modelo, modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios. y un segundo Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. Se concluye que de acuerdo a los resultados en los me´todos de precisi´on aplicados en los modelos propuestos el segundo modelo es excelente para realizar pron´osticos a largo plazo.

# 7 Comparaci´n de resultados

En este cap´ıtulo se hace ´enfasis en los resultados de los modelos propuestos, con el fin de visualizar de mejor forma su precisi´on en cada una de las medidas craneofaciales consideradas. Se evaluo´ el desempen˜o de cada una de las medidas con los diferentes modelos ajustados con el software RStudio.

- La tabla 7-1 presenta los resultados del criterio de informacio´n Akaike el cual sirve para seleccionar el mejor modelo. De acuerdo, a este criterio se evidencia al modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios como el mejor modelo ajustado puesto que presenta el menor valor para cada uno de los a´ngulos. En lo referente a las evidencias de fiabilidad de los modelos se deduce que el proceso de estimacio´n para ambos modelos arrojo excelentes resultados, en cuanto al coeficiente de correlaci´on intraclase. A continuacio´n se presenta un resumen de la modelizacio´n para las medidas craneofaciales correspondientes a los ´angulos:

|Medida de crecimiento craneofacial<br><br>|Modelos Propuestos|Criterio de Informacio´n Akaike (AIC)|Coeficiente de correlacio´n intraclase (ICC)|
|---|---|---|---|
|Angulo´ plano mandibular<br><br>|Modelo lineal mixto con intercepto aleatorio<br><br>|1875.046<br><br>|0.956|
| |Modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios.|1816.418|0.958|
|Angulo´ Goniaco (ArGoMe)|Modelo lineal mixto con intercepto aleatorio<br><br>|2205.352|0.937|
| |Modelo lineal mixto con intercepto aleatorio y splines fijos y aleatorios.<br><br>|2105.200|0.958|

Tabla 7-1: Comparaci´on modelos ajustados para las medidas de ´angulos

- La tabla 7-2 presenta los resultados del criterio de informacio´n Akaike y coeficiente de correlacio´n intraclase el cual sirven para seleccionar el modelo que mejor se ajusta y su confiabilidad. De acuerdo a los resultados obtenidos se evidencia al modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline, como el mejor modelo. Respecto a la confiabilidad de los modelos se concluye la existencia de una confiabilidad perfecta entre los modelos. Seguidamente, se ensen˜a el sumario del modelado para

59

las medidas craneofaciales altura facial anterior y posterior:

|Medida de crecimiento craneofacial<br><br>|Modelos Propuestos|Criterio de Informacio´n Akaike (AIC)|Coeficiente de correlacio´n intraclase (ICC)|
|---|---|---|---|
|Altura facial anterior<br><br>|Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios|2107.255|0.956|
| |Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. .|2048.272|0.799|
|Altura facial posterior|Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios|1966.153<br><br>|0.988|
| |Modelo lineal mixto basado en polinomios de segundo orden con coeficientes aleatorios y funciones spline. .<br><br>|1887.152|0.842|

Tabla 7-2: Comparaci´on modelos ajustados para las medidas

# 8 Conclusiones y recomendaciones

### 8.1. Conclusiones

Se evalu´a el desempen˜o de las medidas de crecimiento craneofacial con modelos lineales mixtos por medio del criterio de informacio´n Akaike, el BIC y la prueba del R2 de Nakagawa para escoger el mejor modelo. Se obtienen los siguientes resultados:

En cada una de las medidas craneofaciales a nivel general no se hallo´ problemas de convergencia con los modelos ajustados.

El desempen˜o de los modelos con splines genera una mayor plausibilidad que el modelo cuadra´tico, ya que para predicciones a largo plazo el modelo cuadra´tico decaer´a mientras que por ejemplo AFH se estabiliza en una meseta y el modelo spline captura esa meseta. Sin embargo, en dos de los modelos el ICC para los modelos sin splines fue menor pero genera valores aceptables desde el punto de vista pr´actico. Con toda seguridad si calcula´ramos valores para el ICC m´as all´a de 20 an˜os, los valores del modelo spline deben de ser mejores que los del modelo cuadra´tico.

En cada medida craneofacial, el modelo ajustado con splines fue el de mejor resultado, en t´erminos del AIC y el BIC, pero con AFH y PFH el ICC de los modelos con splines fue menor. Sin embargo, el valor de su ICC fue aceptable

Una vez realizada la prueba del R2 de Nakagawa para cada una de las medidas craneofaciales se evidencia, que el resultado del modelo 2 en todas estas medidas presentan un valor consistentemente mayor. Es decir, las estimaciones del modelo 2 se ajustan bastante bien.

Con el primer modelo propuesto, modelo lineal mixto con intercepto aleatorio se evidencio´ que el promedio para la medida a´ngulo plano mandibular fue superior 36◦ a la medida promedio 26◦, lo cual muestra la existencia de un ramo mandibular corto, con caracterı´sticas del tipo dolicofacial (individuos que en su rostro predomina el largo sobre el ancho)

Para las medidas altura facial anterior, altura facial posterior y ´angulo goniaco sus medidas promedio para cada una de ellas estuvo por debajo del promedio indicado, lo cual evidencia que los sujetos inicialmente presentaron caracter´ısticas de tipo braquifacial

8.2 Recomendaciones 61

es decir, la particularidad de tener cara ancha, arcadas dentarias bien desarrolladas y con mayor desarrollo muscular.

### 8.2. Recomendaciones

Con el an´alisis realizado a cada una de las medidas craneofaciales se puede dar referencia partiendo de los resultados obtenidos para ejecutar los controles para la toma de decisiones especialmente en los campos de la ortodoncia, cirugı´a maxilofacial y la oclusio´n dental, donde se quieren obtener resultados ´optimos durante cierto tratamiento.

Se recomienda el uso del modelo de spline en el proceso de estimaci´on, puesto que de acuerdo a los resultados obtenidos, estos han de permitir poder realizar prono´sticos ma´s precisos y menos problema´ticos a largo plazo.

# Bibliografı´a

[Bartko, 1966] Bartko, J. J. (1966). The intraclass correlation coefficient as a measure of reliability. Psychological reports, 19(1):3–11.

[Bavia and Garcia, 2016] Bavia, P. F. and Garcia, R. C. M. R. (2016). Vertical craniofacial morphology and its relation to temporomandibular disorders. Journal of Oral & Maxillofacial Research, 7(2).

[Bejarano et al., 2014] Bejarano, L. Y. G., Tejedor, F. H., P´erez, L. A. L., and Contreras, C. I. (2014). Curvas de crecimiento del perı´metro cefa´lico en nin˜os de 0 a 3 a˜nos. una nueva aproximaci´on. Revista Facultad de Odontologı´a Universidad de Antioquia, 26(1).

[Bishara et al., 1985] Bishara, S. E., Ortho, D., and Jakobsen, J. R. (1985). Longitudinal changes in three normal facial types. American journal of orthodontics, 88(6):466–502.

[Brumback and Rice, 1998] Brumback, B. A. and Rice, J. A. (1998). Smoothing spline models for the analysis of nested and crossed samples of curves. Journal of the American Statistical Association, 93(443):961–976.

[Buschang et al., 1988] Buschang, P. H., Tanguay, R., Demirjian, A., Lapalme, L., and Goldstein, H. (1988). Pubertal growth of the cephalometric point gnathion: multilevel models for boys and girls. American Journal of Physical Anthropology, 77(3):347–354.

[Casella and Berger, 2002] Casella, G. and Berger, R. L. (2002). Statistical inference, volume 2. Duxbury Pacific Grove, CA.

[Chvatal et al., 2005] Chvatal, B. A., Behrents, R. G., Ceen, R. F., and Buschang, P. H. (2005). Development and testing of multilevel models for longitudinal craniofacial growth prediction. American Journal of Orthodontics and Dentofacial Orthopedics, 128(1):45–56.

[Cooper and Thompson, 1977] Cooper, D. and Thompson, R. (1977). Note concerning the akaike and hannan estimation procedures for an autoregressive-moving average processa note on the estimation of the parameters of the autoregressive-moving average process. Biometrika, 64(3):625–628.

[Correa Morales et al., 2016] Correa Morales, J. C., Salazar Uribe, J. C., et al. (2016). Introduccio´n a los modelos mixtos.

[Cubillo and Smith, 2006] Cubillo, J. B. B. and Smith, J. B. (2006). Principales ana´lisis cefalome´tricos utilizados para el diagno´stico ortodo´ntico. Revista cientı´fica odontol´gica, 2(1):11–27.

[Durba´n, 2009] Durba´n, M. (2009). An introduction to smoothing with penalties: P-splines. Boletı´n de Estad´ıstica e Investigaci´n Operativa, 25(3):195–205.

[Eilers and Marx, 1996] Eilers, P. H. and Marx, B. D. (1996). Flexible smoothing with bsplines and penalties. Statistical science, pages 89–102.

[Faraway, 2016] Faraway, J. J. (2016). Extending the linear model with R: generalized linear, mixed effects and nonparametric regression models. CRC press.

[Fitzmaurice et al., 2012] Fitzmaurice, G. M., Laird, N. M., and Ware, J. H. (2012). Applied longitudinal analysis, volume 998. John Wiley & Sons.

[Green and Silverman, 1993] Green, P. J. and Silverman, B. W. (1993). Nonparametric regression and generalized linear models: a roughness penalty approach. Chapman and Hall/CRC.

[Guevara, 2015] Guevara, N. E. C. (2015). Variacio´n de patrones morfolo´gicos craneofaciales en relaciones esqueleticas clase i, ii y iii. Revista Facultad de Odontologı´a Universidad de Antioquia, 26(2).

[Harville, 1977] Harville, D. A. (1977). Maximum likelihood approaches to variance component estimation and to related problems. Journal of the American statistical association, 72(358):320–338.

[Isern and Cuesta, 2013] Isern, G. and Cuesta, C. B. (2013). Elecci´on del para´metro de suavizado o´ptimo en regresiones p-spline. un estudio por simulaci´on.

[Jime´nez et al., 2020] Jime´nez, I., Villegas, L., Salazar-Uribe, J. C., and Alvarez,´ L. G. (2020). Facial growth changes in a colombian mestizo population: An 18-year followup longitudinal study using linear mixed models. American Journal of Orthodontics and Dentofacial Orthopedics, 157(3):365–376.

[Jime´nez et al., 2013] Jime´nez, I. D., Villegas, L. F., and Alvarez,´ L. G. (2013). Picos de crecimiento facial vertical antes de los 12 a˜nos de edad y su relacio´n con el desarrollo puberal en 44 mestizos colombianos sin tratamiento. Revista Facultad de Odontologı´a Universidad de Antioquia, 24(2).

[Laird and Ware, 1982] Laird, N. M. and Ware, J. H. (1982). Random-effects models for longitudinal data. Biometrics, pages 963–974.

64 Bibliografı´a

[Lee et al., 2021] Lee, W.-J., Park, K.-H., Kang, Y.-G., and Kim, S.-J. (2021). Automated real-time evaluation of condylar movement in relation to three-dimensional craniofacial and temporomandibular morphometry in patients with facial asymmetry. Sensors, 21(8):2591.

[Moore, 2016] Moore, D. F. (2016). Applied survival analysis using R. Springer. [Pan and Goldstein, 1998] Pan, H. and Goldstein, H. (1998). Multi-level repeated measures

growth modelling using extended spline functions. Statistics in medicine, 17(23):2755– 2770.

[Patterson and Thompson, 1971] Patterson, H. D. and Thompson, R. (1971). Recovery of inter-block information when block sizes are unequal. Biometrika, 58(3):545–554.

[Preece and Heinrich, 1981] Preece, M. A. and Heinrich, I. (1981). Mathematical modellong of individual growth curves. British Medical Bulletin, 37(3):247–252.

[Racine, 2014] Racine, J. S. (2014). A primer on regression splines. URL:

http://cranrprojectorg/web/packages/crs/vignettes/splineprimerpdf. [Ramos-Montiel, 2019] Ramos-Montiel, R. (2019). Cefalometria de bjOrk¨ jarabak. [Ricketts, 1981] Ricketts, R. M. (1981). Perspectives in the clinical application of cephalo-

metrics: the first fifty years. The Angle Orthodontist, 51(2):115–150. [Ruppert et al., 2003] Ruppert, D., Wand, M. P., and Carroll, R. J. (2003). Semiparametric regression. Number 12. Cambridge university press.

[Stoffel et al., 2017] Stoffel, M. A., Nakagawa, S., and Schielzeth, H. (2017). rptr: Repeatability estimation and variance decomposition by generalized linear mixed-effects models. Methods in Ecology and Evolution, 8(11):1639–1644.

[Toquica Vargas, 2017] Toquica Vargas, C. S. (2017). Aproximaci´on bayesiana de un modelo semiparame´trico.

[Verbeke, 1997] Verbeke, G. (1997). Linear mixed models for longitudinal data. In Linear mixed models in practice, pages 63–153. Springer.

[Verbeke and Molenberghs, 2012] Verbeke, G. and Molenberghs, G. (2012). Linear mixed models in practice: a SAS-oriented approach, volume 126. Springer Science & Business Media.

[Verbyla, 1990] Verbyla, A. P. (1990). A conditional derivation of residual maximum likelihood. Australian Journal of Statistics, 32(2):227–230.

[Wand and Jones, 1994] Wand, M. P. and Jones, M. C. (1994). Kernel smoothing. Chapman and Hall/CRC.

[West et al., 2014] West, B. T., Welch, K. B., and Galecki, A. T. (2014). Linear mixed models: a practical guide using statistical software. Chapman and Hall/CRC.

[Wu and Zhang, 2006] Wu, H. and Zhang, J.-T. (2006). Nonparametric regression methods for longitudinal data analysis: mixed-effects modeling approaches, volume 515. John Wiley & Sons.

