$( 'document' ).ready(function(){
    $( '#search' ).keypress( function(e) {
        if (e.which == 13) {
            $.get("http://localhost:5000/search", {q: $(this).val()}, function(data, status) {
                if (status == 'success') {
                    $( 'ul.navbar-nav' ).empty();
                    data.forEach(element => {
                        $( 'ul.navbar-nav' ).append('<li class="nav-item"> <a id="' + element[1] + '"class="nav-link locate">' + element[0] + '</a> </li>');
                    });
                }
            });
        }
    });
});