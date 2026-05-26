// ── NAVBAR SCROLL EFFECT ───────────────────────────────────────────────────
window.addEventListener('scroll', () => {
  const nav = document.getElementById('mainNavbar');
  if (nav) {
    if (window.scrollY > 30) {
      nav.style.background = 'rgba(15,17,23,0.98)';
    } else {
      nav.style.background = 'rgba(15,17,23,0.85)';
    }
  }
});

// ── AUTO-DISMISS ALERTS ────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const alerts = document.querySelectorAll('.plant-alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 5000);
  });
});

// ── ANIMATED COUNTER ──────────────────────────────────────────────────────
function animateCounter(el, target, duration = 1000) {
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start += step;
    if (start >= target) { el.textContent = target; clearInterval(timer); return; }
    el.textContent = Math.floor(start);
  }, 16);
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.stat-card-num').forEach(el => {
    const val = parseFloat(el.textContent);
    if (!isNaN(val) && val > 0) {
      el.textContent = '0';
      const obs = new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) { animateCounter(el, val); obs.disconnect(); } });
      });
      obs.observe(el);
    }
  });
});

// ── DEMO BAR ANIMATION ────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const fill = document.querySelector('.demo-bar-fill');
  if (fill) {
    fill.style.width = '0%';
    setTimeout(() => { fill.style.transition = 'width 1.5s ease'; fill.style.width = '87%'; }, 800);
  }
});
