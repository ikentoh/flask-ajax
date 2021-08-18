$(function(){
  updateBlend();

  // スライダーを操作したときにblend画像を更新する
  $('#blend-slider').on('change', function() {
    updateBlend();
  });
});

function updateBlend() {
  // flaskの/blendエンドポイントにリクエストする
  $.ajax({
    type: 'POST',
    url: '/blend',
    data: $('#blend-slider').val(),
    contentType: 'application/json',
  }).then(
    data => $('#blend-image').attr('src', data),
    error => console.log(error)
  );
};
