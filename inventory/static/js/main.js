$(document).ready(function(){
  $('.myPages').pxpaginate({
    limit: 6,
    callback:function(pagenumber){
          console.log(pagenumber);
        }
      
  });

  NProgress.start();
  NProgress.done();

  $('.datetimeinput').datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});
})