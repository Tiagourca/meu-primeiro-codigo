from pydantic import BaseModel, Field
from typing import List


class TrendEntry(BaseModel):
    trend: str
    keywords_long_tail: List[str] = Field(min_length=1)
    growth_pct: int = Field(gt=0)
    demographics: List[str] = Field(min_length=1)
    seasonal_window: str
    search_volume_tier: str = Field(description="high | medium | emerging")


class TrendHunterOutput(BaseModel):
    """Contrato de saída do Subagente 1 → entrada do Subagente 2."""
    generated_at: str
    total_trends: int
    trends: List[TrendEntry]
    unbranded_search_pct: float = Field(ge=0.0, le=1.0)
    long_tail_multiplier: float = Field(gt=0.0)
    platform_context: str
