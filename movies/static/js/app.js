$(document).ready(function() {

        const baner = $('.alert');

        const checkAccess = function () {
            const movie = $(this);
            $.ajax({
                type: "GET",
                url: movie.attr('data-validate-access-url'),
                data: {
                    'pk': movie.attr('data-moviepk')
                },
                dataType: 'json',
                success: function (data) {
                    if (!data.access) {
                        baner.addClass('alert-danger')
                        baner.text('You do not have access to this video')
                        baner.show()
                    } else {
                        baner.addClass('alert-success')
                        baner.text('In a moment you will be redirected to the page with the movie')
                        baner.show()
                        setTimeout(() => window.location.href = movie.attr('data-href'), 3000)
                    }
                }
            });
        };
        $(document).on('click', '.btn', checkAccess)
    });