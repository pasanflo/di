<?php
	include "configuracion.php";
	include "conexion.php";

	$sql="TRUNCATE TABLE persona";
	$result= mysql_query($sql, $conexion);

	cabecera("¿Borrar datos?");
	print "<p><strong id=\"error\">TODOS LOS DATOS HAN SIDO BORRADOS. ¡¿PERO QUÉ HAS HECHO?!</strong></p>";
	print "<p><a href=\"añadir.php\">Pulsa aquí para añadir unos campos.</a>";
	pie();
?>