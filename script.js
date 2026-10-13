const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');
const year = document.getElementById('year');

year.textContent = new Date().getFullYear();

toggle.addEventListener('click', () => {
  const isOpen = nav.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(isOpen));
});

nav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  });
});

// Links from article pages can return to a section of the framed home page.
if (window.parent !== window && !window.location.hash) {
  try {
    const syncHomeSection = () => {
      const hash = window.parent.location.hash;
      if (hash && window.location.hash !== hash) window.location.hash = hash;
    };
    syncHomeSection();
    window.parent.addEventListener('hashchange', syncHomeSection);
  } catch {
    // A third-party embed cannot read its parent location.
  }
}
