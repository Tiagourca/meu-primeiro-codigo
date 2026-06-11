---
name: sm-publicar
description: Monta o pacote de publicação manual - texto final, arte, hashtags, primeiro comentário, melhor horário e checklist por plataforma, com preview para aprovação. Use quando o usuário disser publicar, postar, agendar, "montar pacote" ou "preparar para postar".
---

# SM Publicar — Pacote de Publicação (modo manual)

Reúne tudo que foi criado em um pacote pronto para o usuário copiar e publicar em cada plataforma, com checklist e registro do que foi publicado.

> Modo atual: **manual**. A skill prepara e organiza; quem aperta o botão é o usuário. (Postagem automática via API pode ser adicionada depois.)

## Pré-requisito
Localize o conteúdo aprovado em `content/final/` e a arte em `art/` do projeto ativo. Se algo estiver faltando (sem arte, por exemplo), pergunte se quer criar (`/sm-arte`) ou seguir sem.

## Processo

### 1. Montar o pacote por plataforma
Para cada plataforma do conteúdo, gere uma seção com TUDO pronto para copiar:

**LinkedIn**
- Texto final (bloco de código, pronto para colar)
- Primeiro comentário (link ou complemento, se houver)
- Arquivo de arte a anexar (caminho)
- Melhor janela de horário: terça a quinta, 8h-10h ou 12h-14h (ajuste se `analytics/` tiver dados reais do projeto)

**Instagram**
- Legenda final (bloco de código)
- Hashtags em bloco separado (para colar na legenda ou no 1º comentário, conforme a voz)
- Arquivos da arte/carrossel em ordem (caminhos numerados)
- Melhor janela: 11h-13h ou 18h-21h (ajuste com dados reais se existirem)
- Se Reels: roteiro + capa + palavra-gatilho do comentário fixado

**YouTube**
- Título final
- Descrição completa (bloco de código, com capítulos se houver)
- Tags sugeridas
- Thumbnail (caminho do arquivo)
- Sugestão de comentário fixado

### 2. Checklist pré-publicação
Apresente e percorra com o usuário:
- [ ] Texto revisado uma última vez em voz alta (erros que o olho pula)
- [ ] Arte legível no celular
- [ ] Link NO PRIMEIRO COMENTÁRIO (LinkedIn), nunca no corpo
- [ ] Hashtags conferidas (sem tag quebrada ou irrelevante)
- [ ] Horário escolhido
- [ ] Perfil certo logado (multi-projeto: confira o projeto ativo!)

### 3. Preview e aprovação
Mostre o pacote completo e peça aprovação explícita antes de considerar fechado. Nunca marque como publicado sem o usuário confirmar que postou.

### 4. Registrar a publicação
Quando o usuário confirmar que publicou, salve o log em `content/published/YYYY-MM-DD-<plataforma>-<slug>.md` com:
- Texto publicado, plataforma, data/hora real
- URL do post (peça ao usuário)
- Campo vazio de métricas para o `/sm-analisar` preencher depois:
  ```
  ## Métricas (preencher em 7 dias)
  - Impressões:
  - Curtidas:
  - Comentários:
  - Compartilhamentos/Salvos:
  - Cliques/Novos seguidores:
  ```

### 5. Próximo passo
Sugira: "Em 7 dias, traga os números e rode `/sm-analisar` para eu aprender o que funciona neste projeto."

## Regras
- Nunca declare algo publicado sem confirmação do usuário.
- Cada projeto tem seu próprio log; nunca misture.
- Horários sugeridos são ponto de partida; dados reais do projeto (analytics/) sempre têm prioridade sobre benchmarks genéricos.
