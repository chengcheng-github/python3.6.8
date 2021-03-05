function(){
    $(".catalog").hide(), $(this).children().first().removeClass("boxBtnHover")
  }
  function(){
    $(".catalog").show();
    var t = $(this).attr("data-tag");
    t == 1 && (e.tabDirScroll(), $(this).attr("data-tag", 2)), $(this).children().first().addClass("boxBtnHover")
  }

  