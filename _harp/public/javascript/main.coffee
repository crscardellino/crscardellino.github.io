$(document).ready ->
  if $(location).attr('hash') == "#message-success"
    $("#message-success").removeClass("hide")
  return