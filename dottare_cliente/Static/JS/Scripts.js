$(document).ready(function() {
  // Mostrar el botón cuando el usuario se desplaza hacia abajo
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.volver-arriba').fadeIn();
    } else {
      $('.volver-arriba').fadeOut();
    }
  });

  // Desplazarse suavemente hacia la parte superior cuando se hace clic en el botón
  $('.volver-arriba').click(function() {
    $('html, body').animate({scrollTop : 0},100);
    return false;
  });
});