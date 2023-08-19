

const nav = document.querySelector("nav.nav-bar");

/* ---------------------  Sticky Navbar --------------------- */

// function stickyNavbar () {
//     nav.classList.toggle("scrolled", window.pageYOffset > 0);
// }
// window.addEventListener("scroll", stickyNavbar)

/* ---------------------  Menu Profile --------------------- */
let menu_profile = document.querySelector('.nav-bar .container .menu-profile-tab');

// var user_ava = document.querySelector('#user-ava');
//     user_ava.addEventListener("onclick", function(){
//   menu_profile.classList.toggle('active');
// })

/* ---------------------  Option booking bar --------------------- */
// let menu_booking = document.querySelector('.nav-bar .container .links .menu-booking-opt');

// document.querySelector('.nav-bar .container .links #nav-booking').onclick = () =>{
//   menu_booking.classList.toggle('active');
// }

// window.onscroll = () =>{
//   menu_booking.classList.remove('active');
// }

/* ---------------------  Menu bar --------------------- */

let navlink = document.querySelector('header .nav-bar .container .links');

// document.querySelector('#menu-btn').onclick = () =>{
//     navlink.classList.toggle('active');
// }

// window.onscroll = () =>{
//     navlink.classList.remove('active');
// }

/* --------------------- Schedule Box--------------------- */

const today = new Date();
const next_day = new Date();
const dateInput = document.getElementById("date");
const shift = document.getElementsByClassName("shift");
const serviceInfo = document.getElementById("serviceInfo");
const service_label = document.getElementById("service-label");
const service_price = document.getElementById("service-price");

// Cộng thêm 7 ngày
next_day.setDate(today.getDate() + 7);

// Lấy số thứ tự của ngày hiện tại
var current_day = today.getDay();
var default_date = today.toISOString().split("T")[0];
var lastValue = default_date;

// Đặt giá trị mặc định cho input date
dateInput.value = default_date;
dateInput.min = today.toISOString().split("T")[0];
dateInput.max = next_day.toISOString().split("T")[0];


/* --------------------- Shift Option--------------------- */


let current_shift = 0;

dateInput.addEventListener("input", function() {
    // Reset giá trị lựa chọn ca và ẩn thông tin dịch vụ
    for(s of shift){
        s.classList.remove("active");
    };
    serviceInfo.style.display = "none";
  });

function activeShift(){
    for(s of shift){
        s.classList.remove("active");
    };
    event.target.classList.add("active");
    current_shift = event.target.value;
    // '{{order_shift}}' = current_shift ;

    service_label.textContent = "Khám theo yêu cầu chuyên khoa Tai - Mũi - Họng";
    service_price.textContent = "500.000 đ";
    serviceInfo.style.display = "block";
}

var doctorId = '{{doctor.id}}';
var dateOrder = dateInput.value;

// var orderBtns = document.getElementsByClassName("submit");

// orderBtns.addEventListener('click',function(){
//   Appointment(doctorId,dateOrder,current_shift)
// })

function appointment(){
  var url = '/order/';
  fetch(url,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken' : csrftoken,
    },
    body: JSON.stringify({'doctorId': doctorId,'dateOrder':dateOrder,'shift':current_shift})
  })
  .then((response)=>{
    return response.json()
  })
  // .then((data)=>{
  //   console.log
  // })
}
