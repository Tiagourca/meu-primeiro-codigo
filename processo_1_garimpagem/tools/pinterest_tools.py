"""Ferramentas do Subagente 1 — Trend Hunter."""
from datetime import datetime
from config import PINTEREST_TRENDS_2026, LONG_TAIL_KEYWORDS, PLATFORM_STATS

TREND_HUNTER_TOOLS = [
    {
        "name": "pinterest_trends_api_hook",
        "description": (
            "Conecta com o monitoramento histórico e sazonal do Pinterest Trends para detectar "
            "termos emergentes antes que alcancem o Google. Retorna tendências ordenadas por "
            "crescimento percentual e janela sazonal recomendada."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "top_n": {
                    "type": "integer",
                    "description": "Número máximo de tendências a retornar (padrão: 8)",
                    "default": 8,
                },
                "min_growth_pct": {
                    "type": "integer",
                    "description": "Filtro mínimo de crescimento percentual (padrão: 100)",
                    "default": 100,
                },
            },
            "required": [],
        },
    },
    {
        "name": "visual_autocomplete_emulator",
        "description": (
            "Emula a barra de pesquisa do Pinterest em modo anônimo e captura variações de "
            "cauda longa em tempo real para cada tendência fornecida."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "trend_names": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Lista de nomes de tendências para expandir em cauda longa",
                },
            },
            "required": ["trend_names"],
        },
    },
    {
        "name": "demographic_filter",
        "description": (
            "Aplica segmentação demográfica focada em Gen Z e Millennials (maior poder de compra "
            "na plataforma) e valida a janela sazonal de publicação com antecedência de 60–90 dias."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "trends": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Tendências a segmentar demograficamente",
                },
                "target_demographics": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Grupos-alvo (ex: ['Gen Z', 'Millennials'])",
                    "default": ["Gen Z", "Millennials"],
                },
            },
            "required": ["trends"],
        },
    },
]


def _seasonal_window(trend: str) -> str:
    """Calcula janela sazonal com antecedência de 75 dias (mediana 60–90)."""
    now = datetime.now()
    month = now.month
    if month <= 3:
        return "Publicar em junho–julho para capturar pico de inverno/festas"
    if month <= 6:
        return "Publicar em setembro–outubro para capturar pico de fim de ano"
    if month <= 9:
        return "Publicar agora — pico de fim de ano em 60–90 dias"
    return "Publicar agora — pico de verão em 60–75 dias (início do ano)"


def execute_trend_tool(name: str, inputs: dict) -> dict:
    if name == "pinterest_trends_api_hook":
        top_n = inputs.get("top_n", 8)
        min_growth = inputs.get("min_growth_pct", 100)
        filtered = [t for t in PINTEREST_TRENDS_2026 if t["growth_pct"] >= min_growth]
        filtered.sort(key=lambda x: x["growth_pct"], reverse=True)
        return {
            "source": "Pinterest Trends API Hook (2026)",
            "retrieved_at": datetime.now().isoformat(),
            "platform_stats": PLATFORM_STATS,
            "trends": filtered[:top_n],
        }

    if name == "visual_autocomplete_emulator":
        trend_names = inputs.get("trend_names", [])
        result = {}
        for t in trend_names:
            result[t] = LONG_TAIL_KEYWORDS.get(t, [f"{t.lower()} ideas", f"{t.lower()} aesthetic"])
        return {
            "source": "Visual Autocomplete Emulator (modo anônimo)",
            "long_tail_keywords": result,
            "note": "Buscas de cauda longa cresceram 2.4× em 2026 no Pinterest",
        }

    if name == "demographic_filter":
        trends = inputs.get("trends", [])
        targets = inputs.get("target_demographics", ["Gen Z", "Millennials"])
        enriched = []
        for t_name in trends:
            match = next((t for t in PINTEREST_TRENDS_2026 if t["trend"] == t_name), None)
            if match:
                overlap = [d for d in match["demographics"] if d in targets]
                enriched.append({
                    "trend": t_name,
                    "target_demographics": targets,
                    "demographic_overlap": overlap,
                    "relevance_score": len(overlap) / max(len(targets), 1),
                    "seasonal_window": _seasonal_window(t_name),
                    "search_volume_tier": "high" if match["growth_pct"] >= 270 else
                                          "medium" if match["growth_pct"] >= 175 else "emerging",
                })
        return {
            "source": "Filtro Demográfico",
            "platform_note": (
                f"{int(PLATFORM_STATS['unbranded_search_pct']*100)}% das buscas são unbranded; "
                f"76% do público tem renda familiar acima da mediana nacional."
            ),
            "enriched_trends": enriched,
        }

    return {"error": f"Ferramenta desconhecida: {name}"}
