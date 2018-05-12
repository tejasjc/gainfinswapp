$(document).ready(function(){


     new WOW().init();


     $('#main-nav').onePageNav({
        currentClass: 'current',
        changeHash: true,
        scrollSpeed: 1200
    });
     $('#write_us').onePageNav({
        currentClass: 'current',
        changeHash: true,
        scrollSpeed: 1200
    });



    $("#testimonial-slider").owlCarousel({
        items:1,
        itemsDesktop:[1000,1],
        itemsDesktopSmall:[979,1],
        itemsTablet:[768,1],
        pagination:true,
        navigation:false,
        navigationText:["",""],
        slideSpeed:1000,
        singleItem:true,
        autoPlay:true
    });


    $("#contact_form_submit_button").children('img').hide();    //to hide loding animation

    //animated header class
    $(window).scroll(function() {
    var scroll = $(window).scrollTop();
     //console.log(scroll);
    if (scroll > 200) {
        //console.log('a');
        $(".navigation").addClass("animated");
    } else {
        //console.log('a');
        $(".navigation").removeClass("animated");
    }});

     $("#contact-form").validate({
        rules: {
            name: {
                required: true,
                minlength: 2
            },
            mobile: {
                required: true,
            },
            message: {
                required: true,
                minlength: 2
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            name: {
                required: "Please enter Your Name",
                minlength: "Your name must consist of at least 2 characters"
            },
            message: {
                required: "Please Write Something",
                minlength: "Your message must consist of at least 2 characters"
            },
            email: "Please enter a valid email address"
        },
         submitHandler: function(form) {

            $("#contact_form_submit_button").children('img').show();    //to show loding animation
             $("#contact_form_submit_button").children('p').hide();    //to hide send option
              $("#contact_form_submit_button").prop('disabled', true);    //to disable send option

        $.ajax({
            url : "sendmail/", // the endpoint
            type : "POST", // http method
            data : { name : $('#name').val(),
                     email: $('#email').val(),
                     message: $('#message').val(),
                    }, // data sent with the post request

            // handle a successful response
            success : function(json) {
                $('#name').val(''); // remove the value from the input
                $('#mobile').val(''); // remove the value from the input
                $('#email').val(''); // remove the value from the input
                $('#message').val(''); // remove the value from the input
                $("#contact_form_submit_button").children('img').hide();    //to hide loding animation
                 $('#result').show().html(json['result'])
                $("#contact_form_submit_button").prop('disabled', false);    //to enable send option
             $("#contact_form_submit_button").children('p').show();    //to show send option

            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom

            }
        });
        }

    });

     $('#result').hide()


});

/*for typewriter effect*/
var app = document.getElementById('app');

var typewriter = new Typewriter(app, {
    loop: true
});

typewriter.typeString('We don\'t just build Websites' )
    .pauseFor(500)
    .deleteChars(8)
    .typeString('Apps ')
    .pauseFor(500)
    .deleteChars(5)
    .typeString('Softwares ')
    .pauseFor(500)
    .deleteAll()
    .typeString('We build your Business !')
    .pauseFor(2500)
    .deleteChars(10)
    .typeString('Dreams !')
    .pauseFor(2500)
    .deleteAll()
    .start();


function alpha(e) {
    var k;
    document.all ? k = e.keyCode : k = e.which;
    return ((k > 64 && k < 91) || (k > 96 && k < 123) || k == 8 || k == 32 || (k >= 48 && k <= 57));
}




