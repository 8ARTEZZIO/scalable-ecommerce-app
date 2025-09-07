

document.addEventListener('DOMContentLoaded', () => {
          const el = document.getElementById('search-input');
          if (!el) return;

          let phrases;
          try { phrases = JSON.parse(el.dataset.phrases || '[]'); } catch { phrases = []; }
          if (!phrases.length) phrases = ["Wireless Headphones","Laptop Stand","Ceramic Mug","Running Shoes","LED Desk Lamp","Yoga Mat","Mechanical Keyboard"];

          for (let i = phrases.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [phrases[i], phrases[j]] = [phrases[j], phrases[i]];
          }

          let p = 0, c = 0, dir = 1, paused = false, timer;
          function step() {
            if (paused) { timer = setTimeout(step, 200); return; }
            const text = phrases[p];
            c += dir;
            el.placeholder = text.slice(0, Math.max(0, c));
            const typeSpeed = 70, deleteSpeed = 35, holdFull = 1100, holdEmpty = 250;
            if (dir > 0 && c >= text.length) { dir = -1; timer = setTimeout(step, holdFull); }
            else if (dir < 0 && c <= 0) { dir = 1; p = (p + 1) % phrases.length; timer = setTimeout(step, holdEmpty); }
            else { timer = setTimeout(step, dir > 0 ? typeSpeed : deleteSpeed); }
          }
          el.addEventListener('focus', () => { paused = true; });
          el.addEventListener('blur', () => { paused = false; });
          el.addEventListener('input', () => { if (el.value) el.placeholder = ''; });
          window.addEventListener('beforeunload', () => clearTimeout(timer));
          step();
        });