$(function () {
    // init feather icons
    feather.replace();

    // init tooltip & popovers
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover();

    //page scroll
    $("a.page-scroll").bind("click", function (event) {
        var $anchor = $(this);
        $("html, body")
            .stop()
            .animate(
                {
                    scrollTop: $($anchor.attr("href")).offset().top - 20,
                },
                1000
            );
        event.preventDefault();
    });

    // slick slider
    $(".slick-about").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        dots: true,
        arrows: false,
    });

    //toggle scroll menu
    var scrollTop = 0;
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        //adjust menu background
        if (scroll > 80) {
            if (scroll > scrollTop) {
                $(".smart-scroll").addClass("scrolling").removeClass("up");
            } else {
                $(".smart-scroll").addClass("up");
            }
        } else {
            // remove if scroll = scrollTop
            $(".smart-scroll").removeClass("scrolling").removeClass("up");
        }

        scrollTop = scroll;

        // adjust scroll to top
        if (scroll >= 600) {
            $(".scroll-top").addClass("active");
        } else {
            $(".scroll-top").removeClass("active");
        }
        return false;
    });

    // scroll top top
    $(".scroll-top").click(function () {
        $("html, body").stop().animate(
            {
                scrollTop: 0,
            },
            1000
        );
    });
});

$(document).ready(function() {
    $('#btnAnalysis').click(function() {
        text = $('#sentiment_area').val()
        data = JSON.stringify(text);
        if(text.length > 0) {
            let startTime = performance.now()

            $.post('/result',{text:text},function(res) {
                $('#spanResult').html(res)
                let endTime = performance.now()
                console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
            })
                
            
        }else{
            alert('Vui lòng nhập câu cần phân tích !')
        }
    })
})
