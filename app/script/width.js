/**
 * Created with IntelliJ IDEA.
 * User: Chiichan
 * Date: 13/04/07
 * Time: 1:03
 * To change this template use File | Settings | File Templates.
 */
$(function(){
    <!--長さの平均-->
    $(".branch").each(function(){
        var char_length=0;
        var max_char_length=0;
        $(this).children(".node").forEach(function(){
            var len = $(this).text().length();
            char_count +=  len;
            if(max_char_length < len) max_char_length = len;
        });
var node_count = $(this).children(".node").length;
var width = Math.max((char_length/node_count), max_char_length);
$(this).css("width", width*15);

});
});
