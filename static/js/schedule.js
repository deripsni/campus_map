$( 'document' ).ready(function() {
    $( 'ul.navbar-nav' ).on('click', 'a', function() {
        $.get("http://localhost:5000/schedule", {q: $(this).attr("id")}, function(data, status) {
            if (status == 'success') {
                $( 'ul.navbar-nav' ).empty();
                var format = "<table>";
                data.forEach(element => {
                    format += "<tr><td>" + element[0] + "</td><td>" + element[1] + "</td></tr>";
                });
                format += "</table>"
                $( 'ul.navbar-nav' ).append(format);
            }
        });
        $( '#search' ).val($(this).attr("id"));
    });
});