<?php
	
	include "configuracion.php";
	cabecera("Modificar registro");
?>
<form method="get" name="formulario" action="modifica.php">
	Inserta ID para modificar <input type="text" value="" name="id" size="3"></br>
	<input type="submit" value="Modificar">
</form>
<?php
	pie();
?>

