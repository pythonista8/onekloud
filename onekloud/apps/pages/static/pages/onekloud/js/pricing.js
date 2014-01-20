$('.contact').on('click', function(event) {
  var modal = $('#contact-form-modal');

  modal.dialog({
    autoOpen: true,
    modal: true,
    closeOnEscape: true,
    closeText: '&#xf00d',
    width: 450,
    title: "Contact Us"
  });

  var type = $(this).data('type');
  var html = "<input type=\"hidden\" name=\"pricing\" value=\"" + type + "\">";

  modal.find('.pure-form').append(html);

  return false;
});

$('.signup').on('click', function(event) {
  var modal = $('#signup-form-modal');

  modal.dialog({
    autoOpen: true,
    modal: true,
    closeOnEscape: true,
    closeText: '&#xf00d',
    width: 450,
    title: "Sign Up"
  });

  return false;
});

