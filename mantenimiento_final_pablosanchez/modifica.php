<?php
	include "configuracion.php";
	include "conexion.php";
	cabecera("Datos modificados");

	$id = $_REQUEST[id];
	$nombre = $_REQUEST[nombre];
	$apellido = $_REQUEST[apellido];

	$sql="UPDATE persona SET nombre='$nombre', apellido='$apellido' WHERE id = '$id'";
	$result= mysql_query($sql, $conexion);
	if($id == ""){
		print "<p><strong id=\"error\">¡No has introducido un dato!</strong></p>"; 
		print "<p><a href=\"modificar.php\">Pulsa para intentar de nuevo.</a></p>";
	} else {
		print "<p><strong id=\"correcto\">Datos modificados</strong></p>";
		print "<p><a href=\"listar.php\">Pulsa para ver la tabla.</a></p>";
		
	}
	pie();
?>
