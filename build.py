"""Generates the Cozyware studio site (https://cozyware.app) in English (root), Ukrainian (uk/) and Russian (ru/).

Pages per language:
  /                      studio home
  /couchpad/             Couchpad app page
  /couchpad/support.html, /couchpad/privacy.html
  /support.html, /privacy.html   legacy URLs given to App Store Connect (same content, canonical -> /couchpad/)

Edit the texts (here and in texts_couchpad.py) and run: python3 build.py
After the app is live in the App Store set APP_LIVE = True.
"""
import os
from texts_couchpad import T as APP

DOMAIN = "https://cozyware.app"
HELLO = "hello@cozyware.app"
SUPPORT = "support@cozyware.app"
APP_ID = "6827098264"
APP_STORE_URL = f"https://apps.apple.com/app/id{APP_ID}"
APP_LIVE = False  # flip to True once Couchpad is approved and released

STYLE = """
:root{--bg:#0b0c10;--text:#e6e8ec;--dim:#8c919e;--amber:#ffb547;--line:#2b2e37}
*{box-sizing:border-box}
html{scroll-behavior:smooth;background:var(--bg)}
body{margin:0;background:radial-gradient(ellipse at top,#2a2214 0%,var(--bg) 55%) fixed;color:var(--text);
font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:40px 20px 64px}
header{display:flex;align-items:center;flex-wrap:wrap;gap:14px;margin-bottom:44px}
header img.logo{width:44px;height:44px;border-radius:11px;box-shadow:0 6px 20px rgba(0,0,0,.5)}
header .brand{color:var(--text);text-decoration:none;font:800 22px/1 ui-rounded,-apple-system,sans-serif;letter-spacing:-.3px}
nav{margin-left:auto;display:flex;flex-wrap:wrap;gap:18px;align-items:center}
nav a{color:var(--dim);text-decoration:none;font:600 15px/1.4 -apple-system,BlinkMacSystemFont,sans-serif}
nav a:hover,nav a.on{color:var(--amber)}
.langs{display:flex;gap:10px;padding-left:14px;border-left:1px solid var(--line)}
h1{font:800 40px/1.15 ui-rounded,-apple-system,sans-serif;margin:0 0 12px;letter-spacing:-.6px}
h2{font:700 21px/1.3 ui-rounded,-apple-system,sans-serif;margin:44px 0 10px;color:var(--amber)}
p,li{color:#cfd2d8} a{color:var(--amber)}
.lead{font-size:20px;color:var(--dim);margin:0 0 28px}
.card{background:linear-gradient(#24262e,#16171c);border:1px solid var(--line);border-radius:18px;padding:20px 22px;margin:14px 0}
.card h3{margin:0 0 6px;font-size:17px;color:var(--text)}
.card p{margin:0}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.grid .card{margin:0}
.app{display:flex;gap:18px;align-items:center;text-decoration:none;color:inherit}
.app img{width:72px;height:72px;border-radius:17px;flex:none;box-shadow:0 8px 24px rgba(0,0,0,.5)}
.app h3{font-size:19px}
.app .tag{color:var(--amber);font-weight:600;font-size:14px;margin:0 0 4px}
.app:hover{border-color:#4a3c22}
.hero{display:flex;gap:20px;align-items:center;margin-bottom:22px}
.hero img{width:84px;height:84px;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.55);flex:none}
.hero h1{margin:0}
.btns{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:8px 0 6px}
.btn{display:inline-block;background:linear-gradient(#ffb547,#ee7a19);color:#1a1205;font-weight:700;text-decoration:none;
padding:14px 26px;border-radius:999px;box-shadow:0 0 24px rgba(255,181,71,.35)}
.btn.ghost{background:none;color:var(--text);border:1px solid var(--line);box-shadow:none}
.btn.off{background:#23252c;color:var(--dim);box-shadow:none;cursor:default}
.shots{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 2px 18px;margin:0 -20px;padding-left:20px;padding-right:20px}
.shots img{height:360px;width:auto;border-radius:20px;scroll-snap-align:start;flex:none;border:1px solid var(--line)}
footer{margin-top:56px;color:var(--dim);font-size:14px;border-top:1px solid var(--line);padding-top:20px}
footer a{color:var(--dim)}
@media (max-width:640px){.grid{grid-template-columns:1fr}h1{font-size:31px}nav{margin-left:0;width:100%}.shots img{height:380px}}
@media (max-width:420px){.hero{flex-direction:column;align-items:flex-start}}
"""

STUDIO = {
"en": dict(
    tagline="Small apps, cozy by design.",
    lead="Cozyware is an independent studio making simple, private apps for iPhone. No accounts, no ads, no tracking — just tools that do one thing well.",
    desc="Cozyware is an independent studio making simple, private apps for iPhone.",
    apps_h="Our apps", app_tag="Simple TV remote",
    app_blurb="Control your TV from your iPhone over Wi-Fi. No hub, no account, no cloud.",
    learn="Learn more", principles_h="How we make apps",
    principles=[("Private by design", "Your data stays on your device. We don't run analytics, ads or trackers."),
                ("Fair and simple", "Clear prices, a free trial where it makes sense, and no dark patterns."),
                ("Calm interfaces", "Focused screens that do one job well and stay out of your way.")],
    contact_h="Say hello", contact_p="Questions, ideas or press? Write to <a href=\"mailto:{e}\">{e}</a>.",
    store="Download on the App Store", soon="Coming soon to the App Store",
    shots_h="See it in action",
    footer_studio="Cozyware — small apps, cozy by design.",
),
"uk": dict(
    tagline="Невеликі застосунки, затишні за задумом.",
    lead="Cozyware — незалежна студія, що створює прості й приватні застосунки для iPhone. Без акаунтів, реклами та стеження — лише інструменти, які добре роблять одну справу.",
    desc="Cozyware — незалежна студія, що створює прості й приватні застосунки для iPhone.",
    apps_h="Наші застосунки", app_tag="Простий пульт для ТВ",
    app_blurb="Керуйте телевізором з iPhone через Wi-Fi. Без хаба, без акаунта, без хмари.",
    learn="Докладніше", principles_h="Як ми робимо застосунки",
    principles=[("Приватність за замовчуванням", "Ваші дані залишаються на вашому пристрої. Ми не використовуємо аналітику, рекламу чи трекери."),
                ("Чесно й просто", "Зрозумілі ціни, безкоштовний пробний період там, де це доречно, і жодних темних патернів."),
                ("Спокійні інтерфейси", "Зосереджені екрани, що добре роблять одну справу й не заважають.")],
    contact_h="Привітайтеся", contact_p="Питання, ідеї чи преса? Пишіть на <a href=\"mailto:{e}\">{e}</a>.",
    store="Завантажити в App Store", soon="Незабаром в App Store",
    shots_h="Дивіться в дії",
    footer_studio="Cozyware — невеликі застосунки, затишні за задумом.",
),
"ru": dict(
    tagline="Небольшие приложения, уютные по задумке.",
    lead="Cozyware — независимая студия, создающая простые и приватные приложения для iPhone. Без аккаунтов, рекламы и слежки — только инструменты, которые хорошо делают одно дело.",
    desc="Cozyware — независимая студия, создающая простые и приватные приложения для iPhone.",
    apps_h="Наши приложения", app_tag="Простой пульт для ТВ",
    app_blurb="Управляйте телевизором с iPhone через Wi-Fi. Без хаба, без аккаунта, без облака.",
    learn="Подробнее", principles_h="Как мы делаем приложения",
    principles=[("Приватность по умолчанию", "Ваши данные остаются на вашем устройстве. Мы не используем аналитику, рекламу и трекеры."),
                ("Честно и просто", "Понятные цены, бесплатный пробный период там, где это уместно, и никаких тёмных паттернов."),
                ("Спокойные интерфейсы", "Сосредоточенные экраны, которые хорошо делают одно дело и не мешают.")],
    contact_h="Поздоровайтесь", contact_p="Вопросы, идеи или пресса? Пишите на <a href=\"mailto:{e}\">{e}</a>.",
    store="Скачать в App Store", soon="Скоро в App Store",
    shots_h="Смотрите в действии",
    footer_studio="Cozyware — небольшие приложения, уютные по задумке.",
),
}
LANGS = [("en", "EN", ""), ("uk", "UA", "uk/"), ("ru", "RU", "ru/")]
HREFLANG = {"en": "en", "uk": "uk", "ru": "ru"}


def url(lang, rel):
    """Absolute path of page `rel` ('index.html', 'couchpad/support.html', ...) in `lang`."""
    prefix = dict((l, p) for l, _, p in LANGS)[lang]
    path = rel[:-len("index.html")] if rel.endswith("index.html") else rel
    return "/" + prefix + path


def store_button(lang):
    s = STUDIO[lang]
    if APP_LIVE:
        return f'<a class="btn" href="{APP_STORE_URL}">{s["store"]}</a>'
    return f'<span class="btn off">{s["soon"]}</span>'


def page(lang, rel, title, desc, content, canonical_rel=None, app_page=False):
    t = APP[lang]
    here = canonical_rel or rel
    links = "".join(
        f'<a href="{url(l, here)}"{" class=on" if l == lang else ""} hreflang="{HREFLANG[l]}">{label}</a>'
        for l, label, _ in LANGS)
    alternates = "".join(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{DOMAIN}{url(l, here)}">' for l, _, _ in LANGS)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{url("en", here)}">'
    canonical = f'{DOMAIN}{url(lang, here)}'
    banner = f'<meta name="apple-itunes-app" content="app-id={APP_ID}">' if (app_page and APP_LIVE) else ""
    nav_class = lambda r: " class=on" if here.startswith(r) else ""
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0b0c10">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cozyware">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/og.png">
<meta name="twitter:card" content="summary_large_image">
{banner}
{alternates}
<style>{STYLE}</style>
</head>
<body>
<main>
<header>
<img class="logo" src="/logo.svg" alt="">
<a class="brand" href="{url(lang, 'index.html')}">Cozyware</a>
<nav><a href="{url(lang, 'couchpad/index.html')}"{nav_class('couchpad/index')}>Couchpad</a><a href="{url(lang, 'couchpad/support.html')}"{nav_class('couchpad/support')}>{t['support']}</a><a href="{url(lang, 'couchpad/privacy.html')}"{nav_class('couchpad/privacy')}>{t['privacy']}</a><span class="langs">{links}</span></nav>
</header>
{content}
<footer>© 2026 Cozyware · <a href="mailto:{HELLO}">{HELLO}</a>{'<br>' + t['footer'] if app_page else ''}</footer>
</main>
</body>
</html>
"""


def studio_home(lang):
    s = STUDIO[lang]
    principles = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in s["principles"])
    return f"""<h1>{s['tagline']}</h1>
<p class="lead">{s['lead']}</p>
<h2>{s['apps_h']}</h2>
<a class="card app" href="{url(lang, 'couchpad/index.html')}">
<img src="/couchpad/icon.png" alt="Couchpad" width="72" height="72">
<div><p class="tag">{s['app_tag']}</p><h3>Couchpad</h3><p>{s['app_blurb']}</p></div>
</a>
<h2>{s['principles_h']}</h2>
<div class="grid">{principles}</div>
<h2>{s['contact_h']}</h2>
<p>{s['contact_p'].format(e=HELLO)}</p>"""


def app_home(lang):
    t, s = APP[lang], STUDIO[lang]
    cards = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["cards"])
    shots = "".join(
        f'<img src="/couchpad/img/{lang}-{n}.jpg" width="260" height="565" alt="Couchpad screenshot {n}" loading="lazy">'
        for n in (1, 2, 3, 5))
    return f"""<div class="hero"><img src="/couchpad/icon.png" alt="" width="84" height="84"><div><h1>Couchpad</h1><p class="lead" style="margin:0">{s['app_tag']}</p></div></div>
<p class="lead">{t['index_lead']}</p>
<div class="btns">{store_button(lang)}<a class="btn ghost" href="{url(lang, 'couchpad/support.html')}">{t['get_help']}</a></div>
<h2>{s['shots_h']}</h2>
<div class="shots">{shots}</div>
{cards}"""


def privacy_content(lang):
    t = APP[lang]
    return f"""<h1>{t['privacy_title']}</h1>
<p class="lead">{t['effective']}</p>
{t['privacy_body'].format(email=SUPPORT)}"""


def support_content(lang):
    t = APP[lang]
    faq = "".join(f'<div class="card"><h3>{q}</h3><p>{a}</p></div>' for q, a in t["faq"])
    return f"""<h1>{t['support_title']}</h1>
<p class="lead">{t['support_lead'].format(email=SUPPORT)}</p>
<h2>{t['faq_title']}</h2>
{faq}"""


def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


urls = []
for lang, _, prefix in LANGS:
    t, s = APP[lang], STUDIO[lang]
    pages = [
        ("index.html", None, f"Cozyware — {s['tagline']}", s["desc"], studio_home(lang), False),
        ("couchpad/index.html", None, t["index_title"], t["index_desc"], app_home(lang), True),
        ("couchpad/privacy.html", None, f"{t['privacy_title']} — Couchpad", t["privacy_title"], privacy_content(lang), True),
        ("couchpad/support.html", None, f"{t['support_title']} — Couchpad", t["support_title"], support_content(lang), True),
        # legacy URLs already submitted to App Store Connect — keep them working
        ("privacy.html", "couchpad/privacy.html", f"{t['privacy_title']} — Couchpad", t["privacy_title"], privacy_content(lang), True),
        ("support.html", "couchpad/support.html", f"{t['support_title']} — Couchpad", t["support_title"], support_content(lang), True),
    ]
    for rel, canon, title, desc, content, app_page in pages:
        write(prefix + rel, page(lang, rel, title, desc, content, canonical_rel=canon, app_page=app_page))
        if canon is None:
            urls.append(url(lang, rel))

write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"<url><loc>{DOMAIN}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
write("CNAME", "cozyware.app\n")
write("404.html", f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Not found — Cozyware</title><link rel="icon" href="/logo.svg" type="image/svg+xml"><style>{STYLE}</style></head>
<body><main><header><img class="logo" src="/logo.svg" alt=""><a class="brand" href="/">Cozyware</a></header>
<h1>Page not found</h1><p class="lead">This page doesn't exist. <a href="/">Back to the home page</a>.</p></main></body></html>
""")
print("built", len(urls), "pages per site")
