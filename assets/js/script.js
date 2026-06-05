// Petderma Food — interações leves
(function () {
  // Menu mobile
  const header = document.querySelector('.header');
  const toggle = document.getElementById('navToggle');
  if (toggle && header) {
    toggle.addEventListener('click', function () {
      const open = header.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // fecha ao clicar num link
    header.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        header.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // FAQ — abre só um por vez (comportamento de acordeão)
  const accs = Array.from(document.querySelectorAll('.faq .acc'));
  accs.forEach(function (acc) {
    acc.addEventListener('toggle', function () {
      if (acc.open) {
        accs.forEach(function (other) {
          if (other !== acc) other.open = false;
        });
      }
    });
  });

  // Newsletter — feedback simples
  const form = document.querySelector('.newsletter__form');
  if (form) {
    form.addEventListener('submit', function () {
      const input = form.querySelector('input');
      const btn = form.querySelector('button');
      if (input && input.value && btn) {
        btn.textContent = 'Recebido! ✓';
        input.value = '';
        setTimeout(function () { btn.textContent = 'Quero receber'; }, 2500);
      }
    });
  }

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'none';
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.highlight,.value-card,.step,.post,.feature').forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(24px)';
      el.style.transition = 'opacity .5s ease, transform .5s ease';
      obs.observe(el);
    });
  }
})();
