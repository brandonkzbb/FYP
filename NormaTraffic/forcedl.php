<?php
	if ($_GET['run']){
		$output = shell_exec("sudo /var/www/html/dl.sh");
		echo "<pre>$output\n</pre>";
	}
?>

<a href="?run=true">Click Here</a>