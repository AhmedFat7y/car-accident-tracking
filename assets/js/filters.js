$(function(){
  var timeout = 0;
  $("input[type='checkbox'].filter-option").change(function(){
    if(timeout!=0) {
      clearTimeout(timeout);
      timeout = 0;
    }
    timeout = setTimeout("filter", 300);
  });//end handler filter-options checkbox

  function filter() {
    $("#novels").load();
  }//end function filter
});