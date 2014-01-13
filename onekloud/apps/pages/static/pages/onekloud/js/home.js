$('#learn-more').on('click', function() {
  scrollToAnchor('content');
  return false;
});

$('#signup .pure-button').on('click', function() {
  scrollToAnchor('showcase', function() {
    var signupContainer = $('#signup-form-container');

    $('.fade').fadeIn(250);
    signupContainer.find('input[name="email"]').focus();

    signupContainer.css('border-radius', 5).animate({
      backgroundColor: '#202021'
    }, 250, 'easeOutQuart', function() {

      setTimeout(function() {
        $('.fade').fadeOut(250);

        signupContainer.animate({
          backgroundColor: 'transparent'
        }, 250, 'easeOutQuart', function() {
          signupContainer.css('border-radius', 0);
        });
      }, 3000);

    });
  });

  return false;
});
