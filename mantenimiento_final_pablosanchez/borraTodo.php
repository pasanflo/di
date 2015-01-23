<?php
	include "configuracion.php";
	include "conexion.php";

	$sql="TRUNCATE TABLE persona"; //Truncate reinicializa los ids.

	//$sql="DELETE * FROM persona" //Si usamos DELETE, los ids seguirían desde el último generado.

	$result= mysql_query($sql, $conexion);

	cabecera("Todos los datos borrados");
	print "<p><strong id=\"error\">TODOS LOS DATOS HAN SIDO BORRADOS. ¡¿PERO QUÉ HAS HECHO?!</strong></p>";
	print "<p><a href=\"añadir.php\">Pulsa aquí para añadir unos campos.</a>";
	pie();
?>
