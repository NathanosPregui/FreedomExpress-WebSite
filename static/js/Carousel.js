   var swiper = new Swiper(".mySwiper", {
    loop:true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      autoplay: {
        delay: 2000,
        disableOnInteraction: true,
    },
    });

    var sliders = [];


 var swiper = new Swiper(".mySwiper2", {
      loop:true,
      slidesPerView: 4,
      centeredSlides: true,
      spaceBetween: 30,
      grabCursor: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });


$('.swiper-container').each(function(index, element){

    $(this).addClass('s'+index);
    var slider = new Swiper('.s'+index, { /* Options here */ });
    sliders.push(slider);

});

$('.swiperproducts-container').each(function(index, element){

  $(this).addClass('s'+index);
  var slider = new Swiper('.s'+index, { /* Options here */ });
  sliders.push(slider);

});