// Petderma Food — interações leves
(function () {
  // Menu mobile
  const header = document.querySelector('.header');
  const toggle = document.getElementById('navToggle');

  // Header compacto ao rolar
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 20);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }
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

  // Reveal on scroll — purely additive, never leaves content hidden
  var revealEls = Array.prototype.slice.call(
    document.querySelectorAll('.highlight,.value-card,.step,.post,.feature')
  );
  function showAll() {
    revealEls.forEach(function (el) {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  }
  var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduced && 'IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'none';
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function (el, i) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(26px) scale(.98)';
      // stagger por posição dentro do mesmo "grupo" (reinicia a cada 4)
      var delay = (i % 4) * 0.08;
      el.style.transition = 'opacity .6s ease ' + delay + 's, transform .6s cubic-bezier(.22,1,.36,1) ' + delay + 's';
      obs.observe(el);
    });
    // Safety net: if anything is still hidden after 2.5s, force-show it.
    setTimeout(showAll, 2500);
  } else {
    showAll();
  }
})();
