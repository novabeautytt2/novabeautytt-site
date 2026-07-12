# Novabeautytt — novabeautytt.com.au

Static website for Novabeautytt, a nail and lash studio in Caroline Springs,
Melbourne West. No build step required: the HTML in this folder is the site.

## Deploy with GitHub + Vercel (about 5 minutes)

1. Create a new GitHub repository (e.g. `novabeautytt-site`) and push this
   entire folder to it (all HTML files and the `assets` folder at the root).
2. Go to vercel.com, sign in with GitHub, click "Add New Project", and import
   the repository. Framework preset: **Other**. No build command, no output
   directory. Deploy.
3. In the Vercel project, open Settings → Domains and add
   `novabeautytt.com.au` (and `www.novabeautytt.com.au`). Vercel shows the
   DNS records to add at the domain registrar. Done.

Every future edit is: change a file, commit, push. Vercel redeploys
automatically.

The site uses clean URLs: pages live at `/services`, `/gallery`, `/booking`
and so on, with no `.html` in the address bar. `vercel.json` handles this
automatically on Vercel (the `.html` files stay in the repo; Vercel maps the
clean URL to the file).

**Previewing locally:** because of clean URLs, double-clicking the HTML
files or using `python3 -m http.server` will break navigation between
pages. To preview properly before deploying, run `npx serve .` in this
folder (it supports clean URLs out of the box), or just push to GitHub and
use Vercel's free preview deployments.

## The three things to update later

1. **Fresha booking link** — open `assets/js/main.js` and paste the link into
   `FRESHA_URL` at the top. Every "Book now" button across the site and the
   booking page calendar section update automatically.
2. **Colours** — the palette lives in `:root` at the top of
   `assets/css/style.css`, sampled from the logo and business card: deep
   plum ink, warm cream, forest green (the logo's tt), and chartreuse lime
   (the card's botanicals). Change any value there and the whole site
   updates.

## Logo files

The header uses `assets/img/logo.png` (transparent) and the footer uses
`assets/img/logo-cream.png` (cream version for the plum background). To
update either, replace the file and keep the same name.

## Adding or changing gallery photos

Drop optimised images into `assets/img/full/` (max ~1400px) and
`assets/img/thumb/` (max ~640px) with matching filenames, then copy one of
the `masonry__item` blocks in `gallery.html` and update the filename,
`data-cat` (`nails`, `lashes`, or `besties`) and alt text.

## Regenerating pages (optional)

`generate.py` produced the HTML and keeps header/footer consistent across
pages. Editing the HTML files directly is completely fine; only re-run
`python3 generate.py` if making structural changes across every page, and
note it will overwrite direct HTML edits.

## Also included

- `404.html` — branded not-found page, picked up automatically by Vercel.
- `assets/img/og-image.jpg` — the image shown when the site is shared in
  DMs or on socials. Swap it for any 1200x630 image to change the preview.
- `assets/apple-touch-icon.png` — the icon shown if someone saves the site
  to their phone home screen.

## Deliberately excluded (per the brief)

- No testimonials or reviews section, and no placeholder for one.
- No fixed business hours anywhere; all availability language points to the
  booking flow.
- No logo or business card in this pass.
