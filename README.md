# alchapone

Landing page katalog streetwear interaktif (HTML, CSS, GSAP 3.13, Lenis smooth scroll).

## Live URL
- **Production**: [https://alchapone.pages.dev](https://alchapone.pages.dev)
- **GitHub Target**: [https://github.com/ngempetbuko-afk/alchapone](https://github.com/ngempetbuko-afk/alchapone)

## Local Development
Server berjalan pada port dedicated **47315** sesuai aturan per-project port:
```bash
python serve.py
```
Akses di browser: [http://127.0.0.1:47315/](http://127.0.0.1:47315/)

## Deployment
Deploy manual ke Cloudflare Pages menggunakan Wrangler CLI:
```bash
wrangler pages deploy . --project-name alchapone
```
