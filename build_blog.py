# -*- coding: utf-8 -*-
"""Gera o blog da Petderma Food: páginas de post, índice, sitemap, robots."""
import os, json, html

BASE = "https://petdermafood.com.br"
WA = "https://api.whatsapp.com/send/?phone=5511989812898&text=Ol%C3%A1%21%20Vim%20pelo%20blog%20da%20Petderma%20Food%20e%20quero%20montar%20o%20kit%20ideal%20para%20meu%20pet."
STORE = "https://petdermastore.com.br/"
ROOT = os.path.dirname(os.path.abspath(__file__))

WA_ICON = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" '
'd="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>')

def header(prefix):
    return f'''<header class="header" id="top">
  <div class="header__pill">
    <a href="{prefix}index.html" class="header__logo" aria-label="Petderma Food — início">
      <img src="{prefix}assets/img/logo.png" alt="Petderma Food" width="200" height="31">
    </a>
    <nav class="nav">
      <a href="{prefix}blog/index.html">Blog</a>
      <a href="{prefix}index.html#beneficios">Quem Somos</a>
      <a href="{prefix}index.html#contato">Contato</a>
    </nav>
    <div class="header__actions">
      <a href="{STORE}" class="btn btn--ghost" target="_blank" rel="noopener">Compre na loja</a>
      <a href="{WA}" class="btn btn--whats" target="_blank" rel="noopener">{WA_ICON} Whatsapp</a>
    </div>
    <button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>'''

def footer(prefix):
    return f'''<footer class="footer" id="contato">
  <div class="container footer__inner">
    <div class="footer__brand">
      <img src="{prefix}assets/img/logo.png" alt="Petderma Food" width="200" height="31">
      <p>Comida natural e hipoalergênica desenvolvida por especialistas em dermatologia veterinária. Nutrição de verdade para pets com sensibilidades.</p>
    </div>
    <div class="footer__col"><h3>Links rápidos</h3><ul>
      <li><a href="{prefix}index.html#beneficios">Quem Somos</a></li>
      <li><a href="{prefix}blog/index.html">Blog</a></li>
      <li><a href="{prefix}index.html#faq">Dúvidas</a></li>
      <li><a href="{STORE}" target="_blank" rel="noopener">Loja oficial</a></li>
    </ul></div>
    <div class="footer__col"><h3>Suporte &amp; Políticas</h3><ul>
      <li><a href="{prefix}index.html#faq">Dúvidas frequentes</a></li>
      <li><a href="#">Termos e Condições</a></li>
      <li><a href="#">Políticas de Privacidade</a></li>
    </ul></div>
    <div class="footer__col"><h3>Contato</h3>
      <p class="footer__contact"><strong>Endereço</strong><br>R. República do Iraque, 1497 — Campo Belo, São Paulo · SP</p>
      <p class="footer__contact"><strong>Atendimento</strong><br><a href="{WA}">(11) 98981-2898</a></p>
    </div>
  </div>
  <div class="footer__bottom"><div class="container">© 2025 Petderma Food. Todos os direitos reservados.</div></div>
</footer>
<a href="{WA}" class="fab-whats" target="_blank" rel="noopener" aria-label="Fale conosco no WhatsApp">{WA_ICON.replace('width="18" height="18"','width="30" height="30"')}</a>
<script src="{prefix}assets/js/script.js" defer></script>'''

def head(title, desc, canonical, prefix, image, extra_ld=""):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{BASE}/assets/img/{image}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Petderma Food">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{BASE}/assets/img/{image}">
<link rel="icon" type="image/png" href="{prefix}assets/img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700&family=Baloo+2:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/styles.css">
{extra_ld}
</head>
<body>'''

# ---- Conteúdo dos posts ----
CTA = ('<div class="article__cta"><h3>Pronto para transformar a alimentação do seu pet?</h3>'
'<p>Monte o kit ideal com nosso time — rápido, sem complicação.</p>'
f'<a href="{WA}" class="btn btn--lg" target="_blank" rel="noopener">Montar meu kit no WhatsApp</a></div>')

POSTS = [
 dict(slug="alimentacao-natural-para-caes-guia-completo", img="blog-1.jpg", cat="Nutrição", date="2025-05-02",
  title="Alimentação natural para cães: o guia completo para começar",
  desc="Tudo o que você precisa saber sobre alimentação natural para cães: benefícios, ingredientes, porções e como iniciar com segurança a dieta do seu pet.",
  kw="alimentação natural para cães, comida natural para cachorro, dieta natural pet",
  body=f"""<p>A <strong>alimentação natural para cães</strong> deixou de ser tendência e virou uma escolha consciente de tutores que querem mais saúde e qualidade de vida para o pet. Mas por onde começar? Neste guia, explicamos de forma simples o que é, quais os benefícios e como dar o primeiro passo com segurança.</p>
<h2>O que é alimentação natural para cães?</h2>
<p>É uma dieta preparada com <strong>ingredientes naturais e selecionados</strong> — proteínas, legumes e vegetais — sem grãos, corantes, conservantes ou aditivos artificiais. Na Petderma Food, cada fórmula é balanceada por nutricionistas e aprovada por dermatologistas veterinários.</p>
<h2>Principais benefícios</h2>
<ul>
<li><strong>Digestão mais leve</strong> e melhor aproveitamento dos nutrientes;</li>
<li><strong>Pele e pelagem saudáveis</strong>, especialmente em pets com sensibilidades;</li>
<li>Mais <strong>energia e disposição</strong> no dia a dia;</li>
<li>Controle de porção e menos desperdício.</li>
</ul>
<h2>Como começar</h2>
<p>Escolha o sabor mais adequado ao seu cão, defina a porção certa para o porte dele e faça a transição de forma gradual. Para entender o tamanho ideal de cada refeição, veja nosso conteúdo sobre <a href="porcao-ideal-comida-natural-caes.html">a porção ideal de comida natural</a>.</p>
{CTA}
<p>Quer saber se a comida natural é indicada para o seu caso? Fale com nosso time e receba uma recomendação personalizada.</p>"""),

 dict(slug="alergia-alimentar-em-caes-sintomas-causas", img="dogs-veggies.png", cat="Saúde", date="2025-05-05",
  title="Alergia alimentar em cães: sintomas, causas e como a dieta ajuda",
  desc="Coceira, vermelhidão e problemas digestivos? Entenda os sintomas da alergia alimentar em cães, as causas mais comuns e como a dieta hipoalergênica ajuda.",
  kw="alergia alimentar em cães, cachorro com coceira, dieta hipoalergênica",
  body=f"""<p>A <strong>alergia alimentar em cães</strong> é uma das causas mais comuns de coceira e problemas de pele. A boa notícia é que, com a dieta certa, muitos sinais melhoram de forma significativa.</p>
<h2>Principais sintomas</h2>
<ul>
<li>Coceira frequente (patas, orelhas, focinho e barriga);</li>
<li>Vermelhidão, descamação e otites de repetição;</li>
<li>Problemas digestivos como diarreia e gases;</li>
<li>Queda de pelo e lambedura excessiva.</li>
</ul>
<h2>O que causa a alergia?</h2>
<p>Geralmente, o sistema imune reage a <strong>proteínas ou aditivos</strong> presentes na alimentação. Corantes, conservantes e certos grãos estão entre os gatilhos mais frequentes.</p>
<h2>Como a dieta hipoalergênica ajuda</h2>
<p>Uma alimentação <strong>limpa e funcional</strong>, com proteína de fácil digestão e sem ingredientes inflamatórios, reduz a exposição aos gatilhos. As fórmulas da Petderma Food foram desenvolvidas justamente para pets com sensibilidades. Saiba mais sobre o impacto da comida na <a href="dermatite-em-caes-alimentacao-saude-da-pele.html">saúde da pele do seu cão</a>.</p>
{CTA}"""),

 dict(slug="dermatite-em-caes-alimentacao-saude-da-pele", img="blog-3.jpg", cat="Dermatologia", date="2025-05-07",
  title="Dermatite em cães: como a alimentação influencia a saúde da pele",
  desc="A dermatite em cães tem ligação direta com a alimentação. Veja como uma dieta natural e hipoalergênica apoia a saúde da pele e da pelagem do seu pet.",
  kw="dermatite em cães, saúde da pele do cachorro, alimentação e pele pet",
  body=f"""<p>A pele é o maior órgão do corpo do cão e um espelho da saúde interna. Quando há <strong>dermatite</strong>, a alimentação é um dos fatores que mais influenciam a recuperação.</p>
<h2>A relação entre comida e pele</h2>
<p>Nutrientes de qualidade fortalecem a <strong>barreira cutânea</strong> e modulam processos inflamatórios. Já ingredientes artificiais podem agravar quadros de coceira e vermelhidão.</p>
<h2>O que priorizar na dieta</h2>
<ul>
<li>Proteínas de boa digestibilidade, como o lombo suíno;</li>
<li>Ausência de corantes, conservantes e transgênicos;</li>
<li>Vegetais e legumes que ajudam na digestão.</li>
</ul>
<p>Conheça os benefícios da <a href="proteina-de-lombo-suino-pets-sensiveis.html">proteína de lombo suíno para pets sensíveis</a>.</p>
{CTA}
<p><strong>Importante:</strong> alimentação é parte do cuidado, mas o acompanhamento de um médico-veterinário é essencial para o diagnóstico correto.</p>"""),

 dict(slug="proteina-de-lombo-suino-pets-sensiveis", img="product-packs.jpg", cat="Ingredientes", date="2025-05-09",
  title="Proteína de lombo suíno: por que é ideal para pets sensíveis",
  desc="Entenda por que a proteína de lombo suíno é altamente digestível, palatável e indicada para cães com sensibilidades alimentares e dermatológicas.",
  kw="proteína de lombo suíno, proteína para cães alérgicos, comida natural proteína",
  body=f"""<p>Nem toda proteína é igual. Para pets com sensibilidades, a escolha da fonte proteica faz toda a diferença — e o <strong>lombo suíno</strong> é uma das melhores opções.</p>
<h2>Por que lombo suíno?</h2>
<ul>
<li><strong>Alta digestibilidade:</strong> leve para o organismo, reduz desconfortos;</li>
<li><strong>Palatabilidade:</strong> sabor e aroma que agradam até os mais exigentes;</li>
<li><strong>Suporte à pele e pelagem:</strong> aminoácidos de qualidade.</li>
</ul>
<h2>50% de proteína em cada porção</h2>
<p>As receitas da Petderma Food trazem <strong>alta concentração de proteína de lombo suíno</strong>, garantindo energia e nutrição de verdade. Veja como ela se compara em nosso conteúdo <a href="comida-natural-x-racao-seca.html">comida natural x ração seca</a>.</p>
{CTA}"""),

 dict(slug="comida-natural-x-racao-seca", img="bowl-fresh.png", cat="Nutrição", date="2025-05-11",
  title="Comida natural x ração seca: qual a melhor para o seu cão?",
  desc="Comparativo honesto entre comida natural e ração seca: digestibilidade, ingredientes, hidratação e custo. Descubra qual faz mais sentido para o seu pet.",
  kw="comida natural x ração seca, ração ou comida natural, melhor alimentação cães",
  body=f"""<p>Uma das dúvidas mais comuns dos tutores: vale a pena trocar a ração seca pela <strong>comida natural</strong>? Vamos comparar de forma honesta.</p>
<h2>Ingredientes e processamento</h2>
<p>A comida natural usa ingredientes reais e pouco processamento. Muitas rações passam por altas temperaturas e incluem aditivos para cor, sabor e conservação.</p>
<h2>Digestibilidade e hidratação</h2>
<p>Alimentos frescos costumam ser <strong>mais digestíveis</strong> e têm maior teor de água, o que ajuda na hidratação e no funcionamento intestinal.</p>
<h2>E o custo?</h2>
<p>A comida natural pode ter custo por refeição um pouco maior, mas oferece controle de porção, qualidade e foco em saúde — especialmente para pets com <a href="alergia-alimentar-em-caes-sintomas-causas.html">alergias alimentares</a>.</p>
{CTA}"""),

 dict(slug="transicao-racao-para-comida-natural", img="blog-1.jpg", cat="Guia prático", date="2025-05-13",
  title="Como fazer a transição da ração para a comida natural",
  desc="Passo a passo para trocar a ração pela comida natural sem desconforto: cronograma de adaptação, sinais para observar e dicas para uma transição tranquila.",
  kw="transição ração comida natural, trocar ração por comida natural, adaptação alimentar cães",
  body=f"""<p>A troca para a <strong>comida natural</strong> deve ser feita de forma gradual para respeitar o sistema digestivo do seu cão. Veja o passo a passo.</p>
<h2>Cronograma sugerido</h2>
<ol>
<li><strong>Dias 1–3:</strong> 25% de comida natural + 75% do alimento atual;</li>
<li><strong>Dias 4–6:</strong> 50% + 50%;</li>
<li><strong>Dias 7–9:</strong> 75% + 25%;</li>
<li><strong>Dia 10 em diante:</strong> 100% comida natural.</li>
</ol>
<h2>O que observar</h2>
<p>Acompanhe fezes, apetite e disposição. Pequenos ajustes no ritmo são normais. Para acertar a quantidade, veja <a href="porcao-ideal-comida-natural-caes.html">a porção ideal</a>.</p>
{CTA}"""),

 dict(slug="ingredientes-que-fazem-mal-caes-alergicos", img="dogs-veggies.png", cat="Ingredientes", date="2025-05-15",
  title="Ingredientes que fazem mal para cães alérgicos (e o que usar no lugar)",
  desc="Conheça os ingredientes que mais causam alergia em cães e descubra alternativas naturais e seguras para a alimentação do seu pet sensível.",
  kw="ingredientes que fazem mal para cães, alergia ingredientes cachorro, comida natural sem grãos",
  body=f"""<p>Para cães alérgicos, alguns ingredientes são verdadeiros gatilhos. Saber identificá-los é o primeiro passo para uma alimentação mais segura.</p>
<h2>Evite</h2>
<ul>
<li><strong>Corantes e conservantes artificiais;</strong></li>
<li><strong>Grãos</strong> em excesso (gatilho comum de sensibilidades);</li>
<li>Transgênicos e aditivos de sabor;</li>
<li>Excesso de sal e temperos.</li>
</ul>
<h2>Prefira</h2>
<ul>
<li>Proteína de lombo suíno, de fácil digestão;</li>
<li>Abóbora, mandioquinha, chuchu e ervilha;</li>
<li>Receitas limpas, sem aditivos.</li>
</ul>
<p>Entenda por que <a href="alimentacao-natural-para-caes-guia-completo.html">a alimentação natural</a> é uma aliada dos pets sensíveis.</p>
{CTA}"""),

 dict(slug="porcao-ideal-comida-natural-caes", img="product-packs.jpg", cat="Guia prático", date="2025-05-17",
  title="Qual a porção ideal de comida natural para o seu cão?",
  desc="Tabela de porção diária por peso e dicas para ajustar a quantidade de comida natural conforme o porte, a idade e o nível de atividade do seu cão.",
  kw="porção comida natural cães, quantidade comida natural cachorro, tabela porção pet",
  body=f"""<p>Servir a <strong>quantidade certa</strong> é essencial para manter o peso ideal e a saúde do seu cão. A porção varia conforme o peso do pet.</p>
<h2>Tabela de referência</h2>
<ul>
<li>Até 4 kg — 200 g/dia;</li>
<li>De 4 a 7 kg — 300 g/dia;</li>
<li>De 7 a 9 kg — 350 g/dia;</li>
<li>De 9 a 13 kg — 400 g/dia;</li>
<li>De 13 a 16 kg — 500 g/dia;</li>
<li>De 16 a 20 kg — 600 g/dia.</li>
</ul>
<p>Cães acima de 20 kg precisam de cálculo personalizado — fale com nosso time pelo WhatsApp.</p>
<h2>Fatores que influenciam</h2>
<p>Idade, nível de atividade e condição corporal também contam. Em fase de <a href="transicao-racao-para-comida-natural.html">transição alimentar</a>, ajuste aos poucos.</p>
{CTA}"""),

 dict(slug="comida-natural-para-gatos", img="hero.png", cat="Gatos", date="2025-05-19",
  title="Comida natural para gatos: cuidados e benefícios",
  desc="Gatos também se beneficiam da alimentação natural. Veja cuidados específicos, benefícios e o que considerar antes de mudar a dieta do seu felino.",
  kw="comida natural para gatos, alimentação natural felinos, dieta natural gato",
  body=f"""<p>Os gatos são <strong>carnívoros estritos</strong> e têm necessidades nutricionais específicas. A alimentação natural, quando bem balanceada, traz ótimos benefícios.</p>
<h2>Benefícios para felinos</h2>
<ul>
<li>Maior ingestão de água via alimento úmido;</li>
<li>Pele e pelagem mais saudáveis;</li>
<li>Digestão leve e controle de peso.</li>
</ul>
<h2>Cuidados importantes</h2>
<p>Gatos precisam de nutrientes como <strong>taurina</strong> e não devem receber dietas improvisadas. Por isso, conte sempre com fórmulas balanceadas e orientação profissional.</p>
<p>Veja também como funciona a <a href="conservacao-comida-natural-armazenar.html">conservação da comida natural</a>.</p>
{CTA}"""),

 dict(slug="conservacao-comida-natural-armazenar", img="bowl-fresh.png", cat="Guia prático", date="2025-05-21",
  title="Conservação da comida natural: como armazenar e servir com segurança",
  desc="Aprenda a armazenar e servir a comida natural do seu pet com segurança: congelamento, validade após aberto, descongelamento e boas práticas de higiene.",
  kw="conservação comida natural, como armazenar comida natural pet, validade comida natural cães",
  body=f"""<p>Por ser um alimento fresco e <strong>embalado a vácuo</strong>, a comida natural exige cuidados simples de conservação para manter o frescor e a segurança.</p>
<h2>Boas práticas</h2>
<ul>
<li><strong>Mantenha congelado</strong> até o momento do uso;</li>
<li>Descongele na geladeira, nunca em temperatura ambiente por longos períodos;</li>
<li>Após aberto, consuma em até <strong>48 horas</strong>;</li>
<li>Sirva em vasilha limpa e na porção certa.</li>
</ul>
<h2>Por que isso importa</h2>
<p>A conservação correta preserva nutrientes e evita contaminações. Combinada com a <a href="porcao-ideal-comida-natural-caes.html">porção ideal</a>, garante praticidade e zero desperdício.</p>
{CTA}"""),
]

def render_post(p, idx):
    canonical = f"{BASE}/blog/{p['slug']}.html"
    date_br = "{}/{}/{}".format(*reversed(p['date'].split('-')))
    ld = {
      "@context":"https://schema.org","@type":"BlogPosting",
      "headline":p['title'],"description":p['desc'],
      "image":f"{BASE}/assets/img/{p['img']}",
      "datePublished":p['date'],"dateModified":p['date'],
      "author":{"@type":"Organization","name":"Petderma Food"},
      "publisher":{"@type":"Organization","name":"Petderma Food","logo":{"@type":"ImageObject","url":f"{BASE}/assets/img/logo.png"}},
      "mainEntityOfPage":{"@type":"WebPage","@id":canonical},
      "keywords":p['kw']
    }
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Início","item":f"{BASE}/"},
      {"@type":"ListItem","position":2,"name":"Blog","item":f"{BASE}/blog/"},
      {"@type":"ListItem","position":3,"name":p['title'],"item":canonical}]}
    extra = ('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>\n'
             '<script type="application/ld+json">'+json.dumps(bc,ensure_ascii=False)+'</script>')
    related = [q for q in POSTS if q['slug']!=p['slug']][idx%9: idx%9+3]
    if len(related)<3: related = [q for q in POSTS if q['slug']!=p['slug']][:3]
    rel_cards = "".join(card(q, "") for q in related)
    out = head(p['title']+" | Petderma Food", p['desc'], canonical, "../", p['img'], extra)
    out += header("../")
    out += f'''
<article class="article">
  <div class="container">
    <nav class="breadcrumb" aria-label="Trilha"><a href="../index.html">Início</a><span>›</span><a href="index.html">Blog</a><span>›</span>{html.escape(p['title'])}</nav>
    <div class="article__wrap">
      <div class="article__meta"><span class="article__tag">{p['cat']}</span><time datetime="{p['date']}">{date_br}</time><span>·</span><span>Petderma Food</span></div>
      <h1 class="article__title">{html.escape(p['title'])}</h1>
      <img class="article__cover" src="../assets/img/{p['img']}" alt="{html.escape(p['title'])}" width="1200" height="600">
      <div class="article__body">
        {p['body']}
      </div>
    </div>
  </div>
</article>
<section class="related">
  <div class="container">
    <h2>Continue lendo</h2>
    <div class="related__grid">{rel_cards}</div>
  </div>
</section>
'''
    out += footer("../")
    out += "\n</body>\n</html>"
    return out

def card(p, prefix_blog):
    href = f"{prefix_blog}{p['slug']}.html"
    return f'''<article class="post">
  <a href="{href}" class="post__media"><img src="../assets/img/{p['img']}" alt="{html.escape(p['title'])}" width="650" height="365" loading="lazy"></a>
  <div class="post__body">
    <h3><a href="{href}">{html.escape(p['title'])}</a></h3>
    <p>{html.escape(p['desc'][:120])}…</p>
    <a href="{href}" class="post__link">Ler mais →</a>
  </div>
</article>'''

def render_index():
    canonical = f"{BASE}/blog/"
    ld = {"@context":"https://schema.org","@type":"Blog","name":"Blog Petderma Food",
      "description":"Conteúdos sobre alimentação natural, saúde, pele e bem-estar de cães e gatos.",
      "url":canonical,"publisher":{"@type":"Organization","name":"Petderma Food"},
      "blogPost":[{"@type":"BlogPosting","headline":p['title'],"url":f"{BASE}/blog/{p['slug']}.html","datePublished":p['date']} for p in POSTS]}
    extra = '<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>'
    out = head("Blog Petderma Food — Alimentação natural, saúde e pele dos pets",
      "Dicas e guias sobre alimentação natural, alergias, dermatologia e bem-estar de cães e gatos, por especialistas da Petderma Food.",
      canonical, "../", "dogs-veggies.png", extra)
    out += header("../")
    cards = "".join(card(p, "") for p in POSTS)
    out += f'''
<section class="page-hero">
  <div class="container">
    <p class="eyebrow">Blog</p>
    <h1>Alimentação natural, saúde e pele do seu pet</h1>
    <p>Guias práticos e conteúdos confiáveis sobre nutrição, alergias e dermatologia veterinária para cães e gatos.</p>
  </div>
</section>
<section class="blog-list">
  <div class="container">
    <div class="blog-list__grid">{cards}</div>
  </div>
</section>
'''
    out += footer("../")
    out += "\n</body>\n</html>"
    return out

# ---- escrever arquivos ----
os.makedirs(os.path.join(ROOT,"blog"), exist_ok=True)
for i,p in enumerate(POSTS):
    with open(os.path.join(ROOT,"blog",p['slug']+".html"),"w",encoding="utf-8") as f:
        f.write(render_post(p,i))
with open(os.path.join(ROOT,"blog","index.html"),"w",encoding="utf-8") as f:
    f.write(render_index())

# sitemap
urls = [(f"{BASE}/","1.0","weekly"),(f"{BASE}/blog/","0.9","weekly")]
urls += [(f"{BASE}/blog/{p['slug']}.html","0.7","monthly") for p in POSTS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u,pr,fr in urls:
    sm += f'  <url><loc>{u}</loc><changefreq>{fr}</changefreq><priority>{pr}</priority></url>\n'
sm += '</urlset>\n'
with open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8") as f:
    f.write(sm)

with open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

print("OK:", len(POSTS), "posts +", "blog/index.html + sitemap.xml + robots.txt")
print("slugs:", ", ".join(p['slug'] for p in POSTS))
