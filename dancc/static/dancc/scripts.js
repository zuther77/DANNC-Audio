
    (function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 70,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 100,
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict






// const uploadForm = document.getElementById('upload-form')
// const input = document.getElementById('video')
// const progressBox = document.getElementById('progress-box')

// const csrf = document.getElementsByName('csrfmiddlewaretoken')

// input.addEventListener('change', ()=>{
//     progressBox.classList.remove('not-visible')

//     const video_data = input.files[0] 

//     const fd = new FormData
//     fd.append('csrfmiddlewaretoken', csrf[0].value)
//     fd.append('video', video_data)

//     $.ajax({
//         type:'POST',
//         url: uploadForm.action, 
//         enctype: 'mutltipart/form-data',
//         data: fd,
//         beforeSend: function(){

//         },
//         xhr: function(){
//             const xhr = new window.XMLHttpRequest();
//             xhr.upload.addEventListener('progress', e=>{
//                 if (e.lengthComputable){
//                     const percent = e.loaded / e.total * 100
//                     progressBox.innerHTML = `<div class="progress md-progress">
//                     <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
//                 </div>`
//                 }
//             })
//             return xhr
//         },
//         success: function(response){

//         },
//         error: function(error){
//             console.log(error);
//         },
//         cache: false,
//         contentType: false,
//         processData: false,
//     })


// })

