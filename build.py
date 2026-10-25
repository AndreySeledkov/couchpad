"""Generates the Couchpad support site in English (root), Ukrainian (uk/) and Russian (ru/).
Edit the texts below and run: python3 build.py"""
import os

EMAIL = "seledkovandrey@gmail.com"
STYLE = """
:root{--bg:#0b0c10;--text:#e6e8ec;--dim:#8c919e;--amber:#ffb547;--line:#2b2e37}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(ellipse at top,#2a2214 0%,var(--bg) 55%) fixed;color:var(--text);
font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:48px 20px 64px}
header{display:flex;align-items:center;flex-wrap:wrap;gap:14px;margin-bottom:36px}
header img{width:56px;height:56px;border-radius:13px;box-shadow:0 8px 24px rgba(0,0,0,.5)}
header .brand{color:var(--text);text-decoration:none;font:800 24px/1 ui-rounded,-apple-system,sans-serif}
nav{margin-left:auto;display:flex;flex-wrap:wrap;gap:18px;align-items:center}
nav a{color:var(--dim);text-decoration:none;font:600 15px/1.4 -apple-system,BlinkMacSystemFont,sans-serif}
nav a:hover,nav a.on{color:var(--amber)}
.langs{display:flex;gap:10px;padding-left:14px;border-left:1px solid var(--line)}
h1{font:800 34px/1.2 ui-rounded,-apple-system,sans-serif;margin:0 0 8px}
h2{font:700 21px/1.3 ui-rounded,-apple-system,sans-serif;margin:36px 0 8px;color:var(--amber)}
p,li{color:#cfd2d8} a{color:var(--amber)}
.lead{font-size:20px;color:var(--dim);margin:0 0 28px}
.card{background:linear-gradient(#24262e,#16171c);border:1px solid var(--line);border-radius:18px;padding:20px 22px;margin:14px 0}
.card h3{margin:0 0 6px;font-size:17px;color:var(--text)}
.card p{margin:0}
.btn{display:inline-block;background:linear-gradient(#ffb547,#ee7a19);color:#1a1205;font-weight:700;text-decoration:none;
padding:14px 26px;border-radius:999px;box-shadow:0 0 24px rgba(255,181,71,.35)}
footer{margin-top:56px;color:var(--dim);font-size:14px;border-top:1px solid var(--line);padding-top:20px}
@media (max-width:520px){nav{margin-left:0;width:100%}h1{font-size:28px}}
"""

T = {
"en": dict(
    html_lang="en", support="Support", privacy="Privacy",
    footer="Couchpad is not affiliated with LG, Samsung, Sony, Roku or Google. All trademarks belong to their owners.",
    index_title="Couchpad — Simple TV remote", index_desc="Simple TV remote. Simple price. Control your TV from your iPhone over Wi-Fi.",
    index_h1="Simple TV remote.<br>Simple price.",
    index_lead="Control your TV from your iPhone over Wi-Fi. No ads, no accounts, no cloud. Try it free for 7 days.",
    cards=[("Works with your TV","LG webOS, Samsung Tizen, Sony BRAVIA, Android TV, Google TV and Roku."),
           ("More than buttons","Touchpad, keyboard, one-tap app launch, inputs, volume and channels."),
           ("Private by design","Your phone talks to the TV directly on your home network. Nothing is sent to us.")],
    get_help="Get help",
    privacy_title="Privacy Policy", effective="Effective October 25, 2026",
    privacy_body="""<p>Couchpad is a TV remote app for iPhone. This policy explains what information the app uses and what happens to it. The short version: <strong>we do not collect any personal data.</strong></p>
<h2>Information we collect</h2><p>None. Couchpad has no user accounts, no analytics, no advertising and no tracking. The app does not send any information to us or to third parties.</p>
<h2>Information stored on your device</h2><p>To remember your TVs, the app stores on your iPhone only:</p>
<ul><li>the names, network addresses and network (MAC) addresses of the TVs you add, and the names you give them;</li><li>the pairing keys your TVs issue to the app, kept in the iOS Keychain;</li><li>your app settings, such as the language.</li></ul>
<p>This information never leaves your device except as part of your encrypted iPhone backup. Removing a TV in the app or deleting the app removes it.</p>
<h2>Local network</h2><p>Couchpad asks for Local Network access to find TVs on your Wi-Fi and send them commands. All communication happens directly between your iPhone and your TV inside your home network. The app does not connect to any server of ours.</p>
<h2>Subscription</h2><p>The Couchpad subscription is sold through Apple's App Store. Payments are processed by Apple; we do not receive your payment details. Apple tells the app only whether your subscription or free trial is active. See <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>
<h2>Children</h2><p>Couchpad does not knowingly collect information from anyone, including children under 13.</p>
<h2>Changes</h2><p>If this policy changes, we will update this page and the date above.</p>
<h2>Contact</h2><p>Questions about privacy: <a href="mailto:{email}">{email}</a></p>""",
    support_title="Support",
    support_lead="""Something not working? Write to <a href="mailto:{email}?subject=Couchpad%20support">{email}</a> — we usually reply within 1–2 days. In the app, Settings › Contact Support adds your iPhone and TV details to the email automatically.""",
    faq_title="Frequently asked questions",
    faq=[("The app doesn't find my TV","Make sure the TV is on and your iPhone is on the same Wi-Fi network (not a guest network). Check that Couchpad is allowed in iPhone Settings › Privacy &amp; Security › Local Network. Then tap Search Network again — it takes up to 20 seconds."),
         ("How do I connect without the TV's remote?","LG, Sony and Android TV / Google TV show a code on the screen — type it in the app. Samsung asks you to select Allow on the TV once. Roku needs no confirmation."),
         ("The code didn't appear on my LG TV","Some webOS versions don't support code pairing. Long-press the TV in the list and choose Confirm with TV Remote, then select Yes on the TV."),
         ("Roku doesn't respond to buttons","On the Roku, open Settings › System › Advanced system settings › Control by mobile apps and set it to Default or Permissive."),
         ("I can turn the TV off, but not on","Turning on works over Wi-Fi only if the TV supports it. LG: turn on Settings › General › Devices › TV Management › Turn on via Wi-Fi. Samsung: Settings › General › Network › Expert Settings › Power On with Mobile. Turn the TV on with its remote once afterwards so the app can learn it."),
         ("The TV says the app is no longer recognized","This happens after a TV reset. Remove the TV in the app and add it again."),
         ("How does the subscription work?","Finding and adding your TV is free, so you can check it's supported. The remote needs a subscription: 7 days free, then monthly or yearly. If you cancel during the free week, you won't be charged."),
         ("How do I cancel or restore the subscription?","Cancel: iPhone Settings › your name › Subscriptions › Couchpad, at least 24 hours before renewal. Restore on a new iPhone: in the app, Settings › Restore Purchases."),
         ("How do I change the app's language?","In the app, Settings › Language: English, Українська or Русский. System follows your iPhone's language.")],
),
"uk": dict(
    html_lang="uk", support="Підтримка", privacy="Конфіденційність",
    footer="Couchpad не пов'язаний з LG, Samsung, Sony, Roku чи Google. Усі торговельні марки належать їхнім власникам.",
    index_title="Couchpad — простий пульт для ТВ", index_desc="Простий пульт. Проста ціна. Керуйте телевізором з iPhone через Wi-Fi.",
    index_h1="Простий пульт.<br>Проста ціна.",
    index_lead="Керуйте телевізором з iPhone через Wi-Fi. Без реклами, без акаунтів, без хмари. 7 днів безкоштовно.",
    cards=[("Працює з вашим ТВ","LG webOS, Samsung Tizen, Sony BRAVIA, Android TV, Google TV і Roku."),
           ("Більше, ніж кнопки","Тачпад, клавіатура, запуск застосунків одним дотиком, джерела, гучність і канали."),
           ("Приватність за замовчуванням","Телефон працює з ТВ напряму в домашній мережі. Нам нічого не надсилається.")],
    get_help="Допомога",
    privacy_title="Політика конфіденційності", effective="Діє з 25 жовтня 2026 року",
    privacy_body="""<p>Couchpad — застосунок-пульт для телевізора на iPhone. Ця політика пояснює, яку інформацію використовує застосунок і що з нею відбувається. Коротко: <strong>ми не збираємо жодних персональних даних.</strong></p>
<h2>Які дані ми збираємо</h2><p>Жодних. У Couchpad немає акаунтів, аналітики, реклами чи відстеження. Застосунок не надсилає інформацію ні нам, ні третім особам.</p>
<h2>Дані на вашому пристрої</h2><p>Щоб пам'ятати ваші ТВ, застосунок зберігає на iPhone лише:</p>
<ul><li>назви, мережеві адреси й MAC-адреси доданих ТВ і назви, які ви їм дали;</li><li>ключі підключення, які видають телевізори, — у Keychain iOS;</li><li>налаштування застосунку, наприклад мову.</li></ul>
<p>Ці дані не залишають пристрій, окрім як у складі зашифрованої резервної копії iPhone. Видалення ТВ у застосунку або видалення застосунку їх стирає.</p>
<h2>Локальна мережа</h2><p>Couchpad просить доступ до локальної мережі, щоб знаходити ТВ у вашому Wi-Fi і надсилати їм команди. Увесь обмін відбувається напряму між iPhone і телевізором у домашній мережі. Застосунок не підключається до наших серверів.</p>
<h2>Підписка</h2><p>Підписка Couchpad продається через App Store. Платежі обробляє Apple; ми не отримуємо ваших платіжних даних. Apple повідомляє застосунку лише, чи активна підписка або пробний період. Див. <a href="https://www.apple.com/legal/privacy/">Політику конфіденційності Apple</a>.</p>
<h2>Діти</h2><p>Couchpad свідомо не збирає інформацію ні від кого, зокрема від дітей до 13 років.</p>
<h2>Зміни</h2><p>Якщо політика зміниться, ми оновимо цю сторінку й дату вище.</p>
<h2>Контакт</h2><p>Питання щодо конфіденційності: <a href="mailto:{email}">{email}</a></p>""",
    support_title="Підтримка",
    support_lead="""Щось не працює? Напишіть на <a href="mailto:{email}?subject=Couchpad%20support">{email}</a> — зазвичай відповідаємо протягом 1–2 днів. У застосунку Налаштування › Написати в підтримку автоматично додає до листа дані про iPhone і ТВ.""",
    faq_title="Часті запитання",
    faq=[("Застосунок не знаходить ТВ","Переконайтеся, що ТВ увімкнений, а iPhone у тій самій мережі Wi-Fi (не гостьовій). Перевірте, що Couchpad дозволено в Налаштування iPhone › Конфіденційність і безпека › Локальна мережа. Потім знову натисніть «Шукати в мережі» — це займає до 20 секунд."),
         ("Як підключитися без пульта від ТВ?","LG, Sony та Android TV / Google TV показують код на екрані — введіть його в застосунку. Samsung один раз просить натиснути «Дозволити» на ТВ. Roku не потребує підтвердження."),
         ("На LG не з'явився код","Деякі версії webOS не підтримують підключення за кодом. Довго натисніть на ТВ у списку, виберіть «Підтвердити пультом ТВ» і натисніть «Так» на телевізорі."),
         ("Roku не реагує на кнопки","На Roku відкрийте Settings › System › Advanced system settings › Control by mobile apps і виберіть Default або Permissive."),
         ("ТВ вимикається, але не вмикається","Увімкнення через Wi-Fi працює, лише якщо ТВ це підтримує. LG: Налаштування › Загальні › Пристрої › Керування ТВ › Увімкнення через Wi-Fi. Samsung: Налаштування › Загальні › Мережа › Експертні налаштування › Увімкнення з мобільного. Після цього один раз увімкніть ТВ його пультом, щоб застосунок його запам'ятав."),
         ("ТВ пише, що більше не впізнає застосунок","Так буває після скидання ТВ. Видаліть ТВ у застосунку й додайте знову."),
         ("Як працює підписка?","Знайти й додати ТВ можна безкоштовно — так ви перевірите, що він підтримується. Для пульта потрібна підписка: 7 днів безкоштовно, далі щомісяця або щороку. Якщо скасувати протягом безкоштовного тижня, оплати не буде."),
         ("Як скасувати або відновити підписку?","Скасувати: Налаштування iPhone › ваше ім'я › Підписки › Couchpad, щонайменше за 24 години до продовження. Відновити на новому iPhone: у застосунку Налаштування › Відновити покупки."),
         ("Як змінити мову застосунку?","У застосунку Налаштування › Мова: English, Українська або Русский. «Як у системі» — мова вашого iPhone.")],
),
"ru": dict(
    html_lang="ru", support="Поддержка", privacy="Конфиденциальность",
    footer="Couchpad не связан с LG, Samsung, Sony, Roku или Google. Все товарные знаки принадлежат их владельцам.",
    index_title="Couchpad — простой пульт для ТВ", index_desc="Простой пульт. Простая цена. Управляйте телевизором с iPhone через Wi-Fi.",
    index_h1="Простой пульт.<br>Простая цена.",
    index_lead="Управляйте телевизором с iPhone через Wi-Fi. Без рекламы, без аккаунтов, без облака. 7 дней бесплатно.",
    cards=[("Работает с вашим ТВ","LG webOS, Samsung Tizen, Sony BRAVIA, Android TV, Google TV и Roku."),
           ("Больше, чем кнопки","Тачпад, клавиатура, запуск приложений одним касанием, источники, громкость и каналы."),
           ("Приватность по умолчанию","Телефон работает с ТВ напрямую в домашней сети. Нам ничего не отправляется.")],
    get_help="Помощь",
    privacy_title="Политика конфиденциальности", effective="Действует с 25 октября 2026 года",
    privacy_body="""<p>Couchpad — приложение-пульт для телевизора на iPhone. Эта политика объясняет, какую информацию использует приложение и что с ней происходит. Коротко: <strong>мы не собираем никаких персональных данных.</strong></p>
<h2>Какие данные мы собираем</h2><p>Никаких. В Couchpad нет аккаунтов, аналитики, рекламы и отслеживания. Приложение не отправляет информацию ни нам, ни третьим лицам.</p>
<h2>Данные на вашем устройстве</h2><p>Чтобы помнить ваши ТВ, приложение хранит на iPhone только:</p>
<ul><li>названия, сетевые адреса и MAC-адреса добавленных ТВ и имена, которые вы им дали;</li><li>ключи подключения, которые выдают телевизоры, — в Keychain iOS;</li><li>настройки приложения, например язык.</li></ul>
<p>Эти данные не покидают устройство, кроме как в составе зашифрованной резервной копии iPhone. Удаление ТВ в приложении или удаление приложения их стирает.</p>
<h2>Локальная сеть</h2><p>Couchpad запрашивает доступ к локальной сети, чтобы находить ТВ в вашем Wi-Fi и отправлять им команды. Весь обмен идёт напрямую между iPhone и телевизором в домашней сети. Приложение не подключается к нашим серверам.</p>
<h2>Подписка</h2><p>Подписка Couchpad продаётся через App Store. Платежи обрабатывает Apple; мы не получаем ваших платёжных данных. Apple сообщает приложению только, активна ли подписка или пробный период. См. <a href="https://www.apple.com/legal/privacy/">Политику конфиденциальности Apple</a>.</p>
<h2>Дети</h2><p>Couchpad сознательно не собирает информацию ни от кого, включая детей до 13 лет.</p>
<h2>Изменения</h2><p>Если политика изменится, мы обновим эту страницу и дату выше.</p>
<h2>Контакт</h2><p>Вопросы о конфиденциальности: <a href="mailto:{email}">{email}</a></p>""",
    support_title="Поддержка",
    support_lead="""Что-то не работает? Напишите на <a href="mailto:{email}?subject=Couchpad%20support">{email}</a> — обычно отвечаем в течение 1–2 дней. В приложении Настройки › Написать в поддержку автоматически добавляет к письму данные об iPhone и ТВ.""",
    faq_title="Частые вопросы",
    faq=[("Приложение не находит ТВ","Убедитесь, что ТВ включён, а iPhone в той же сети Wi-Fi (не гостевой). Проверьте, что Couchpad разрешён в Настройки iPhone › Конфиденциальность и безопасность › Локальная сеть. Затем снова нажмите «Искать в сети» — это занимает до 20 секунд."),
         ("Как подключиться без пульта от ТВ?","LG, Sony и Android TV / Google TV показывают код на экране — введите его в приложении. Samsung один раз просит нажать «Разрешить» на ТВ. Roku не требует подтверждения."),
         ("На LG не появился код","Некоторые версии webOS не поддерживают подключение по коду. Долго нажмите на ТВ в списке, выберите «Подтвердить пультом ТВ» и нажмите «Да» на телевизоре."),
         ("Roku не реагирует на кнопки","На Roku откройте Settings › System › Advanced system settings › Control by mobile apps и выберите Default или Permissive."),
         ("ТВ выключается, но не включается","Включение через Wi-Fi работает, только если ТВ это поддерживает. LG: Настройки › Общие › Устройства › Управление ТВ › Включение через Wi-Fi. Samsung: Настройки › Общие › Сеть › Экспертные настройки › Включение с мобильного. После этого один раз включите ТВ его пультом, чтобы приложение его запомнило."),
         ("ТВ пишет, что больше не узнаёт приложение","Так бывает после сброса ТВ. Удалите ТВ в приложении и добавьте заново."),
         ("Как работает подписка?","Найти и добавить ТВ можно бесплатно — так вы проверите, что он поддерживается. Для пульта нужна подписка: 7 дней бесплатно, затем ежемесячно или ежегодно. Если отменить в течение бесплатной недели, оплаты не будет."),
         ("Как отменить или восстановить подписку?","Отменить: Настройки iPhone › ваше имя › Подписки › Couchpad, не позднее чем за 24 часа до продления. Восстановить на новом iPhone: в приложении Настройки › Восстановить покупки."),
         ("Как сменить язык приложения?","В приложении Настройки › Язык: English, Українська или Русский. «Как в системе» — язык вашего iPhone.")],
),
}
LANGS = [("en", "EN", ""), ("uk", "UA", "uk/"), ("ru", "RU", "ru/")]

def page(lang, name, title, desc, content):
    t = T[lang]
    prefix = "" if lang == "en" else "../"
    here = dict((l, p) for l, _, p in LANGS)[lang]
    links = "".join(
        f'<a href="{prefix}{p}{name}"{" class=on" if l == lang else ""} hreflang="{l}">{label}</a>'
        for l, label, p in LANGS)
    alternates = "".join(f'<link rel="alternate" hreflang="{l}" href="https://andreyseledkov.github.io/couchpad/{p}{name}">' for l, _, p in LANGS)
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{prefix}icon.png">
{alternates}
<style>{STYLE}</style>
</head>
<body>
<main>
<header>
<img src="{prefix}icon.png" alt="">
<a class="brand" href="index.html">Couchpad</a>
<nav><a href="support.html">{t['support']}</a><a href="privacy.html">{t['privacy']}</a><span class="langs">{links}</span></nav>
</header>
{content}
<footer>© 2026 Couchpad · <a href="mailto:{EMAIL}">{EMAIL}</a><br>{t['footer']}</footer>
</main>
</body>
</html>
"""

for lang, _, path in LANGS:
    t = T[lang]
    os.makedirs(path or ".", exist_ok=True)
    cards = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["cards"])
    index = f"""<h1>{t['index_h1']}</h1>
<p class="lead">{t['index_lead']}</p>
{cards}
<p style="margin-top:28px"><a class="btn" href="support.html">{t['get_help']}</a></p>"""
    privacy = f"""<h1>{t['privacy_title']}</h1>
<p class="lead">{t['effective']}</p>
{t['privacy_body'].format(email=EMAIL)}"""
    faq = "".join(f'<div class="card"><h3>{q}</h3><p>{a}</p></div>' for q, a in t["faq"])
    support = f"""<h1>{t['support_title']}</h1>
<p class="lead">{t['support_lead'].format(email=EMAIL)}</p>
<h2>{t['faq_title']}</h2>
{faq}"""
    for name, title, desc, content in [
        ("index.html", t["index_title"], t["index_desc"], index),
        ("privacy.html", f"{t['privacy_title']} — Couchpad", t["privacy_title"], privacy),
        ("support.html", f"{t['support_title']} — Couchpad", t["support_title"], support),
    ]:
        with open(os.path.join(path, name), "w", encoding="utf-8") as f:
            f.write(page(lang, name, title, desc, content))
print("built")
