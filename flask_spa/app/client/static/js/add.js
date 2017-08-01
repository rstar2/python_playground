$(document).ready(function () {
    // on form submission ...
    $('form').on('submit', function () {

        var numOne = $('input[name="num1"]').val();
        var numTwo = $('input[name="num2"]').val();

        $.ajax({
            type: "POST",
            // url: "/",
            data: { num1: numOne, num2: numTwo },
            success: function (data) {
                $('#result').html(data.total)
                $('input').val('')
            },
            error: function (error) {
                console.log(error)
            }
        });

        return false;
    });

});