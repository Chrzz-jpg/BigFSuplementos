document.addEventListener("DOMContentLoaded", function (e) {
  $(".radio-group .radio").click(function () {
    console.log("clicou 0");
    $(".radio").addClass("gray");
    $(this).removeClass("gray");
  });

  $(".plus-minus .plus").click(function () {
    console.log("clicou");
    var count = $(this).parent().prev().text();
    $(this)
      .parent()
      .prev()
      .html(Number(count) + 1);
  });

  $(".plus-minus .minus").on('click', function () {
    console.log("clicou 2");
    var count = $(this).parent().prev().text();
    $(this)
      .parent()
      .prev()
      .html(Number(count) - 1);
  });
  $("#minus").on('click', function () {
    console.log("clicou 2");
    var count = $(this).parent().prev().text();
    $(this)
      .parent()
      .prev()
      .html(Number(count) - 1);
  });
});
