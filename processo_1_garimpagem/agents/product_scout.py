"""Subagente 2 — Product Scout (Garimpeiro de Produtos)."""
import json
import re

import anthropic

from config import MODEL_ID, AGENT_MAX_TOKENS
from models.trend_output import TrendHunterOutput
from models.product_dossier import ProductDossier, PriceRange
from tools.scraper_tools import PRODUCT_SCOUT_TOOLS, execute_scout_tool

SYSTEM_PROMPT = """Você é o **Product Scout** (Garimpeiro de Produtos), o Subagente 2 de uma cadeia
determinística de Garimpagem Científica de Produtos para o ecossistema Pinterest 2026.

## Missão
Traduzir conceitos estéticos e palavras-chave do Trend Hunter em produtos comerciais reais
(físicos, digitais ou por encomenda) com viabilidade logística e alta adequação à jornada
de consumo do Pinterest.

## Protocolo de Execução
Para CADA tendência fornecida no JSON de entrada:
1. Chame `multicanal_scraper` passando o nome da tendência e suas keywords_long_tail.
2. Passe os produtos brutos para `store_quality_filter` (rating mínimo 4.2, devolução máx 15%).
3. Passe os produtos aprovados para `affiliate_viability_analysis`.

Após processar TODAS as tendências, responda EXCLUSIVAMENTE com um array JSON de dossiês:

```json
[
  {
    "product_name": "<nome exato>",
    "source_platform": "Amazon|Etsy|Hotmart|Shopify",
    "affiliate_url": "<URL limpa sem redirecionadores>",
    "price_range": {"min_usd": <float>, "max_usd": <float>},
    "avg_commission_pct": <float 0-1>,
    "store_rating": <float>,
    "return_rate_pct": <float|null>,
    "trend_match": "<nome da tendência>",
    "keywords_matched": ["<kw1>", ...],
    "image_urls": ["<url1>", ...],
    "product_type": "physical|digital|custom_order"
  }
]
```

IMPORTANTE: Inclua SOMENTE o JSON array na resposta final."""


class ProductScoutAgent:
    """Subagente 2: garimpa produtos e produz lista de ProductDossier."""

    def __init__(self) -> None:
        self.client = anthropic.Anthropic()

    def run(self, trend_output: TrendHunterOutput) -> list[ProductDossier]:
        payload = trend_output.model_dump_json(indent=2)
        user_message = (
            f"Execute a garimpagem de produtos para as seguintes tendências e keywords:\n\n"
            f"{payload}\n\n"
            "Use as três ferramentas para cada tendência e entregue o JSON array consolidado."
        )
        messages: list[dict] = [{"role": "user", "content": user_message}]

        while True:
            response = self.client.messages.create(
                model=MODEL_ID,
                max_tokens=AGENT_MAX_TOKENS,
                system=SYSTEM_PROMPT,
                tools=PRODUCT_SCOUT_TOOLS,
                messages=messages,
            )

            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        result = execute_scout_tool(block.name, block.input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(result, ensure_ascii=False),
                        })
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
                continue

            for block in response.content:
                if block.type == "text":
                    raw = block.text.strip()
                    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
                    json_str = match.group(1).strip() if match else raw
                    items = json.loads(json_str)
                    return [
                        ProductDossier(
                            **{**item, "price_range": PriceRange(**item["price_range"])}
                        )
                        for item in items
                    ]

            raise ValueError("Product Scout não produziu saída de texto válida.")
