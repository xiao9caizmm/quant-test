# Agent Strategy Reference

This reference was extracted and condensed from `agent策略.docx`. Preserve the original meaning: this is not a fixed formula from the source author, but an executable Agent translation of the review method.

Core sentence: 赚钱效应 = 进攻强度 - 亏钱反馈 + 主线持续性 + 接力安全性 + 量能燃料.

## Scoring Order

Always score in this order:

1. Apply hard veto rules.
2. Score the six money-making effect components to a direct 100-point total.
3. Classify the emotional position.
4. Score candidate main lines with the 100-point main-line model.
5. Choose stage-matched trading style.
6. Apply position and risk-control adjustments.

## Hard Veto Rules

Before normal scoring, cap the market score when any hard risk appears:

- If 跌停数量 > 60, cap total money-making score at 40.
- If 炸板率 > 45%, cap total money-making score at 40.
- If high-board stocks break and A-sha declines spread, cap total money-making score at 40.
- If the main-line sector index breaks MA5/MA10 with volume, cap total money-making score at 40.
- Under any hard veto, prohibit high-position relay even if the limit-up count looks good.
- If 跌停数量 > 100, classify as strong retreat; if >300, classify as extreme ice point and allow only tiny trial positions.

Reason: many limit-ups under these conditions can be high-low switching, dealer names, arbitrage, or defensive local themes; short-term relay safety is low.

## Money-Making Effect Weights

Use direct component points. The six component maxima add to 100.

| 指标 | 满分 | 判断作用 |
| --- | ---: | --- |
| 涨停数量 | 20 | 判断市场进攻意愿 |
| 炸板率 | 20 | 判断封板质量和接力安全性 |
| 跌停数量 | 20 | 判断亏钱效应和流动性风险 |
| 连板高度/梯队 | 15 | 判断情绪空间和投机天花板 |
| 主线板块指数 | 15 | 判断是否有持续赚钱方向 |
| 成交额/量能 | 10 | 判断市场是否有燃料 |

Total score formula: `total = sum(component_points)`, after hard-veto caps.

## Component Scoring

### 涨停数量, 20 points

Limit-up count measures attack willingness, but not main-line quality by itself.

| 涨停数量 | 得分 |
| --- | --- |
| 0-20 | 0-5 |
| 20-40 | 5-10 |
| 40-70 | 10-15 |
| 70-100 | 15-18 |
| >100 | 18-20 |

If >100 limit-ups are mostly back-row small caps with no capacity core, subtract 2-5 points.

### 炸板率, 20 points

Failed-board rate measures board quality and relay safety.

| 炸板率 | 得分 |
| --- | --- |
| <15% | 18-20 |
| 15%-25% | 15-18 |
| 25%-35% | 10-15 |
| 35%-45% | 5-10 |
| >45% | 0-5; high risk, prohibit high-position relay |

### 跌停数量, 20 points

Limit-down count is the hard indicator of loss-making effect.

| 跌停数量 | 得分 |
| --- | --- |
| 0-5 | 18-20 |
| 5-15 | 15-18 |
| 15-30 | 10-15 |
| 30-60 | 5-10 |
| >60 | 0-5 |

### 连板高度/梯队, 15 points

Height measures speculation space; the ladder measures sustainability.

| 最高连板 | 得分 |
| --- | --- |
| 2板 | 0-3 |
| 3板 | 3-6 |
| 4板 | 6-9 |
| 5-6板 | 9-12 |
| ≥7板 | 12-15, but trigger climax-risk warning |

If there is only an isolated high board with no 3-board/2-board ladder, subtract 3-5 points. If leader, center, and supplement structure is complete, add 2-3 points within the 15-point cap.

### 主线板块指数, 15 points

Main line means sustained money-making effect, not the hottest board of one day.

| 主线状态 | 得分 |
| --- | --- |
| 无主线、涨停散乱 | 0-5 |
| 有热点但只强1天 | 5-8 |
| 板块连续2天强于指数 | 8-12 |
| 板块指数放量上行，龙头/中军/补涨完整 | 12-15 |

If indices rise but sentiment is poor or only weights support the index, main-line score cannot exceed 5.

### 成交额/量能, 10 points

Volume is fuel, necessary but not sufficient.

| 成交额相对20日均额 | 得分 |
| --- | --- |
| 高于20%以上 | 9-10 |
| 高于0%-20% | 7-9 |
| 低于0%-10% | 5-7 |
| 低于10%-20% | 2-5 |
| 低于20%以上 | 0-2 |

Add within band for volume-up rises. Deduct for shrinking rebounds. Volume-down declines trigger risk warning.

## Total Score Mapping

| 总分 | 状态 | 操作 |
| --- | --- | --- |
| 75-100 | 赚钱效应强 | 进攻，做主线核心/龙头/中军 |
| 60-75 | 修复可做 | 中小仓做核心分歧、弱转强 |
| 40-60 | 混沌轮动 | 小仓试错，首板/低吸核心为主 |
| 0-40 | 亏钱效应 | 空仓或极轻仓，禁止高位接力 |

## Emotion Position

- 冰点: 涨停少、跌停多、炸板高、连板低、成交缩。Observe or use tiny trial positions.
- 修复: 跌停减少、炸板下降、涨停回升、最高板拓展。Trade core divergence only.
- 主升: 涨停多、炸板低、跌停少、主线连续、成交放大。Attack core names.
- 高潮: 百股涨停、利好刷屏、后排批量涨停、连板高度很高。Hold core, sell back row, prepare for next-day divergence.
- 退潮: 高标A杀、炸板率高、跌停扩散、主线跌破短均线。Reduce or stay out.

Key rules:

- If 涨停 > 70, 炸板率 < 25%, 跌停 < 15, and a clear main line exists:赚钱效应强, attack core names.
- If 涨停 40-70, 炸板率 declines, 跌停 decreases, and chain height expands:情绪修复, trade core divergence.
- If indices rise but跌停多/炸板高/无主线: classify as index false strength, not strong money-making effect.
- If 百股涨停 and back-row climax appears: classify as climax and guard against next-day divergence.

## Main-Line 100-Point Model

Main line is not the hottest sector of the day. It is the line with sustained money-making effect.

| 维度 | 权重 | Scoring guidance |
| --- | ---: | --- |
| 板块指数趋势 | 25 | 3-day relative strength vs major index 8; standing above MA5/MA10 and MA5 rising 5; 5/10-day stage high 5; pullback not breaking MA5/MA10 4; rising RS 3 |
| 板块成交额 | 20 | 2-3 days above 20-day average 6; market share rising 5; up days with volume and pullback with shrinking volume 5; capacity core volume expands 4 |
| 板块宽度 | 15 | >70% sector names rising 4; >5% movers expanding 4; multiple 20/60-day or historical highs 4; recurring limit-ups 3 |
| 核心结构 | 15 | clear leader/core 4; capacity center 4; low-level supplements 3; 20cm/10cm/trend forms coexist 2; replacement core after divergence 2 |
| 分歧后回流 | 15 | return after spike-fade next day 5; core break without A-sha and new core appears 4; intraday selloff followed by late return 3; money returns from other diverging themes 3 |
| 叙事/催化强度 | 10 | policy/industry/earnings/price/overseas/order/tech catalyst 4; trackable catalyst 3; can expand branches 2; discussion heats but not overhyped 1 |

Main-line grade:

| 主线分 | 定性 | 操作 |
| --- | --- | --- |
| 80-100 | 唯一共识/最强共识 | Around core names; low吸核心、分歧回封、弱转强; do not chase back-row climax |
| 65-80 | 有效主线 | Participate with divergence confirmation; avoid blind position increase |
| 50-65 | 轮动热点 | First board, arbitrage, low-level supplement only; no heavy position |
| <50 | 穿插题材/杂音 | Usually first-day premium only; spike and leave |

Main-line hard denial:

- If the sector index has not made a stage high and is only up for one day, do not call it a main line.
- If volume has not expanded repeatedly and only a few small caps limit up, do not call it a main line.
- If core stocks have no next-day premium, do not call it a main line.
- If there is no return after divergence, do not call it a main line.
- If many limit-ups are back-row small caps with no capacity center, downgrade to emotional pulse.
- If the first day explodes and the second day opens broadly weak, classify as a passing theme.
- If multiple sectors rotate and no direction keeps making new highs, classify as no main line and reduce position.

## Main-Line Stage Selector

First judge stage, then choose trading style. Do not mix styles across stages.

| 主线阶段 | 核心特征 | 交易方式 | 仓位 |
| --- | --- | --- | --- |
| 初期 | 新题材、新催化、板块首次放量、核心率先涨停 | 抢先手 | 20%-40% |
| 分歧 | 主线确认后第一次/第二次回调，核心承接强 | 做弱转强/分歧低吸 | 30%-50% |
| 高潮 | 后排批量涨停、利好刷屏、加速一致 | 减仓/卖后排 | 降至20%-40% |
| 退潮 | 高标A杀、炸板率高、跌停扩散、主线破位 | 冰点小仓试错 | 0%-15% |

Stage execution:

- 初期: buy first confirmed core names: core first board, 1-to-2 core, capacity center breakout, strongest 20cm elasticity. Start 20%-30%, add only if next day has premium and sector diffuses. Do not chase back row.
- 分歧: only core weak-to-strong. Require at least 3 of 5 signals: better-than-expected auction, fast recovery above VWAP, sector index repairs, core repairs before back row, healthy volume. Use 30%-50%; fail means immediate risk cut.
- 高潮: do not open new back-row positions. Sell back row first, sell supplements on spike, reduce capacity center on volume-stalling, keep only core observation.
- 退潮: mostly stay out. After common ice point, use 5%-15% only on previous main-line survivor weak-to-strong or first core of new theme. Wrong means exit; never average down.

Required sentence in outputs: `当前处于主线初期/分歧/高潮/退潮，因此采用抢先手/弱转强/减仓/冰点试错策略。`

## Position Control

Base position by money-making effect:

| 赚钱效应评分 | 市场状态 | 短线总仓位上限 | 单票仓位上限 |
| --- | --- | --- | --- |
| 75-100 | 主升/强赚钱效应 | 60%-80% | 龙头15%-25%，后排≤10% |
| 60-75 | 修复/可做 | 40%-60% | 核心10%-20%，后排≤8% |
| 40-60 | 混沌轮动 | 15%-35% | 核心5%-10%，后排≤5% |
| 0-40 | 亏钱效应 | 0%-15% | 试错≤5% |

Dynamic profit/loss adjustment:

- If account gains ≥1R today and profit comes from main-line core, next-day short-term cap +10 percentage points.
- If account profits for 2 consecutive days and main-line score ≥65, move toward the high end of the base cap.
- If account profits for 3 consecutive days and no single loss exceeds 0.5R, leader single-stock cap can rise to 20%-25%.
- If account loses ≥1R today, next-day short-term cap -15 percentage points.
- If account loses for 2 consecutive days, total short-term position ≤20%.
- If account loses for 3 consecutive days, stop opening new positions for 1-2 days and only manage existing holdings.

Recent trade result rules:

| 最近交易结果 | Agent动作 |
| --- | --- |
| 最近3笔交易2赚1亏，合计盈利>1R | 允许标准仓 |
| 最近3笔交易3赚，合计盈利>2R | 允许加仓，但只加主线核心 |
| 最近3笔交易1赚2亏 | 仓位减半 |
| 最近3笔交易3亏 | 停止新开仓，至少休息1天 |
| 单日回撤>2R | 当日不再开新仓 |
| 单周回撤>5% | 下周前三天仓位上限≤20% |
| 从阶段高点回撤>8% | 停止短线，只做观察或小仓试错 |

Calendar rules:

- 每月1-10日: if money-making score ≥60, use normal base position.
- 每月11-20日: base position * 0.8.
- Last 5 trading days of month: base position * 0.5.
- Last 2 trading days of month: short-term total cap ≤30%; if score <60, cap ≤15%.
- If month-end coincides with shrinking volume, tight funding, or theme retreat, reduce to 0%-10%.
- Three trading days before long holidays: day -3 use 0.8x, day -2 use 0.6x, final day cap ≤30%.
- If long-holiday risk includes overseas macro, FOMC, CPI, geopolitics, earnings, or regulatory meetings, pre-holiday cap ≤20%.

Regulatory and negative-news rules:

- If regulation targets one stock, cut that stock at least by half.
- If regulation targets the whole theme, theme position ≤10%.
- If leader is suspended/key-monitored, downgrade all back-row names and prohibit relay.
- If regulatory pressure makes the sector index break MA5, clear short-term theme positions.
- For major single-stock negative news, reduce 50% at open; if it cannot recover VWAP before 10:00, keep reducing.
- For sector-level negative news, sector position ≤20%.
- For macro-level negative news, total short-term position ≤30%.
- If negative news day also has跌停>60 or炸板率>45%, total short-term position ≤10%.

Consecutive loss rules:

| 连续亏损状态 | 仓位处理 |
| --- | --- |
| 连续2笔亏损 | 新仓减半，只做主线核心 |
| 连续3笔亏损 | 停止开仓1天，仓位≤10% |
| 连续2天账户亏损 | 次日仓位≤20% |
| 连续3天账户亏损 | 强制空仓或只保留中线仓 |
| 单笔亏损>1.5R | 当日停止交易 |
| 当周亏损>5% | 下周只允许10%试错仓 |
| 当月亏损>8% | 本月剩余时间进入防守模式，总仓≤20% |

Profit retracement rules:

- Single-stock profit ≥10%: reduce by half if it gives back over 30% of the profit.
- Single-stock profit ≥20%: lock at least one-third.
- Single-stock profit ≥30%: break MA5 reduce by half; break MA10 clear short-term position.
- Account monthly profit >10%: before month-end, short-term position * 0.7.
- Account monthly profit >20%: preserving profit is first goal; position ≤40%.

Single-stock cap rules:

- First-board/low-level trial ≤5%.
- Confirmed main-line core 10%-15%.
- Leader weak-to-strong or divergence回封 up to 20%.
- Extremely strong main line plus consecutive account profits: leader max 25%, never higher.
- Back-row supplement ≤8%; high-position back row ≤5%; retreat-period new positions ≤5%.

Compressed rule: position is not decided by "how bullish I am"; it is decided by money-making effect, account state, calendar timing, regulatory environment, and negative-news intensity. Add only to main-line core when making money; cut first when losing; reduce proactively near month-end and holidays; survive first under regulation and negative news.
