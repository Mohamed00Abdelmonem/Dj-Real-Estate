(function ($) {
  "use strict";
  /*-------------------------------------
        Contact Form initiating
    -------------------------------------*/
  var contactForm = $(".rt-contact-form");
  if (contactForm.length) {
    contactForm.validator().on("submit", function (e) {
      var $this = $(this),
        $target = contactForm.find(".form-response");
      if (e.isDefaultPrevented()) {
        $target.html(
          "<div class='alert alert-danger'><p>Please select all required field.</p></div>"
        );
      } else {
        $.ajax({
          url: "php/form-process.php",
          type: "POST",
          data: contactForm.serialize(),
          beforeSend: function () {
            $target.html(
              "<div class='alert alert-info'><p>Loading ...</p></div>"
            );
          },
          success: function (response) {
            var res = JSON.parse(response);
            console.log(res);
            if (res.success) {
              $this[0].reset();
              $target.html(
                "<div class='alert alert-success'><p>Message has been sent successfully.</p></div>"
              );
            } else {
              if (res.message.length) {
                var messages = null;
                res.message.forEach(function (message) {
                  messages += "<p>" + message + "</p>";
                });
                $target.html(
                  "<div class='alert alert-success'><p>" +
                    messages +
                    "</p></div>"
                );
              }
            }
          },
          error: function () {
            $target.html(
              "<div class='alert alert-success'><p>Error !!!</p></div>"
            );
          },
        });
        return false;
      }
    });
  }

  /*----------------------------- Product Image Zoom --------------------------------*/
  $('.zoom-image-hover').zoom();
  /*-------------------------------------
    Wow Js
    -------------------------------------*/
  var wow = new WOW({
    boxClass: "wow",
    animateClass: "animated",
    offset: 0,
    mobile: false,
    live: true,
    scrollContainer: null,
  });
  wow.init();

  /*-------------------------------------
    Swiper Js
    -------------------------------------*/

  /*---------------------------------------
// rt-slider-style-6
----------------------------------------*/
  $(".testimonial-layout1").each(function (i) {
    let rtSliderStyle1 = $(this).get(0);
    let prev = $(this)
      .parents(".rt-slide-wrap")
      .find(".swiper-button-prev")
      .get(0);
    let next = $(this)
      .parents(".rt-slide-wrap")
      .find(".swiper-button-next")
      .get(0);

    new Swiper(rtSliderStyle1, {
      slidesPerView: 1,
      spaceBetween: 24,
      loop: true,
      slideToClickedSlide: true,
      autoplay: {
        delay: 4000,
      },
      navigation: {
        nextEl: next,
        prevEl: prev,
      },
      speed: 800,
    });
  });

  let testWrap2 = new Swiper(".test-wrap2", {
    slidePereView: 1,
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  let testWrap3 = new Swiper(".testimonial-layout3", {
    slidePereView: 1,
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  /*-------------------------------------
  Swiper Js
  -------------------------------------*/

  const swiper2 = new Swiper(".testimonial-layout2", {
    // Optional parameters
    slidePereView: 1,
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  /*-------------------------------------
  Swiper Js
  -------------------------------------*/

  const swiper3 = new Swiper(".location-layout1", {
    // Optional parameters
    slidePereView: 1,
    loop: true,

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  /*-------------------------------------
      Swiper Js
  -------------------------------------*/

  // $(window).on('load', function () {
  var featureBoxSlider = new Swiper(".featured-thum-slider", {
    spaceBetween: 20,
    slidesPerView: 3,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    loop: true,
    breakpoints: {
      0: {
        slidesPerView: 2,
      },
      576: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      992: {
        slidesPerView: 2,
      },
      1200: {
        slidesPerView: 3,
      },
      1500: {
        slidesPerView: 3,
      },
    },
  });
  var featuredBoxThumbs = new Swiper(".feature-box2", {
    loop: true,
    spaceBetween: 20,
    slidesPerView: 1,
    thumbs: {
      swiper: featureBoxSlider,
    },
  });
  // });
  /*-------------------------------------
      Swiper Js
  -------------------------------------*/
  var featureBoxSlider = new Swiper(".featured-thum-slider2", {
    spaceBetween: 5,
    slidesPerView: 5,
    freeMode: true,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    loop: true,
    breakpoints: {
      0: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 5,
      },
    },
  });
  var featuredBoxThumbs = new Swiper(".feature-box3", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    loop: true,
    thumbs: {
      swiper: featureBoxSlider,
    },
  });
  /*-------------------------------------
      Swiper Js
  -------------------------------------*/
  $(".feature-layout-style-1").each(function (i) {
    const __swiper = $(this).get(0);
    const prev = $(this)
      .parents(".rt-feature-slide-wrap")
      .find(".feature-btn-prev")
      .get(0);
    const next = $(this)
      .parents(".rt-feature-slide-wrap")
      .find(".feature-btn-next")
      .get(0);

    new Swiper(__swiper, {
      slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    slideToClickedSlide: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      480: {
        slidesPerView: 2,
      },
      576: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      992: {
        slidesPerView: 4,
      },
      1200: {
        slidesPerView: 5,
      },
    },
      autoplay: {
        delay: 4000,
      },
      navigation: {
        nextEl: next,
        prevEl: prev,
      },
      speed: 800,
    });
  });
 

  /*-------------------------------------
      Swiper Js
  -------------------------------------*/
  var swiper4 = new Swiper(".property-layout1", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    slideToClickedSlide: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      576: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      992: {
        slidesPerView: 2,
      },
      1200: {
        slidesPerView: 6,
      },
    },
  });

  /*-------------------------------------
      Swiper Js
  -------------------------------------*/
  var swiper5 = new Swiper(".brand-layout", {
    slidesPerView: 5,
    spaceBetween: 30,
    autoplay: {
      delay: 4000,
    },
    speed: 800,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      576: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      992: {
        slidesPerView: 3,
      },
      1200: {
        slidesPerView: 4,
      },
      1500: {
        slidesPerView: 5,
      },
    },
  });

  /*-------------------------------------
      Swiper Js
  -------------------------------------*/
  var swiper6 = new Swiper(".single-slider-layout1", {
    slidesPerView: 1,
    spaceBetween: 0,
    loop: true,
    slideToClickedSlide: true,
    pagination: {
      el: ".rt-swiper-pagination",
      clickable: true,
    },
  });
  /*-------------------------------------
    Section background image
    -------------------------------------*/
  imageFunction();

  function imageFunction() {
    $("[data-bg-image]").each(function () {
      var img = $(this).data("bg-image");
      $(this).css({
        backgroundImage: "url(" + img + ")",
      });
    });
  }

  /*---------------------------------------
    Background Parallax
    --------------------------------------- */

  $(window).on("load resize", function () {
    if ($(window).width() >= 768) {
      if ($(".parallaxie").length) {
        $(".parallaxie").parallaxie({
          speed: 0.5,
          offset: 0,
        });
      }
    }
  });

  /*------------------------------
   // Tooltip
   ------------------------------*/
   $(function () {
    $('[data-bs-toggle="tooltip"]').tooltip({
      offset: [0, 5],
    });
  });

  /*-------------------------------------
    Jquery Serch Box
    -------------------------------------*/
  $('a[href="#template-search"]').on("click", function (event) {
    event.preventDefault();
    var target = $("#template-search");
    target.addClass("open");
    setTimeout(function () {
      target.find("input").focus();
    }, 600);
    return false;
  });
  $("#template-search, #template-search button.close").on(
    "click keyup",
    function (event) {
      if (
        event.target === this ||
        event.target.className === "close" ||
        event.keyCode === 27
      ) {
        $(this).removeClass("open");
      }
    }
  );
  /*-------------------------------------
    YouTube Popup
    -------------------------------------*/
  var yPopup = $(".play-btn");
  if (yPopup.length) {
    yPopup.magnificPopup({
      disableOn: 700,
      type: "iframe",
      mainClass: "mfp-fade",
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
    });
  }
  var yPopup = $(".video-btn");
  if (yPopup.length) {
    yPopup.magnificPopup({
      disableOn: 700,
      type: "iframe",
      mainClass: "mfp-fade",
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
    });
  }
  // Page Preloader
  let preloader = $("#preloader");
  preloader &&
    $("#preloader").fadeOut("slow", function () {
      $(this).remove();
    });
  /*-------------------------------------
  dropdown Filter
   -------------------------------------*/
  $(".dropdown-filter, .rt-filter-btn-1").on("click", function () {
    $(".explore__form-checkbox-list").toggleClass("filter-block");
  });

  /*---------------------------------------
    On Click Section Switch
    --------------------------------------- */
  $('[data-type="section-switch"]').on("click", function () {
    if (
      location.pathname.replace(/^\//, "") ===
        this.pathname.replace(/^\//, "") &&
      location.hostname === this.hostname
    ) {
      var target = $(this.hash);
      if (target.length > 0) {
        target = target.length
          ? target
          : $("[name=" + this.hash.slice(1) + "]");
        $("html,body").animate(
          {
            scrollTop: target.offset().top,
          },
          1000
        );
        return false;
      }
    }
  });
  /*-------------------------------------
    On Scroll 
    -------------------------------------*/
  $(window).on("scroll", function () {
    // Back Top Button
    if ($(window).scrollTop() > 500) {
      $(".scrollup").addClass("back-top");
    } else {
      $(".scrollup").removeClass("back-top");
    }

    // Sticky Header
    if ($("body").hasClass("sticky-header")) {
      var stickyPlaceHolder = $("#rt-sticky-placeholder"),
        menu = $("#header-menu"),
        menuMobile = $("#meanmenu"),
        menuH = menu.outerHeight(),
        menuMobileH = menu.outerHeight(),
        topHeaderH = $("#header-topbar").outerHeight() || 0,
        middleHeaderH = $("#header-middlebar").outerHeight() || 0,
        targrtScroll = topHeaderH + middleHeaderH;
      if ($(window).scrollTop() > targrtScroll) {
        menu.addClass("rt-sticky");
        stickyPlaceHolder.height(menuH);
      } else {
        menu.removeClass("rt-sticky");
        stickyPlaceHolder.height(0);
      }
      if ($(window).scrollTop() > 300) {
        menuMobile.addClass("rt-sticky");
        stickyPlaceHolder.height(menuMobileH);
      } else {
        menuMobile.removeClass("rt-sticky");
        stickyPlaceHolder.height(0);
      }
    }
  });

  // Fixed header
  $(window).on("scroll", function () {
    if ($(".rt-header").hasClass("sticky-on")) {
      let stickyPlaceHolder = $("#sticky-placeholder"),
        menu = $("#navbar-wrap"),
        menuH = menu.outerHeight(),
        menuMobile = $("#meanmenu"),
        topbarH = $("#topbar-wrap").outerHeight() || 0,
        targrtScroll = topbarH,
        header = $("header");
      if ($(window).scrollTop() > targrtScroll) {
        header.addClass("sticky");
        stickyPlaceHolder.height(menuH);
      } else {
        header.removeClass("sticky");
        stickyPlaceHolder.height(0);
      }
      if ($(window).scrollTop() > 300) {
        menuMobile.addClass("rt-sticky");
      } else {
        menuMobile.removeClass("rt-sticky");
      }
    }
  });
  /*-----------------------------------
 // Pannellum up
 ----------------------------------*/
  var panoramaEl = $("#panorama");
  if (panoramaEl.length) {
    pannellum.viewer("panorama", {
      type: "equirectangular",
      panorama: "https://pannellum.org/images/alma.jpg",
    });
  }

  /*-----------------------------------
 // counter up
 ----------------------------------*/
  let counter = true;
  $(".counter-appear").appear();
  $(".counter-appear").on("appear", function () {
    if (counter) {
      // with skill bar
      $(".skill-per").each(function () {
        let $this = $(this);
        let per = $this.attr("data-per");
        $this.css("width", per + "%");
        $({ animatedValue: 0 }).animate(
          { animatedValue: per },
          {
            duration: 1000,
            step: function () {
              $this.attr("data-per", Math.floor(this.animatedValue) + "%");
            },
            complete: function () {
              $this.attr("data-per", Math.floor(this.animatedValue) + "%");
            },
          }
        );
      });

      // Only number counter
      $(".counterUp").each(function () {
        let $this = $(this);
        jQuery({
          Counter: 0,
        }).animate(
          {
            Counter: $this.attr("data-counter"),
          },
          {
            duration: 3000,
            easing: "swing",
            step: function () {
              let num = Math.ceil(this.Counter).toString();
              if (Number(num) > 99999999) {
                while (/(\d+)(\d{8})/.test(num)) {
                  num = num.replace(/(\d+)(\d{8})/, "");
                }
              }
              $this.html(num);
            },
          }
        );
      });

      counter = false;
    }
  });

  // var counterContainer = $(".counter");
  // if (counterContainer.length) {
  //   counterContainer.counterUp({
  //     delay: 50,
  //     time: 5000,
  //   });
  // }
  /*-------------------------------------
      Mobile Menu Toggle
      -------------------------------------*/
  $(".sidebarBtn").on("click", function (e) {
    e.preventDefault();
    if ($(".rt-slide-nav").is(":visible")) {
      $(".rt-slide-nav").slideUp();
      $("body").removeClass("slidemenuon");
    } else {
      $(".rt-slide-nav").slideDown();
      $("body").addClass("slidemenuon");
    }
  });
  /*-------------------------------------
    Mobile Menu Dropdown
    -------------------------------------*/
  var a = $(".offscreen-navigation .menu");
  if (a.length) {
    a.children("li").addClass("menu-item-parent");
    a.find(".menu-item-has-children > a").on("click", function (e) {
      e.preventDefault();
      $(this).toggleClass("opened");
      var n = $(this).next(".sub-menu"),
        s = $(this).closest(".menu-item-parent").find(".sub-menu");
      a.find(".sub-menu").not(s).slideUp(250).prev("a").removeClass("opened"),
        n.slideToggle(250);
    });
    a.find(".menu-item:not(.menu-item-has-children) > a").on(
      "click",
      function (e) {
        $(".rt-slide-nav").slideUp();
        $("body").removeClass("slidemenuon");
      }
    );
  }
  /*-------------------------------------
    Offcanvas Menu activation code
    -------------------------------------*/
  $("#wrapper").on("click", ".offcanvas-menu-btn", function (e) {
    e.preventDefault();
    var $this = $(this),
      wrapper = $(this).parents("body").find(">#wrapper"),
      wrapMask = $("<div />").addClass("offcanvas-mask"),
      offCancas = $("#offcanvas-wrap"),
      position = offCancas.data("position") || "left";

    if ($this.hasClass("menu-status-open")) {
      wrapper.addClass("open").append(wrapMask);
      $this.removeClass("menu-status-open").addClass("menu-status-close");
      offCancas.css({
        transform: "translateX(0)",
      });
    } else {
      removeOffcanvas();
    }

    function removeOffcanvas() {
      wrapper.removeClass("open").find("> .offcanvas-mask").remove();
      $this.removeClass("menu-status-close").addClass("menu-status-open");
      if (position === "left") {
        offCancas.css({
          transform: "translateX(-105%)",
        });
      } else {
        offCancas.css({
          transform: "translateX(105%)",
        });
      }
    }
    $(".offcanvas-mask, .offcanvas-close").on("click", function () {
      removeOffcanvas();
    });

    return false;
  });

  /*--------------------------------------
   Isotope initialization
   --------------------------------------*/
  var $container = $(".isotope-wrap");
  if ($container.length > 0) {
    var $isotope;
    var blogGallerIso = $(".featuredContainer", $container).imagesLoaded(
      function () {
        $isotope = $(".featuredContainer", $container).isotope({
          filter: "*",
          transitionDuration: "1s",
          hiddenStyle: {
            opacity: 0,
            transform: "scale(0.001)",
          },
          visibleStyle: {
            transform: "scale(1)",
            opacity: 1,
          },
        });
      }
    );
    $container.find(".isotope-classes-tab").on("click", "a", function () {
      var $this = $(this);
      $this.parent(".isotope-classes-tab").find("a").removeClass("current");
      $this.addClass("current");
      var selector = $this.attr("data-filter");
      $isotope.isotope({
        filter: selector,
      });
      return false;
    });
  }

  /*======================================
  //TweenMax Mouse Effect
  ====================================*/
  $(".motion-effects-wrap").mousemove(function (e) {
    parallaxIt(e, ".motion-effects1", -30);
    parallaxIt(e, ".motion-effects2", -30);
    parallaxIt(e, ".motion-effects3", -30);
    parallaxIt(e, ".motion-effects4", -10);
    parallaxIt(e, ".motion-effects5", -30);
    parallaxIt(e, ".motion-effects6", -30);
    parallaxIt(e, ".motion-effects7", -30);
    parallaxIt(e, ".motion-effects8", -30);
    parallaxIt(e, ".motion-effects9", -30);
    parallaxIt(e, ".motion-effects10", -30);
    parallaxIt(e, ".motion-effects11", 30);
    parallaxIt(e, ".motion-effects12", -100);
    parallaxIt(e, ".motion-effects13", 100, -50);
  });
  function parallaxIt(e, target_class, movement) {
    let $wrap = $(e.target).parents(".motion-effects-wrap");
    if (!$wrap.length) return;
    let $target = $wrap.find(target_class);
    let relX = e.pageX - $wrap.offset().left;
    let relY = e.pageY - $wrap.offset().top;
    TweenMax.to($target, 1, {
      x: ((relX - $wrap.width() / 2) / $wrap.width()) * movement,
      y: ((relY - $wrap.height() / 2) / $wrap.height()) * movement,
    });
  }
  /*======================================
      //Radio
    ====================================*/
  let $searcHradioButtons = $('.search-radio input[type="radio"]');
  $searcHradioButtons.click(function () {
    $searcHradioButtons.each(function () {
      $(this).parent().toggleClass("active", this.checked);
    });
  });
  /*======================================
      //Nice Select
    ====================================*/
  $(document).ready(function () {
    $("select").niceSelect();
  });

  /*==============================
     //  Back to Top
     ===============================*/
  let $window = $(window);
  let distance = 300;
  $window.scroll(function () {
    if ($window.scrollTop() >= distance) {
      $("#back-to-top").fadeIn();
    } else {
      $("#back-to-top").fadeOut();
    }
  });
  $("#back-to-top").click(function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      800
    );
  });

  /*==============================
     //  Custom Owl
     ===============================*/

  $(".product-slider-style-4").owlCarousel({
    items: 5,
    margin: 30,
    nav: false,
    dot: true,
    loop: true,
    center: true,
    // autoplay: true,
    // autoplayTimeout: 6000,
    responsive: {
      0: {
        items: 1,
      },
      576: {
        items: 2,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
      1200: {
        items: 3,
      },
      1500: {
        items: 4.6,
      },
    },
  });

  /*-------------------------------------
    Carousel slider initiation
    -------------------------------------*/
  $(".rc-carousel").each(function () {
    var carousel = $(this),
      loop = carousel.data("loop"),
      Canimate = carousel.data("animate"),
      items = carousel.data("items"),
      margin = carousel.data("margin"),
      stagePadding = carousel.data("stage-padding"),
      autoplay = carousel.data("autoplay"),
      autoplayTimeout = carousel.data("autoplay-timeout"),
      smartSpeed = carousel.data("smart-speed"),
      dots = carousel.data("dots"),
      nav = carousel.data("nav"),
      navSpeed = carousel.data("nav-speed"),
      rXsmall = carousel.data("r-x-small"),
      rXsmallNav = carousel.data("r-x-small-nav"),
      rXsmallDots = carousel.data("r-x-small-dots"),
      rXmedium = carousel.data("r-x-medium"),
      rXmediumNav = carousel.data("r-x-medium-nav"),
      rXmediumDots = carousel.data("r-x-medium-dots"),
      rSmall = carousel.data("r-small"),
      rSmallNav = carousel.data("r-small-nav"),
      rSmallDots = carousel.data("r-small-dots"),
      rMedium = carousel.data("r-medium"),
      rMediumNav = carousel.data("r-medium-nav"),
      rMediumDots = carousel.data("r-medium-dots"),
      rLarge = carousel.data("r-large"),
      rLargeNav = carousel.data("r-large-nav"),
      rLargeDots = carousel.data("r-large-dots"),
      rExtraLarge = carousel.data("r-extra-large"),
      rExtraLargeNav = carousel.data("r-extra-large-nav"),
      rExtraLargeDots = carousel.data("r-extra-large-dots"),
      center = carousel.data("center"),
      custom_nav = carousel.data("custom-nav") || "";
    carousel.addClass("owl-carousel");
    var owl = carousel.owlCarousel({
      loop: loop ? true : false,
      animateOut: Canimate,
      items: items ? items : 1,
      lazyLoad: true,
      margin: margin ? margin : 0,
      autoplay: autoplay ? true : false,
      autoplayTimeout: autoplayTimeout ? autoplayTimeout : 1000,
      smartSpeed: smartSpeed ? smartSpeed : 250,
      dots: dots ? true : false,
      nav: nav ? true : false,
      navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>',
      ],
      navSpeed: navSpeed ? true : false,
      center: center ? true : false,
      responsiveClass: true,
      responsive: {
        0: {
          items: rXsmall ? rXsmall : 1,
          nav: rXsmallNav ? true : false,
          dots: rXsmallDots ? true : false,
        },
        576: {
          items: rXmedium ? rXmedium : 2,
          nav: rXmediumNav ? true : false,
          dots: rXmediumDots ? true : false,
        },
        768: {
          items: rSmall ? rSmall : 3,
          nav: rSmallNav ? true : false,
          dots: rSmallDots ? true : false,
        },
        992: {
          items: rMedium ? rMedium : 4,
          nav: rMediumNav ? true : false,
          dots: rMediumDots ? true : false,
        },
        1200: {
          items: rLarge ? rLarge : 5,
          nav: rLargeNav ? true : false,
          dots: rLargeDots ? true : false,
        },
        1240: {
          items: rExtraLarge ? rExtraLarge : 5,
          nav: rExtraLargeNav ? true : false,
          dots: rExtraLargeDots ? true : false,
        },
      },
    });

    if (custom_nav) {
      var nav = $(custom_nav),
        nav_next = $(".rt-next", nav),
        nav_prev = $(".rt-prev", nav);

      nav_next.on("click", function (e) {
        e.preventDefault();
        owl.trigger("next.owl.carousel");
        return false;
      });

      nav_prev.on("click", function (e) {
        e.preventDefault();
        owl.trigger("prev.owl.carousel");
        return false;
      });
    }
  });

  // Price range filter
  let priceSlider = document.getElementById("price-range-filter");
  if (priceSlider) {
    noUiSlider.create(priceSlider, {
      start: [10, 70],
      connect: true,
      range: {
        min: 0,
        max: 100,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min"),
      marginMax = document.getElementById("price-range-max");
    priceSlider.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle] + "%";
      } else {
        marginMin.innerHTML = values[handle] + "%";
      }
    });
  }
  // Price range filter
  let priceSlider2 = document.getElementById("price-range-filter-2");
  if (priceSlider2) {
    noUiSlider.create(priceSlider2, {
      start: [0, 500],
      connect: true,
      range: {
        min: 0,
        max: 700,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min-2"),
      marginMax = document.getElementById("price-range-max-2");
    priceSlider2.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle];
      } else {
        marginMin.innerHTML = values[handle];
      }
    });
  }
  // Price range filter
  let priceSlider3 = document.getElementById("price-range-filter-3");
  if (priceSlider3) {
    noUiSlider.create(priceSlider3, {
      start: [0, 20000],
      connect: true,
      range: {
        min: 0,
        max: 30000,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min-3"),
      marginMax = document.getElementById("price-range-max-3");
    priceSlider3.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle];
      } else {
        marginMin.innerHTML = values[handle];
      }
    });
  }
  // Price range filter
  let priceSlider4 = document.getElementById("price-range-filter-4");
  if (priceSlider4) {
    noUiSlider.create(priceSlider4, {
      start: [0, 500000],
      connect: true,
      range: {
        min: 0,
        max: 700000,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min-4"),
      marginMax = document.getElementById("price-range-max-4");
    priceSlider4.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle];
      } else {
        marginMin.innerHTML = values[handle];
      }
    });
  }
  // Price range filter
  let priceSlider5 = document.getElementById("price-range-filter-5");
  if (priceSlider5) {
    noUiSlider.create(priceSlider5, {
      start: [0, 20000],
      connect: true,
      range: {
        min: 0,
        max: 30000,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min-5"),
      marginMax = document.getElementById("price-range-max-5");
    priceSlider5.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle];
      } else {
        marginMin.innerHTML = values[handle];
      }
    });
  }
  // Price range filter
  let priceSlider6 = document.getElementById("price-range-filter-6");
  if (priceSlider6) {
    noUiSlider.create(priceSlider6, {
      start: [0, 500],
      connect: true,
      range: {
        min: 0,
        max: 700,
      },
      format: wNumb({
        decimals: 0,
      }),
    });
    let marginMin = document.getElementById("price-range-min-6"),
      marginMax = document.getElementById("price-range-max-6");
    priceSlider6.noUiSlider.on("update", function (values, handle) {
      if (handle) {
        marginMax.innerHTML = values[handle];
      } else {
        marginMin.innerHTML = values[handle];
      }
    });
  }
})(jQuery);
