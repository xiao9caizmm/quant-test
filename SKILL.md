---
name: quant-test
description: Quantitative Chinese A-share review and stock-selection workflow for "量化测试skill". Use when asked for 量化测试skill, 复盘选股, 量化评分, 情绪评分, 主线板块打分, 仓位上限, or date-specific A股复盘+选股.
---

# 量化测试skill

Use this skill to turn an A-share daily review into a rule-based short-term stock-selection plan. It combines the user's `agent策略.docx` quantitative tables with the existing `a-share-short-review` data/style workflow.

## Workflow

1. Confirm the target trading day and previous trading day. If the target is a weekend or exchange holiday, write a non-trading-day strategy note instead of inventing data.
2. Use `a-share-short-review` if available for market data and prose style. Follow its data priority: MXSKILLS first, Eastmoney public APIs second, reputable public review sources third. Always label fallback data.
3. For every trading-day review, search 财联社 with the exact date plus `焦点复盘`. Prefer the original `cls.cn` article; if blocked, use reputable mirrors that clearly转载财联社 such as 东方财富 or 新浪. Extract and source-tag: 涨停数、炸板数、封板率、连板晋级率、主线热点催化、人气股反馈、后市展望.
4. Collect these fields for the target day and prior day: 涨停数量, 炸板率 or failed-board quality, 跌停数量, 最高连板/连板梯队, 主线板块指数或核心股表现, 成交额/量能, 涨跌家数, 创历史新高数量, 资金流向, and leading-sector stock pools.
5. Apply hard veto rules before scoring: 跌停>60, 炸板率>45%, 高标断板后A杀扩散, or 主线板块指数跌破MA5/MA10并放量下跌 caps the money-making score at 40 and prohibits high-position relay.
6. Score the market money-making effect by direct component points, not by vague impression: 涨停数量20, 炸板率20, 跌停数量20, 连板高度/梯队15, 主线板块指数15, 成交额/量能10. Use 财联社焦点复盘封板率 to derive 炸板率 whenever available: `炸板率 = 1 - 封板率`; if both涨停分析 and焦点复盘 exist, prefer焦点复盘 for the written review and mention口径差异 if material. Use `scripts/score_quant.py` when component points are available as JSON; otherwise compute manually from `references/agent-strategy.md`.
7. Classify the emotional position as 冰点/修复/主升/高潮/退潮. Use the score as a base, then adjust by structure: index false strength, back-row climax, or divergence-day return can change the action even when the total score looks acceptable.
8. Score candidate main lines with the 100-point model: 板块指数趋势25, 板块成交额20, 板块宽度15, 核心结构15, 分歧后回流15, 叙事/催化强度10. Main-line judgment must compare with the previous trading day; one-day strength is only rebound unless divergence-day return and sector diffusion confirm it. Use 财联社焦点复盘主线热点 paragraphs as the first source for catalysts and sector narrative.
9. Determine main-line stage: 初期/分歧/高潮/退潮. The output must state the stage and use only the matching trading method.
10. Apply position rules after market and main-line scoring: base cap, recent trading result, consecutive losses, month-end/holiday timing, regulatory pressure, negative news, and profit retracement.
11. Build the selection pool only from the strongest one or two directions. Prefer 龙头/中军/趋势核心/创新高核心; avoid 后排杂毛 and climax extensions unless the output labels them as observation-only.
12. Write a Markdown file under the current workspace unless the user gives another folder. Suggested filename: `YYYYMMDD量化复盘选股.md`.

## Required Output

For a trading day, write these sections in order:

1. `◆ 一、量化核心结论`
2. `◆ 二、市场全景与前日对比`
3. `◆ 三、赚钱效应量化评分`
4. `◆ 四、主线板块量化排名`
5. `◆ 五、选股观察池`
6. `◆ 六、仓位与风控`
7. `◆ 七、次日验证点`

Required tables:

- Money-making score table columns: `指标`, `原始数据`, `得分上限`, `实际得分`, `判断`.
- Main-line ranking table columns: `排名`, `板块`, `指数趋势`, `成交额`, `宽度`, `核心结构`, `分歧回流`, `叙事催化`, `总分`, `定性`.
- Stock-selection table columns: `股票`, `方向`, `角色`, `入选逻辑`, `触发条件`, `失效条件`, `仓位上限`, `风险`.
- Include a concise `财联社焦点复盘口径` note when the article is available: 封板率/炸板数, 连板晋级率, main catalysts, and outlook risk.

## Selection Rules

- If total score is `75-100`, allow attack mode: select main-line 龙头/中军/趋势核心, but still require trigger and invalidation conditions.
- If total score is `60-75`, use repair mode: select only core divergence, weak-to-strong, or new-high core stocks; use mid/small position caps.
- If total score is `40-60`, list only observation candidates and trial conditions; avoid high-position relays.
- If total score is below `40`, do not output an active buy pool. Output defensive observation names only if needed.
- If hard veto is triggered, cap the score as instructed even if other metrics look good, reduce the position cap, and explicitly write the veto reason.
- Never select a stock only because it涨停. It must belong to a scored main line, have a clear role, and have a next-day trigger.
- Prefer names with at least one of: 创历史新高, high turnover core, sector middle-cap center, divergence-day return, or repeated capital return.
- Always include an invalidation condition such as 跌破分时均线, 跌破开盘价, 跌破前高/5日线, 放量滞涨, or sector diffusion failure.
- Keep language as a review and selection plan, not an investment promise. End user-facing outputs with a risk disclaimer.

## Missing Data Rules

- If 炸板率 is unavailable, use failed-board quality from public review sources or describe it qualitatively; mark the score as `估算`.
- If 财联社焦点复盘 provides 封板率, do not estimate 炸板率. Convert it directly and label it `财联社焦点复盘口径`.
- If main-line board indices are unavailable, use core-stock performance plus sector breadth; mark it as `核心股口径`.
- If new-high data is unavailable, do not invent it. Use `公开源未稳定返回` and rely on limit-up/board/core-stock evidence.
- If sources disagree materially, use ranges such as `约`, explain the口径, and reduce confidence in the score.
- If no account trading history is provided, state that profit/loss dynamic adjustments are not applied; do not invent recent wins/losses.

## References

- Full strategy tables and default scoring rubrics: `references/agent-strategy.md`.
- Optional score calculator: `scripts/score_quant.py`.
