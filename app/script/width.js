/**
 * Created with IntelliJ IDEA.
 * User: Chiichan
 * Date: 13/04/07
 * Time: 1:03
 * To change this template use File | Settings | File Templates.
 */
$(function(){
    var branches = $('#torifuda .branch').each(function(){
        node_num = $(this).children().length;
        $(this).css('width',Math.ceil(Math.sqrt(node_num))*16+'px');
    });

    $('#yomifuda .branch').each(function(){
        calcFontSize($(this));
        calcWidth($(this));
    });

});

var calcWidth = function(el){
    var allLength = 0;
    var longest = 0;
    var padding = 3;
    el.children('.node_box').each(function(){
        var len = $(this).width();
        allLength += len;
        longest = Math.max(longest, len);
    });
    var width = Math.max(allLength/2, longest);
//    console.log(width+" "+allLength+":"+longest);
    el.css('width',width+padding+"px");
}

var calcFontSize = function(el){
    el.children(".node_box").each(function(){
        var priority = $(this).attr('data-priority');
        var size = fontSize(priority)
        $(this).css('font-size', size+"px");
    });
}

//あとでもう少し柔軟な感じにする
var fontSize = function(priority){
    if(priority > 500)  return 24;
    if(priority > 100)  return 20;
    if(priority > 20)   return 18;
    if(priority > 1)    return 16;
    return 14;
}