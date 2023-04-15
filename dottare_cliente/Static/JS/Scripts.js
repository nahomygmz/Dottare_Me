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

//galeria de imagenes
$(document).ready(function() {
  // Manejador de eventos para cambiar la imagen grande al hacer clic en una imagen pequeña
  $(".thumbnail").on("click", function() {
    // Obtener la ruta de la imagen grande
    var mainImageUrl = $(this).attr("src");
    
    // Actualizar la imagen grande
    $(".main-image img").attr("src", mainImageUrl);
  });
});

$(document).ready(function() {
  // Intercepta el evento submit del formulario
  $('#form').submit(function(e) {
    // Detiene el comportamiento por defecto del evento submit
    e.preventDefault();
    
    // Obtiene la acción y los datos del formulario
    const action = $(this).attr('action');
    const formData = $(this).serialize();
    
    // Envía los datos mediante AJAX
    $.ajax({
      url: action,
      type: 'POST',
      data: formData,
      success: function(response) {
        // Muestra la notificación en caso de éxito
        toastr.success('El formulario se envió correctamente.');
        
        // Resetea el formulario
        $('#form')[0].reset();
      },
      error: function(xhr, status, error) {
        // Muestra la notificación en caso de error
        toastr.error('Hubo un error al enviar el formulario.');
      }
    });
  });
});
