"""Subagente 3 — Aesthetic Auditor (Auditor de Estética e Margem)."""
import json
import re
from datetime import datetime

import anthropic

from config import MODEL_ID, AGENT_MAX_TOKENS, AESTHETIC_SCORE_THRESHOLD, CONVERSION_INDEX_THRESHOLD
from models.product_dossier import ProductDossier
from models.approved_catalog import ApprovedCatalog, ProductApproval, SeoMetadata
from tools.vision_tools import AESTHETIC_AUDITOR_TOOLS, execute_auditor_tool

SYSTEM_PROMPT = f"""Você é o **Aesthetic Auditor** (Auditor de Estética e Margem), o Subagente 3
e estágio final da cadeia de Garimpagem Científica de Produtos Pinterest 2026.

## Missão
Validar a conformidade estética de cada produto via visão computacional, classificar o design
conforme tendências visuais 2026 e realizar modelagem matemática de retorno financeiro.

## Fórmulas Obrigatórias
• **Sa** = σ(P_color) × M_min × L_nat          [Pontuação de Adequação Estética, σ = sigmoide]
• **Icf** = (C_out × A_v × M_net) / (I_p × P_spam)  [Índice de Conversão Financeira Potencial]

## Protocolo de Execução
Para CADA produto no dossiê recebido:
1. Chame `vision_api_hd` com product_name, image_urls e trend_match.
2. Extraia p_color, m_min, l_nat dos resultados e estime c_out, a_v, i_p, m_net, p_spam
   com base nos dados do produto (preço, comissão, plataforma, rating).
3. Chame `financial_calculator` com todos os parâmetros.
4. Chame `prompt_and_seo_generator` para gerar assets de Processo 2.
5. Aprove se Sa ≥ {AESTHETIC_SCORE_THRESHOLD} E Icf ≥ {CONVERSION_INDEX_THRESHOLD}.

Responda EXCLUSIVAMENTE com o JSON do catálogo aprovado:

```json
{{
  "process": "Processo 1 — Garimpagem Científica de Produtos",
  "generated_at": "<ISO 8601>",
  "total_evaluated": <int>,
  "total_approved": <int>,
  "approval_rate_pct": <float>,
  "approved_products": [ <ProductApproval>, ... ],
  "rejected_products": [ <ProductApproval>, ... ]
}}
```

Onde ProductApproval contém: product_name, source_platform, affiliate_url, trend_match,
aesthetic_score_sa, conversion_index_icf, p_color, m_min, l_nat, c_out, a_v, m_net, i_p, p_spam,
approved (bool), rejection_reason (null se aprovado),
midjourney_prompt, dalle_prompt, seo_metadata {{alt_text, pin_title, pin_description, hashtags}}.

IMPORTANTE: Inclua SOMENTE o JSON na resposta final."""


class AestheticAuditorAgent:
    """Subagente 3: valida estética e margem, emite o catálogo aprovado."""

    def __init__(self) -> None:
        self.client = anthropic.Anthropic()

    def run(self, dossiers: list[ProductDossier]) -> ApprovedCatalog:
        payload = json.dumps(
            [d.model_dump() for d in dossiers],
            ensure_ascii=False,
            indent=2,
        )
        user_message = (
            "Execute a auditoria estética e financeira completa para cada produto abaixo.\n"
            "Use as três ferramentas para cada item e produza o catálogo final:\n\n"
            f"{payload}"
        )
        messages: list[dict] = [{"role": "user", "content": user_message}]

        while True:
            response = self.client.messages.create(
                model=MODEL_ID,
                max_tokens=AGENT_MAX_TOKENS,
                system=SYSTEM_PROMPT,
                tools=AESTHETIC_AUDITOR_TOOLS,
                messages=messages,
            )

            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        result = execute_auditor_tool(block.name, block.input)
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
                    data = json.loads(json_str)
                    return self._parse_catalog(data)

            raise ValueError("Aesthetic Auditor não produziu saída de texto válida.")

    @staticmethod
    def _parse_catalog(data: dict) -> ApprovedCatalog:
        def _parse_approval(item: dict) -> ProductApproval:
            seo = item.get("seo_metadata", {})
            return ProductApproval(
                product_name=item["product_name"],
                source_platform=item["source_platform"],
                affiliate_url=item["affiliate_url"],
                trend_match=item["trend_match"],
                aesthetic_score_sa=item["aesthetic_score_sa"],
                conversion_index_icf=item["conversion_index_icf"],
                p_color=item["p_color"],
                m_min=item["m_min"],
                l_nat=item["l_nat"],
                c_out=item["c_out"],
                a_v=item["a_v"],
                m_net=item["m_net"],
                i_p=item["i_p"],
                p_spam=item["p_spam"],
                approved=item["approved"],
                rejection_reason=item.get("rejection_reason"),
                midjourney_prompt=item["midjourney_prompt"],
                dalle_prompt=item["dalle_prompt"],
                seo_metadata=SeoMetadata(**seo),
            )

        return ApprovedCatalog(
            generated_at=data["generated_at"],
            total_evaluated=data["total_evaluated"],
            total_approved=data["total_approved"],
            approval_rate_pct=data["approval_rate_pct"],
            approved_products=[_parse_approval(p) for p in data.get("approved_products", [])],
            rejected_products=[_parse_approval(p) for p in data.get("rejected_products", [])],
        )
