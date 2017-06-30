$(document).ready(function () {
    $('#try-again').hide();

    // on form submission ...
    $('form').on('submit', function () {

        // grab values
        loc = $('input[name="location"]').val();
        lang = $('input[name="language"]').val();

        $.ajax({
            type: "POST",
            data: { 'loc': loc, 'lang': lang },
            success: function (results) {
                if (results.items.length > 0) {
                    $('input').hide();
                    $('#try-again').show();
                    var randNum = Math.floor(Math.random() * Object.keys(results.items).length)
                    $('#results').html('<a href="' + results.items[randNum].html_url + '">' + results.items[randNum].login +
                        '</a><br><img src="' + results.items[randNum].avatar_url + '" class="avatar">')
                    // $('input').val('')
                } else {
                    $('#results').html('Something went terribly wrong! Please try again.')
                }
            },
            error: function (error) {
                console.log(error)
            }
        });

    });

    $('#try-again').on('click', function () {
        $('input').val('').show();
        $('#try-again').hide();
        $('#results').html('');
    });

});