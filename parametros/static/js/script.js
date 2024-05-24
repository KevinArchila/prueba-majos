var scrollUp = window.pageYOffset;
    
window.onscroll = function() {
    var scrollDown = window.pageYOffset;
    
    if (scrollUp > scrollDown){
        document.getElementById("sticky").classList.add("headerHide")
    } else {
        document.getElementById("sticky").classList.remove("headerHide")
    }
    scrollUp = scrollDown;
}