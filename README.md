# Petderma Food — Landing Page

Versão redesenhada do site institucional da **Petderma Food** — linha de
alimentação natural e hipoalergênica para cães e gatos, desenvolvida por
especialistas em dermatologia veterinária.

Site original: <https://petdermafood.com.br/>

## O que mudou

Mesma estrutura, mesmo conteúdo e mesmas imagens do site original (WordPress/
Elementor), reconstruído como **site estático leve** (HTML + CSS + JS puro),
com design modernizado:

- Identidade visual mantida: verde `#3fb284` + azul `#115c8d`, logo e fotos originais
- Tipografia amigável (Nunito + Baloo 2) para um tom acolhedor de marca pet
- Hero com CTA duplo (WhatsApp + Loja) e provas de valor (50% proteína, 0 grãos, 100% natural)
- Ícones em SVG inline (substituem os PNGs brancos do original, mais nítidos e escaláveis)
- Seções: Benefícios, Por que Petderma, Saúde em 1º lugar, Produtos, Como funciona (4 passos), FAQ com tabela de porções, Blog, Newsletter
- FAQ em acordeão (abre um item por vez) com a tabela de porção diária por peso
- Responsivo (desktop / tablet / mobile) com menu hambúrguer
- Botão flutuante de WhatsApp + animações suaves de reveal no scroll
- SEO: meta tags, Open Graph e Twitter Card

## Estrutura

```
.
├── index.html              # página única
├── assets/
│   ├── css/styles.css      # design system + responsivo
│   ├── js/script.js        # menu mobile, acordeão FAQ, reveal, newsletter
│   └── img/                # imagens originais do site (renomeadas)
├── public/img/             # backup das imagens com nomes originais
└── index_original.html     # snapshot do site WordPress original (referência)
```

## Links de conversão

- **Loja**: <https://petdermastore.com.br/>
- **WhatsApp**: +55 11 98981-2898
- **Instagram**: <https://www.instagram.com/petderma/>

## Rodar localmente

```bash
python3 -m http.server 4178
# abra http://localhost:4178
```

## Deploy

Site 100% estático — deploy automático na **Vercel** a cada push na branch `main`.
Não há build step (`vercel.json` aponta a raiz como output estático).
