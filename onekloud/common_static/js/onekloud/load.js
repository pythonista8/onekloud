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
