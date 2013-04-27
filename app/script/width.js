/**
 * Created with IntelliJ IDEA.
 * User: Chii
 * Date: 13/04/07
 * Time: 1:03
 * To change this template use File | Settings | File Templates.
 */
$(function(){

//キーワード側
    $('#yomifuda .branch').each(function(){
        calcFontSize($(this));
        calcWidth($(this));
    });

    $('#yomifuda .branch .node_box').bind('click', function(){
        coloringPages($(this));
    });

//ページ側
    var branches = $('#torifuda .branch').each(function(){
        node_num = $(this).children().length;
        $(this).css('width',Math.ceil(Math.sqrt(node_num))*16+'px');
    });

    $("#torifuda .node").hover(function(){
        $(this).parent().children(".arrow_box").show();
    },function(){
        $(this).parent().children(".arrow_box").hide();
    });

//static
    var data = $('#static_data').attr("data-json");
    data = data.replace(/u'/g, "'");    //parseできる形に変更
    data = data.replace(/'/g, '"');
    jsonData = JSON.parse(data);

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
    el.css('min-width',longest+"px");
    el.css('max-width',width+padding+"px");
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
    if(priority > 1000)  return 24;
    if(priority > 100)  return 20;
    if(priority > 20)   return 16;
    if(priority > 1)    return 14;
    return 12;
}

var CalcColor = function(val){
    val = Math.min(Math.round(val * 2.5), 255);
    var y = Math.max(126 - val, 0);
    return "rgb("+val+","+y+","+(255-(val))+")";
}

var coloringPages = function(el){
    var keyword = el.attr('data-keyword');
    var keywordData = $('#yomifuda .branch .node_box').attr('data-keyword');
    for(page in jsonData.pages){
        var priority = parseFloat(jsonData.pages[page].keyword[keywordData]);
        if(priority > 0){
            var color = CalcColor(priority);
            console.log(color);
            $("#"+jsonData.pages[page].page).css('background-color',color);
        }
    }
}