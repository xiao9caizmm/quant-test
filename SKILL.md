---
name: quant-test
description: Quantitative Chinese A-share review and stock-selection workflow for "量化测试skill". Use when asked for 量化测试skill, 复盘选股, 量化评分, 情绪评分, 880005情绪钟摆, 日内窗口计划, 主线板块打分, 仓位上限, or date-specific A股复盘+选股.
---

# 量化测试skill

Use this skill to turn an A-share daily review into a rule-based short-term stock-selection plan. It combines the user's `agent策略.docx` quantitative tables with the existing `a-share-short-review` data/style workflow.

## Workflow

1. Confirm the target trading day and previous trading day. If the target is a weekend or exchange holiday, write a non-trading-day strategy note instead of inventing data.
2. Use `a-share-short-review` if available for market data and prose style. Follow its data priority: MXSKILLS first, Eastmoney public APIs second, reputable public review sources third. Always label fallback data.
3. For every trading-day review, search 财联社 with the exact date plus `焦点复盘`. Prefer the original `cls.cn` article; if blocked, use reputable mirrors that clearly转载财联社 such as 东方财富 or 新浪. Extract and source-tag: 涨停数、炸板数、封板率、连板晋级率、主线热点催化、人气股反馈、后市展望. 涨停、跌停、炸板、连板晋级率默认使用非 ST 口径；若原文只给含 ST 口径，必须标注并降置信度。
4. Collect these fields for the target day and prior day: 涨停数量, 炸板率 or failed-board quality, 跌停数量, 最高连板/连板梯队, 回头波>8%股票数量, 主线板块指数或核心股表现, 成交额/量能, 涨跌家数, 创历史新高数量, 资金流向, and leading-sector stock pools. Pull limit-up/limit-down/failed-board/consecutive-board details with ST stocks excluded unless the user explicitly asks to include ST.
5. Before market-environment scoring, run the `880005情绪钟摆` and `日内四窗口` checks below. They act as short-term position switches: cycle decides base position, extremes decide the trading mode.
6. Apply hard veto rules before scoring: 跌停>60, 炸板率>45%, 高标断板后A杀扩散, 880005/RedCount进入高潮区仍追高, or 主线板块指数跌破MA5/MA10并放量下跌 caps the money-making score at 40 and prohibits high-position relay.
7. Score the market money-making effect by direct component points, not by vague impression: 涨停数量20, 炸板率20, 跌停数量20, 连板高度/梯队15, 主线板块指数15, 成交额/量能10. Use 财联社焦点复盘封板率 to derive 炸板率 whenever available: `炸板率 = 1 - 封板率`; if both涨停分析 and焦点复盘 exist, prefer焦点复盘 for the written review and mention口径差异 if material. Use non-ST counts for scoring; do not mix all-market counts that include ST with non-ST ladder data. 回头波>8% count is a risk modifier: if it expands materially or concentrates in a top-ranked theme, reduce continuation confidence and mention it in the score judgment. Use `scripts/score_quant.py` when component points are available as JSON; otherwise compute manually from `references/agent-strategy.md`.
8. Classify the emotional position as 冰点/修复/主升/高潮/退潮. Use the score as a base, then adjust by structure: index false strength, back-row climax, 880005情绪钟摆, or divergence-day return can change the action even when the total score looks acceptable.
9. Score candidate main lines with the 100-point model: 板块指数趋势25, 板块成交额20, 板块宽度15, 核心结构15, 分歧后回流15, 叙事/催化强度10. Main-line judgment must compare with the previous trading day; one-day strength is only rebound unless divergence-day return and sector diffusion confirm it. Use 财联社焦点复盘主线热点 paragraphs as the first source for catalysts and sector narrative.
10. Determine main-line stage: 初期/分歧/高潮/退潮. The output must state the stage and route only to the matching trading methods below.
11. Apply position rules after market and main-line scoring: base cap, recent trading result, consecutive losses, month-end/holiday timing, regulatory pressure, negative news, and profit retracement.
12. Build the selection pool only from the strongest one or two directions. Prefer 龙头/中军/趋势核心/创新高核心; avoid 后排杂毛 and climax extensions unless the output labels them as observation-only.
13. Write a Markdown file under `A股复盘/量化复盘选股` in the current workspace unless the user gives another folder. Suggested filename: `YYYYMMDD量化复盘选股.md`.

## Limit-Up/Limit-Down ST Exclusion

- For all quantitative scoring and route decisions, 涨停数、跌停数、炸板数、封板率、连板梯队、连板晋级率默认使用非 ST 口径。
- When using `mx-xuangu` / `MX_StockPick`, include `剔除ST、*ST、S*ST、退市股` in every natural-language query for 涨停、跌停、炸板、连板 or 连续涨停天数.
- When using 财联社、东方财富、同花顺、公开复盘文本 or Eastmoney public APIs, remove stocks whose names contain `ST`、`*ST`、`S*ST`、`退市` before counting or building ladders.
- If a source only reports aggregate all-market counts and cannot separate ST, label the value as `含ST口径`, do not mix it with non-ST detail tables, and reduce confidence in the money-making score.
- ST names may appear only in a data note unless the user explicitly asks to include ST stocks; they must not enter active observation pools by default.

## Emotion Clock, Windows, and Mode Routing

This module must run before `市场环境评分`. It is a position switch and mode router, not a replacement for main-line scoring.

### 880005情绪钟摆

- Use 通达信 `880005` daily data as the required source for this module. Calculate `880005` MA5 to define the short-term cycle. `MA5 < 2000` = 冰点/进攻观察; `MA5 > 2300-2500` = 高潮/降仓区.
- If 通达信 `880005` data is unavailable, write `通达信880005未稳定返回` and do not substitute another index silently. You may use RedCount alone as a lower-confidence trigger, but label the cycle judgment as incomplete.
- Use real-time or same-day `RedCount` as the trigger. 红盘家数 `<=1000` = 冰点; extreme panic can relax to `<=1500`; `>=4000` = 高潮.
- Cycle determines base position; extreme RedCount determines mode. Low cycle + low RedCount routes to 冰点修复; high cycle + high RedCount routes to 降仓/不追高.

### 日内四窗口

- `9:15-9:30`: only emotion positioning and pre-market hypothesis. Do not force trades.
- `9:30-10:30`: primary execution window. Confirm 共振日、反弹日、最快反包首板、最高板弱转强.
- `10:30-14:30`: certainty drops. Handle rotation and risk control only; if afternoon index expectation weakens, prohibit divergence dip-buying and weak-to-strong chasing.
- `14:30-15:00`: confirm tail-session ice point and lock next-day plan.
- Every quantitative daily review must include `明日窗口计划`; do not output only a stock pool.

### 极值-反弹-强化三日循环

- `Day1`: tail-session RedCount `<=1000` confirms ice point.
- `Day2`: rebound day. Prefer earliest reversal first-board, highest-board weak-to-strong, and high-recognition long-leg dip-buying, only if the previous high-position loss effect stops spreading.
- `Day3`: strengthening day. If emotion remains low, consider fastest 1-to-2 or independent-logic second board. If already hot, skip new second-board positions.
- Optional `Day4`补票: only when index opens low + emotion re-enters a low point; watch flat/green auction 2-to-3 weak-to-strong.
- Use this cycle in `次日候选模式路由`.

### 容错率辅助指标

- 同花顺全A `CCI(5)`: from around `-100` turning up = capacity-stock swing start support; above `+100` or upper-band turn-down = reduce/switch signal.
- `昨日炸板股指数` vs its MA5: far above MA5 and rising = repair force strong and tolerance improves; close to or below MA5 = tolerance drops and position must be reduced.
- These indicators only validate market tolerance. They do not override main-line scoring.

### 容量过滤和竞价门槛

- Most modes require daily turnover `>=10亿`; around `20亿` is ideal capacity.
- In weak or shrinking-volume markets, require both `成交额>=10亿` and `流通市值>=100亿`.
- Auction watchlist gate: auction amount `>2000万` and volume ratio `>1.5`.
- Traditional 1-to-2 may require auction volume `>=15%` of previous-day total volume plus a high open, but treat this as a historical reference, not a mechanical rule.
- `成交额/流通市值/竞价量比` are preconditions before any mode trigger.

### 涨停板质量评分

- First priority is sector linkage. After an individual limit-up, the sector index should rise together and 2-3 recognizable followers should appear within 10-30 minutes.
- For capacity stocks, early-board sealed order around `3-4亿` adds quality. In weak or stock-only liquidity, sealed order above `15亿` can signal excessive consensus and should not be blindly chased.
- If a failed board refills within 5 minutes with active sweep orders, second volume expansion, and thicker sealed orders, add quality.
- Repeated failed boards, weak refills, or no sector followers downgrade quality.

### 回头波风险统计

`回头波` is the intraday pullback from a stock's daily high to its close:

`回头波 = (日内最高价 - 收盘价) / 日内最高价 * 100%`

Every quantitative review must count non-ST stocks where `回头波 > 8%` on the target day. Exclude `ST`, `*ST`, `S*ST`, and `退市` names by default.

Use this as a chasing-loss and hot-theme fade indicator:

- If the count expands versus the previous trading day, reduce market tolerance and note that intraday追高亏钱效应 is rising.
- If `回头波 > 8%` names concentrate in a ranked main-line direction, downgrade that direction's `分歧回流` or `核心结构` evidence unless its core stocks still close strongly.
- If the count is low while涨停/新高扩散, it supports higher continuation quality.
- Do not treat 回头波 as炸板率. 炸板率 only measures failed limit-up boards; 回头波 measures all-stock high-to-close fade.

### 拿货分时

- Only identify this pattern when the index is one-way down, emotion is extremely poor, and the stock has continuous one-word board opening or high-recognition leader attributes.
- Required traits:逆势震荡走高, repeated board touches without sealing or repeated failed boards, full-day volume, intraday amplitude usually `>10%`, and a high-volume bullish daily candle.
- Next-day shrink-volume acceleration confirms; a low open in auction can become an add point only after confirmation.
- This is dangerous. Limit it to a `2%-5%` trial layer. Never use it to justify ordinary weak stocks.

### 四类模式路由

- `首板`: only for emotion turn-up, early main-rally resonance, or low-position independent strength.
- `二波反包`: only for absolute prior popularity leaders or core capacity names on the day after an ice point.
- `一进二`: only on TurnUp strengthening day or early MainRally theme fermentation; prefer the fastest turnover second board.
- `分歧低吸`: only for the total leader or core capacity stock in a main rally's first strong divergence. Prohibited during retreat and during afternoon index expected weakness.
- `撬跌停`: extreme ice-point play only. Pry-board volume must reach `15%-25%` of a recent historical huge-volume day's turnover, otherwise it is not valid support.

### 最终执行路由

Use this order every time:

1. Judge market environment and 通达信 `880005` cycle.
2. Classify the day as 冰点日、反弹日、强化日、高潮日, or 退潮日.
3. Select only the modes allowed by that day type.
4. Filter candidates by成交额、流通市值、板块联动、涨停板质量.
5. Output position caps after all filters, not before.

`杰哥模式` is only a超短节点识别器. It may help identify ice-point/rebound/strengthening nodes, but it must never raise the position cap or relax discipline.

Default position discipline:

- 普通票单票上限 `20%`.
- 试错层 `2%-10%`.
- After consecutive losses, reduce trial layer to `2%-5%`.
- When trading is out of control or rules are repeatedly violated, reduce active position to `0%`.

### 纪律补丁

The following are hard violations and must be labeled as违规 in the review/plan:

- 下午指数走弱时低吸.
- 退潮期弱转强.
- 非主线最快二板.
- 没有板块联动的孤立涨停.
- 用拿货分时解释亏损票.
- 错过第一个最快二板后追第二、第三个低质量卡位.

Do not use `杰哥模式`, concept tags, or post-hoc narratives to justify these violations.

## Required Output

For a trading day, write these sections in order:

1. `◆ 一、量化核心结论`
2. `◆ 二、市场全景与前日对比`
3. `◆ 三、赚钱效应量化评分`
4. `◆ 四、主线板块量化排名`
5. `◆ 五、选股观察池`
6. `◆ 六、明日窗口计划`
7. `◆ 七、仓位与风控`
8. `◆ 八、次日验证点`

Required tables:

- Money-making score table columns: `指标`, `原始数据`, `得分上限`, `实际得分`, `判断`.
- Main-line ranking table columns: `排名`, `板块`, `指数趋势`, `成交额`, `宽度`, `核心结构`, `分歧回流`, `叙事催化`, `总分`, `定性`.
- Stock-selection table columns: `股票`, `方向`, `角色`, `入选逻辑`, `触发条件`, `失效条件`, `仓位上限`, `风险`.
- Include a concise `财联社焦点复盘口径` note when the article is available: 封板率/炸板数, 连板晋级率, main catalysts, and outlook risk.
- Include a `回头波风险统计` note or table: count of non-ST stocks with `回头波 > 8%`, concentrated themes, representative names, and impact on continuation confidence.

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
- If 回头波 OHLC data is unavailable, do not invent it. Write `回头波结构化数据未稳定返回`, then use public review descriptions only as qualitative fade-risk evidence.
- If sources disagree materially, use ranges such as `约`, explain the口径, and reduce confidence in the score.
- If no account trading history is provided, state that profit/loss dynamic adjustments are not applied; do not invent recent wins/losses.

## New-High StockPick Data Rule

For all quantitative reviews and stock-selection outputs, historical-new-high stocks are a required input to main-line scoring and the observation pool. The primary source is 妙想 `MX_StockPick` through the local `mx-xuangu` skill.

Recommended query:

```powershell
$env:PYTHONIOENCODING='utf-8'; $env:PYTHONUTF8='1'; python 'C:\Users\33256\.codex\skills\mx-xuangu\mx_xuangu.py' "YYYY年M月D日创历史新高的A股，显示股票简称、东财行业、概念、总市值"
```

Usage rules:

- Read the CSV/JSON output path printed by `mx_xuangu.py`; do not reuse stale data from another date. On Windows, keep `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1` if GBK encoding errors appear.
- Rate-limit `MX_StockPick` conservatively. Empirical rule from local runs: back-to-back dated historical-new-high queries can trigger status `112` / `请求频率过高`; one query every 35 seconds completed a 7-date batch without triggering frequency control. For future batch reviews, wait at least 35 seconds between `mx-xuangu` calls; after any status `112`, stop the batch, wait 60-120 seconds, then resume from the failed date. Never retry status `112` in a tight loop.
- Cache and reuse the CSV/JSON path for each target date. If the target-date CSV already exists and its row count/date fields match the task, read it instead of calling `MX_StockPick` again.
- Verify the returned date fields match the target trading day. Treat the CSV row count as the historical-new-high count only after this check.
- Extract `名称`/`股票简称`, `东财行业分类二级`, `概念`, `总市值`, price/change fields, and the historical-high date when present.
- Group by industry/theme to quantify new-high concentration. This grouping must feed the `主线板块量化排名`: add evidence to `宽度`, `核心结构`, and `分歧回流` when core names keep making new highs after prior-day divergence.
- In the stock pool, prefer names from the new-high pool when they also belong to a ranked direction. Label their role as `新高核心`, `趋势核心`, `中军`, or `弹性核心`; do not select them only because they made a new high.
- If `MX_StockPick` returns empty, malformed, wrong-date, or unrelated rows, explicitly mark the field as `MX_StockPick未稳定返回`, then fall back to Tonghuashun Data Center historical-new-high data if available, and finally to public review/news sources as lower-confidence supplements.

## References

- Full strategy tables and default scoring rubrics: `references/agent-strategy.md`.
- Optional score calculator: `scripts/score_quant.py`.

## Main-Line Ranking Detail Override

When writing `◆ 四、主线板块量化排名`, the output must expose the numeric score for each 100-point main-line component instead of only prose labels.

Use this required table structure:

| 排名 | 板块 | 指数趋势/25 | 成交额/20 | 宽度/15 | 核心结构/15 | 分歧回流/15 | 叙事催化/10 | 总分 | 较前日变化 | 定性 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |

Rules:

- The ranking table must include exactly 6 sector/theme rows, ordered by total score. If fewer than 6 strong sectors exist, fill the lower rows with `弱轮动线`, `防守线`, or `退潮观察线` rather than omitting them.
- Each component cell must include the score and a short evidence phrase, for example `21：科创50领涨，板块强于指数`.
- `总分` must equal the six component scores.
- `较前日变化` must compare with the prior trading day's main-line ranking and score when available, using formats such as `第2->第1，+10分`, `第1->第1，-5分`, `新进，+68分`, or `第1->第3，-18分`.
- After the ranking table, add a `主线较前日变化分析` subsection. It must explain:
  - which sectors rose in ranking and why;
  - which sectors fell in ranking and why;
  - whether the top-ranked sector is confirmed main line, divergence repair, strong rotation, or retreat observation;
  - whether the change is driven by core-stock new highs, sector breadth, volume, divergence-day return, catalyst strength, or only one-day emotion.
- Do not call a sector a main line only because it ranks first that day. If it is new, low-capacity, or one-day event-driven, label it as `强轮动线` or `抱团线` until it proves next-day return and board diffusion.

## Stock Pool Direction Coverage Override

When writing `◆ 五、选股观察池`, the pool must cover every direction listed in `◆ 四、主线板块量化排名`.

Rules:

- The ranking table may contain six sector/theme rows, but the stock pool must not force-fill names for weak or unmatched directions.
- Select 2-3 stocks for each ranked sector/theme direction only when enough valid matched candidates exist. If fewer than 2 valid stocks exist, output the valid names only; if none exist, write one row with `暂无可验证候选` and explain the missing evidence.
- Add a `对应排名` or `主线方向` column so every stock maps back to one of the six ranked directions.
- For confirmed or effective main lines, prefer `核心`, `中军`, `趋势核心`, `弹性核心`, and `新高核心`.
- For `强轮动线`, `弱轮动线`, `防守线`, or `退潮观察线`, list stocks only after passing the direction-consistency gate below; label the role as `观察` or `轻仓观察`, and set a lower position cap.
- Do not add stocks from unranked themes. If a stock cannot be mapped to a ranked direction, exclude it.
- Do not select a stock only because it hit limit-up. It must have a clear role, a next-day trigger condition, an invalidation condition, a position cap, and a risk note.

## Stock Pool Direction Consistency Gate

Before a stock enters `◆ 五、选股观察池`, it must pass a direction-consistency check against its ranked sector/theme. This gate overrides any instruction to output 2-3 stocks per direction.

Evidence that can validate a stock-direction match:

- The stock's `东财行业分类二级`, `申万行业分类`, or `概念` directly contains the ranked direction keyword or a clear synonym, such as `通信设备/光模块/光通信/CPO/数据中心`, `化学制药/生物制品/医疗服务/创新药`, `半导体/光学光电子/PCB/服务器/算力硬件`, `自动化设备/机器人/专用设备`, `电网设备/火电/绿电/煤炭`, etc.
- The stock is named in the target-day limit-up ladder, focus-review article, or catalyst paragraph as a core stock of that ranked direction.
- The stock is a widely recognized upstream/downstream core of the direction and the review explicitly states the mapping, for example `光通信器件 -> 算力硬件` or `电网设备 -> 电力设备`. Do not rely on loose imagination.
- Use industry-first matching and concept-assisted confirmation. A loose concept tag alone is not enough when the industry clearly points elsewhere. For example, `医药电商` does not make an `电机` stock an `创新药` stock; `新能源车/锂电池概念` does not make a `通信设备` stock a `锂电` stock; `油运/航运` does not make a `航运港口` stock an `油气` stock; a generic `军工` tag does not make an unrelated stock a `商业航天` core unless `商业航天/卫星导航/航天装备` evidence is present.

Negative rules:

- Never allocate new-high stocks by market-cap order, CSV row order, or fixed slicing across ranked directions.
- Never put an unrelated industry into a direction just to satisfy the 2-3 stock count. Examples: `航运港口` cannot be placed under `光通信/数据中心`; `半导体/通信设备` cannot be placed under `创新药/医药`; `生物制品/医疗服务` cannot be placed under `算力硬件`; `非白酒` cannot be placed under `机器人`.
- For mixed or broad directions such as `普反低位`, `防御`, `低位轮动`, `商业航天`, `贵金属`, `油气`, and `旅游体育`, be stricter rather than looser. If the data only gives a weak or generic concept tag and no industry match, output `暂无可验证候选`.
- A stock can appear in only one direction unless there is explicit source evidence for dual attributes. If overlap exists, assign it to the direction with the strongest source evidence and explain briefly.
- ST stocks are excluded from active observation pools by default. If a historical-new-high result contains an ST stock, only mention it in a data note unless the user explicitly asks to include ST names.
- If a direction has ranking evidence but no valid candidate stock, keep the direction in the ranking table and write `暂无可验证候选` in the stock pool. This is better than inventing a candidate.

Required validation note:

- After the stock-selection table, add one sentence: `方向一致性检查：本表仅保留行业/概念/连板梯队/公开复盘文本能够映射到对应主线方向的个股；未匹配方向不强行补位。`

## Mandatory Stock Classification Source Check

Before classifying any stock into a main-line direction or stock-selection pool, verify the classification with the same source chain every time:

1. **MX_StockPick / `mx-xuangu` first.** Check `东财行业分类二级`, `申万行业分类`, `概念`, target-day涨跌幅, and market cap. Treat `东财行业分类二级` and `申万行业分类` as the first gate, not just the concept tags.
2. **`mx-search` second.** Search the target date plus the stock name and likely directions, such as `YYYY年M月D日 股票名 上涨 原因 机器人 商业航天 光通信`. Use it to identify the actual same-day catalyst, abnormal-move announcement, Dragon-Tiger list, or public review explanation.
3. **财联社焦点复盘/连板分析 third.** If the stock is being used for a hot theme such as 机器人、商业航天、CPO、AI应用、PCB, verify whether 财联社 or another reputable same-day review explicitly names the stock under that theme.

Classification priority:

- If all three sources agree, classify the stock into that direction.
- If industry and same-day catalyst point to one direction but loose concept tags point to another, follow the industry plus same-day catalyst. Do not follow loose concept tags.
- If only a concept tag links the stock to a direction and there is no industry match or same-day review confirmation, exclude it from that direction.
- If the stock is a mixed-attribute name, classify it by the strongest same-day reason and write the nuance in `入选逻辑`; otherwise leave it out.

Examples from local validation:

- `三瑞智能` on 2026-05-08 should not be treated as a商业航天 core just because it has low-altitude/eVTOL-style tags. `mx-search` showed the stronger same-day logic was 人形机器人/机器人动力模组/次新/异动公告.
- `中瓷电子` on 2026-05-08 should not be treated as a商业航天 core. The stronger evidence was 通信设备、光通信陶瓷封装、6G、第三代半导体.
- `杰普特` on 2026-05-08 should not be used as a机器人主线 stock. It is better classified as 激光设备、光通信设备链、PCB/先进封装设备, and the target-day涨幅 was not strong.
- `大族激光` on 2026-05-08 has robot/减速器 tags, but the stronger move reason was 激光设备、PCB设备、先进封装设备、AI光通信设备链. Do not use it as a pure机器人 representative unless same-day review explicitly frames it that way.
