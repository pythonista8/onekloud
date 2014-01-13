$('#learn-more').on('click', function() {
  scrollToAnchor('content');
});

$('#signup .pure-button').on('click', function(event) {
  event.preventDefault;

  scrollToAnchor('showcase', function() {
    var signupContainer = $('#signup-form-container');

    $('.fade').fadeIn(250);

    signupContainer.animate({
      backgroundColor: '#202021'
    }, 250, 'easeOutQuart', function() {
      setTimeout(function() {
        $('.fade').fadeOut(250);

        signupContainer.animate({
          backgroundColor: 'transparent'
        }, 250, 'easeOutQuart');

      }, 3000);
    });
  });

  return false;
});
