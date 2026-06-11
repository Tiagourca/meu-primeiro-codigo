---
name: sm-analisar
description: Analisa a performance dos posts contra o histórico do próprio projeto, identifica padrões dos melhores e piores conteúdos e gera ações concretas. Aceita métricas manuais ou export xlsx do LinkedIn. Use quando o usuário trouxer números, pedir análise de performance, "como foram meus posts" ou dashboard.
---

# SM Analisar — Performance e Aprendizado

Transforma métricas em aprendizado: o que funcionou, o que não funcionou e o que fazer diferente. O resultado alimenta os próximos ciclos do `/sm-criar`.

## Pré-requisito
Projeto ativo identificado. Fontes de dados aceitas (nesta ordem de preferência):
1. Export oficial (xlsx do LinkedIn Analytics, CSV do YouTube Studio / Meta Insights)
2. Logs em `content/published/` com métricas preenchidas
3. Dados informados manualmente (mínimo: 5 posts com impressões, curtidas e comentários)

Se não houver dados suficientes, diga claramente o que falta e como obter (LinkedIn: perfil → Análise → Exportar; YouTube: Studio → Analytics; Instagram: Insights de cada post).

## Princípio central

**O baseline é o próprio projeto, nunca benchmark genérico.** Um post com 50 curtidas em 500 impressões (10% de engajamento) é MELHOR que um com 200 curtidas em 10.000 impressões (2%). Sempre calcule taxas, não números absolutos.

## Processo

### 1. Organizar os dados
Para cada post: data, plataforma, formato, pilar/tema, gancho usado, e métricas em 3 grupos:
- **Alcance**: impressões, contas alcançadas, visitas ao perfil
- **Engajamento**: curtidas, comentários, compartilhamentos, salvos → taxa de engajamento = interações ÷ impressões
- **Conversão**: cliques, DMs, novos seguidores

Atualize os arquivos em `content/published/` com as métricas recebidas.

### 2. Análise obrigatória (4 saídas)

**Top performers** — os 3 a 5 melhores posts com diagnóstico específico: tema, formato, tipo de gancho (contrário, número, história, pergunta, notícia), horário e CTA. O que eles têm em comum?

**Bottom performers** — os 3 a 5 piores com hipótese honesta do que falhou (gancho fraco? tema fora do pilar? formato errado para a plataforma?).

**Tendências** — direção do engajamento, alcance e crescimento ao longo do tempo. Dia da semana e horário com melhor resposta (se houver dados).

**Ações** — 3 a 5 recomendações concretas, priorizadas e amarradas a achados específicos ("seus 3 melhores posts abrem com número; teste isso nos próximos 5") — nunca conselhos genéricos.

### 3. Atualizar a memória do projeto
Salve a análise em `analytics/YYYY-MM-DD-analise.md` e adicione/atualize a seção **"Padrões comprovados"** em `voice.md`:
```
## Padrões comprovados (atualizado YYYY-MM-DD)
- Ganchos que funcionam neste projeto: ...
- Formatos com melhor taxa: ...
- Temas com melhor resposta: ...
- Evitar: ...
```
Assim o `/sm-criar` usa dados reais no score das próximas criações.

### 4. Dashboard (opcional)
Se o usuário pedir dashboard ou enviar um export xlsx completo, gere um HTML autocontido em `analytics/dashboard.html` com: métricas de destaque, tendência de engajamento, dispersão dos posts em 4 quadrantes (Estrelas / Viral raso / Ouro de nicho / Abaixo da média) e heatmap por dia da semana.

### 5. Próximo passo
Ofereça transformar as recomendações em pauta: "Quer que eu rascunhe posts aplicando esses padrões? (`/sm-criar`)"

## Regras
- Nunca invente métricas. Sem dados, sem análise.
- Honestidade acima de gentileza: se está tudo abaixo do esperado, diga e explique a hipótese.
- Análises separadas por projeto E por plataforma (o que funciona no LinkedIn pode falhar no Instagram).
- Recomende ciclo mensal de análise.
