for(var i=0; i<5; i++){
	hexHeight = (50*i)+1;
	for(var j=0; j<4; j++){
		var hexWidth = (50*j)+1;
		var hex = '<div class="hexagon position" style:"margin-left:'+ hexWidth+'px; margin-top:'+hexHeight+'px"><span></span></div>';
		$('body').append(hex);
	}
}