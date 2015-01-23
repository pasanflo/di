<?php
	include "configuracion.php";
	include "conexion.php";

	cabecera("¿Borrar datos?");
	print "<p><strong id=\"error\">¿Seguro que quieres borrar todos los datos?</strong></p>";
?>
<form method="get" name="formulario" action="borraTodo.php">

	<input type="submit" value="SI" name="Enviar">

</form>
<?php
	pie();
?>