// ====== Mobile Menu Toggle ======
function toggleMenu() {
  const navList = document.getElementById('navList');
  navList.classList.toggle('open');
}

// ====== Dropdown Menu for Mobile ======
document.querySelectorAll('.navbar-item > a').forEach(link => {
  link.addEventListener('click', e => {
    const dropdown = link.nextElementSibling;
    if (window.innerWidth < 768 && dropdown) {
      e.preventDefault();
      dropdown.classList.toggle('open-dropdown');
    }
  });
});

// ====== Smooth Scroll for Anchor Links ======
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ====== Dynamic Hero Text Animation (optional) ======
const heroText = document.querySelector('.hero h1');
if (heroText) {
  let originalText = heroText.textContent;
  let index = 0;
  setInterval(() => {
    heroText.textContent =
      originalText.substring(0, index) + (index % 2 === 0 ? "|" : "");
    index = (index + 1) % (originalText.length + 1);
  }, 200);
}

// ====== Contact Form Submission ======
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', async e => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    try {
      const response = await fetch('http://127.0.0.1:8000/api/contacts/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, message })
      });

      if (response.ok) {
        alert('Message sent successfully!');
        contactForm.reset();
      } else {
        alert('Failed to send message.');
      }
    } catch (err) {
      console.error(err);
      alert('Error: Could not send message.');
    }
  });
}
