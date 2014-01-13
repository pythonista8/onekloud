$('#learn-more').on('click', function() {
  scrollToAnchor('content');
});

$('#signup .pure-button').on('click', function(event) {
  event.preventDefault;

  scrollToAnchor('showcase', function() {
    $('.fade').hide().css('display', 'block').fadeIn();

    var signupContainer = $('#signup-form-container');

    signupContainer.animate({
      background: '#202021'
    }, 1000, 'easeOutQuart', function() {
      setTimeout(function() {
        $('.fade').fadeOut();
        signupContainer.animate({
          background: 'transparent'
        });
      }, 3000);
    });
  });

  return false;
});
