MODEL_ID = "claude-sonnet-4-6"
AGENT_MAX_TOKENS = 4096

# Limiares de aprovação do Aesthetic Auditor
AESTHETIC_SCORE_THRESHOLD = 0.60   # Sa mínimo para aprovação
CONVERSION_INDEX_THRESHOLD = 0.50  # Icf mínimo para aprovação
STORE_RATING_MIN = 4.2             # Avaliação mínima aceita pelo Product Scout

# Dados de tendências 2026 embutidos (fonte: pesquisa de ecossistema Pinterest 2026)
PINTEREST_TRENDS_2026 = [
    {"trend": "Scent Stacking",    "growth_pct": 500, "demographics": ["Gen Z", "Millennials"]},
    {"trend": "Glitchy Glam",      "growth_pct": 270, "demographics": ["Gen Z", "Millennials"]},
    {"trend": "Throwback Kid",     "growth_pct": 225, "demographics": ["Boomers", "Gen X"]},
    {"trend": "Glamoratti",        "growth_pct": 225, "demographics": ["Gen Z", "Millennials"]},
    {"trend": "Afrohemian Decor",  "growth_pct": 220, "demographics": ["Boomers", "Gen X"]},
    {"trend": "Vamp Romantic",     "growth_pct": 180, "demographics": ["Millennials", "Gen Z"]},
    {"trend": "Poetcore",          "growth_pct": 175, "demographics": ["Gen Z", "Millennials"]},
    {"trend": "Cool Blue",         "growth_pct": 150, "demographics": ["Gen Z", "Millennials"]},
]

# Estatísticas globais da plataforma (2026)
PLATFORM_STATS = {
    "unbranded_search_pct": 0.88,       # 80–96% buscas sem marca (mediana 88%)
    "long_tail_multiplier": 2.4,        # crescimento de buscas de cauda longa
    "visual_search_monthly_bn": 1.5,    # bilhões de pesquisas visuais/mês (Pinterest Lens)
    "purchase_conversion_pct": 0.85,    # 85% usuários semanais realizaram compra via Pin
    "cart_size_uplift": 0.40,           # carrinhos 40% maiores vs redes de rolagem passiva
    "seasonal_lead_days": 75,           # 60–90 dias de antecedência vs Google (mediana 75)
    "visual_conversion_uplift": 0.62,   # 62% maior conversão via busca visual vs texto
    "alt_text_impression_uplift": 0.25, # +25% impressões com Alt Text descritivo
    "alt_text_click_uplift": 1.23,      # +123% cliques de saída com Alt Text descritivo
    "pin_traction_months": 3.76,        # meses médios de tração por postagem (TransActV2)
}

# Catálogo de cauda longa por tendência
LONG_TAIL_KEYWORDS: dict[str, list[str]] = {
    "Scent Stacking":   ["how to layer perfumes for women", "unisex fragrance combinations 2026",
                         "layering body mist and eau de parfum", "indie perfume stack guide"],
    "Glitchy Glam":     ["glitchy glam makeup look tutorial", "digital distortion aesthetic outfit",
                         "Y2K glitch fashion accessories", "cyber glam eyeshadow palette"],
    "Throwback Kid":    ["90s nostalgia kids room decor", "retro childhood aesthetic gifts",
                         "vintage toy collection display ideas", "gen x nostalgia home decor"],
    "Glamoratti":       ["old money aesthetic wardrobe essentials", "quiet luxury outfits women",
                         "glamoratti fashion capsule wardrobe", "elevated everyday style pieces"],
    "Afrohemian Decor": ["afrocentric boho living room ideas", "african inspired wall art prints",
                         "natural fiber woven baskets decor", "earthy tone african textile cushions"],
    "Vamp Romantic":    ["dark romantic bedroom aesthetic", "moody floral arrangements gothic",
                         "vamp romantic candle holders", "dark academia fashion women"],
    "Poetcore":         ["poetcore aesthetic outfit ideas", "literary cottagecore stationery",
                         "vintage book aesthetic home office", "poetry inspired jewelry etsy"],
    "Cool Blue":        ["cool blue aesthetic room decor", "cerulean fashion accessories 2026",
                         "blue toned photography presets", "cobalt and slate color palette home"],
}
