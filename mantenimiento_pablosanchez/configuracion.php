<?php
function cabecera($pagina){
    print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\">
<head>
  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />
  <title>$pagina</title>
  <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>
</head>
<body>
<h1>$pagina</h1>
<div id=\"menu\">
  <ul>\n";
    print "
    <li><a href=\"listar.php\">Listar</a></li>
	<li><a href=\"añadir.php\">Añadir registro</a></li>
    <li><a href=\"borrar.php\">Borrar</a></li>
    <li><a href=\"modificar.php\">Modificar</a></li>
    <li><a href=\"borrarTodo.php\">Borrar todo</a></li>
	<li><a href=\"buscar.php\">Buscar</a></li>\n";
    print "</ul>
</div>
</br>
<div id=\"body\"><div id=\"cuadro\">\n";
}

function pie(){ print '</div></body></html>'; }
?>
