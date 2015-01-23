<?php
	include "configuracion.php";
	cabecera("Borrar");
?>
<form method="get" name="formulario" action="borra.php">
	Inserta una ID para borrar: <input type="text" value="" name="id" size="3"></br>
	<input type="submit" value="Borrar" title="Enviar">
</form>
<?php
	pie();
?>
