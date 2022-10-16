// $(".race").input(function (event) {
//   if ($(".race") != null) {
//     $(".subrace").toggleClass("is-hidden");
//   }
//   console.log($(".race"));
//   console.log();
// });

$(".name").input(function (event) {
  $("#racial").textContent = event.target.value;
});
