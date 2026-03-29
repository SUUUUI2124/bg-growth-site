// Scroll fade-in via Intersection Observer
(function () {
  var targets = document.querySelectorAll('.fade-in');

  if (!('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -30px 0px'
  });

  targets.forEach(function (el) { observer.observe(el); });
})();

// FAQ Accordion
(function () {
  var triggers = document.querySelectorAll('.accordion-trigger');

  triggers.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      var panel = btn.nextElementSibling;

      if (expanded) {
        btn.setAttribute('aria-expanded', 'false');
        panel.classList.remove('open');
        panel.setAttribute('hidden', '');
      } else {
        btn.setAttribute('aria-expanded', 'true');
        panel.removeAttribute('hidden');
        panel.offsetHeight;
        panel.classList.add('open');
      }
    });
  });
})();
