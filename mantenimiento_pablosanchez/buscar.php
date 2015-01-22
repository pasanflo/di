<?php
	
	include "configuracion.php";
	cabecera("Añadir registro");
?>
<form method="get" name="formulario" action="busca.php">
	<strong>Introduce un término a buscar.</strong></br>
	Nombre: &nbsp;<input type="text" value="" name="nombre"></br>
	<strong>o</strong></br>
	Apellidos: <input type="text" value="" name="apellido"></br>
	<input type="submit" value="Enviar" name="Enviar" title="Enviar">
	<input type="reset" value="Resetear">
</form>
<?php
	pie();
?>
