#!/usr/bin/env python3
"""Novabeautytt static site generator (brand v3: designed menu).
Writes plain HTML pages into the site root. Edit templates here, re-run,
commit, push. The output needs no build step to deploy."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "index":      {"file": "index.html",      "nav": "Home",       "num": "01",
                   "title": "Novabeautytt | Nails and Lash Extensions in Caroline Springs, Melbourne West",
                   "desc": "Novabeautytt is a nails and lashes studio in Caroline Springs, Melbourne's west. Gel X nail sets, lash extensions, and 2 in 1 appointments by one dedicated technician. Book now."},
    "services":   {"file": "services.html",   "nav": "Services",   "num": "02",
                   "title": "Nail and Lash Prices | Novabeautytt Caroline Springs",
                   "desc": "Full price list and style guide for Gel X nails, lash extensions and refills, toe sets, 2 in 1 and duo appointments at Novabeautytt, Caroline Springs in Melbourne's west."},
    "gallery":    {"file": "gallery.html",    "nav": "Gallery",    "num": "03",
                   "title": "Nail Art and Lash Gallery | Novabeautytt Melbourne West",
                   "desc": "Real client sets from Novabeautytt: Gel X nail art, French tips, chrome, 3D details and wispy lash extensions, all done in Caroline Springs, Melbourne west."},
    "experience": {"file": "experience.html", "nav": "Experience", "num": "04",
                   "title": "The Novabeautytt Experience | Prep, Aftercare and What to Expect",
                   "desc": "What a Novabeautytt appointment feels like: how to prep, how long sets take, aftercare for lashes and Gel X nails, and the comfort-first studio policy."},
    "booking":    {"file": "booking.html",    "nav": "Book",       "num": "05",
                   "title": "Book an Appointment | Novabeautytt Caroline Springs",
                   "desc": "Book nails, lashes or a 2 in 1 appointment at Novabeautytt in Caroline Springs. See availability and lock in a time that suits."},
    "policies":   {"file": "policies.html",   "nav": "Policies",   "num": "06",
                   "title": "Booking Policies and FAQ | Novabeautytt",
                   "desc": "Cancellations, removals, prep and comfort policies for appointments at Novabeautytt, Caroline Springs."},
    "contact":    {"file": "contact.html",    "nav": "Contact",    "num": "07",
                   "title": "Contact Novabeautytt | Caroline Springs, Melbourne West",
                   "desc": "Get in touch with Novabeautytt on Instagram or TikTok @novabeautytt, or by email. Appointment-only studio serving Caroline Springs and Melbourne's west."},
}

NAV_ORDER = ["index", "services", "gallery", "experience", "policies", "contact"]

def url_of(key):
    return "/" if key == "index" else "/" + PAGES[key]["file"].replace(".html", "")

IG = "https://www.instagram.com/novabeautytt"
TT = "https://www.tiktok.com/@novabeautytt"
EMAIL = "novabeautytt@gmail.com"


def head(page):
    p = PAGES[page]
    canonical = "https://novabeautytt.com.au" + ("/" if page == "index" else url_of(page))
    schema = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "NailSalon",
    "name": "Novabeautytt",
    "slogan": "2 in 1. Nails and lashes, one appointment.",
    "url": "https://novabeautytt.com.au",
    "email": "mailto:novabeautytt@gmail.com",
    "image": "https://novabeautytt.com.au/assets/img/og-image.jpg",
    "logo": "https://novabeautytt.com.au/assets/img/logo.png",
    "priceRange": "$10-$95",
    "address": {"@type": "PostalAddress", "addressLocality": "Caroline Springs", "addressRegion": "VIC", "addressCountry": "AU"},
    "areaServed": ["Caroline Springs", "Taylors Hill", "Hillside", "Sydenham", "Sunshine", "Deer Park", "St Albans", "Melbourne West"],
    "sameAs": ["https://www.instagram.com/novabeautytt", "https://www.tiktok.com/@novabeautytt"],
    "makesOffer": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Gel X nail extensions"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Eyelash extensions"}},
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "2 in 1 nails and lashes appointment"}}
    ]
  }
  </script>""" if page == "index" else ""
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['title']}</title>
  <meta name="description" content="{p['desc']}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Novabeautytt">
  <meta property="og:title" content="{p['title']}">
  <meta property="og:description" content="{p['desc']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://novabeautytt.com.au/assets/img/og-image.jpg">
  <meta property="og:locale" content="en_AU">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="/assets/svg/favicon.svg">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta name="theme-color" content="#F5E4D2">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
  <script>document.documentElement.classList.add('js')</script>{schema}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(page):
    links = ""
    mm_links = ""
    for i, key in enumerate(NAV_ORDER, 1):
        p = PAGES[key]
        cur = ' aria-current="page"' if key == page else ""
        links += f'      <a href="{url_of(key)}"{cur}>{p["nav"]}</a>\n'
        mm_links += (f'      <li><a class="mm-link" href="{url_of(key)}"{cur}>'
                     f'<span class="mm-num">{i:02d}</span>{p["nav"]}</a></li>\n')
    return f"""<header class="header">
  <div class="wrap header__inner">
    <a class="wordmark" href="/" aria-label="Novabeautytt home">
      <img src="/assets/img/logo.png" alt="Novabeautytt" width="1000" height="202">
    </a>
    <nav class="nav" aria-label="Main">
{links}    </nav>
    <a class="btn btn--green header__book js-book" href="/booking">Book now</a>
    <button class="burger" aria-expanded="false" aria-label="Open menu"><span></span></button>
  </div>
</header>

<div class="mobile-menu" role="dialog" aria-label="Menu">
  <nav aria-label="Mobile">
    <ul>
{mm_links}    </ul>
  </nav>
  <div class="mobile-menu__foot">
    <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
    <div class="mm-socials">
      <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
      <a href="{TT}" target="_blank" rel="noopener">TikTok</a>
      <a href="mailto:{EMAIL}">Email</a>
    </div>
  </div>
</div>

<main id="main">
"""


FOOTER = f"""</main>

<div class="fab-book"><a class="btn btn--green js-book" href="/booking">Book now</a></div>

<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="wordmark" href="/" aria-label="Novabeautytt home">
          <img src="/assets/img/logo-cream.png" alt="Novabeautytt" width="1000" height="202">
        </a>
        <p>Nails and lashes, 2 in 1. An appointment-only studio in Caroline Springs, serving Melbourne's western suburbs.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/services">Services and prices</a></li>
          <li><a href="/gallery">Gallery</a></li>
          <li><a href="/experience">The experience</a></li>
          <li><a href="/booking">Book an appointment</a></li>
          <li><a href="/policies">Policies and FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Say hello</h4>
        <ul>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram @novabeautytt</a></li>
          <li><a href="{TT}" target="_blank" rel="noopener">TikTok @novabeautytt</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Caroline Springs, Melbourne West</li>
        </ul>
      </div>
    </div>
    <div class="footer__bar">
      <span>&copy; <span data-year>2026</span> Novabeautytt. All rights reserved.</span>
      <span>Caroline Springs &middot; Taylors Hill &middot; Hillside &middot; Sydenham &middot; Deer Park &middot; St Albans</span>
    </div>
  </div>
</footer>

<script src="/assets/js/main.js"></script>
</body>
</html>
"""

def flora(name, pos="br", extra=""):
    """Decorative botanical accent. pos: br|bl (panel corners)."""
    cls = f"panel__flora panel__flora--{pos}"
    if extra: cls += f" {extra}"
    return f'<img class="{cls}" src="/assets/img/flora/{name}.webp" alt="" aria-hidden="true" loading="lazy">'

FLORA_TOES     = flora("pink-orchid", "br")
FLORA_REMOVALS = flora("pink-sprig", "bl")
FLORA_LASH_AC  = flora("pink-lily", "br")
FLORA_NAIL_AC  = flora("pink-sprig", "bl")

BLOSSOM = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3c1.8 2.4 1.8 4.8 0 6.4C10.2 7.8 10.2 5.4 12 3Zm6.5 3.2c-.3 3-1.9 4.8-4.3 5 .3-3 1.9-4.7 4.3-5ZM5.5 6.2c2.4.3 4 2 4.3 5-2.4-.2-4-2-4.3-5ZM12 12.5c2.6 0 4.6 1.6 5.4 4.6-3 .4-5-1-5.4-4.6Zm0 0c-.4 3.6-2.4 5-5.4 4.6.8-3 2.8-4.6 5.4-4.6Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><circle cx="12" cy="11" r="1.4" fill="currentColor"/></svg>"""


def page_hero(eyebrow, title, lede):
    """Shared page header. One class in CSS instead of inline styles on
    every page, so the whole site's page heads stay in step."""
    return f"""
<section class="section section--blush page-hero">
  <img class="page-hero__flora" src="/assets/img/flora/pink-bouquet.webp" alt="" aria-hidden="true">
  <div class="wrap center">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
"""


# ----------------------------------------------------------- LASH MENU DATA
LASH_STYLES = [
    ("Nova bare", "classics", 30, 15, 20,
     "One featherlight extension on each natural lash. Clean length and definition that reads as your lashes, just better. The everyday no-makeup set."),
    ("Nova doll", "doll eye", 40, 20, 30,
     "Mapped with length through the centre of the eye for that wide-awake, doe-eyed effect. Softly opens the eyes and flatters almond and monolid shapes."),
    ("Nova silk", "wispy", 50, 25, 40,
     "The signature. Longer spikes layered through a soft base for texture and flutter. Airy, editorial, and unreal on camera without looking heavy."),
    ("Nova luxe", "volume", 60, 30, 50,
     "Handmade fans of ultra-fine lashes on each natural lash for full, fluffy density. The one to book if your inspo folder says full glam."),
    ("Nova dewy", "wet look", 70, 35, 60,
     "Closed fans styled into glossy, piecey spikes. The freshly-applied-mascara effect that is all over TikTok, made to last for weeks."),
    ("Nova Elite", "mega volume", 80, 40, 70,
     "Dense, ultra-fine mega fans for maximum drama. The boldest set on the menu, built for events, shoots, and main-character energy."),
]

# Lash density/length patterns per style, used to draw a tiny honest
# "map" of each set: (number of lashes, list of lengths in px).
_LASH_PATTERNS = {
    "Nova bare":  [7, 7, 7, 7, 7, 7, 7, 7, 7],
    "Nova doll":  [5, 6, 8, 10, 11, 11, 10, 8, 6, 5],
    "Nova silk":  [6, 12, 6, 11, 6, 13, 6, 11, 6, 12, 6, 11, 6],
    "Nova luxe":  [9] * 16,
    "Nova dewy":  [10, 12, 10, 0, 10, 12, 10, 0, 10, 12, 10, 0, 10, 12, 10],
    "Nova Elite": [12] * 21,
}


def lash_icon(name):
    """Draws a miniature lash map for a style: an eyelid arc with lashes
    whose count and length pattern reflect the real set. Structure that
    encodes information rather than decoration."""
    pattern = _LASH_PATTERNS[name]
    n = len(pattern)
    w, base_y = 72.0, 24.0
    strokes = ""
    for i, ln in enumerate(pattern):
        if ln == 0:
            continue  # gaps between dewy clusters
        t = i / (n - 1)
        x = 5 + t * (w - 10)
        # quadratic arc y from (5,24) via (36,15) to (67,24)
        y = (1 - t) ** 2 * base_y + 2 * (1 - t) * t * 15 + t ** 2 * base_y
        lean = (t - 0.5) * 6          # lashes fan outward from centre
        strokes += (f'<line x1="{x:.1f}" y1="{y:.1f}" '
                    f'x2="{x + lean:.1f}" y2="{y - ln:.1f}"/>')
    return (f'<svg viewBox="0 0 72 28" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" aria-hidden="true">'
            f'<path d="M5 24 Q36 15 67 24" stroke-width="1.8"/>{strokes}</svg>')


def lash_cards():
    out = ""
    for name, vibe, full, r2, r3, desc in LASH_STYLES:
        sig = name == "Nova silk"
        ribbon = ('        <span class="lash-card__ribbon">Signature &middot; most loved</span>\n'
                  '        <img class="lash-card__flora" src="/assets/img/flora/gold-lily.webp" alt="" aria-hidden="true" loading="lazy">\n'
                  if sig else '')
        out += f"""      <article class="lash-card{' lash-card--sig' if sig else ''} reveal">
{ribbon}        <div class="lash-card__ill">{lash_icon(name)}</div>
        <div class="lash-card__title"><h3>{name}</h3><span class="vibe">{vibe}</span></div>
        <p class="lash-card__desc">{desc}</p>
        <div class="lash-card__prices">
          <div class="pp pp--main"><span>Full set</span><b>${full}</b></div>
          <div class="pp"><span>2 wk refill</span><b>${r2}</b></div>
          <div class="pp"><span>3 wk refill</span><b>${r3}</b></div>
        </div>
      </article>
"""
    return out


# ------------------------------------------------------------ NAIL MENU DATA
NAIL_LENGTHS = [
    ("XShort", "0 to 1 magnets", 1,  30),
    ("Short",  "2 to 3 magnets", 3,  40),
    ("Medium", "4 to 5 magnets", 5,  50),
    ("Long",   "6 to 7 magnets", 7,  60),
    ("XLong",  "8 to 10 magnets", 10, 70),
]

ART_TIERS = [
    ("No added art", "length price only", 0),
    ("Tier 1", "simple accents, minimal art", 10),
    ("Tier 2", "detailed art on several nails", 15),
    ("Tier 3", "full set art, chrome, cat eye", 20),
    ("Tier 4", "complex art, 3D, charms", 25),
]


def length_rows():
    out = ""
    for name, magnets, lit, price in NAIL_LENGTHS:
        ticks = "".join('<i class="on"></i>' if i < lit else "<i></i>" for i in range(10))
        out += f"""          <button class="len" type="button" aria-pressed="false" data-price="{price}">
            <span class="len__name">{name} <small>{magnets}</small></span>
            <span class="len__ticks" aria-hidden="true">{ticks}</span>
            <span class="len__price">${price}</span>
          </button>
"""
    return out


def tier_cards():
    out = ""
    for name, detail, price in ART_TIERS:
        pressed = "true" if price == 0 else "false"
        amount = "+$" + str(price) if price else "$0"
        out += f"""          <button class="tier" type="button" aria-pressed="{pressed}" data-price="{price}">
            <span class="t-name">{name} <small>{detail}</small></span>
            <b>{amount}</b>
          </button>
"""
    return out


# ----------------------------------------------------------------- HOME
HOME = f"""
<section class="hero">
  <div class="hero__media">
    <img src="/assets/img/full/hero-besties-01.jpg"
         alt="Five friends lying in a circle showing off fresh Novabeautytt nail sets and lashes"
         fetchpriority="high">
  </div>
  <div class="wrap hero__inner">
    <span class="hero__badge">{BLOSSOM} 2 in 1 &middot; nails + lashes</span>
    <h1>Nails + lashes.<br>One appointment.</h1>
    <p class="hero__sub">Gel X sets and lash extensions done in one place, by one dedicated technician. Caroline Springs, Melbourne West.</p>
    <div class="hero__ctas">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
      <a class="btn btn--ghost-light btn--lg" href="/services">View prices</a>
    </div>
    <ul class="hero__meta">
      <li>Appointment only</li>
      <li>One technician, start to finish</li>
      <li>Your inspo pic, made real</li>
    </ul>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker__track">
    <span>Gel X sets</span><span>Wispy lashes</span><span>Cat eye</span><span>Chrome</span><span>3D flowers</span><span>French tips</span><span>2 in 1 appointments</span><span>Caroline Springs</span>
    <span>Gel X sets</span><span>Wispy lashes</span><span>Cat eye</span><span>Chrome</span><span>3D flowers</span><span>French tips</span><span>2 in 1 appointments</span><span>Caroline Springs</span>
  </div>
</div>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Signature services</span>
      <h2>The sets everyone books</h2>
      <p class="lede">Every set is built by hand, one client at a time. These are the looks living rent free on the feed right now.</p>
    </div>
    <div class="grid-3">
      <a class="sig-card reveal" href="/services#lashes">
        <img src="/assets/img/thumb/lashes-03.jpg" alt="Close up of wispy Nova silk lash extensions" loading="lazy">
        <div class="sig-card__body">
          <span class="sig-card__tag">Most loved</span>
          <h3>Nova silk</h3>
          <p>Wispy, feathered lashes that read natural in person and unreal on camera.</p>
          <span class="from">From $50</span>
        </div>
      </a>
      <a class="sig-card reveal" href="/services#nails">
        <img src="/assets/img/thumb/nails-19.jpg" alt="Long pink Gel X set with 3D flowers, pearls and charms" loading="lazy">
        <div class="sig-card__body">
          <span class="sig-card__tag">Trending</span>
          <h3>3D + charms</h3>
          <p>Hand-built florals, pearls and charms on a milky pink base. Straight off the feed.</p>
          <span class="from">Tier 4 art &middot; +$25 on any length</span>
        </div>
      </a>
      <a class="sig-card reveal" href="/services#two-in-one">
        <img src="/assets/img/thumb/besties-04.jpg" alt="Group of friends showing matching nail sets after a duo appointment" loading="lazy">
        <div class="sig-card__body">
          <span class="sig-card__tag">2 in 1</span>
          <h3>Nails + lashes</h3>
          <p>Both done in one sitting, one place, one person. Snacks provided.</p>
          <span class="from">One appointment</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap">
    <div class="split">
      <div class="split__media split__media--offset reveal">
        <img src="/assets/img/full/portrait-01.jpg" alt="Client showing a finished Novabeautytt set against a dark studio backdrop" loading="lazy">
        <span class="frame"></span>
      </div>
      <div class="split__body reveal">
        <span class="eyebrow">The 2 in 1 difference</span>
        <h2>One chair. Both looks.</h2>
        <p>Novabeautytt does what two separate bookings usually can't: lashes and nails in a single appointment, by the same technician, so everything matches and nothing gets rushed between salons.</p>
        <ul class="ticks">
          <li>Combined appointments run around 3.5 to 4 hours, with snacks and water provided</li>
          <li>Duo appointments let you and a friend book side by side</li>
          <li>Every set is one on one. No double booking, no waiting around</li>
        </ul>
        <a class="btn btn--green js-book" href="/booking">Book a 2 in 1</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">How it works</span>
      <h2>Booked to obsessed, in four steps</h2>
      <p class="lede">From first scroll to fresh set, the whole thing is designed to be easy.</p>
    </div>
    <ol class="flow">
      <li class="flow__step reveal">
        <span class="flow__num">01</span>
        <h3>Pick your set</h3>
        <p>Browse the <a class="in-link" href="/services">menu</a>: choose a lash style, or build a nail set from length, art tier and shape. Or go 2 in 1 and take both.</p>
      </li>
      <li class="flow__step reveal">
        <span class="flow__num">02</span>
        <h3>Book + send inspo</h3>
        <p>Lock in a time on the <a class="in-link" href="/booking">booking page</a>, then send design photos with your preferred shape and length so everything is confirmed before the day.</p>
      </li>
      <li class="flow__step reveal">
        <span class="flow__num">03</span>
        <h3>The appointment</h3>
        <p>One on one, at your pace. Mapping, shape and finish are all agreed before anything starts. <a class="in-link" href="/experience">See what to expect</a>.</p>
      </li>
      <li class="flow__step reveal">
        <span class="flow__num">04</span>
        <h3>Wear it for weeks</h3>
        <p>Leave with <a class="in-link" href="/experience#aftercare">aftercare that actually works</a>, then keep lashes full with refills every 2 to 3 weeks.</p>
      </li>
    </ol>
  </div>
</section>

<section class="stat-band" aria-label="The studio at a glance">
  <img class="stat-band__flora" src="/assets/img/flora/gold-sprig.webp" alt="" aria-hidden="true" loading="lazy">
  <div class="wrap stat-band__grid">
    <div class="stat reveal"><b>1</b><span>technician, start to finish</span></div>
    <div class="stat reveal"><b>6</b><span>mapped lash styles</span></div>
    <div class="stat reveal"><b>5</b><span>Gel X nail shapes</span></div>
    <div class="stat reveal"><b>2<i>in</i>1</b><span>both looks, one appointment</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Fresh off the table</span>
      <h2>Recent sets</h2>
      <p class="lede">Real clients, real sets, zero stock photos. See the full gallery for more.</p>
    </div>
    <div class="ig-band reveal">
      <div class="ig-grid">
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-19.jpg" alt="Pink Gel X set with 3D flowers and charms" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-20.jpg" alt="French set with gold bows and jewel charms" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/lashes-02.jpg" alt="Wispy natural lash extensions close up" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-17.jpg" alt="Chrome and charm Gel X set" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-11.jpg" alt="Soft French ombre almond set" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/besties-06.jpg" alt="Friends together after matching appointments" loading="lazy"></a>
      </div>
    </div>
    <div class="center" style="margin-top:34px">
      <a class="text-link" href="/gallery">See the full gallery</a>
      <span style="display:inline-block;width:26px"></span>
      <a class="text-link" href="{IG}" target="_blank" rel="noopener">Follow @novabeautytt</a>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Why one technician</span>
      <h2>Small studio, on purpose</h2>
      <p class="lede">Two bookings at two salons on two schedules never made sense. Novabeautytt was built around a different idea: one chair, one artist, and both looks designed together.</p>
    </div>
    <div class="why-grid">
      <div class="why reveal">
        {BLOSSOM}
        <h3>Same hands, both looks</h3>
        <p>The person mapping your lashes is the person building your nails, so shape, tone and vibe actually match.</p>
      </div>
      <div class="why reveal">
        {BLOSSOM}
        <h3>One on one, always</h3>
        <p>No double bookings, no waiting room. The studio and the full attention are yours for the whole session.</p>
      </div>
      <div class="why reveal">
        {BLOSSOM}
        <h3>Your inspo, honoured</h3>
        <p>Photos are checked before the day and the art tier is confirmed upfront, so the finished set matches the picture. No surprises.</p>
      </div>
      <div class="why reveal">
        {BLOSSOM}
        <h3>Comfort built in</h3>
        <p>Snacks and water on longer sittings, duo bookings for nervous first-timers, and photos only ever taken with your okay.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Nova notes</span>
      <h2>Know your set</h2>
      <p class="lede">A little lash and nail literacy goes a long way. The short version of the questions every first-timer asks.</p>
    </div>
    <div class="grid-3">
      <a class="note-card reveal" href="/services#good-to-know">
        <span class="note-card__k">Gel X 101</span>
        <h3>Why soft gel, not acrylic</h3>
        <p>Featherlight tips, no harsh drilling, no acrylic fumes, and a gentle soak-off when it's time for the next set.</p>
        <span class="text-link">Read on the menu</span>
      </a>
      <a class="note-card reveal" href="/services#good-to-know">
        <span class="note-card__k">Lash mapping</span>
        <h3>Designed for your eyes</h3>
        <p>Lengths and curls are planned zone by zone before a single lash goes on, so the style suits your eye shape, not a chart.</p>
        <span class="text-link">How mapping works</span>
      </a>
      <a class="note-card reveal" href="/experience#aftercare">
        <span class="note-card__k">Aftercare</span>
        <h3>Make it last for weeks</h3>
        <p>Cuticle oil, oil-free cleanser, a spoolie and a few small habits are the difference between two weeks and four.</p>
        <span class="text-link">Aftercare that works</span>
      </a>
    </div>
  </div>
</section>

<section class="cta-band">
  <img class="cta-band__flora cta-band__flora--r" src="/assets/img/flora/gold-bouquet.webp" alt="" aria-hidden="true" loading="lazy">
  <img class="cta-band__flora cta-band__flora--l" src="/assets/img/flora/gold-lily.webp" alt="" aria-hidden="true" loading="lazy">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--lime)">Caroline Springs &middot; Melbourne West</span>
    <h2>Your next set is waiting</h2>
    <p class="lede">Pick a time that suits, send your inspo, and turn up. The rest is handled.</p>
    <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
  </div>
</section>
"""

# ----------------------------------------------------------------- SERVICES
SERVICES = f"""{page_hero(
    "Services and prices",
    "The menu",
    "Every price below is exactly what you pay. Lashes, Gel X nails, toes, and combined appointments, all in Caroline Springs.")}
<nav class="subnav" aria-label="Menu sections">
  <div class="wrap subnav__track">
    <a href="#lashes">Lashes</a>
    <a href="#nails">Nails</a>
    <a href="#toes">Toes</a>
    <a href="#two-in-one">2 in 1</a>
    <a href="#removals">Removals</a>
    <a href="#good-to-know">Good to know</a>
  </div>
</nav>

<section class="section" id="lashes">
  <div class="wrap">
    <div class="menu-head reveal">
      <span class="eyebrow">Lash extensions</span>
      <h2>Six styles, mapped to your eyes</h2>
      <p class="lede">From barely-there classics to full mega volume. Every set is mapped to your eye shape before a single lash goes on, so the finished look is designed for your face, not copied off a chart.</p>
      <p class="menu-meta">Full sets take 1.5 to 2.5 hours &middot; refill pricing is on every card</p>
    </div>
    <div class="lash-deck">
{lash_cards()}    </div>
    <p class="price-legend reveal"><b>Refill rule:</b> extensions shed naturally with your lash cycle, so refills every 2 to 3 weeks keep the set full. Refills need enough of your original set remaining; past 3 weeks, book a fresh full set.</p>
  </div>
</section>

<section class="section section--blush" id="nails">
  <div class="wrap">
    <div class="menu-head reveal">
      <span class="eyebrow">Gel X nails</span>
      <h2>Build your set</h2>
      <p class="lede">All sets are Gel X: featherlight soft gel extensions bonded to your natural nail and cured under LED, with no harsh drilling and no acrylic fumes. Every set starts with a length; art is added on top.</p>
      <p class="menu-meta">Sets take 1.5 to 3 hours with art &middot; length is measured in magnet sizes</p>
    </div>
    <div class="build reveal" data-build>
      <div class="build__step">
        <h3><span class="build__num">1</span>Pick a length</h3>
        <div class="len-list" role="group" aria-label="Choose a length">
{length_rows()}        </div>
      </div>
      <div class="build__step">
        <h3><span class="build__num">2</span>Add art &middot; on top of the length price</h3>
        <div class="tier-grid" role="group" aria-label="Choose an art tier">
{tier_cards()}        </div>
        <label class="french"><input type="checkbox" id="frenchTip" data-price="10"> Full French tip <b>+$10</b></label>
      </div>
      <div class="build__step">
        <h3><span class="build__num">3</span>Pick a shape &middot; no extra cost</h3>
        <div class="chips">
          <span class="chip">Duck</span><span class="chip">Square</span><span class="chip">Stiletto</span><span class="chip">Coffin</span><span class="chip">Almond</span>
        </div>
      </div>
      <div class="build__total" data-build-total hidden>
        <span>Estimated set</span><b data-total>$30</b>
        <small>Estimate only. Send your inspo pic when booking and the exact tier is confirmed before your appointment. No surprises on the day.</small>
      </div>
    </div>
    <p class="price-legend reveal">Gel X is the perfect canvas for chrome, cat eye, ombre, hand-painted art and 3D work. Send your inspo pic when booking and the right tier is confirmed before your appointment. No surprises on the day.</p>
  </div>
</section>

<section class="section" id="toes">
  <div class="wrap">
    <div class="panel reveal">
      <div class="z">
        <h2 class="panel__title">Toe sets</h2>
        <p class="panel__note">Gel X toe sets with the same featherlight finish as a hand set. Please arrive with clean feet and toenails in workable condition so the tips can be fitted properly. Message on Instagram if unsure.</p>
        <div class="price-group">
          <div class="price-row"><span class="name">All white toes</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">Whole colour</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">Cat eye</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">French tip</span><span class="rule"></span><span class="amount">$35</span></div>
          <div class="price-row"><span class="name">Designs</span><span class="rule"></span><span class="amount acc">+$5</span></div>
          <div class="price-row"><span class="name">3D flowers</span><span class="rule"></span><span class="amount acc">+$5</span></div>
        </div>
      </div>
      {FLORA_TOES}
    </div>
  </div>
</section>

<section class="section section--blush" id="two-in-one">
  <div class="wrap">
    <div class="grid-2">
      <div class="panel reveal" style="background:var(--bone)">
        <div class="z">
          <h2 class="panel__title" style="font-size:clamp(1.3rem,4vw,1.8rem)">2 in 1</h2>
          <p class="panel__note" style="margin-bottom:0">Lashes and nails done in one place, in one appointment, by the same person. Combined appointments usually run 3.5 to 4 hours depending on the style, with snacks and water provided so you can settle in and relax. Message with the treatments you want and the times that suit when booking.</p>
        </div>
      </div>
      <div class="panel reveal" style="background:var(--bone)">
        <div class="z">
          <h2 class="panel__title" style="font-size:clamp(1.3rem,4vw,1.8rem)">Duo appointment</h2>
          <p class="panel__note" style="margin-bottom:0">Bring a friend. Duo appointments let you both book your chosen services at the same time and enjoy the experience side by side. Perfect if you would feel more at ease with your bestie right there, and yes, snacks and water are provided for two.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="removals">
  <div class="wrap">
    <div class="panel reveal">
      <div class="z">
        <h2 class="panel__title">Removals</h2>
        <p class="panel__note">Both lashes and Gel X sets are designed to come off gently. Lash extensions are dissolved with a professional remover that protects your natural lashes, and Gel X soaks off with acetone, never pried or drilled, so your natural nails stay healthy underneath.</p>
        <div class="price-group">
          <h3>Lash removals</h3>
          <div class="price-row"><span class="name">Sets applied at Novabeautytt</span><span class="rule"></span><span class="amount">$10</span></div>
          <div class="price-row"><span class="name">Sets applied elsewhere</span><span class="rule"></span><span class="amount">$15</span></div>
        </div>
        <div class="price-group">
          <h3>Nail removals</h3>
          <div class="price-row"><span class="name">Sets applied at Novabeautytt</span><span class="rule"></span><span class="amount">$10</span></div>
        </div>
        <p class="price-legend">Nail removals are offered for Novabeautytt sets only. Mention any removal when booking so enough time is set aside for your service.</p>
      </div>
      {FLORA_REMOVALS}
    </div>
  </div>
</section>

<section class="section section--blush" id="good-to-know">
  <div class="wrap" style="max-width:820px">
    <div class="menu-head reveal">
      <span class="eyebrow">Good to know</span>
      <h2>Nails + lashes, explained</h2>
      <p class="lede">The short answers to the questions every first-timer sends before booking.</p>
    </div>
    <details class="acc-item reveal">
      <summary>Gel X vs acrylic, in one minute <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Gel X sets are pre-shaped soft gel tips bonded to your natural nail and cured under LED light. They are featherlight, flex like real nails, and soak off gently in acetone when you're done. Acrylic is built from liquid and powder, sets much harder and heavier, and usually needs filing or drilling to remove, which is where natural nail damage tends to happen. That is why everything at Novabeautytt is Gel X: no harsh drilling, no acrylic fumes, and healthier natural nails underneath set after set.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>How lash mapping works <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Before any extensions go on, the eye is divided into zones and each zone is assigned a length and curl, like a blueprint for the finished set. Length through the centre opens the eye up (that's the Nova doll effect); longer spikes over a soft base create wispy texture (hello, Nova silk); an even map keeps things clean and natural. The map is drawn for your eye shape on the day, which is why the same style can look different, and right, on different faces.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Choosing a length that fits your life <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Nail length is measured in magnet sizes, from XShort at 0 to 1 magnets up to XLong at 8 to 10. Type all day, hit the gym, or work with your hands? XShort to Medium keeps things practical while still looking done. Booked for an event or a photo-heavy weekend? Long and XLong are where the drama lives. Not sure? Send an inspo pic when booking and the length gets talked through before the appointment.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>How long does a set last? <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>With the right prep and aftercare, Gel X sets are built to wear for weeks; small habits like daily cuticle oil and gloves for dishes are the difference between two weeks and four. Lash extensions shed with your natural lash cycle, so refills every 2 to 3 weeks keep a set looking full. The <a class="text-link" href="/experience#aftercare">aftercare guide</a> has the full routine.</p>
      </div>
    </details>
    <div class="center" style="margin-top:clamp(36px,6vw,56px)">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book your appointment</a>
      <p style="margin-top:18px"><a class="text-link" href="/experience">First time? Read what to expect</a></p>
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- GALLERY
GALLERY_ITEMS = [
    ("nails-19", "nails", "Pink Gel X set with 3D flowers, pearls and charms"),
    ("lashes-03", "lashes", "Wispy lash extensions close up"),
    ("nails-20", "nails", "French set with gold bows and jewel charms"),
    ("besties-04", "besties", "Friends in a circle showing matching sets"),
    ("nails-08", "nails", "Long stiletto Gel X set with 3D bows"),
    ("nails-17", "nails", "Chrome Gel X set with charms"),
    ("lashes-02", "lashes", "Natural volume lash set close up"),
    ("nails-11", "nails", "Soft French ombre almond nails"),
    ("besties-06", "besties", "Group photo after duo appointments"),
    ("nails-05", "nails", "Long square French tip set"),
    ("nails-07", "nails", "Pink stiletto set with fine detail"),
    ("lashes-04", "lashes", "Doll eye lash extensions close up"),
    ("nails-04", "nails", "Two hands showing French Gel X sets"),
    ("besties-02", "besties", "Besties circle overhead shot"),
    ("nails-14", "nails", "Almond ombre set with shimmer"),
    ("nails-01", "nails", "French tip set with gold jewellery"),
    ("portrait-02", "besties", "Client showing a finished set"),
    ("nails-09", "nails", "Stiletto set with white floral art"),
    ("lashes-01", "lashes", "Wispy hybrid lash set"),
    ("nails-06", "nails", "Long French set with charm detail"),
    ("besties-08", "besties", "Circle of hands with fresh sets"),
    ("nails-10", "nails", "French tips over lace"),
    ("nails-12", "nails", "Neutral French set with ring stack"),
    ("besties-03", "besties", "Group of friends with matching nails"),
    ("nails-15", "nails", "Soft pink almond set"),
    ("nails-16", "nails", "Black and chrome art set"),
    ("lashes-05", "lashes", "Lash lift and extension detail"),
    ("nails-02", "nails", "Long coffin French set"),
    ("besties-05", "besties", "Friends lying in a circle"),
    ("nails-03", "nails", "French set with cross necklace"),
    ("portrait-03", "besties", "Client portrait with fresh lashes"),
    ("nails-13", "nails", "White tip Gel X set close up"),
    ("nails-18", "nails", "Dark chrome stiletto set"),
    ("besties-07", "besties", "Group shot with fresh sets"),
]


def img_dims(rel):
    from PIL import Image as _I
    with _I.open(os.path.join(ROOT, rel)) as im:
        return im.size


def gallery_html():
    items = ""
    for name, cat, alt in GALLERY_ITEMS:
        w, h = img_dims(f"assets/img/thumb/{name}.jpg")
        items += f"""      <a class="masonry__item reveal" href="/assets/img/full/{name}.jpg" data-cat="{cat}" data-full="/assets/img/full/{name}.jpg">
        <img src="/assets/img/thumb/{name}.jpg" alt="{alt}" width="{w}" height="{h}" loading="lazy">
      </a>\n"""
    return f"""{page_hero(
        "The portfolio",
        "Gallery",
        "Every photo here is a real Novabeautytt client. Tap any set to view it up close, and screenshot freely for your inspo folder.")}
<section class="section">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter gallery">
      <button class="filter-btn is-active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="nails">Nails</button>
      <button class="filter-btn" data-filter="lashes">Lashes</button>
      <button class="filter-btn" data-filter="besties">Besties</button>
    </div>
    <div class="masonry">
{items}    </div>
    <div class="center" style="margin-top:44px">
      <p class="lede" style="margin:0 auto 22px">Found your next set? Send the screenshot with your booking.</p>
      <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
    </div>
  </div>
</section>

<div class="lightbox" role="dialog" aria-label="Image viewer">
  <button class="lightbox__close">Close &times;</button>
  <button class="lightbox__nav lightbox__nav--prev" aria-label="Previous image">&larr;</button>
  <img src="" alt="">
  <button class="lightbox__nav lightbox__nav--next" aria-label="Next image">&rarr;</button>
</div>
"""

# ----------------------------------------------------------------- EXPERIENCE
EXPERIENCE = f"""{page_hero(
    "First visit to fresh set",
    "The experience",
    "Everything to know before, during and after your appointment, so you walk in relaxed and walk out obsessed.")}
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media split__media--offset reveal">
        <img src="/assets/img/full/portrait-03.jpg" alt="Portrait of a Novabeautytt client with a fresh lash set" loading="lazy">
        <span class="frame"></span>
      </div>
      <div class="split__body reveal">
        <span class="eyebrow">In the chair</span>
        <h2>Your appointment, your pace</h2>
        <p>Novabeautytt is appointment-only, which means the studio is yours for the session. No queue behind you, no one rushing the details, and the same hands on your set from prep to finishing photo.</p>
        <ul class="ticks">
          <li>Lash sets usually take 1.5 to 2.5 hours depending on the style; nail sets 1.5 to 3 hours with art</li>
          <li>2 in 1 appointments run 3.5 to 4 hours, with snacks and water provided</li>
          <li>Bring your inspo photos, or talk it through on the day. Shape, length, mapping and finish are all confirmed before anything starts</li>
        </ul>
        <a class="btn btn--green js-book" href="/booking">Book your visit</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--blush" id="prep">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Come prepared</span>
      <h2>Before you arrive</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <h3>Nails</h3>
        <p>Come with clean, bare nails, or book a removal if you're wearing an old set. Gel X bonds best to a clean natural nail, and good prep is what makes a set last for weeks instead of days.</p>
      </div>
      <div class="step reveal">
        <h3>Lashes</h3>
        <p>Arrive with clean, makeup-free eyes. No mascara, no eyeliner, no strip lash glue. Skip the coffee right before if you can; relaxed eyes make for the neatest application.</p>
      </div>
      <div class="step reveal">
        <h3>Toes</h3>
        <p>For Gel X toe sets, feet should be cleaned and toenails in workable condition so the tips can be fitted properly. Not sure if yours qualify? Send a photo on Instagram before booking.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="aftercare">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Make it last</span>
      <h2>Aftercare that actually works</h2>
      <p class="lede">A great set is a team effort. These small habits are the difference between two weeks and four.</p>
    </div>
    <div class="grid-2">
      <div class="panel reveal">
        <div class="z">
          <h3 style="text-align:center;letter-spacing:.18em;margin-bottom:16px">Lashes</h3>
          <ul class="ticks">
            <li>Keep lashes completely dry for the first 24 hours while the adhesive cures. No steam, saunas or swimming</li>
            <li>Cleanse daily with an oil-free lash cleanser, and keep oil-based skincare and makeup away from the lash line</li>
            <li>Brush gently with a clean spoolie each morning to keep the set fluffy and separated</li>
            <li>Sleep on your back or on a silk pillowcase where you can. Friction is the number one set-killer</li>
            <li>Book refills every 2 to 3 weeks to stay full as your natural lashes cycle through</li>
          </ul>
        </div>
        {FLORA_LASH_AC}
      </div>
      <div class="panel reveal">
        <div class="z">
          <h3 style="text-align:center;letter-spacing:.18em;margin-bottom:16px">Gel X nails</h3>
          <ul class="ticks">
            <li>Cuticle oil daily. It keeps the gel flexible and the bond strong, and it's the single biggest thing you can do for wear time</li>
            <li>Wear gloves for dishes, cleaning products and long hot showers where you can</li>
            <li>Nails are jewels, not tools. Use a key or a spoon, not your fresh set</li>
            <li>If a tip lifts or pops, don't glue it or pick it. Message and it gets fixed properly</li>
            <li>When it's time, book a removal. Soaking off protects your natural nail; peeling takes layers of it with the gel</li>
          </ul>
        </div>
        {FLORA_NAIL_AC}
      </div>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="wrap" style="max-width:820px">
    <div class="center reveal">
      <span class="eyebrow">Comfort first</span>
      <h2 style="margin-bottom:16px">Camera optional, always</h2>
      <p class="lede" style="margin:0 auto 18px">Photos and videos of finished sets are only ever taken with your okay. Prefer close-up shots only, or none at all? Just say so before your appointment. Zero pressure, zero awkwardness.</p>
      <p class="lede" style="margin:0 auto">Feeling nervous about a first appointment is normal. Book a duo with a friend, bring your headphones, or just say it's your first time and everything gets explained as it happens.</p>
    </div>
    <div class="center" style="margin-top:clamp(36px,6vw,56px)">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book your visit</a>
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- BOOKING
BOOKING = f"""
<section class="section book-hero page-hero">
  <div class="wrap center">
    <span class="eyebrow">Live availability</span>
    <h1>Book now</h1>
    <p class="lede">No fixed hours, just real availability. Pick a time that suits and your spot is locked in.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="steps reveal">
      <div class="step">
        <h3>Choose your service</h3>
        <p>Nails, lashes, toes, or a 2 in 1. Check the <a class="text-link" href="/services">price list</a> for lengths, tiers and styles first.</p>
      </div>
      <div class="step">
        <h3>Pick a time</h3>
        <p>See what's genuinely available and choose a slot that works. Booking a removal or a 2 in 1? Mention it so enough time is set aside.</p>
      </div>
      <div class="step">
        <h3>Send your inspo</h3>
        <p>After booking, send design or inspiration photos with your preferred shape and length so everything is ready when you arrive.</p>
      </div>
    </div>

    <div class="fresha-slot reveal" data-fresha-slot>
      <!-- FRESHA EMBED SLOT
           When the Fresha booking link is live, paste it into FRESHA_URL
           at the top of assets/js/main.js and this section updates itself,
           along with every Book now button across the site. -->
      <span class="eyebrow">Booking calendar</span>
      <h2 style="font-size:clamp(1.3rem,4vw,1.9rem);margin-bottom:14px">Online booking is coming soon</h2>
      <p class="lede" style="margin:0 auto 26px">Until the booking calendar goes live, appointments are booked through Instagram. It takes two minutes.</p>
      <a class="btn btn--green btn--lg" href="{IG}" target="_blank" rel="noopener">Book via Instagram DM</a>
      <p style="margin-top:18px;font-size:.85rem;color:var(--ink-soft)">Send the date and time you want, plus design or inspo photos with your preferred shape and length.</p>
    </div>

    <div class="notice reveal">
      <strong>Before you book:</strong> please read the <a class="text-link" href="/policies">booking policies</a>. By booking, you agree to all terms and conditions. They exist to protect your time and keep every appointment running smoothly.
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- POLICIES
POLICIES = f"""{page_hero(
    "The fine print, made friendly",
    "Policies + FAQ",
    "Everything you need to know before your appointment. By booking, you agree to these terms.")}
<section class="section">
  <div class="wrap" style="max-width:820px">
    <details class="acc-item reveal" open>
      <summary>Cancellations + reschedules <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>A minimum of <strong>24 to 48 hours notice</strong> is required for cancellations or reschedules. Every appointment is one on one, so late changes and no-shows mean that time can't be offered to anyone else, and repeated late changes may affect future bookings.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Running late <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Please arrive on time so your service can be completed properly. If you are more than <strong>10 to 15 minutes late</strong>, your appointment may need to be shortened or rescheduled.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Before your appointment <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Please come with <strong>clean, bare nails</strong> unless a removal has been booked. Extra time and charges may apply for removals, long lengths, nail art, or complex designs.</p>
        <p>For Gel X toe sets, toenails need to be in workable condition and feet cleaned before the appointment so the tips can be fitted and applied properly. Not sure if yours qualify? Send a message on Instagram before booking.</p>
        <p>For lashes, arrive with clean, makeup-free eyes. The <a class="text-link" href="/experience">experience page</a> has the full prep rundown.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Removals <span class="ind">+</span></summary>
      <div class="acc-body">
        <p><strong>Lash removals</strong> can be added to your appointment: $10 for sets applied at Novabeautytt and $15 for lashes applied by another lash tech. Mention it when booking so enough time is allowed for your service.</p>
        <p><strong>Nail removals</strong> are $10 and offered for Novabeautytt sets only. Removals for work done by other nail techs are not currently offered, so please keep that in mind when booking.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Photos + videos <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Prefer not to have photos or videos taken? Just say so before your appointment. If close-up shots of the finished set are okay, that is greatly appreciated, but there is absolutely no pressure either way.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Refills <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>Lash refills are priced at 2 week and 3 week rates, listed on the <a class="text-link" href="/services#lashes">price list</a>. Refills need enough of the original set remaining; past three weeks, a fresh full set is the way to go.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>2 in 1 + duo appointments <span class="ind">+</span></summary>
      <div class="acc-body">
        <p><strong>2 in 1:</strong> lashes and nails in one sitting, usually 3.5 to 4 hours depending on the style and service. Snacks and water are provided so you can relax and feel comfortable throughout.</p>
        <p><strong>Duo:</strong> book with a friend and get your chosen services at the same time, side by side. A great way to feel more at ease, knowing your friend is right there with you.</p>
      </div>
    </details>

    <div class="notice reveal">
      Questions about anything here? Send a DM to <a class="text-link" href="{IG}" target="_blank" rel="noopener">@novabeautytt</a> before booking. Always happy to help.
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- CONTACT
CONTACT = f"""{page_hero(
    "Say hello",
    "Contact",
    "Instagram DM is the fastest way to reach the studio. Bookings, questions, inspo checks, all welcome.")}
<section class="section">
  <div class="wrap" style="max-width:720px">
    <div class="contact-list reveal">
      <a href="{IG}" target="_blank" rel="noopener">
        <span class="ic">{BLOSSOM}</span>
        <span><small>Instagram &middot; fastest reply</small>@novabeautytt</span>
      </a>
      <a href="{TT}" target="_blank" rel="noopener">
        <span class="ic">{BLOSSOM}</span>
        <span><small>TikTok</small>@novabeautytt</span>
      </a>
      <a href="mailto:{EMAIL}">
        <span class="ic">{BLOSSOM}</span>
        <span><small>Email</small>{EMAIL}</span>
      </a>
      <div>
        <span class="ic">{BLOSSOM}</span>
        <span><small>Studio</small>Caroline Springs, Melbourne West &middot; appointment only, address shared on booking</span>
      </div>
    </div>

    <div class="divider-flora" aria-hidden="true">{BLOSSOM}</div>

    <div class="center reveal">
      <span class="eyebrow">Service area</span>
      <h2 style="font-size:clamp(1.3rem,4vw,1.9rem);margin-bottom:14px">Melbourne's west, covered</h2>
      <p class="lede" style="margin:0 auto 26px">Clients visit from Caroline Springs, Taylors Hill, Hillside, Sydenham, Sunshine, Deer Park, St Albans and across Melbourne's western suburbs.</p>
      <a class="btn btn--green btn--lg js-book" href="/booking">Book an appointment</a>
    </div>
  </div>
</section>
"""


def build():
    bodies = {
        "index": HOME, "services": SERVICES, "gallery": gallery_html(),
        "experience": EXPERIENCE, "booking": BOOKING, "policies": POLICIES, "contact": CONTACT,
    }
    for key, body in bodies.items():
        html = head(key) + header(key) + body + FOOTER
        path = os.path.join(ROOT, PAGES[key]["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", PAGES[key]["file"])


if __name__ == "__main__":
    build()
