# Eigen.wear

A digital closet that runs entirely in your browser. Photograph your clothes, and Eigen.wear plans colour-matched outfits for the week.

- **Private by design.** No account, no server, no cloud uploads, no AI. Everything is stored on your device (IndexedDB and localStorage).
- **Works offline.** Installable as a home-screen app (PWA).
- **One file.** The whole app is a single HTML file with no dependencies and no build step beyond wrapping it for installation.

## Features

- Closet for tops, bottoms, one-pieces, layers, suits, shoes, belts, watches, bags and accessories
- Quick adding: paste a cut-out photo (for example iPhone "Lift subject"), take a photo, or choose one
- Colour extraction (k-means in OKLab) with accent detection and tap-on-photo colour picking
- Weekly planner with strict, explained outfit scores (neutral, pop, tonal, analogous, contrast)
- Dress-code aware shoe pairing (sneakers, smart-casual, dress shoes, boots, heels and sandals)
- Suits on smart/formal days, optional belts, laundry tracking
- Favourites, "restyle" suggestions and backup / restore to a JSON file with photos

## Run it

You need Python 3 only.

```bash
python3 build.py
python3 -m http.server -d dist 8000
```

Open <http://localhost:8000>. The service worker and "Add to Home Screen" need HTTPS, or `localhost`.

## Deploy

`dist/` is a static site. Upload it to any static host:

- **GitHub Pages**: publish the contents of `dist/`
- **Cloudflare Pages**, **Netlify**, **Vercel**: set the output directory to `dist` and the build command to `python3 build.py`

`dist/_headers` sets `Cache-Control: no-cache` for Cloudflare Pages and Netlify so updates appear quickly.

## Project layout

```
src/app.html                the whole app (HTML, CSS, JavaScript)
src/sw.js                   service worker (offline cache, network-first pages)
src/manifest.webmanifest    PWA manifest
src/icons/                  app icons
src/_headers                cache headers for static hosts
build.py                    wraps the app for install and writes dist/
```

## Where is my data?

Photos and outfits live in your browser's storage for the site's address. A different address (or clearing site data) means a different, empty closet. Use **More → Backup** to export a JSON file and restore it anywhere.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bump `VERSION` in `src/app.html` for every release; the build copies it into the service worker cache name.

## Licence

[MIT](LICENSE)
