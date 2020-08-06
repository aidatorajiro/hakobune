<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<title>Toranomori Login</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<?php echo style(); ?>
		<style>
			body {
				margin: 0px;
				padding: 0px;
				background: #ccffff;
			}
			.textbox {
				margin: 24px;
			}
			.textbox .text {
				padding: 12px;
				background: #ccffcc;
				display: block;
			}
			.textbox .time {
				padding: 12px;
				background: #ffffcc;
				display: block;
				float: right;
			}
		</style>
	</head>
	<body>
		<?php echo $htmldata; ?>
		<form action="chat" method="post">
			<input type="hidden" name="token" value="<?php echo $_GET['token'] ?>"/>
			<input type="text" name="name"/><br>
			<textarea name="text"></textarea><br>
			<input type="submit" value="submit"/><br>
		</form>
	</body>
</html>