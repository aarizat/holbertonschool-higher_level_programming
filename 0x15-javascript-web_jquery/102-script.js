$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?' + $.param({ lang: code }), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
