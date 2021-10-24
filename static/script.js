
var kp = document.querySelector('#kp')
var ti = document.querySelector('#ti')
var td = document.querySelector('#td')

var a = document.querySelector('#a')
var qdmax = document.querySelector('#qdmax')
var umax = document.querySelector('#umax')

var kp_v = document.querySelector('#kp_r')
var ti_v = document.querySelector('#ti_r')
var td_v = document.querySelector('#td_R')

var a_v = document.querySelector('#a_r')
var qdmax_v = document.querySelector('#qdmax_r')
var umax_v = document.querySelector('#umax_r')

kp.oninput = function(){
    kp_v.innerHTML = kp.value
}
ti.oninput = function(){
    ti_v.innerHTML = ti.value
}
td.oninput = function(){
    td_v.innerHTML = td.value
}

a.oninput = function(){
    a_v.innerHTML = a.value
}
qdmax.oninput = function(){
    qdmax_v.innerHTML = gdmax.value
}
umax.oninput = function(){
    umax_v.innerHTML = umax.value
}