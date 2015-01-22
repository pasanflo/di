<?php
	include "configuracion.php";
	include "conexion.php";

	$nombre = $_REQUEST[nombre];
	$apellido = $_REQUEST[apellido];
	
	$sql="INSERT INTO persona (nombre, apellido) VALUES('$nombre', '$apellido')";
	$result= mysql_query($sql, $conexion);
	cabecera("Datos añadidos.");
	print "<p><strong id=\"correcto\">Datos añadidos correctamente.</strong></p>";
	if($nombre=="" || $apellido==""){ print "<p><strong id=\"error\">Pero uno de los campos lo dejaste vacío...</strong></p>"; }
	print "<p><a href=\"añadir.php\">¿Añadir más campos?</a>";
	pie();
?>