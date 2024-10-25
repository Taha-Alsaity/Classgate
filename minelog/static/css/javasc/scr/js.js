let nums = document.querySelectorAll(".nums .num");
let section = document.querySelector(".three");
let ssa = document.querySelector(".ssa");
let section2 = document.querySelector('.sec-3');
let talent = document.querySelector(".talent");
let babel = document.querySelector(".babel");
let started = false; // Function Started ? No
let list = document.querySelector('.list-m');


window.addEventListener('load', function() {
  document.querySelector('.sec-2').style.display = 'block';
  document.querySelector('.three').style.display = 'block';
  document.querySelector('.sec-3').style.display = 'block';
  document.querySelector('.fooo').style.display = 'block';
  document.querySelector('.load-con').style.display = 'none';
  document.querySelector('header').style.display = 'flex';
  


});


window.addEventListener('DOMContentLoaded',()=>{
  document.querySelector("body").style.opacity = '1';
});




window.onscroll = function () {

  if(screen.width < 630 ){
    if(window.scrollY >= section.offsetTop - 1200){
      ssa.style.opacity = '1';
      ssa.style.transform = 'translatex(0)';
      ssa.style.filter = 'blur(0)';
      ssa.style.transition = '900ms'
      talent.style.opacity = '1';
      talent.style.transform = 'translatex(0)';
      talent.style.filter = 'blur(0)';
      talent.style.transition = '1200ms'
      babel.style.opacity = '1';
      babel.style.transform = 'translatex(0)';
      babel.style.filter = 'blur(0)';
      babel.style.transition = '500ms'
      };

  };
  if (window.scrollY >= section2.offsetTop - 500) {
    document.querySelector('.online').style.opacity = '1';
    document.querySelector('.online').style.transform = 'translatex(0)';
    document.querySelector('.online').style.filter = 'blur(0)';
    document.querySelector('.online').style.transition = '600ms'

    document.querySelector('.online-2').style.opacity = '1';
    document.querySelector('.online-2').style.transform = 'translatex(0)';
    document.querySelector('.online-2').style.filter = 'blur(0)';
    document.querySelector('.online-2').style.transition = '1000ms'


    document.querySelector('.part-1').style.opacity = '1';
    document.querySelector('.part-1').style.transform = 'translatex(0)';
    document.querySelector('.part-1').style.filter = 'blur(0)';
    document.querySelector('.part-1').style.transition = '600ms'

    document.querySelector('.part-2').style.opacity = '1';
    document.querySelector('.part-2').style.transform = 'translatex(0)';
    document.querySelector('.part-2').style.filter = 'blur(0)';
    document.querySelector('.part-2').style.transition = '1000ms'
  }
  if(window.scrollY >= section.offsetTop - 900){
  ssa.style.opacity = '1';
  ssa.style.transform = 'translatex(0)';
  ssa.style.filter = 'blur(0)';
  ssa.style.transition = '900ms'
  talent.style.opacity = '1';
  talent.style.transform = 'translatex(0)';
  talent.style.filter = 'blur(0)';
  talent.style.transition = '1200ms'
  babel.style.opacity = '1';
  babel.style.transform = 'translatex(0)';
  babel.style.filter = 'blur(0)';
  babel.style.transition = '500ms'
  };

  if (window.scrollY >= section.offsetTop - 500) {

    if (!started) {
      nums.forEach((num) => startCount(num));
    }
    started = true;
  };
};

function startCount(el) {
  let goal = el.dataset.goal;
  let count = setInterval(() => {
    el.textContent++;
    if (el.textContent == goal) {
      clearInterval(count);
    };
  }, 2000 / goal);
};



list.addEventListener('click', function(){
  document.querySelector('.spans').style.transition = 'all 1s'
  document.querySelector('.spans').style.transform = 'translatey(0)'
})

document.querySelector('.exit i').addEventListener('click', function(){
  document.querySelector('.spans').style.transition = 'all 1s'
  document.querySelector('.spans').style.transform = 'translatey(-100%)'
})

document.querySelector('.v').addEventListener('click', function(){
  if(screen.width < 755){
  document.querySelector('.spans').style.transition = '0s'
  document.querySelector('.spans').style.transform = 'translatey(-100%)'
};
});



document.querySelector('.side').addEventListener('click', function(){

  document.querySelector('aside').style.transform = 'translatey(0)'
});

