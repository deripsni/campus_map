
var mymap = P.map('mapid').setView([46.04698, -118.39085], 17);

	P.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		minZoom: 17,
		
		id: 'mapbox.streets'
	}).addTo(mymap);
     
    var bounds = [[46.044612, -118.396032], [46.049482, -118.386923]]
            
    //var rectangle = L.rectangle(bounds, {color: "black", weight: 1, fill: false}).addTo(mymap);   
    mymap.setMaxBounds(bounds)
    
            
	var popup = L.popup();

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(mymap);
	}

	mymap.on('click', onMapClick);
