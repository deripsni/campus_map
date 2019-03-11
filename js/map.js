
var mymap = P.map('mapid', {
		crs: P.CRS.Simple,
		minZoom: -3
	});
     

    var bounds = [xy(-25, -26.5), xy(1023, 1021.5)];

    var image = P.imageOverlay('uqm_map_full.png', bounds).addTo(map);
            
    //var rectangle = L.rectangle(bounds, {color: "black", weight: 1, fill: false}).addTo(mymap);   
    //mymap.setMaxBounds(bounds)
    
    var yx = P.latLng;

	var xy = function(x, y) {
		if (L.Util.isArray(x)) {    // When doing xy([x, y]);
			return yx(x[1], x[0]);
		}
		return yx(y, x);  // When doing xy(x, y);
	};


	var popup = P.popup();

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(mymap);
	}

	mymap.on('click', onMapClick);

    map.setView(xy(120, 70), 1);
