#!/usr/bin/env python3
"""Score A-share short-term money-making effect from component points.

Input JSON example:
{
  "date": "2026-04-15",
  "components": [
    {"name": "涨停数量", "raw": "68", "points": 14, "max": 20},
    {"name": "炸板率", "raw": "估算偏高", "points": 8, "max": 20}
  ],
  "hard_veto": []
}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


DEFAULT_MAX = {
    "涨停数量": 20,
    "炸板率": 20,
    "跌停数量": 20,
    "连板高度/梯队": 15,
    "主线板块指数": 15,
    "成交额/量能": 10,
}


def band(total: float) -> tuple[str, str, str, str]:
    if total >= 75:
        return ("赚钱效应强", "进攻，做主线核心/龙头/中军", "60%-80%", "龙头15%-25%，后排≤10%")
    if total >= 60:
        return ("修复可做", "中小仓做核心分歧、弱转强", "40%-60%", "核心10%-20%，后排≤8%")
    if total >= 40:
        return ("混沌轮动", "小仓试错，首板/低吸核心为主", "15%-35%", "核心5%-10%，后排≤5%")
    return ("亏钱效应", "空仓或极轻仓，禁止高位接力", "0%-15%", "试错≤5%")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: score_quant.py input.json", file=sys.stderr)
        return 2

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    components = data.get("components", [])
    hard_veto = data.get("hard_veto", [])
    rows = []
    total = 0.0
    for item in components:
        name = item["name"]
        max_points = float(item.get("max", item.get("weight", DEFAULT_MAX.get(name, 0))))
        if "points" in item:
            points = float(item["points"])
        else:
            # Backward-compatible path: score is a 0-100 percentage of max_points.
            score = float(item["score"])
            points = score * max_points / 100.0
        points = max(0.0, min(points, max_points))
        total += points
        rows.append(
            {
                "name": name,
                "raw": item.get("raw", ""),
                "max": max_points,
                "points": round(points, 2),
                "judgment": item.get("judgment", ""),
            }
        )

    uncapped_total = total
    if hard_veto:
        total = min(total, 40.0)
    state, action, total_cap, single_cap = band(total)
    result = {
        "date": data.get("date"),
        "total_score": round(total, 2),
        "uncapped_total_score": round(uncapped_total, 2),
        "hard_veto": hard_veto,
        "state": state,
        "action": action,
        "total_position_cap": total_cap,
        "single_stock_cap": single_cap,
        "rows": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
