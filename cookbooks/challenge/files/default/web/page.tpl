<!DOCTYPE html>

<head>
	<title>Star Trek Trivia Game</title>
	<!-- TODO move this to the correct location-->
	<link rel="stylesheet" href="/static/css/main.css" type="text/css"/>
</head>

<body>
	<h3 style="text-align:center">Star Trek Trivia Game</h3>
	<p style="text-align:center">Select the ship captain with 
	the vessel on the right! It&#39;s a matching game!</p>

	<form method="GET" action="index.php">
	<div id="container">
	<div id="capList">
%count = 1
%for capPath in caps:
		<img src="{{capPath}}" alt="Captain"/>
		{{count}}
%count += 1
%end
	</div>
	<div id="shipList">
%for shipName in ships:
		<span>
			<select>
%for count2 in range(count - 1):
%	count2 += 1
			<option value="{{count2}}">{{count2}}</option>
%end
			</select>
			{{shipName}}
			<br/>
		</span>
%end
	<input type="submit"/>
	</div>
	</div>
	</form>
</body>
