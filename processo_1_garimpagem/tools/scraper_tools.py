"""Ferramentas do Subagente 2 — Product Scout."""
import random
from config import STORE_RATING_MIN

# Catálogo simulado de produtos por tendência e plataforma
_PRODUCT_CATALOG: dict[str, list[dict]] = {
    "Scent Stacking": [
        {
            "product_name": "Layering Perfume Discovery Set — Indie Niche Collection",
            "platform": "Etsy",
            "affiliate_url": "https://www.etsy.com/listing/scent-stacking-discovery-set",
            "price_min": 38.00, "price_max": 72.00,
            "commission_pct": 0.08, "rating": 4.8, "return_rate_pct": 0.02,
            "product_type": "physical",
            "images": [
                "https://i.etsystatic.com/scent-stack-01.jpg",
                "https://i.etsystatic.com/scent-stack-02.jpg",
            ],
        },
        {
            "product_name": "Digital Guide: The Art of Scent Layering for Gen Z",
            "platform": "Hotmart",
            "affiliate_url": "https://go.hotmart.com/scent-layering-guide",
            "price_min": 19.90, "price_max": 19.90,
            "commission_pct": 0.40, "rating": 4.6, "return_rate_pct": 0.05,
            "product_type": "digital",
            "images": ["https://hotmart.com/product/scent-guide-cover.jpg"],
        },
    ],
    "Glitchy Glam": [
        {
            "product_name": "Y2K Glitch Holographic Eyeshadow Palette — 18 Shades",
            "platform": "Amazon",
            "affiliate_url": "https://www.amazon.com/dp/B0GLITCH2026",
            "price_min": 24.99, "price_max": 34.99,
            "commission_pct": 0.06, "rating": 4.5, "return_rate_pct": 0.04,
            "product_type": "physical",
            "images": [
                "https://m.media-amazon.com/glitch-palette-01.jpg",
                "https://m.media-amazon.com/glitch-palette-02.jpg",
            ],
        },
    ],
    "Glamoratti": [
        {
            "product_name": "Quiet Luxury Capsule Wardrobe Starter Kit — Linen Blend",
            "platform": "Shopify",
            "affiliate_url": "https://glamoratti-brand.myshopify.com/products/capsule-kit",
            "price_min": 89.00, "price_max": 149.00,
            "commission_pct": 0.12, "rating": 4.7, "return_rate_pct": 0.03,
            "product_type": "physical",
            "images": [
                "https://cdn.shopify.com/glamoratti/capsule-01.jpg",
                "https://cdn.shopify.com/glamoratti/capsule-02.jpg",
            ],
        },
    ],
    "Poetcore": [
        {
            "product_name": "Poetcore Wax Seal Stationery Set — Vintage Parchment",
            "platform": "Etsy",
            "affiliate_url": "https://www.etsy.com/listing/poetcore-stationery-set",
            "price_min": 28.00, "price_max": 55.00,
            "commission_pct": 0.08, "rating": 4.9, "return_rate_pct": 0.01,
            "product_type": "physical",
            "images": [
                "https://i.etsystatic.com/poetcore-set-01.jpg",
                "https://i.etsystatic.com/poetcore-set-02.jpg",
            ],
        },
    ],
    "Vamp Romantic": [
        {
            "product_name": "Dark Romance Dried Florals Candle — Black Velvet & Oud",
            "platform": "Etsy",
            "affiliate_url": "https://www.etsy.com/listing/vamp-romantic-candle",
            "price_min": 32.00, "price_max": 48.00,
            "commission_pct": 0.08, "rating": 4.7, "return_rate_pct": 0.02,
            "product_type": "physical",
            "images": [
                "https://i.etsystatic.com/vamp-candle-01.jpg",
                "https://i.etsystatic.com/vamp-candle-02.jpg",
            ],
        },
    ],
    "Cool Blue": [
        {
            "product_name": "Cobalt Blue Aesthetic Desk Organizer Set — Matte Ceramic",
            "platform": "Amazon",
            "affiliate_url": "https://www.amazon.com/dp/B0COOLBLUE26",
            "price_min": 42.00, "price_max": 58.00,
            "commission_pct": 0.06, "rating": 4.4, "return_rate_pct": 0.06,
            "product_type": "physical",
            "images": [
                "https://m.media-amazon.com/cool-blue-desk-01.jpg",
                "https://m.media-amazon.com/cool-blue-desk-02.jpg",
            ],
        },
    ],
    "Throwback Kid": [
        {
            "product_name": "90s Nostalgia Collectible Mini Toy Capsule — Mystery Box",
            "platform": "Shopify",
            "affiliate_url": "https://throwback-store.myshopify.com/products/mini-toy-capsule",
            "price_min": 18.00, "price_max": 35.00,
            "commission_pct": 0.10, "rating": 4.3, "return_rate_pct": 0.07,
            "product_type": "physical",
            "images": ["https://cdn.shopify.com/throwback/toy-capsule-01.jpg"],
        },
    ],
    "Afrohemian Decor": [
        {
            "product_name": "Hand-Woven Seagrass Basket Set — African Textile Inspired",
            "platform": "Etsy",
            "affiliate_url": "https://www.etsy.com/listing/afrohemian-basket-set",
            "price_min": 65.00, "price_max": 95.00,
            "commission_pct": 0.08, "rating": 4.8, "return_rate_pct": 0.02,
            "product_type": "physical",
            "images": [
                "https://i.etsystatic.com/afrohemian-basket-01.jpg",
                "https://i.etsystatic.com/afrohemian-basket-02.jpg",
            ],
        },
    ],
}

PRODUCT_SCOUT_TOOLS = [
    {
        "name": "multicanal_scraper",
        "description": (
            "Varredura integrada em Amazon, Etsy, Hotmart e Shopify para rastrear mercadorias "
            "em conformidade com palavras-chave de cauda longa. Retorna dossiês técnicos brutos "
            "de cada produto encontrado."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "trend_name": {"type": "string", "description": "Nome da tendência a pesquisar"},
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Palavras-chave de cauda longa para refinar a busca",
                },
                "platforms": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Plataformas a varrer (padrão: todas)",
                    "default": ["Amazon", "Etsy", "Hotmart", "Shopify"],
                },
            },
            "required": ["trend_name", "keywords"],
        },
    },
    {
        "name": "store_quality_filter",
        "description": (
            "Aplica o algoritmo de descarte: remove produtos com avaliação < 4.2 estrelas "
            "ou índice de devolução elevado (> 15%). Retorna apenas produtos aprovados."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "Lista de produtos brutos do multicanal_scraper",
                },
                "min_rating": {
                    "type": "number",
                    "description": "Avaliação mínima aceita",
                    "default": 4.2,
                },
                "max_return_rate": {
                    "type": "number",
                    "description": "Taxa máxima de devolução aceita (0–1)",
                    "default": 0.15,
                },
            },
            "required": ["products"],
        },
    },
    {
        "name": "affiliate_viability_analysis",
        "description": (
            "Valida os links de afiliado: confirma ausência de redirecionadores mascarados, "
            "verifica comissões limpas e projeta retorno estimado por 1000 cliques."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "products": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "Produtos filtrados para validação de afiliação",
                },
            },
            "required": ["products"],
        },
    },
]


def execute_scout_tool(name: str, inputs: dict) -> dict:
    if name == "multicanal_scraper":
        trend = inputs.get("trend_name", "")
        platforms = inputs.get("platforms", ["Amazon", "Etsy", "Hotmart", "Shopify"])
        raw_products = _PRODUCT_CATALOG.get(trend, [])
        filtered = [p for p in raw_products if p["platform"] in platforms]
        return {
            "source": "Multicanal Scraper (Amazon/Etsy/Hotmart/Shopify)",
            "trend_searched": trend,
            "total_found": len(filtered),
            "products": filtered,
        }

    if name == "store_quality_filter":
        products = inputs.get("products", [])
        min_rating = inputs.get("min_rating", STORE_RATING_MIN)
        max_return = inputs.get("max_return_rate", 0.15)
        approved, rejected = [], []
        for p in products:
            rating_ok = p.get("rating", 0) >= min_rating
            return_ok = (p.get("return_rate_pct") or 0) <= max_return
            if rating_ok and return_ok:
                approved.append(p)
            else:
                rejected.append({
                    "product_name": p.get("product_name"),
                    "reason": (
                        f"Rating {p.get('rating')} < {min_rating}" if not rating_ok
                        else f"Taxa devolução {p.get('return_rate_pct')*100:.0f}% > {max_return*100:.0f}%"
                    ),
                })
        return {
            "source": "Filtro de Qualidade de Loja",
            "approved": approved,
            "rejected_count": len(rejected),
            "rejected": rejected,
        }

    if name == "affiliate_viability_analysis":
        products = inputs.get("products", [])
        validated = []
        for p in products:
            url = p.get("affiliate_url", "")
            has_redirect = any(tok in url for tok in ["redirect", "r=", "go.php", "track.php"])
            commission = p.get("commission_pct", 0)
            price_mid = (p.get("price_min", 0) + p.get("price_max", 0)) / 2
            rev_per_1k = round(1000 * commission * price_mid, 2)
            validated.append({
                **p,
                "url_clean": not has_redirect,
                "p_spam": 1.0 if not has_redirect else 1.8,
                "estimated_revenue_per_1k_clicks_usd": rev_per_1k,
            })
        return {
            "source": "Análise de Viabilidade de Afiliação",
            "validated_products": validated,
        }

    return {"error": f"Ferramenta desconhecida: {name}"}
