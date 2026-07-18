# Reviewer 2 Response Plan

Article: `ARTICLE-NA-009`

Status: `REVIEWER_RESPONSE_PLAN_COMPLETE`

## Likely Objections

1. **There is no downstream NLP task.**
   Response: correct. The article is a bounded baseline/project-note style
   result and refuses performance claims until a task dataset exists.
2. **The local corpus may not be representative.**
   Response: the paper reports the sample size and treats representativeness as
   a human-review and future-experiment issue.
3. **The derived f/v tokenizer has the same metrics as the source-layer
   tokenizer.**
   Response: the equality is a result for this run, not evidence that the
   derived layer is source-observed.
4. **BPE slightly reduces mean tokens per word.**
   Response: token count alone is not task quality. The paper reports the delta
   without treating it as task improvement.
5. **Data-release rights are unclear.**
   Response: the current package is metric-only; public corpus release remains
   blocked until rights clearance.

## Revision Priority

Prioritize corpus-scope review, then target-venue framing, then supplementary
data policy.
