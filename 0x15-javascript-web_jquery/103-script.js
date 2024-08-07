/* global $ */
$(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation');
    });
  }

  // Fetch translation when button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when ENTER is pressed in the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the ENTER key
      fetchTranslation();
    }
  });
});
