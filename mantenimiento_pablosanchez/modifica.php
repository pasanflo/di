<?php
	
	include "configuracion.php";
	cabecera("Modificar registro");
	
	$id = $_REQUEST[id];
	$sql="SELECT id, nombre, apellido FROM persona WHERE id='$id'";
	print($sql);
	$result= mysql_query($sql, $conexion);
	$fila = mysql_fetch_array($result);
?>
<form method="get" name="formulario" action="modificaHecho.php">
	Id:<?php echo "<input type=\"text\" value=\" {$fila["id"]};?>\" disabled=true ></br>"; ?>
	Nombre:<?php echo "<input type=\"text\" value=\" {$fila["nombre"]};?>\" name=\"nombre\"></br>"; ?>
	Apellidos: <?php echo "<input type=\"text\" value=\" {$fila["apellido"]};?>\" name=\"apellido\"></br>"; ?>
	<input type="submit" value="Modificar">
</form>
<?php
	pie();
?>