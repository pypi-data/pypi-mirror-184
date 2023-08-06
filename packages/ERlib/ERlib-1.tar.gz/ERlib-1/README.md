Para imprimir tu tabla simplemente tienes que crear tu tabla y mandar a llamar a la función, puedes colocar un título a la tabla el cual si lo colocas se imprimirá primero el título y después la tabla, la tabla se imprime con el estilo de salida de MySQL.

Ejemplo de uso:

from ERlib import printTable

TituloDeLaTabla = "Los equipos con más Champions League"

Tabla = [
   ["Posición", "Equipo", "Títulos"],
   ["1°", "Real Madrid Club de Fútbol", 14],
   ["2°", "Associazione Calcio Milán", 7],
   ["3°", "Bayern de Múnich", 6],
   ["4°", "Liverpool Fútbol Club", 6],
   ["5°", "Fútbol Club Barcelona", 5]
]

printTable(Tabla, TituloDeLaTabla)

Salida:

****** Los equipos con más Champions League *******
+----------+----------------------------+---------+
| Posición | Equipo                     | Títulos |
+----------+----------------------------+---------+
| 1°       | Real Madrid Club de Fútbol | 14      |
+----------+----------------------------+---------+
| 2°       | Associazione Calcio Milán  | 7       |
+----------+----------------------------+---------+
| 3°       | Bayern de Múnich           | 6       |
+----------+----------------------------+---------+
| 4°       | Liverpool Fútbol Club      | 6       |
+----------+----------------------------+---------+
| 5°       | Fútbol Club Barcelona      | 5       |
+----------+----------------------------+---------+