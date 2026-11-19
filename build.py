from pathlib import Path
import json, re, html, hashlib, shutil
ROOT=Path(__file__).resolve().parent
DIST=ROOT/'dist'; T=ROOT/'template'
# Root files are published by GitHub Pages; keep the build copy in sync.
DIST.mkdir(exist_ok=True)
for folder in ('css', 'js', 'img'):
    shutil.copytree(ROOT/folder, DIST/folder, dirs_exist_ok=True)
def read(name):
    content = (T/name).read_text(encoding='utf-8')
    for asset in ('css/custom.css', 'js/custom.js'):
        if asset in content:
            version = hashlib.sha256((DIST/asset).read_bytes()).hexdigest()[:12]
            content = content.replace('"' + asset + '"', '"' + asset + '?v=' + version + '"')
    return content
def esc(value): return html.escape(str(value),quote=True)
def entries(kind, limit=None):
    items=json.loads((ROOT/'data'/f'{kind}.json').read_text(encoding='utf-8'))
    if not items:
        return '<p class="empty-note">'+('Group news will be posted here.' if kind=='news' else 'Upcoming seminars, conferences, and group events will be listed here.')+'</p>'
    out='<ul class="dated-list">'
    for item in sorted(items,key=lambda item:item['date'],reverse=True)[:limit]:
        title=esc(item['title']); url=item.get('url','')
        if url:
            if not url.startswith(('https://','http://')): raise ValueError('News links must use http or https')
            title='<a href="'+esc(url)+'">'+title+'</a>'
        out+='<li><time datetime="'+esc(item['date'])+'">'+esc(item.get('display_date',item['date']))+'</time><div><span class="entry-title">'+title+'</span>'
        if item.get('description') and limit is None:
            description = esc(item['description'])
            link = item.get('description_link')
            if link:
                if not link['url'].startswith(('https://', 'http://')):
                    raise ValueError('Description links must use http or https')
                label = esc(link['text'])
                if label not in description:
                    raise ValueError('Description link text must appear in description')
                description = description.replace(label, '<a href="' + esc(link['url']) + '">' + label + '</a>', 1)
            out += '<p>' + description + '</p>'
        out+='</div></li>'
    return out+'</ul>'
header=read('header.htm').replace('Web Template 3.0','<span class="lab-name">HAN Lab</span><span class="lab-expansion">Health, Adaptation &amp; Nitrogen</span>')
header=re.sub(r'<!--div.*?</div-->','',header,flags=re.S)
footer=read('footer.htm').replace('<!--#include file="footer-links.htm"-->',read('footer-links.htm')).replace('<!--#include file="footer-media.htm"-->','<ul class="cityu-footer-media"><li><a href="https://scholars.cityu.edu.hk/en/persons/pinghan/">CityUHK Scholars</a></li></ul>')
nav=[('index.html','Home'),('research.html','Research'),('people.html','People'),('publications.html','Publications'),('news.html','News & events'),('gallery.html','Gallery'),('contact.html','Contact')]
contact='<p><strong>Prof. Penny Han</strong><br>School of Energy and Environment<br>State Key Laboratory of Marine Environmental Health<br>City University of Hong Kong</p><p>Office: YEUNG-G5705<br>Email: <a href="mailto:pinghan@cityu.edu.hk">pinghan@cityu.edu.hk</a><br>Tel: <a href="tel:+85234426069">+852 3442 6069</a></p>'
pages={
'index.html':('Home','''<div class="welcome"><div class="welcome-copy"><h1>Welcome to HAN Lab</h1><p class="lab-focus"><strong>H</strong>ealth, <strong>A</strong>daptation &amp; <strong>N</strong>itrogen</p><p>How do tiny microbes shape the health of our planet? We study the microorganisms that drive the nitrogen cycle—from soils and coastal waters to Antarctic ecosystems and engineered treatment systems.</p><p>Led by <a href="people.html">Prof. Penny Han</a>, we connect microbial ecology, biogeochemistry, and environmental engineering to understand adaptation to environmental change, reduce nitrous oxide emissions, and support sustainable water treatment.</p>'''+read('profiles.htm')+'''<p class="welcome-links"><a href="research.html">Explore our research <span aria-hidden="true">→</span></a><a href="people.html">Meet the team <span aria-hidden="true">→</span></a></p></div>'''+read('planet.htm')+'''</div><div class="home-columns"><div><section aria-labelledby="news-title"><h2 id="news-title">News</h2>'''+entries('news', 4)+'''<p class="archive-link"><a href="news.html#group-news">All news <span aria-hidden="true">→</span></a></p></section><section aria-labelledby="events-title"><h2 id="events-title">Events</h2>'''+entries('events', 3)+'''<p class="archive-link"><a href="news.html#events">All events <span aria-hidden="true">→</span></a></p></section><div class="affiliation-logos" aria-label="Affiliated institutions"><a href="https://www.cityu.edu.hk/see/" aria-label="School of Energy and Environment"><img class="see-logo" src="img/see-logo.png" alt="School of Energy and Environment" loading="lazy"></a><a href="https://www.cityu.edu.hk/sklmeh/" aria-label="State Key Laboratory of Marine Environmental Health"><img class="sklmeh-logo" src="img/sklmeh-logo.png" alt="State Key Laboratory of Marine Environmental Health" loading="lazy"></a></div></div><aside aria-label="Group information"><section><h2>Prospective students</h2><p>Prof. Han is accepting PhD students. Please <a href="contact.html">get in touch</a> to discuss research interests.</p></section><section><h2>Contact</h2>'''+contact+'''</section><section class="linkedin-connect" aria-labelledby="linkedin-title"><h2 id="linkedin-title">Connect on LinkedIn</h2><a class="linkedin-qr" href="https://www.linkedin.com/in/ping-penny-han-62222938/" aria-label="Visit Prof. Penny Han on LinkedIn"><img src="img/penny-han-linkedin-qr.jpg" width="282" height="282" alt="QR code for Prof. Penny Han’s LinkedIn profile" loading="lazy"></a><p><a href="https://www.linkedin.com/in/ping-penny-han-62222938/">Prof. Penny Han on LinkedIn</a><br><span class="qr-caption">Scan the code or follow the link.</span></p></section></aside></div>'''),
'research.html':('Research',read('research.htm')),
'people.html':('People',read('people.htm').replace('<!-- PI_PROFILES -->',read('profiles.htm'))),
'gallery.html':('Gallery',read('gallery.htm')),
'publications.html':('Publications','''<h1>Selected publications</h1><p>For the full publication list, please visit <a href="https://scholar.google.com/citations?hl=en&amp;user=BTB54fsAAAAJ">Google Scholar</a>.</p><section><h2>2026</h2><ol class="publication-list"><li><a href="https://doi.org/10.1126/sciadv.aef4314">Hypoxia and acidification antagonistically suppress nitrification but enhance its N₂O production in coastal waters.</a><p>Zhou, J. et al.<br><em>Science Advances</em>, 12(39), eaef4314.</p></li><li><a href="https://scholars.cityu.edu.hk/en/publications/nitrification-couples-microbial-cosub2sub-fixation-to-warming-and/">Nitrification Couples Microbial CO₂ Fixation to Warming and Drought Responses in Alpine Grassland Soils.</a><p>Su, Y. et al.<br><em>Environmental Science & Technology</em>, 60(29), 20304–20318.</p></li><li><a href="https://scholars.cityu.edu.hk/en/publications/microplastics-promote-nsub2subo-emissions-by-enhancing-nitrificat/">Microplastics promote N₂O emissions by enhancing nitrification via ammonia-oxidizing bacteria in estuarine and coastal sediments.</a><p>Tang, X., Bao, Y. et al.<br><em>Water Research</em>, 293, 125458.</p></li></ol></section>'''),
'news.html':('News & events','<h1>News & events</h1><p>From new lab members to research talks and conversations beyond the lab.</p><nav class="archive-nav" aria-label="News and events sections"><a href="#group-news">Group news</a><a href="#events">Events</a></nav><section id="group-news"><h2>Group news</h2>'+entries('news')+'</section><section id="events"><h2>Events</h2>'+entries('events')+'</section>'),
'contact.html':('Contact','<h1>Contact</h1>'+contact+'''<section><h2>PhD enquiries</h2><p>Prof. Han is accepting PhD students. If you are interested in environmental microbiology and microbial nitrogen cycling, please contact her by email to discuss possible research opportunities.</p></section><section><h2>Research collaboration</h2><p>For research and collaboration enquiries, please email <a href="mailto:pinghan@cityu.edu.hk">pinghan@cityu.edu.hk</a>.</p></section>''')}
for filename,(title,content) in pages.items():
    items='<ul class="cityu-menu-main navbar-nav me-auto">'+''.join('<li class="nav-item"><a class="nav-link'+(' active' if filename==f else '')+'"'+(' aria-current="page"' if filename==f else '')+' href="'+('/' if f=='index.html' else f)+'">'+esc(label)+'</a></li>' for f,label in nav)+'</ul>'
    menu=read('menu.htm').replace('aria-labelledby="mainMenu"','aria-label="Main navigation"').replace('aria-controls="mainMenu"','aria-controls="mainMenu" aria-label="Open navigation"').replace('<!--#include file="menu-main.htm"-->',items).replace('<!--#include file="menu-tools.htm"-->','')
    markup='<!doctype html><html lang="en"><head>'+read('meta.htm')+'<title>'+esc(title)+' | HAN Lab — Health, Adaptation &amp; Nitrogen | CityUHK</title><meta name="description" content="HAN Lab — Health, Adaptation &amp; Nitrogen. Environmental microbiology and microbial nitrogen cycling at City University of Hong Kong."></head><body class="cityu-template-3 cityu-template-3-0 cityu-base-layout cityu-base-style"><a class="lab-skip" href="#main">Skip to content</a>'+header+menu+'<div class="cityu"><main class="cityu-main" id="main"><div class="cityu-main-inner"><div class="group-site '+('home-page' if filename=='index.html' else 'inner-page')+'">'+content+'</div></div></main></div>'+footer+read('script.htm')+'</body></html>'
    (DIST/filename).write_text(markup + "\n", encoding="utf-8", newline="\n")
    (ROOT/filename).write_text(markup + "\n", encoding="utf-8", newline="\n")
print(f'Built {len(pages)} academic pages with shared CityUHK header and footer.')
