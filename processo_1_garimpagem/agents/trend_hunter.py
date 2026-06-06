"""Subagente 1 — Trend Hunter (Caçador de Tendências)."""
import json
import re
from datetime import datetime

import anthropic

from config import MODEL_ID, AGENT_MAX_TOKENS
from models.trend_output import TrendHunterOutput
from tools.pinterest_tools import TREND_HUNTER_TOOLS, execute_trend_tool

SYSTEM_PROMPT = """Você é o **Trend Hunter** (Caçador de Tendências), o Subagente 1 de uma cadeia
determinística de Garimpagem Científica de Produtos para o ecossistema Pinterest 2026.

## Missão
Monitorar e catalogar tendências emergentes e palavras-chave "unbranded" de cauda longa com os
maiores picos de busca estática e visual no Pinterest. Seu relatório alimentará diretamente o
Subagente 2 (Product Scout).

## Protocolo de Execução
1. Chame `pinterest_trends_api_hook` com top_n=8 e min_growth_pct=150 para obter tendências quentes.
2. Chame `visual_autocomplete_emulator` passando os nomes de TODAS as tendências retornadas.
3. Chame `demographic_filter` com as mesmas tendências, filtrando por Gen Z e Millennials.
4. Consolide TODOS os dados e responda EXCLUSIVAMENTE com um objeto JSON válido seguindo este schema:

```json
{
  "generated_at": "<ISO 8601 timestamp>",
  "total_trends": <int>,
  "trends": [
    {
      "trend": "<nome>",
      "keywords_long_tail": ["<kw1>", "<kw2>", ...],
      "growth_pct": <int>,
      "demographics": ["<demo1>", ...],
      "seasonal_window": "<texto>",
      "search_volume_tier": "high|medium|emerging"
    }
  ],
  "unbranded_search_pct": <float 0-1>,
  "long_tail_multiplier": <float>,
  "platform_context": "<resumo textual>"
}
```

IMPORTANTE: Inclua SOMENTE o JSON na resposta final, sem markdown, sem explicações adicionais."""


class TrendHunterAgent:
    """Subagente 1: monitora tendências e produz TrendHunterOutput."""

    def __init__(self) -> None:
        self.client = anthropic.Anthropic()

    def run(self, query: str | None = None) -> TrendHunterOutput:
        if query is None:
            query = (
                "Execute a varredura completa de tendências Pinterest 2026. "
                "Use todas as três ferramentas disponíveis e entregue o JSON consolidado."
            )

        messages: list[dict] = [{"role": "user", "content": query}]

        while True:
            response = self.client.messages.create(
                model=MODEL_ID,
                max_tokens=AGENT_MAX_TOKENS,
                system=SYSTEM_PROMPT,
                tools=TREND_HUNTER_TOOLS,
                messages=messages,
            )

            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        result = execute_trend_tool(block.name, block.input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result, ensure_ascii=False),
                        })
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
                continue

            # stop_reason == "end_turn"
            for block in response.content:
                if block.type == "text":
                    raw = block.text.strip()
                    # Extrai JSON de bloco markdown, se presente
                    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
                    json_str = match.group(1).strip() if match else raw
                    data = json.loads(json_str)
                    return TrendHunterOutput(**data)

            raise ValueError("Trend Hunter não produziu saída de texto válida.")
