---
name: sm-pesquisa
description: Pesquisa os assuntos mais relevantes do nicho do projeto nos últimos 7 dias, com links e datas verificadas. Use quando o usuário pedir pesquisa de nicho, tendências, "o que está em alta", "sobre o que postar", ou notícias da semana.
---

# SM Pesquisa — Radar de Assuntos

Encontra de 10 a 20 temas relevantes e recentes do nicho do projeto ativo, com fontes reais, para alimentar a criação de conteúdo.

## Pré-requisito
Leia `social-media/projects/<projeto>/profile.md` para conhecer o nicho, os pilares e a audiência. Se houver mais de um projeto, pergunte qual usar. Se não existir nenhum, oriente rodar `/sm-setup` primeiro.

## Processo

### 1. Definir frentes de busca
A partir dos pilares do projeto, monte 5 frentes de pesquisa:
1. **Notícias** do nicho (últimos 7 dias)
2. **Lançamentos** (produtos, ferramentas, recursos)
3. **Controvérsias / debates** acalorados
4. **Pesquisas e dados** novos (estudos, relatórios, estatísticas)
5. **Tendências e mudanças** (algoritmos, regulação, comportamento)

### 2. Executar as buscas
Use WebSearch para cada frente (queries em português E inglês para cobertura máxima). Use WebFetch para verificar as fontes mais promissoras. Sempre filtre mentalmente para os últimos 7 dias a partir da data atual.

### 3. Verificar antes de incluir
- **Data de publicação verificada** — exclua qualquer item com mais de 7 dias ou sem data confirmável
- **Link real e acessível** — nunca invente links, métricas ou datas
- Não complete a lista com itens fracos: 12 temas fortes valem mais que 20 medianos

### 4. Entregar o radar
Tabela markdown com colunas:

| # | Tema | Pilar relacionado | Fonte (link) | Data | Sinal de atenção | Resumo do debate | Ângulo compartilhável |

- **Sinal de atenção**: por que está chamando atenção (viralizou, polêmica, dado surpreendente)
- **Ângulo compartilhável**: como o projeto poderia abordar com seu ponto de vista único (use o `profile.md`)

### 5. Salvar e oferecer próximo passo
Salve em `social-media/projects/<projeto>/research/YYYY-MM-DD.md`.
Ofereça: "Quer transformar algum desses temas em conteúdo? (`/sm-criar` + número do tema)"

## Regras
- Zero invenção: todo link, data e métrica deve vir de fonte verificada.
- Os ângulos devem refletir o ponto de vista do projeto (profile.md), não opiniões genéricas.
- Priorize temas que cruzam com os pilares; marque os que fogem deles como "fora do pilar (oportunidade)".
