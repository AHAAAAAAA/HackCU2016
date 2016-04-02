
var pattern = Trianglify({
	width: window.innerWidth,
	height: window.innerHeight,
	variance: "0.98",
	seed: '32yy1',
	x_colors: 'random'});

document.body.appendChild(pattern.canvas())
// var colorbbrewer = {YlGnBu: {
// 3: ["#edf8b1","#7fcdbb","#2c7fb8"],
// 4: ["#ffffcc","#a1dab4","#41b6c4","#225ea8"],
// 5: ["#ffffcc","#a1dab4","#41b6c4","#2c7fb8","#253494"],
// 6: ["#ffffcc","#c7e9b4","#7fcdbb","#41b6c4","#2c7fb8","#253494"],
// 7: ["#ffffcc","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#0c2c84"],
// 8: ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#0c2c84"],
// 9: ["#ffffd9","#edf8b1","#c7e9b4","#7fcdbb","#41b6c4","#1d91c0","#225ea8","#253494","#081d58"]
// }};
