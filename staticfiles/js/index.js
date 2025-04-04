// message disappearing
setTimeout(function() {
    document.getElementById('welcome-message').style.display = 'none';
}, 3000);

document.getElementById('close-message').onclick = function() {
    document.getElementById('welcome-message').style.display = 'none';
};


// side navigation on small devices
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main-body").style.backgroundColor = "rgba(0,0,0,0.4)"; // Dim background
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main-body").style.backgroundColor = ""; // Reset background
}
