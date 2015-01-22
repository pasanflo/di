<?php
	include "configuracion.php";
	include "conexion.php";
	cabecera("Borrar datos");
	$id = $_REQUEST[id];
	$sql="DELETE FROM persona WHERE id = $id";
	$result= mysql_query($sql, $conexion);
	if($id == ""){
		print "<p><strong id=\"error\">¡No has introducido un dato!</strong></p>"; 
		print "<p><a href=\"borrar.php\">Pulsa para intentar de nuevo.</a></p>";
	} else {
		print "<p><strong id=\"correcto\">Datos borrados</strong> (o no en la base de datos).</p>";
	}
	pie();
?>