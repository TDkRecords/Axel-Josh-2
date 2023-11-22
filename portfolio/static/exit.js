window.onbeforeunload = function() {
    // Hacer petición AJAX a la vista exit
    $.ajax({
      method: 'GET',
      url: '/exit/'
    });
  }