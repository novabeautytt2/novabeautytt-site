#!/usr/bin/env python3
"""Novabeautytt static site generator.
Writes plain HTML pages into the site root. Edit templates here, re-run,
commit, push. The output needs no build step to deploy."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "index":    {"file": "index.html",    "nav": "Home",     "num": "01",
                 "title": "Novabeautytt | Nails and Lash Extensions in Caroline Springs, Melbourne West",
                 "desc": "Novabeautytt is a nails and lashes studio in Caroline Springs, Melbourne's west. Gel X nail sets, lash extensions, and 2 in 1 appointments by one dedicated technician. Book now."},
    "services": {"file": "services.html", "nav": "Services", "num": "02",
                 "title": "Nail and Lash Prices | Novabeautytt Caroline Springs",
                 "desc": "Full price list for Gel X nails, lash extensions and refills, toe sets, 2 in 1 and duo appointments at Novabeautytt, Caroline Springs in Melbourne's west."},
    "gallery":  {"file": "gallery.html",  "nav": "Gallery",  "num": "03",
                 "title": "Nail Art and Lash Gallery | Novabeautytt Melbourne West",
                 "desc": "Real client sets from Novabeautytt: Gel X nail art, French tips, chrome, 3D details and wispy lash extensions, all done in Caroline Springs, Melbourne west."},
    "about":    {"file": "about.html",    "nav": "About",    "num": "04",
                 "title": "About Novabeautytt | Caroline Springs Nail and Lash Studio",
                 "desc": "The story behind Novabeautytt, a one-technician nail and lash studio serving Caroline Springs and Melbourne's western suburbs."},
    "booking":  {"file": "booking.html",  "nav": "Book",     "num": "05",
                 "title": "Book an Appointment | Novabeautytt Caroline Springs",
                 "desc": "Book nails, lashes or a 2 in 1 appointment at Novabeautytt in Caroline Springs. See live availability and secure your spot with a $10 deposit."},
    "policies": {"file": "policies.html", "nav": "Policies", "num": "06",
                 "title": "Booking Policies and FAQ | Novabeautytt",
                 "desc": "Deposits, cancellations, removals, prep and comfort policies for appointments at Novabeautytt, Caroline Springs."},
    "contact":  {"file": "contact.html",  "nav": "Contact",  "num": "07",
                 "title": "Contact Novabeautytt | Caroline Springs, Melbourne West",
                 "desc": "Get in touch with Novabeautytt on Instagram or TikTok @novabeautytt, or by email. Appointment-only studio serving Caroline Springs and Melbourne's west."},
}

NAV_ORDER = ["index", "services", "gallery", "about", "policies", "contact"]

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
    "priceRange": "$25-$120",
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
  <meta property="og:image" content="https://novabeautytt.com.au/assets/img/og-image.jpg">\n  <meta property="og:locale" content="en_AU">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="/assets/svg/favicon.svg">\n  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">\n  <meta name="theme-color" content="#DDD5D6">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
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
    <a class="wordmark" href="/" aria-label="Novabeautytt home">Novabeauty<span>tt</span></a>
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
        <a class="wordmark" href="/">Novabeauty<span>tt</span></a>
        <p>Nails and lashes, 2 in 1. An appointment-only studio in Caroline Springs, serving Melbourne's western suburbs.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/services">Services and prices</a></li>
          <li><a href="/gallery">Gallery</a></li>
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

ORCHID = '<img class="panel__flora panel__flora--br" src="/assets/svg/orchid.svg" alt="" aria-hidden="true">'
ORCHID_L = '<img class="panel__flora panel__flora--bl" src="/assets/svg/orchid.svg" alt="" aria-hidden="true">'

BLOSSOM = """<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3c1.8 2.4 1.8 4.8 0 6.4C10.2 7.8 10.2 5.4 12 3Zm6.5 3.2c-.3 3-1.9 4.8-4.3 5 .3-3 1.9-4.7 4.3-5ZM5.5 6.2c2.4.3 4 2 4.3 5-2.4-.2-4-2-4.3-5ZM12 12.5c2.6 0 4.6 1.6 5.4 4.6-3 .4-5-1-5.4-4.6Zm0 0c-.4 3.6-2.4 5-5.4 4.6.8-3 2.8-4.6 5.4-4.6Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><circle cx="12" cy="11" r="1.4" fill="currentColor"/></svg>"""


def lash_rows(kind):
    data = [
        ("Nova bare", "classics", 30, 15, 20),
        ("Nova doll", "doll eye", 40, 20, 30),
        ("Nova silk", "wispy", 50, 25, 40),
        ("Nova luxe", "volume", 60, 30, 50),
        ("Nova dewy", "wet look", 70, 35, 60),
        ("Nova Elite", "mega volume", 80, 40, 70),
    ]
    idx = {"full": 2, "r2": 3, "r3": 4}[kind]
    out = ""
    for row in data:
        acc = ' acc' if row[0] == "Nova silk" else ''
        out += f"""        <div class="price-row">
          <span class="name">{row[0]} <small>{row[1]}</small></span>
          <span class="rule"></span>
          <span class="amount{acc}">${row[idx]}</span>
        </div>\n"""
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
    <h1>Novabeautytt</h1>
    <p class="hero__sub">Gel X nails and lash extensions done in one place, by one dedicated technician. Caroline Springs, Melbourne West.</p>
    <div class="hero__ctas">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
      <a class="btn btn--ghost-light btn--lg" href="/services">View prices</a>
    </div>
    <ul class="hero__meta">
      <li>Appointment only</li>
      <li>One technician, start to finish</li>
      <li>$10 deposit secures your spot</li>
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
  <span class="watermark watermark--onbone watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z">
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
        <img src="/assets/img/thumb/nails-08.jpg" alt="Long stiletto Gel X set with 3D bows and chrome detail" loading="lazy">
        <div class="sig-card__body">
          <span class="sig-card__tag">Trending</span>
          <h3>Cat eye + chrome</h3>
          <p>Magnetic depth and mirror shine. The finish that moves when you do.</p>
          <span class="from">From $40</span>
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
  <span class="watermark watermark--br" aria-hidden="true">T9</span>
  <div class="wrap z">
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
      <span class="eyebrow">Fresh off the table</span>
      <h2>Recent sets</h2>
      <p class="lede">Real clients, real sets, zero stock photos. See the full gallery for more.</p>
    </div>
    <div class="ig-band reveal">
      <div class="ig-grid">
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-17.jpg" alt="Chrome and charm Gel X set" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-11.jpg" alt="Soft French ombre almond set" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/lashes-02.jpg" alt="Wispy natural lash extensions close up" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-07.jpg" alt="Pink stiletto set with fine art detail" loading="lazy"></a>
        <a class="ig-cell" href="/gallery"><img src="/assets/img/thumb/nails-05.jpg" alt="Long square French tip set" loading="lazy"></a>
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

<section class="cta-band">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z">
    <span class="eyebrow">Caroline Springs &middot; Melbourne West</span>
    <h2>Your next set is waiting</h2>
    <p class="lede">A $10 deposit secures your appointment. See live availability and pick a time that suits.</p>
    <a class="btn btn--green btn--lg js-book" href="/booking">Book now</a>
  </div>
</section>
"""

# ----------------------------------------------------------------- SERVICES
SERVICES = f"""
<section class="section section--blush" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">Services and prices</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">The menu</h1>
    <p class="lede" style="margin:16px auto 0">Every price below is exactly what you pay. Lashes, Gel X nails, toes, and combined appointments, all in Caroline Springs.</p>
  </div>
</section>

<section class="section" id="lashes">
  <div class="wrap">
    <div class="panel reveal">
      <span class="watermark watermark--tl" aria-hidden="true">T9</span>
      <div class="z">
        <h2 class="panel__title">Lash price list</h2>
        <p class="panel__note">Six styles, from barely-there classics to full mega volume. Nova silk wispy is the signature and the most requested set on the books.</p>
        <div class="price-group">
          <h3>Extensions &middot; full set</h3>
{lash_rows('full')}        </div>
        <div class="price-group">
          <h3>2 week refills</h3>
{lash_rows('r2')}        </div>
        <div class="price-group">
          <h3>3 week refills</h3>
{lash_rows('r3')}        </div>
        <p class="price-legend"><b>Refill rule:</b> refills need enough of your original set remaining. Past 3 weeks, book a fresh full set.</p>
      </div>
      {ORCHID}
    </div>
  </div>
</section>

<section class="section section--blush" id="nails">
  <div class="wrap">
    <div class="panel reveal" style="background:var(--bone)">
      <span class="watermark watermark--br" aria-hidden="true">T9</span>
      <div class="z">
        <h2 class="panel__title">Nail price list</h2>
        <p class="panel__note">Gel X extensions priced by length, with art tiers added on top. Length is measured in magnet sizes, from a clean short set to full XLong drama.</p>
        <div class="price-group">
          <h3>Lengths &middot; Gel X</h3>
          <div class="price-row"><span class="name">XShort <small>0 to 1 magnets</small></span><span class="rule"></span><span class="amount">$30</span></div>
          <div class="price-row"><span class="name">Short <small>2 to 3 magnets</small></span><span class="rule"></span><span class="amount">$40</span></div>
          <div class="price-row"><span class="name">Medium <small>4 to 5 magnets</small></span><span class="rule"></span><span class="amount">$50</span></div>
          <div class="price-row"><span class="name">Long <small>6 to 7 magnets</small></span><span class="rule"></span><span class="amount">$60</span></div>
          <div class="price-row"><span class="name">XLong <small>8 to 10 magnets</small></span><span class="rule"></span><span class="amount">$70</span></div>
        </div>
        <div class="price-group">
          <h3>Art tiers &middot; added to length price</h3>
          <div class="price-row"><span class="name">Tier 1 <small>simple accents, minimal art</small></span><span class="rule"></span><span class="amount acc">+$10</span></div>
          <div class="price-row"><span class="name">Tier 2 <small>detailed art on several nails</small></span><span class="rule"></span><span class="amount acc">+$15</span></div>
          <div class="price-row"><span class="name">Tier 3 <small>full set art, chrome, cat eye</small></span><span class="rule"></span><span class="amount acc">+$20</span></div>
          <div class="price-row"><span class="name">Tier 4 <small>complex art, 3D, charms</small></span><span class="rule"></span><span class="amount acc">+$25</span></div>
          <div class="price-row"><span class="name">Full French tip</span><span class="rule"></span><span class="amount acc">+$10</span></div>
        </div>
        <div class="price-group">
          <h3>Shapes</h3>
          <div class="chips">
            <span class="chip">Duck</span><span class="chip">Square</span><span class="chip">Stiletto</span><span class="chip">Coffin</span><span class="chip">Almond</span>
          </div>
        </div>
        <p class="price-legend">Send your inspo pic when booking and the right tier is confirmed before your appointment. No surprises on the day.</p>
      </div>
      {ORCHID_L}
    </div>
  </div>
</section>

<section class="section" id="toes">
  <div class="wrap">
    <div class="panel reveal">
      <span class="watermark watermark--tl" aria-hidden="true">T9</span>
      <div class="z">
        <h2 class="panel__title">Toe sets</h2>
        <p class="panel__note">Gel X toe sets. Please arrive with clean feet and toenails in workable condition so the tips can be fitted properly. Message on Instagram if unsure.</p>
        <div class="price-group">
          <div class="price-row"><span class="name">All white toes</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">Whole colour</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">Cat eye</span><span class="rule"></span><span class="amount">$25</span></div>
          <div class="price-row"><span class="name">French tip</span><span class="rule"></span><span class="amount">$35</span></div>
          <div class="price-row"><span class="name">Designs</span><span class="rule"></span><span class="amount acc">+$5</span></div>
          <div class="price-row"><span class="name">3D flowers</span><span class="rule"></span><span class="amount acc">+$5</span></div>
        </div>
      </div>
      {ORCHID}
    </div>
  </div>
</section>

<section class="section section--blush" id="two-in-one">
  <span class="watermark watermark--br" aria-hidden="true">T9</span>
  <div class="wrap z">
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
      {ORCHID_L}
    </div>
    <div class="center" style="margin-top:clamp(36px,6vw,56px)">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book your appointment</a>
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- GALLERY
GALLERY_ITEMS = [
    ("nails-08", "nails", "Long stiletto Gel X set with 3D bows"),
    ("lashes-03", "lashes", "Wispy lash extensions close up"),
    ("nails-17", "nails", "Chrome Gel X set with charms"),
    ("besties-04", "besties", "Friends in a circle showing matching sets"),
    ("nails-11", "nails", "Soft French ombre almond nails"),
    ("nails-05", "nails", "Long square French tip set"),
    ("lashes-02", "lashes", "Natural volume lash set close up"),
    ("nails-07", "nails", "Pink stiletto set with fine detail"),
    ("besties-06", "besties", "Group photo after duo appointments"),
    ("nails-04", "nails", "Two hands showing French Gel X sets"),
    ("nails-14", "nails", "Almond ombre set with shimmer"),
    ("lashes-04", "lashes", "Doll eye lash extensions close up"),
    ("nails-01", "nails", "French tip set with gold jewellery"),
    ("besties-02", "besties", "Besties circle overhead shot"),
    ("nails-09", "nails", "Stiletto set with white floral art"),
    ("nails-06", "nails", "Long French set with charm detail"),
    ("portrait-02", "besties", "Client showing a finished set"),
    ("nails-10", "nails", "French tips over lace"),
    ("lashes-01", "lashes", "Wispy hybrid lash set"),
    ("nails-12", "nails", "Neutral French set with ring stack"),
    ("besties-08", "besties", "Circle of hands with fresh sets"),
    ("nails-15", "nails", "Soft pink almond set"),
    ("nails-16", "nails", "Black and chrome art set"),
    ("besties-03", "besties", "Group of friends with matching nails"),
    ("nails-13", "nails", "White tip Gel X set close up"),
    ("lashes-05", "lashes", "Lash lift and extension detail"),
    ("nails-02", "nails", "Long coffin French set"),
    ("besties-05", "besties", "Friends lying in a circle"),
    ("nails-03", "nails", "French set with cross necklace"),
    ("portrait-03", "besties", "Client portrait with fresh lashes"),
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
    return f"""
<section class="section section--blush" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">The portfolio</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">Gallery</h1>
    <p class="lede" style="margin:16px auto 0">Every photo here is a real Novabeautytt client. Tap any set to view it up close, and screenshot freely for your inspo folder.</p>
  </div>
</section>

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

# ----------------------------------------------------------------- ABOUT
ABOUT = f"""
<section class="section section--blush" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">The studio</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">About</h1>
    <p class="lede" style="margin:16px auto 0">One technician. One chair. Every set done start to finish by the same hands.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media split__media--offset reveal">
        <img src="/assets/img/full/portrait-03.jpg" alt="Portrait of a Novabeautytt client with a fresh lash set" loading="lazy">
        <span class="frame"></span>
      </div>
      <div class="split__body reveal">
        <span class="eyebrow">The story</span>
        <h2>Meet Novabeautytt</h2>
        <!-- ABOUT BIO SLOT
             Replace this block with the real bio text when ready.
             Keep it to roughly 2 to 4 short paragraphs for this layout. -->
        <div class="about-slot">
          <p>Bio content slot. The real story goes here: how Novabeautytt started, the love for the craft, and what clients can expect when they sit down in the chair. Two to four short paragraphs fits this space perfectly.</p>
        </div>
        <!-- END ABOUT BIO SLOT -->
        <ul class="ticks">
          <li>Based in Caroline Springs, serving Melbourne's western suburbs</li>
          <li>Nails and lashes under one roof, the 2 in 1 way</li>
          <li>Appointment only, so every session is one on one</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--blush">
  <span class="watermark watermark--br" aria-hidden="true">T9</span>
  <div class="wrap z">
    <div class="section-head center reveal">
      <span class="eyebrow">How it feels</span>
      <h2>The appointment experience</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <h3>Settle in</h3>
        <p>Appointment-only means the studio is yours for the session. Snacks and water are always provided, especially for longer 2 in 1 bookings.</p>
      </div>
      <div class="step reveal">
        <h3>Your set, your way</h3>
        <p>Bring inspo photos or talk it through on the day. Shape, length, tier and finish are all confirmed before anything starts.</p>
      </div>
      <div class="step reveal">
        <h3>Camera optional</h3>
        <p>Photos and videos of finished sets are only ever taken with your okay. Prefer close-up shots only, or none at all? Just say so. Zero pressure.</p>
      </div>
    </div>
    <div class="center" style="margin-top:clamp(36px,6vw,56px)">
      <a class="btn btn--green btn--lg js-book" href="/booking">Book your visit</a>
    </div>
  </div>
</section>
"""

# ----------------------------------------------------------------- BOOKING
BOOKING = f"""
<section class="section book-hero" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">Live availability</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">Book now</h1>
    <p class="lede" style="margin:16px auto 0">No fixed hours, just real availability. Pick a time that suits, pay the $10 deposit, and your spot is locked in.</p>
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
        <h3>Secure it</h3>
        <p>A $10 deposit confirms your appointment and comes off your final total. Send design inspo with your shape and length after booking.</p>
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
POLICIES = f"""
<section class="section section--blush" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">The fine print, made friendly</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">Policies + FAQ</h1>
    <p class="lede" style="margin:16px auto 0">Everything you need to know before your appointment. By booking, you agree to these terms.</p>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:820px">
    <details class="acc-item reveal" open>
      <summary>Deposits <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>A <strong>$10 deposit</strong> is required to secure your booking and goes towards your final payment. Appointments are not confirmed until the deposit is paid.</p>
      </div>
    </details>
    <details class="acc-item reveal">
      <summary>Cancellations + reschedules <span class="ind">+</span></summary>
      <div class="acc-body">
        <p>A minimum of <strong>24 to 48 hours notice</strong> is required for cancellations or reschedules. Late changes or no-shows will result in loss of deposit.</p>
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
CONTACT = f"""
<section class="section section--blush" style="padding-bottom:clamp(40px,6vw,64px)">
  <span class="watermark watermark--tl" aria-hidden="true">T9</span>
  <div class="wrap z center">
    <span class="eyebrow">Say hello</span>
    <h1 style="font-size:clamp(1.9rem,7vw,3.6rem)">Contact</h1>
    <p class="lede" style="margin:16px auto 0">Instagram DM is the fastest way to reach the studio. Bookings, questions, inspo checks, all welcome.</p>
  </div>
</section>

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
        "about": ABOUT, "booking": BOOKING, "policies": POLICIES, "contact": CONTACT,
    }
    for key, body in bodies.items():
        html = head(key) + header(key) + body + FOOTER
        path = os.path.join(ROOT, PAGES[key]["file"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", PAGES[key]["file"])


if __name__ == "__main__":
    build()
