$( 'document' ).ready(function() {
    $( 'ul.navbar-nav' ).on('click', '#locate', function() {
        $.get("http://localhost:5000/locate", {q: $(this).text()}, function(data, status) {
            if (status == 'success') {
                alert("hallo");
            }
        });
    });
});
