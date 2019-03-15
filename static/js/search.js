$( 'document' ).ready(function(){
    $( '#search' ).keypress( function(e) {
        if (e.which == 13) {
            $.get("http://localhost:5000/search", {q: $(this).val()}, function(data, status) {
                //alert("sent");
            });
        }
    });
});
