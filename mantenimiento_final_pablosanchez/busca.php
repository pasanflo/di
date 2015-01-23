<?php
	
	include("configuracion.php");
	include("conexion.php");
	cabecera("Búsqueda");
	
	$nombre = $_REQUEST[nombre];
	$apellido = $_REQUEST[apellido];
?>
<table border="1">
	<tr>
		<td><strong>id</strong></td>
		<td><strong>Nombre</strong></td>
		<td><strong>Apellido</strong></td>
	</tr>
<?php
	$sql="SELECT id, nombre, apellido FROM persona WHERE nombre=\"$nombre\" OR apellido=\"$apellido\"";
	echo "Resultados acerca de $nombre $apellido";
	echo "</br>";
	$res= mysql_query($sql, $conexion);
	$fila = mysql_fetch_array($res);
	while($fila){
		echo "<tr>";
		echo "<td>{$fila["id"]}</td>";
		echo "<td>{$fila["nombre"]}</td>";
		echo "<td>{$fila["apellido"]}</td>";
		echo "</tr>";
		$fila = mysql_fetch_array($res);
	}
	echo "</table>";
	pie();
?>
