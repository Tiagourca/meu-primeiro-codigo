# Sistema de Social Media

Sistema modular de criação de conteúdo para Instagram, LinkedIn e YouTube, com suporte a múltiplos projetos independentes (cada um com voz, estratégia e histórico próprios).

Combina o melhor de três sistemas open source:
- [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) — sistema de voz, pesquisa de nicho, score de qualidade, arte
- [blacktwist/social-media-skills](https://github.com/blacktwist/social-media-skills) — regras nativas por plataforma, repurposing, análise contra baseline próprio
- [guyaga/claude-code-social-media-skill](https://github.com/guyaga/claude-code-social-media-skill) — fluxo de publicação com preview e confirmação

## Fluxo completo

```
/sm-setup     → cria o projeto (perfil + voz + estratégia)     [uma vez por projeto]
/sm-pesquisa  → radar de assuntos da semana (10-20 temas)      [semanal]
/sm-criar     → conteúdo nativo por plataforma + score          [por conteúdo]
/sm-arte      → arte (HTML/CSS ou prompt Gemini)                [por conteúdo]
/sm-publicar  → pacote de publicação manual + checklist         [por conteúdo]
/sm-analisar  → análise de performance + aprendizado            [mensal]
```

O ciclo se retroalimenta: o `/sm-analisar` grava os "padrões comprovados" no `voice.md` do projeto, e o `/sm-criar` usa esses padrões nas próximas criações.

## Estrutura de um projeto

```
projects/<nome-do-projeto>/
  profile.md     # Quem é, audiência, plataformas, pilares
  voice.md       # Voz + padrões comprovados por dados
  strategy.md    # Matriz de conteúdo e frequência
  research/      # Radares semanais
  content/
    drafts/      # Rascunhos
    final/       # Aprovados
    published/   # Log de publicados + métricas
  art/           # Artes geradas
  analytics/     # Análises e dashboard
```

## Começando

1. Rode `/sm-setup` e crie seu primeiro projeto
2. Rode `/sm-pesquisa` para ver o que está em alta no seu nicho
3. Escolha um tema e rode `/sm-criar`

## Modo de publicação

Atualmente **manual**: o `/sm-publicar` monta o pacote completo (texto, arte, hashtags, horário, checklist) e você cola nas plataformas. Postagem automática via API (Upload Post ou similar) pode ser plugada depois sem mudar o restante do fluxo.
