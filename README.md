# RedConecta Telecom S.A.

## 1 Objetivo del proyecto:
Analizar la información operacional de RedConecta Telecom S.A. para identificar diferencias en la calidad del servicio entre regiones, tipo de servicio, apoyar la toma de cisiones. 

## 2 Preguntas de investigación:
Que regiones presentan una mayor latencia?
En que regiones se registra un mayor tiempo de resolución?
Que regiones presentan mayor incumplimiento del SLA?
Como los resultados pueden ayudar a priorizar las acciones de mejora?

## 3 Herramientas utilizadas:
Pandas, para carga, procesamiento y análisis de datos.
Matplotlib, para creación de gráficos.
Python, lenguaje utilizado para desarrollar el análisis.
Git, para realizar el control de versiones del proyecto.

## 4 Etapas de análisis:
1.	Carga de los datos.
2.	Revisión y validación de los datos, comprobación de columnas, tipos de datos, valores nulos.
3.	Análisis exploratorio, cálculo de indicadores de latencia, tiempo de resolución, ticket de soporte y cumplimiento de SLA. 
4.	Visualización de los datos, elaboración de gráficos desarrollo de un dashboard exploratorio.
5.	Exportación de los datos, generación de archivos CSV para Soporte técnico y Experiencia de clientes.
6.	Documentación y control de versiones, registro de la estructura, las instrucciones de ejecución y cambios del proyecto. 

## 5 Principal resultado:
La mayor latencia se observa en la región Centro, seguida de Norte y la menor del sur. Esto sugiere que los usuarios de Centro experimentan más problemas con la capacidad de respuesta de la red. La peor situación con el tiempo promedio de resolución se presenta en la región Sur, donde la resolución de incidencias es la más lenta. Norte muestra el mejor resultado en velocidad de resolución, mientras el Centro se ubica en un punto intermedio. 
El servicio de Internet hogar recibe la mayor cantidad de tickets. Esto puede indicar problemas generalizadas o una ata caga. Los servicios de Empresas y Móvil tienen menos tickets. El mayor número de incumplimientos de SLA se observa en el servicio de Internet hogar, y no solo hay muchas solicitudes, sino que una parte significativa no se resuelve dentro del plazo promedio. Los servicios de Empresas y Móvil muestran un mejor cumplimiento del SLA. 
Conclusiones importantes:
Centro sufre de alta latencia, mientras que Sur presenta tiempo de resolución lentos. Internet hogar es la principal fuente de solicitudes e incumplimientos del SLA. 

Estos resultados permiten identificar áreas que requieren una revisión más detallada. Se recomienda investigar las causas del incumplimiento del SLA, revisar los procesos de resolución de incidentes y comparar los indicadores por región y tipo de servicio antes de implementar acciones correctivas.

## 6 Actualización y reutilización

Cuando se incorporan nuevos registros, se deben cargar los datos, validar su estructura, ejecutar nuevamente las funciones de análisis y actualizar los reportes y el dashboard. Si el archivo contiene únicamente registros nuevos, es necesario integrarlos con los datos históricos y revisar posibles duplicados.
