---
name: sm-criar
description: Cria conteúdo nativo para Instagram, LinkedIn e YouTube na voz do projeto, com adaptação entre plataformas (repurposing) e score de qualidade antes de entregar. Use quando o usuário pedir para escrever post, legenda, roteiro, carrossel, adaptar conteúdo ou "criar conteúdo".
---

# SM Criar — Conteúdo Nativo por Plataforma

Escreve conteúdo na voz do projeto, nativo para cada plataforma, e avalia a qualidade contra critérios objetivos antes de entregar.

## Pré-requisito
Leia `profile.md` e `voice.md` do projeto ativo (`social-media/projects/<projeto>/`). Se houver mais de um projeto, confirme qual. Sem esses arquivos, oriente rodar `/sm-setup`.

---

## Processo

### 0. Investigar o nicho e descobrir o tema (nunca pule quando o tema não vier claro)

Antes de qualquer escrita, entenda o território.

**Se o usuário trouxer um tema específico:** vá direto ao Passo 1.

**Se o usuário não trouxer tema (ou pedir sugestões):**

1. Releia `profile.md`: pilares de conteúdo, audiência, dores principais, ponto de vista único.
2. Faça até 3 perguntas de investigação para afinar o nicho. Exemplos:
   - "Aconteceu algo recente na sua empresa, setor ou com clientes que merecia virar post?"
   - "Qual dos seus pilares você quer reforçar desta vez?" (liste os pilares do profile.md)
   - "Tem alguma crença comum no seu mercado que você discorda? Algo que seus clientes erram com frequência?"
   - "O que você se pega repetindo em reuniões de conselho que nunca viu escrito em lugar nenhum?"
3. Com base nas respostas e no profile.md, gere **5 sugestões de temas**, ranqueadas por relevância e oportunidade, cada uma com:
   - Título-gancho provisório (1 linha)
   - Pilar que atende
   - Por que agora (contexto ou dado que torna o tema relevante)
4. Deixe o usuário escolher ou combine os temas se houver complementaridade.

> O objetivo desta etapa é nunca começar a escrever no vazio. Um tema afiado com ângulo claro vale mais do que dez posts genéricos.

---

### 1. Capturar o insumo
Confirme (ou identifique no pedido):
- **Tema**: definido no Passo 0, vindo do radar (`research/`), de notas do usuário, ou da matriz (`strategy.md`)
- **Plataformas**: quais desta vez? (das listadas no profile.md)
- **Formato**: post simples, carrossel, roteiro de vídeo/Reels, ou pacote completo (1 tema → todas as plataformas)?

---

### 2. Planejar o ângulo (nunca pule)
Pesquise o tema se necessário (WebSearch) e apresente **3 ângulos possíveis** com frameworks:
- PAS (problema → agitação → solução)
- How-to (passo a passo prático)
- História pessoal (narrativa com lição)
- Contrário (desafiar o senso comum)

Deixe o usuário escolher ou recomende um com justificativa.

---

### 3. Escrever nativo por plataforma

**LinkedIn**
- 300 a 500 palavras (respeite o range — abaixo de 300 é raso, acima de 500 perde o leitor)
- Estrutura: gancho (1ª linha decide tudo) → contexto com dados → corpo escaneável → conclusão ou CTA
- Parágrafos de 1 a 2 linhas, espaço em branco generoso
- Dados e fatos concretos obrigatórios para sustentar o argumento
- 3 a 5 hashtags no fim (apenas se a voz do projeto usar)
- Link vai no primeiro comentário, nunca no corpo
- Tom: reflexivo e profissional, mas na voz do projeto
- Sem travessão (—) nem símbolos tipográficos formais

**Instagram**
- Gancho nos primeiros 125 caracteres (corte do "mais")
- Legenda: 1 ideia central, escaneável, CTA claro (comentar/salvar/compartilhar)
- 3 a 10 hashtags (mix de nicho + alcance)
- Se carrossel: 6 a 10 slides, 1 ideia por slide, máx. 20 palavras por slide, slide final com CTA
- Se Reels: roteiro de até 45 segundos, máximo 2 pontos-chave, gancho nunca começa com "Eu", incluir sugestão de palavra-gatilho para comentários (UMA palavra maiúscula)

**YouTube**
- Título: 60 a 70 caracteres, curiosidade + palavra-chave
- Descrição: 150+ caracteres acima da dobra com palavras-chave, depois capítulos/timestamps
- Roteiro (se pedido): gancho de 15s → promessa → conteúdo → CTA de inscrição
- Conceito de thumbnail: máx. 4 palavras, emoção clara (passe ao `/sm-arte`)

---

### 4. Repurposing (1 tema → várias plataformas)
Quando for pacote completo:
1. Extraia 3 a 7 insights independentes do tema
2. Ranqueie por impacto; o mais forte vira o conteúdo âncora
3. Adapte cada um para a plataforma: **mesma voz, registro diferente** (LinkedIn reflexivo, Instagram direto e visual, YouTube didático)
4. Cada peça deve parecer escrita PARA aquela plataforma, nunca copy-paste
5. Sugira espaçamento de publicação (3 a 7 dias entre derivados do mesmo tema)

---

### 5. Score de qualidade (antes de entregar)
Avalie o rascunho em 5 dimensões (1 a 10):

| Dimensão | Critério |
|---|---|
| Gancho | Pararia o scroll? Específico ou genérico? |
| Voz | Bate com voice.md? Respeita as "ausências"? |
| Densidade de valor | Ensina, conta ou prova algo com dados? Ou é vazio? |
| Estrutura | Escaneável no celular? Contexto antes da conclusão? CTA claro? |
| Pronto para publicar | Parece autêntico ou parece IA? |

**Floors de qualidade:**
- Verifique se `voice.md` do projeto define critérios mínimos (ex: gancho mínimo 9, média mínima 8,6). Se definir, esses valores prevalecem sobre os defaults abaixo.
- Default geral: nenhuma dimensão abaixo de 7. Se houver, revise antes de mostrar.
- Se alguma dimensão < 7, revise antes de mostrar. Nunca entregue um post abaixo do floor do projeto.

---

### 6. Iterar e finalizar
Até 3 rodadas de ajuste. Quando o usuário aprovar ("aprovado", "fecha", "ship it"):
- Salve em `content/final/YYYY-MM-DD-<plataforma>-<slug>.md`
- Ofereça: arte (`/sm-arte`) ou pacote de publicação (`/sm-publicar`)

Rascunhos intermediários vão em `content/drafts/`.

---

## Regras
- NUNCA escreva sem ler voice.md antes. As "ausências" da voz são invioláveis.
- NUNCA pule a investigação de nicho quando o tema não vier claro.
- Sempre planeje o ângulo antes de escrever.
- Sem travessão (—), sem CTA caça-engajamento, sem hashtags fora do padrão da voz.
- Idioma do profile.md (padrão: português brasileiro).
- Entregue o texto final em bloco de código para facilitar copiar.
- Conteúdo deve soar 100% humano: sem construções simétricas demais, sem listas numeradas em post de texto corrido, sem vocabulário que nenhum humano usa ao falar.
