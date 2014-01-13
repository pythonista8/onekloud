// Smoothly scroll browser window to the anchor. Pass element's id
// without `#`.
function scrollToAnchor(id, fn) {
  var opts = {
    duration: 1000,
    easing: 'easeOutQuart'
  }

  if (fn !== undefined) opts['complete'] = fn;

  var anchor = $('#' + id);

  $('html, body').animate({
    scrollTop: anchor.offset().top
  }, opts);
}
