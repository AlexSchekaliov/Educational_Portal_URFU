
$(document).ready(function() {
     $("#dropdown-menu ul li ul ").hide();
     $("#dropdown-menu ul li a").click(function() {

          // $(this).next().slideToggle("normal");
         $("#dropdown-menu ul li ul:visible").slideUp("normal");
    if (($(this).next().is("ul")) && (!$(this).next().is(":visible"))) {
        $(this).next().slideDown("normal");
    }
     });
});