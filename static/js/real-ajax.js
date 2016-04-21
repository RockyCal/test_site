$(document).ready(function() {

$('.cur_proc').on("click",".complete",function(){
    var dsid;
    dsid  = $(this).attr("data-dsid");
    $.get('/ajax_processed/', {data_set_id: dsid}, function(data){
        $('#cur_proc').html(data);
    }); 
});
});
