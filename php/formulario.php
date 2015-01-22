<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <title>Datos personales 7 (Formulario). Controles en formularios. Ejercicios.
  PHP. Bartolomé Sintes Marco</title>
  <meta name="generator" content="amaya 8.7.1, see http://www.w3.org/Amaya/" />
  <link href="formulario.css" rel="stylesheet" type="text/css"
  title="Color" />
</head>
<body>
	<form action="controles_formularios_7.php" method="get">
		<h1>Datos personales 7 (Formulario)</h1>
		<fieldset>
		  <legend>Formulario</legend>
		  <p>Escriba los datos siguientes:</p>

		  <table cellspacing="5">
		    <tbody>
		      <tr>
		        <td><strong>Nombre:</strong><br />
		          <input type="text" name="nombre" size="20" maxlength="20" /></td>
		        <td><strong>Apellidos:</strong><br />
		          <input type="text" name="apellidos" size="20" maxlength="20" /></td>
		        <td><strong>Edad:</strong><br />

		          <select name="edad">
		            <option selected="selected"></option>
		            <option value="1">Menos de 20 años</option>
		            <option value="2">Entre 20 y 39 años</option>
		            <option value="3">Entre 40 y 59 años</option>
		            <option value="4">60 años o más</option>
		          </select>
		           </td>
		      </tr>
		      <tr>
		        <td><strong>Peso:<br />
		          </strong><input type="text" name="peso" size="3" maxlength="3" />
		        kg</td>
		        <td><strong>Sexo:</strong><br />
		          <input type="radio" name="sekso" value="hombre" />Hombre <input
		          type="radio" name="sekso" value="mujer" />Mujer</td>
		        <td><strong>Estado Civil:</strong><br />
		          <input type="radio" name="estadoCivil" value="soltero" /> Soltero
		          <input type="radio" name="estadoCivil" value="casado" /> Casado
		          <input type="radio" name="estadoCivil" value="otro" /> Otro</td>
		      </tr>
		    </tbody>
		  </table>

		  <table cellspacing="5">
		    <tbody>
		      <tr>
		        <td rowspan="2" class="borde"><strong>Aficiones:</strong></td>
		        <td><input type="checkbox" name="cine" /> Cine</td>
		        <td><input type="checkbox" name="literatura" /> Literatura</td>
		        <td><input type="checkbox" name="tebeos" /> Tebeos</td>
		      </tr>
		      <tr>
		        <td><input type="checkbox" name="deporte" /> Deporte</td>
		        <td><input type="checkbox" name="musica" /> Música</td>
		        <td><input type="checkbox" name="television" /> Televisión</td>
		      </tr>
		    </tbody>
		  </table>

		  <p class="der">
		  <input type="submit" value="Enviar" /> 
		  <input type="reset" value="Borrar" name="Reset" /></p>
		</fieldset>
	</form>
</body>
</html>
