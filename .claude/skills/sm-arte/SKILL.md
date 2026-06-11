---
name: sm-arte
description: Cria a arte do conteúdo - gráficos HTML/CSS prontos para screenshot ou prompts de geração de imagem (Gemini/outros). Suporta post único, carrossel, infográfico e thumbnail de YouTube. Use quando o usuário pedir arte, imagem, gráfico, carrossel visual, thumbnail ou design do post.
---

# SM Arte — Design do Conteúdo

Cria a parte visual do conteúdo por dois caminhos: HTML/CSS renderizável (controle total, screenshot e pronto) ou prompt de geração de imagem (para Gemini ou similar).

## Pré-requisito
Leia o conteúdo aprovado mais recente em `content/final/` do projeto ativo (ou peça o texto). Leia `profile.md` para identidade do projeto (cores de marca, se documentadas).

## Escolher o caminho

**Caminho A — HTML/CSS** (preferido quando o conteúdo tem estrutura: passos, comparações, dados, frameworks, listas)
**Caminho B — Prompt de imagem** (quando o conteúdo é conceitual: histórias, opiniões, metáforas, bastidores)

Pergunte ao usuário ou decida pelo conteúdo e justifique.

## Dimensões por plataforma

| Uso | Dimensão |
|---|---|
| Instagram feed (quadrado) | 1080 × 1080 |
| Instagram feed/carrossel (retrato) | 1080 × 1350 |
| Instagram Stories/Reels capa | 1080 × 1920 |
| LinkedIn post | 1200 × 1400 |
| YouTube thumbnail | 1280 × 720 |

## Caminho A — HTML/CSS

1. Extraia do conteúdo: manchete, 3 a 6 pontos-chave, dado/estatística de destaque, rodapé com atribuição (@handle do projeto)
2. Gere um arquivo HTML único e autocontido em `art/YYYY-MM-DD-<slug>.html`:
   - Dimensões exatas da plataforma (div com width/height fixos)
   - Fundo escuro de alto contraste (ou cores de marca do profile.md)
   - Fonte sans-serif limpa, hierarquia tipográfica clara
   - Máximo 40 palavras visíveis na imagem inteira
   - Legível em tela de celular (teste mental: 5 cm de largura)
3. Para **carrossel**: um arquivo HTML com todos os slides empilhados (cada slide nas dimensões corretas), numerados, slide final com CTA
4. Instrua o usuário: abrir no navegador → screenshot de cada quadro (ou use a skill disponível de screenshot, se houver)

## Caminho B — Prompt de imagem

Gere o prompt pronto para colar no Gemini (ou outro gerador), em inglês, com dois estilos disponíveis:

**Estilo quadro branco**: "hand-drawn whiteboard infographic, marker pen style, notebook paper background..." — bom para dicas, fluxos, conceitos
**Estilo editorial de marca**: "clean modern editorial infographic, [cores da marca], bold typography..." — bom para autoridade e dados

O prompt deve incluir: dimensão/proporção, texto exato a renderizar (máx. 40 palavras, entre aspas), estilo, paleta, e instrução de legibilidade mobile.

## YouTube thumbnail (caso especial)

- Máximo 4 palavras na imagem
- Uma emoção clara (curiosidade, choque, ganho)
- Rosto ou objeto focal grande (se aplicável ao projeto)
- Contraste alto, legível em 120 × 68 px (tamanho que aparece na busca)
- Entregue via Caminho A (HTML 1280×720) ou B (prompt), à escolha

## Finalizar
- Salve tudo em `social-media/projects/<projeto>/art/`
- Pergunte se quer ajustar (até 3 rodadas)
- Ofereça próximo passo: `/sm-publicar` para montar o pacote de publicação

## Regras
- Máximo 40 palavras por imagem. Sem exceção.
- Nada de foto de banco de imagem ou aparência genérica de stock.
- Atribuição do projeto sempre presente (handle ou nome).
- Texto da arte no idioma do projeto.
