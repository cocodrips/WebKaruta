var top_space = "180px";
window.onresize = resize;

function my_init(){
    // resize();
}

$(document).ready(function() {

});

function resize(e){
    var screen_width = document.body.scrollWidth;
    // if(screen_width > 770){
    //     resize_rounds();
    //     resize_rounds_padding();
    // }else{
    //     resize_rounds_default();
    // }
    
}

function resize_rounds(){
    $(".contents_round").each(function(){
        var width = $(this).css("width");
        $(this).css("height", width);
        console.log(width);
    });
}

function resize_rounds_padding(){
    $(".contents_round_text").each(function(){
        var width = $(this).parent(".contents_round").css("width").replace('px','');
        var round_margin = width / 6;
        var size = width - round_margin * 2;
        $(this).css({"width":size + "px", "height":size+ "px", "padding" : round_margin + "px"});
    });
}

function resize_rounds_default(){

    $(".contents_round_text").each(function(){
        $(this).css({"width": "90%", "height":"100%px", "padding" : "30px"});
    });
}






