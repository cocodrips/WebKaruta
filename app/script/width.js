/**
 * Created with IntelliJ IDEA.
 * User: Chiichan
 * Date: 13/04/07
 * Time: 1:03
 * To change this template use File | Settings | File Templates.
 */
$(function(){
    var branches = $("#torifuda .branch").each(function(){
        node_num = $(this).children().length;
        $(this).css('width',Math.ceil(Math.sqrt(node_num))*16+'px');
    });

    $("#yomifuda .branch").each(function(){
        var allLength = 0;
        var longest = 0;
        $(this).children(".node_box").each(function(){
//        var len = $(this).html().replace(/^\s+/, "").length;
            var len = $(this).width();
            allLength += len;
            longest = Math.max(longest, len);
        });
        var width = Math.max(allLength/2, longest);
        console.log(width+" "+allLength+":"+longest);
        $(this).css('width',width+3+"px");
    });
});
