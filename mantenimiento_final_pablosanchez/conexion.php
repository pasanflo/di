<?php
	//
	// BASE DE DATOS DE PABLO SANCHEZ PARA EL MANTENIMIENTO PHP.
	// Si quieres usar el programa para tu base de datos, cambia las variables definidas aquí abajo.
	// Si quieres usar mi base de datos, ejecuta el archivo "persona.sql" en tu consola SQL.
	//
	DEFINE("DB_HOST", "localhost");
	DEFINE("DB_USER", "root"); // Usuario
	DEFINE("DB_PASSWORD", "sistemas"); // Contraseña
	DEFINE("DB_NAME", "mantenimiento_pablosanchez"); // Base de datos

	$conexion = mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
	mysql_select_db(DB_NAME);
?>
