/* All slider functionality*/
function slider(){
  var newSelected = $(this).index()+1;
  $(this).parents(".list-item").children(".rating").children(".num").text(newSelected);

  $(this).parent().children(".active").removeClass("active");
  $(this).addClass("active");
}

/* Only load DOM after jquery is loaded */
/* Fix this later
$(function(){
  $(window).on("load", function(){
    alert("loaded");
    $("html").removeClass("not-loaded");
  });
})
*/
