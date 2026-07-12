/* ============================================================
   NOVABEAUTYTT site scripts
   ============================================================ */

/* ------------------------------------------------------------
   BOOKING CONFIG
   Paste the Fresha booking link between the quotes below and
   every "Book now" button across the site will point to it.
   Leave it empty and buttons point to the booking page, which
   explains how to book through Instagram in the meantime.
   ------------------------------------------------------------ */
const FRESHA_URL = "";

document.addEventListener("DOMContentLoaded", () => {

  /* Book buttons */
  if (FRESHA_URL) {
    document.querySelectorAll(".js-book").forEach(a => {
      a.setAttribute("href", FRESHA_URL);
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener");
    });
    const slot = document.querySelector("[data-fresha-slot]");
    if (slot) {
      slot.innerHTML =
        '<a class="btn btn--green btn--lg" href="' + FRESHA_URL +
        '" target="_blank" rel="noopener">Open the booking calendar</a>' +
        '<p style="margin-top:18px;font-size:.85rem;color:var(--ink-soft)">' +
        'Live availability, service selection and deposits are all handled securely through Fresha.</p>';
    }
  }

  /* Mobile menu */
  const burger = document.querySelector(".burger");
  const menu = document.querySelector(".mobile-menu");
  if (burger && menu) {
    burger.addEventListener("click", () => {
      const open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      burger.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      menu.classList.toggle("is-open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
    menu.querySelectorAll("a").forEach(a =>
      a.addEventListener("click", () => {
        burger.setAttribute("aria-expanded", "false");
        menu.classList.remove("is-open");
        document.body.style.overflow = "";
      })
    );
  }

  /* Floating book button appears after the hero */
  const fab = document.querySelector(".fab-book");
  if (fab) {
    const show = () => fab.classList.toggle("is-visible", window.scrollY > 420);
    window.addEventListener("scroll", show, { passive: true });
    show();
  }

  /* Scroll reveal */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add("is-in"));
  }

  /* Gallery filters */
  const filterBtns = document.querySelectorAll(".filter-btn");
  const items = document.querySelectorAll(".masonry__item");
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("is-active"));
      btn.classList.add("is-active");
      const f = btn.dataset.filter;
      items.forEach(it => {
        it.classList.toggle("is-hidden", f !== "all" && it.dataset.cat !== f);
      });
    });
  });

  /* Lightbox */
  const lb = document.querySelector(".lightbox");
  if (lb && items.length) {
    const lbImg = lb.querySelector("img");
    let current = 0;
    const visible = () => [...items].filter(i => !i.classList.contains("is-hidden"));

    const openAt = idx => {
      const list = visible();
      if (!list.length) return;
      current = (idx + list.length) % list.length;
      lbImg.src = list[current].dataset.full;
      lbImg.alt = list[current].querySelector("img").alt;
      lb.classList.add("is-open");
      document.body.style.overflow = "hidden";
    };
    const close = () => { lb.classList.remove("is-open"); document.body.style.overflow = ""; };

    items.forEach(it => it.addEventListener("click", e => {
      e.preventDefault();
      openAt(visible().indexOf(it));
    }));
    lb.querySelector(".lightbox__close").addEventListener("click", close);
    lb.querySelector(".lightbox__nav--prev").addEventListener("click", () => openAt(current - 1));
    lb.querySelector(".lightbox__nav--next").addEventListener("click", () => openAt(current + 1));
    lb.addEventListener("click", e => { if (e.target === lb) close(); });
    document.addEventListener("keydown", e => {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") openAt(current - 1);
      if (e.key === "ArrowRight") openAt(current + 1);
    });
  }

  /* Current year */
  document.querySelectorAll("[data-year]").forEach(el => el.textContent = new Date().getFullYear());
});
