$( 'document' ).ready(function() {
   $( 'ul.navbar-nav' ).on('click', 'a.locate', function() {
        $.get("http://localhost:5000/locate", {q: $(this).text()}, function(data, status) {
            if (status == 'success') {
		//alert(data);
		marker.setLatLng([data[0][0], data[0][1]]);
		marker.addTo(map);
		map.flyTo([data[0][0], data[0][1]], 0);
		
		//Current = Floor_1;
		$('.leaflet-control-layers-selector')[data[0][2]].click();

		
		if (data[0][2] == 0){
			Current=Floor_0;
		}
		else if (data[0][2] == 1){
			Current=Floor_1;
		}
		else if (data[0][2] == 2){
			Current=Floor_2;
		}
		else if (data[0][2] == 3){
			Current=Floor_3;
		}
		
		$('.leaflet-control-layers-selector')[data[0][2]].click();
            }
	    else{
		alert('Send Help')
		}
        });
    });
});

$( 'document' ).ready(function() {
   $( '.room' ).click( function() {
        $.get("http://localhost:5000/locate", {q: $(this).text()}, function(data, status) {
            if (status == 'success') {
	
		marker.setLatLng([data[0][0], data[0][1]]);
		marker.addTo(map);
		map.flyTo([data[0][0], data[0][1]], 0);
		
		//Current = Floor_1;
		$('.leaflet-control-layers-selector')[1].click();

		
		if (data[0][2] == 0){
			Current=Floor_0;
		}
		else if (data[0][2] == 1){
			Current=Floor_1;
		}
		else if (data[0][2] == 2){
			Current=Floor_2;
		}
		else if (data[0][2] == 3){
			Current=Floor_3;
		}
		
		$('.leaflet-control-layers-selector')[data[0][2]].click();
            }
	    else{
		alert('Send Help')
		}
        });
    });
});