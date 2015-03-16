$('.img_gallery').hover(function(event) {
    $('.img_gallery').css('opacity', 0.6);
    $(this).css('opacity', 1);
});

$('.img_gallery').mouseleave(function(event) {
    $('.img_gallery').css('opacity', 1);
});

$(document).keyup(function(event) {
    if (event.keyCode == 37 || event.keyCode == 39) {
       var img_nb_total = parseInt($('img.img_gallery').attr('data-img-total-nb'));
        var img_nb = parseInt($('#img_modal_content > img').attr('data-img-nb'));
        if (event.keyCode == 37) { // left
            var img_next = (img_nb - 1 + img_nb_total) % img_nb_total;
        } else { // 39 = right arrow key
            var img_next = (img_nb + 1 + img_nb_total) % img_nb_total;
        }
        $('#img_modal_content > img').attr({
            'src': $('img.img_gallery[data-img-nb="' + img_next + '"]').attr('src'),
            'data-img-nb': img_next
        });
    }
});

$('img.img_gallery').click(function(event) {
    $('#img_modal_content > img').attr({
        'src': event.target.src,
        'data-img-nb': $(this).attr('data-img-nb')
    });
    $('.modal-title').html(event.target.alt);
    $('#img_modal').modal();
});

$('.modal').click(function() {
    $('#img_modal').modal('hide');
});