var side_bar = document.querySelector(".side-bar");
var ham = document.querySelector(".ham p");
var closes = document.getElementById("close");

ham.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

closes.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

var nav1 = document.querySelector(".navbar1");
var val;
window.onscroll = function(){
    if(document.documentElement.scrollTop > 20){
        nav1.classList.add("sticky");
    }
    else{
        nav1.classList.remove("sticky");
    }
}

var password1 = document.getElementById("contactPassword");
        var password2 = document.getElementById("registerPassword");
        var span1 = document.querySelector(".span1");
        var span2 = document.querySelector(".span2");
        function toggleShow1(){
            if (password1.type === "password") {
                password1.setAttribute('type', 'text');
                span1.innerHTML = "<i class='fa-solid fa-eye'></i>";
                span1.style.color = "rgb(24,188,156)";
            }
            else{
                password1.setAttribute('type','password') ;
                span1.innerHTML = "<i class='fa-solid fa-eye-slash'></i>";
                span1.style.color = "black";
            }
        }

        function toggleShow2(){
            if (password2.type === "password") {
                password2.setAttribute('type', 'text');
                span2.innerHTML = "<i class='fa-solid fa-eye'></i>";
                span2.style.color = "rgb(24,188,156)";
            }
            else{
                password2.setAttribute('type','password') ;
                span2.innerHTML = "<i class='fa-solid fa-eye-slash'></i>";
                span2.style.color = "black";
            }
        }

        var login = document.getElementById("login");
        var register = document.getElementById("register");
        function Login(){
            login.style.display = "flex";
            register.style.display = "none";
        }
        function Register(){
            login.style.display = "none";
            register.style.display = "flex";
        }