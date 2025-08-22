// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    window.scrollY > 50 ?
        navbar.style.backgroundColor = 'rgba(10, 10, 10, 0.98)' :
        navbar.style.backgroundColor = 'rgba(10, 10, 10, 0.95)';
})

// Mobile navigation toggle
const menuIcon = document.getElementById('menuIcon');
const navLinks = document.getElementById('navLinks');
const closeIcon = document.getElementById('closeIcon');

// Mobile navigation open
menuIcon.addEventListener('click', () => {
    navLinks.classList.add('open');
    menuIcon.classList.add('hide');
    document.body.style.overflow = 'hidden';
}); 

// Mobile navigation close
closeIcon.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuIcon.classList.remove('hide');
    document.body.style.overflow = '';
});
