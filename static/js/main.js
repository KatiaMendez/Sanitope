jQuery('document').ready(function($){
  var menuBtn = $('.menu-icon'),
      menuA = $('#nav'),
      a = 1;

  menuBtn.click (function() {
    if (menuA.hasClass('show')) {
      menuA.removeClass('show');
    }else{
      menuA.addClass('show');
    } 
  });
});