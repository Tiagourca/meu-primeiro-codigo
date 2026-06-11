---
name: sm-setup
description: Cria ou configura um projeto de social media com perfil, voz e estratégia próprios. Use quando o usuário quiser criar um novo projeto, configurar sua voz, definir pilares de conteúdo, ou disser "novo projeto", "configurar voz", "setup de social media".
---

# SM Setup — Projetos e Voz

Configura projetos de social media independentes, cada um com perfil, voz e estratégia próprios. Todos os outros módulos (`sm-pesquisa`, `sm-criar`, `sm-arte`, `sm-publicar`, `sm-analisar`) dependem dos arquivos criados aqui.

## Estrutura de dados

```
social-media/projects/<slug-do-projeto>/
  profile.md     # Quem é, audiência, pilares, promessa, limites
  voice.md       # Tom, ritmo, ganchos, frases assinatura, o que nunca faz
  strategy.md    # Pilares × formatos, mix de conteúdo, frequência
  research/      # Pesquisas do sm-pesquisa
  content/
    drafts/      # Rascunhos do sm-criar
    final/       # Conteúdo aprovado
    published/   # Log do que foi publicado (usado pelo sm-analisar)
  art/           # Artes do sm-arte
  analytics/     # Dados de performance
```

## Processo

### Passo 0 — Identificar o projeto
Liste as pastas em `social-media/projects/`. Se existirem projetos, pergunte (AskUserQuestion): trabalhar em um existente ou criar novo? Se não existir nenhum, vá direto para criação.

### Passo 1 — Entrevista (lote 1: identidade)
Use AskUserQuestion. SEM preâmbulo ou explicação — comece direto:
- Nome do projeto e o que ele é (marca pessoal, empresa, nicho)?
- Quem é a audiência-alvo (cargo, interesse, dor principal)?
- Quais plataformas este projeto usa? (Instagram, LinkedIn, YouTube — pode ser subconjunto)
- Qual idioma do conteúdo? (padrão: português brasileiro)

### Passo 2 — Entrevista (lote 2: posicionamento)
- 3 a 5 pilares de conteúdo (temas que domina e quer ser conhecido por)?
- Ponto de vista único / opinião contrária ao senso comum?
- Promessa da marca (o que a audiência sempre ganha)?
- Assuntos proibidos ou tom a evitar?

### Passo 3 — Criar profile.md
Máximo 300 palavras. Estrutura: Nome | Projeto | Audiência | Plataformas | Idioma | Pilares | Ponto de vista | Promessa | Limites.

### Passo 4 — Coletar amostras de escrita
Peça 3 a 5 amostras de textos reais do usuário (posts antigos, e-mails, qualquer escrita autêntica). Se não tiver, ofereça construir uma voz inicial a partir das respostas da entrevista e refinar depois com posts reais.

### Passo 5 — Analisar amostras e criar voice.md
Analise APENAS o que está nas amostras (nunca template genérico):
- Comprimento médio de frase e parágrafo
- Tom (direto, provocador, didático, caloroso...)
- Como abre e como fecha textos
- Padrões de gancho
- Frases ou construções assinatura
- **Ausências notáveis**: o que essa voz NUNCA faz (emojis? jargão? hashtags? perguntas retóricas?)

Máximo 500 palavras. Salve em `voice.md`.

### Passo 6 — Estratégia (strategy.md)
Monte com o usuário:
1. **Matriz de conteúdo**: pilares (linhas) × 8 formatos (colunas): Prático/How-to, Motivacional, Analítico, Contrário, Observação de tendência, X vs Y, Presente vs Futuro, Lista. Cada célula = uma manchete concreta e específica daquele pilar+formato.
2. **Mix sugerido**: Educacional 30% | Storytelling 25% | Pessoal 20% | Engajamento 15% | Promocional 10% (ajuste conforme objetivo do projeto).
3. **Frequência por plataforma** que o usuário consegue sustentar.

### Passo 7 — Encerramento
Confirme os arquivos criados e ofereça o próximo passo: `/sm-pesquisa` para buscar assuntos ou `/sm-criar` para criar o primeiro conteúdo.

## Regras
- Multi-projeto é obrigatório: NUNCA misture voz ou conteúdo entre projetos. Sempre confirme qual projeto está ativo antes de qualquer ação.
- A análise de voz vem das amostras reais, não de suposições.
- Idioma padrão: português brasileiro (a menos que o profile.md diga outra coisa).
- Sem em dashes (—) no conteúdo gerado, a menos que as amostras do usuário usem.
