### ner_time

#### time recognizer

##### 时间类型

- 绝对时间点

- 相对时间

- 时段

- 集合时间
- 事件触发的时间
- 文化相关的时间
- 不特定的时间

| 时间类型       | 示例          |
| -------------- | ------------- |
| 绝对时间点     | 1998年6月17日 |
| 相对时间       | 昨天、下周    |
| 时段           | 一小时、两周  |
| 集合时间       | 每小时        |
| 事件触发的时间 | 拉宾执政时代  |
| 文化相关的时间 | 马年          |
| 不特定的时间   | 夏天          |

##### 词汇触发词(lexical triggers)

触发词是指表示时间单位或概念的词或数字表达式，如天、月、年、8:00等。

#### time normalizer

2004-ISO 8601标准

| 单位         | 模式                | 示例                |
| ------------ | ------------------- | ------------------- |
| 年月日时分秒 | YYYY-MM-DDTHH:MM:SS | 1991-09-28T11:00:00 |
| 天           | YYYY-MM-DD          | 1991-09-28          |
| 秒           | HH:MM:SS            | 11:13:45            |
|              |                     |                     |
|              |                     |                     |
| 周           | YYYY-nnW            | 2007-27W            |
| 周末         | PnWE                | P1WE                |
| 季           | Qn                  | 1999-3Q             |
|              |                     |                     |
|              |                     |                     |



https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/chinese-timex2-guideline-summary-v1.2.pdf

基于依存分析和错误驱动的中文时间表达式识别, 2007

CTEMP : a Chinese temporal parser for extracting and normalizing temporal information, 2005