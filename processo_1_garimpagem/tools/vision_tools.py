"""Ferramentas do Subagente 3 — Aesthetic Auditor."""
import math
import random

AESTHETIC_AUDITOR_TOOLS = [
    {
        "name": "vision_api_hd",
        "description": (
            "Analisa imagens de produtos com visão computacional de alta definição: "
            "detecta aderência à paleta de cores 2026, mede índice de minimalismo visual "
            "(ausência de watermarks e logos invasivos), avalia qualidade de iluminação natural "
            "e executa OCR para detectar poluição textual."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {"type": "string"},
                "image_urls": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "URLs das imagens do produto",
                },
                "trend_match": {
                    "type": "string",
                    "description": "Tendência estética de referência para comparação",
                },
            },
            "required": ["product_name", "image_urls", "trend_match"],
        },
    },
    {
        "name": "financial_calculator",
        "description": (
            "Aplica as fórmulas matemáticas do Aesthetic Auditor:\n"
            "• Sa = σ(P_color) × M_min × L_nat  [Pontuação de Adequação Estética]\n"
            "• Icf = (C_out × A_v × M_net) / (I_p × P_spam)  [Índice de Conversão Financeira]\n"
            "onde σ(x) = 1/(1 + e^(-x)) é a função sigmoide."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {"type": "string"},
                "p_color": {"type": "number", "description": "Aderência paleta cores 2026 [0–10]"},
                "m_min": {"type": "number", "description": "Índice de minimalismo [0–1]"},
                "l_nat": {"type": "number", "description": "Taxa luminosidade natural [0–1]"},
                "c_out": {"type": "integer", "description": "Volume estimado de cliques de saída"},
                "a_v": {"type": "number", "description": "Fator de apelo visual [0–1]"},
                "i_p": {"type": "integer", "description": "Impressões orgânicas esperadas"},
                "m_net": {"type": "number", "description": "Retorno líquido de comissão (USD)"},
                "p_spam": {"type": "number", "description": "Penalidade de spam [1.0 = limpo]"},
            },
            "required": ["product_name", "p_color", "m_min", "l_nat",
                         "c_out", "a_v", "i_p", "m_net", "p_spam"],
        },
    },
    {
        "name": "prompt_and_seo_generator",
        "description": (
            "Gera prompts otimizados para Midjourney e DALL-E para variações visuais do produto, "
            "e produz metadados de SEO (Alt Text, título e descrição de Pin) prontos para publicação. "
            "Alt Text descritivo gera +25% de impressões e +123% de cliques de saída."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {"type": "string"},
                "trend_match": {"type": "string"},
                "aesthetic_score_sa": {"type": "number"},
                "platform": {"type": "string"},
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Palavras-chave de cauda longa associadas ao produto",
                },
            },
            "required": ["product_name", "trend_match", "aesthetic_score_sa", "platform", "keywords"],
        },
    },
]

# Paletas de cores canonicamente alinhadas por tendência em 2026
_TREND_PALETTES: dict[str, dict] = {
    "Scent Stacking":   {"palette": "warm amber, vanilla cream, smoky mauve",  "base_p_color": 7.2},
    "Glitchy Glam":     {"palette": "holographic silver, electric purple, neon",  "base_p_color": 8.5},
    "Throwback Kid":    {"palette": "primary red, sky blue, sunshine yellow",  "base_p_color": 7.8},
    "Glamoratti":       {"palette": "champagne, ivory, taupe, soft camel",     "base_p_color": 8.8},
    "Afrohemian Decor": {"palette": "terracotta, ochre, deep forest green",    "base_p_color": 8.1},
    "Vamp Romantic":    {"palette": "deep burgundy, black, dusty rose, gold",  "base_p_color": 7.9},
    "Poetcore":         {"palette": "parchment, sepia, forest green, rust",    "base_p_color": 8.3},
    "Cool Blue":        {"palette": "cobalt, cerulean, slate, matte white",    "base_p_color": 8.6},
}


def _sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def execute_auditor_tool(name: str, inputs: dict) -> dict:
    if name == "vision_api_hd":
        trend = inputs.get("trend_match", "")
        palette_data = _TREND_PALETTES.get(trend, {"palette": "neutral", "base_p_color": 6.0})
        # Simula análise de visão computacional com variação realista
        seed = hash(inputs.get("product_name", "")) % 100
        p_color = round(palette_data["base_p_color"] + (seed % 20 - 10) * 0.05, 2)
        m_min = round(0.70 + (seed % 30) * 0.01, 2)
        l_nat = round(0.65 + (seed % 35) * 0.01, 2)
        has_watermark = seed > 90
        ocr_noise = seed > 85
        return {
            "source": "Vision API HD",
            "product": inputs["product_name"],
            "trend_palette": palette_data["palette"],
            "vision_scores": {
                "p_color": p_color,
                "m_min": m_min if not has_watermark else round(m_min * 0.6, 2),
                "l_nat": l_nat,
                "watermark_detected": has_watermark,
                "ocr_noise_detected": ocr_noise,
                "images_analyzed": len(inputs.get("image_urls", [])),
            },
        }

    if name == "financial_calculator":
        p_color = inputs["p_color"]
        m_min = inputs["m_min"]
        l_nat = inputs["l_nat"]
        c_out = inputs["c_out"]
        a_v = inputs["a_v"]
        i_p = inputs["i_p"]
        m_net = inputs["m_net"]
        p_spam = inputs["p_spam"]

        sa = round(_sigmoid(p_color) * m_min * l_nat, 4)
        icf = round((c_out * a_v * m_net) / (i_p * p_spam), 6) if (i_p * p_spam) != 0 else 0.0

        return {
            "source": "Módulo de Cálculo Financeiro",
            "product": inputs["product_name"],
            "formula_sa": f"σ({p_color}) × {m_min} × {l_nat} = {_sigmoid(p_color):.4f} × {m_min} × {l_nat}",
            "formula_icf": f"({c_out} × {a_v} × {m_net}) / ({i_p} × {p_spam})",
            "aesthetic_score_sa": sa,
            "conversion_index_icf": icf,
            "sigmoid_p_color": round(_sigmoid(p_color), 4),
        }

    if name == "prompt_and_seo_generator":
        product = inputs["product_name"]
        trend = inputs["trend_match"]
        sa = inputs["aesthetic_score_sa"]
        platform = inputs["platform"]
        keywords = inputs.get("keywords", [])
        kw_str = ", ".join(keywords[:3]) if keywords else trend.lower()

        quality_tag = "cinematic, 8K, studio lighting, minimalist background" if sa >= 0.70 \
            else "lifestyle photography, natural light, editorial style"

        return {
            "source": "Prompt & SEO Generator",
            "midjourney_prompt": (
                f"/imagine {product}, {trend} aesthetic 2026, "
                f"{quality_tag}, Pinterest viral composition, "
                f"unbranded flat lay, soft bokeh --ar 2:3 --v 6.1 --style raw"
            ),
            "dalle_prompt": (
                f"A professional Pinterest-style product photograph of {product}. "
                f"Aesthetic: {trend} 2026. Style: {quality_tag}. "
                f"Vertical format 2:3, no text, no watermarks, no brand logos."
            ),
            "seo_metadata": {
                "alt_text": (
                    f"A beautifully styled {product} in {trend} aesthetic — "
                    f"perfect for {kw_str}. Discover on Pinterest 2026."
                ),
                "pin_title": f"{product} | {trend} 2026",
                "pin_description": (
                    f"Obsessed with this {trend} find! {product} is the perfect piece "
                    f"for your {kw_str} collection. Shop via affiliate link in bio. "
                    f"Save for later and share with your {', '.join(keywords[-2:]) if len(keywords)>=2 else trend} community! "
                    f"#PinterestFinds #{trend.replace(' ', '')} #AffiliateLink"
                ),
                "hashtags": [
                    f"#{trend.replace(' ', '')}",
                    f"#Pinterest2026",
                    "#AestheticFinds",
                    "#ShopTheLook",
                    "#AffiliateLink",
                ],
            },
        }

    return {"error": f"Ferramenta desconhecida: {name}"}
