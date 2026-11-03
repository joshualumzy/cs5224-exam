# Mock C: answer key and source map

Do not open before sitting the paper. Source codes: 24S2 = 2425-Sem2 paper, 25S1 = 2526-Sem1, 25S2 = 2526-Sem2, OWN = written for this mock. Question wording is the past paper's own, except arrows fixed, a stray backtick removed (25S2 Q6 not used here) and the `deployment*` correction in 24S2 Q25 applied.

Marks: 26 MCQ x 1 + 9 short answers x 2 = 44. Time: 125 min.

## MCQ

| # | Source | Lecture | Answer | Official note |
|---|---|---|---|---|
| 1 | 25S1 Q1 | L02 | (c) | Option (c). (a) and (d) are not guaranteed. |
| 2 | OWN-C8 | L01 (own) | (b) | Option (b). Adding more instances is horizontal; doing it by hand on a fixed schedule means it is not elastic, because elastic scaling is usually automatic and follows the load, not a fixed time period (25S1 Q15). Mock A Q18 was the same distinction. |
| 3 | 25S2 Q13 | L09 | (b) | Option (b). Copy-paste leads to issues; one environment is error-prone because it is monolithic; hardcoding is not an option; separate code repositories are harder to manage. |
| 4 | 24S2 Q10 | L05 | (e) | Option (e). Adding more physical servers may help, but it depends more on how the virtualisation is set up. |
| 5 | OWN-C5 | L07 (own) | (c) | Option (c). Centroids are in log2, so a difference of d means a ratio of 2^d: 10 - 4 = 6, and 2^6 = 64. Source: L07 notes, Concept 2 (reading output, slides s17-18). |
| 6 | 25S1 Q14 | L01 | (b) | Option (b). |
| 7 | 25S2 Q18 | L03 | (b) | Option (b). The rest are not practical. A cooldown period gives resources time to adjust before any further change. |
| 8 | 24S2 Q17 | L10 | (d) | Option (d). You could end up with less space for the data on one of the clouds. |
| 9 | OWN-C9 | L01 (own) | (a) | Option (a). Both have organisational boundaries, but only the consumer extends its trust boundary to cover the provider, never the reverse (24S2 Q8). Mock A Q4 was a miss on this. |
| 10 | 25S2 Q2 | L06 | (d) | Option (d). PaaS enables the fastest building and deployment. IaaS takes time while SaaS is too restrictive since you wish to build your own application. |
| 11 | 24S2 Q13 | L02 | (a) | Option (a). Not much extra maintenance, since the extra resources come from the cloud, which is managed by the cloud provider. There are likely extra running costs. |
| 12 | OWN-C1 | L09 (own) | (d) | Option (d). The state file does not update itself. Plan and apply first refresh: they look up each tracked resource in the real cloud, compare with the configuration and act on the difference. Source: L09 notes, Concept 5 (state vs configuration; your repeated slip). |
| 13 | 25S1 Q19 | L06 | (d) | Option (d), as it provides scaling. (a) and (c) are not service models. |
| 14 | 25S2 Q15 | L06 | (d) | Option (d). Security and keeping software updated do not directly translate into availability. |
| 15 | 24S2 Q20 | L01 | (e) | Option (e). (b) is not an issue if you choose the right cloud. |
| 16 | OWN-C6 | L07 (own) | (e) | Option (e). K-means sees only distance, so the widest-range attribute dominates; a few extreme points pull a centroid out to themselves and waste one of the k clusters. Log compresses big values and makes equal ratios equal distances. Source: L07 notes, Concept 2 (slide s12 plus reasoning). |
| 17 | 25S1 Q16 | UNMAPPED | (c) | Option (c). All of these are fine. Asking clients is risky in case they forget. (Not covered by any lecture slide.) |
| 18 | 24S2 Q14 | L05 | (b) | Option (b). |
| 19 | 25S2 Q14 | L09 | (e) | Option (e). |
| 20 | OWN-C3 | L09 (own) | (e) | Option (e). IaC defines the server so any copy is identical and quick to build; it does not watch servers. Detection and replacement come from health checks and auto-scaling. Source: L09 notes, Concept 3 (pets vs cattle) and its WARNING box. |
| 21 | 25S1 Q12 | L02 | (d) | Option (d), as either would be fine depending on your needs. |
| 22 | 24S2 Q3 | L02 | (a) | Option (a). |
| 23 | 25S2 Q19 | L02 | (d) | Option (d). (b) may not be a choice depending on the application. The rest all take much more time and effort. (e) is not really an option. |
| 24 | OWN-C2 | L09 (own) | (a) | Option (a). Separate environments need separate state files. Putting them in different modules but one state does not separate them: one state means every apply covers production too. Using one module is the right part (it stops copies diverging). Source: L09 notes, Concept 5 and its WARNING box. |
| 25 | 25S1 Q2 | L06 | (d) | Option (d). SaaS gives the least manual work, but the data processing cannot be real-time and data privacy is also a concern. PaaS minimises work while meeting the privacy and real-time requirements. |
| 26 | 25S1 Q15 | L03 | (d) | Option (d). There is no specific time period; elastic scaling depends on the load. |

## Short answer

### Q27 (25S2 Q25, L06)

**Sample answer:** The primary issue is the sequence of operations before the gate opens. Do only what is necessary to let the user through and do the other operations later: asynchronous processing, where FaaS or a similar element helps. Scalability must be elastic, scaling up and down with the number of users.

**Marking:** Needs (1) asynchronous offloading of non-essential steps and (2) elastic scaling that also scales down.

### Q28 (OWN-C4, L09 (own))

**Sample answer:** Port 8080 is closed again. Apply makes its own plan first, checking the real cloud; it sees that the firewall (a resource it tracks) differs from the code, so the plan includes reverting it, and if nobody reads the plan the emergency fix is silently undone. The engineer should have put the change into the code (or reverted it) through normal review.

**Marking:** 1 mark: port closed again with the reason (apply checks live state against code and reverts the difference). 1 mark: put the hand change into the code via review. Common slip: assuming apply only touches what the teammate was changing.

### Q29 (24S2 Q22, L03)

**Sample answer:** Availability = high probability the system is operational at a given time. Use scaling (auto-scaling in particular), and have redundancy where server instances are in multiple zones/locations.

**Marking:** 1 mark per valid way. Load balancer with health checks routing away from failed instances also fits.

### Q30 (25S1 Q23, L04)

**Sample answer:** Use caching, CDNs, optimise the database for faster query processing, etc.

**Marking:** 1 mark per valid way; auto-scaling and load balancing are excluded by the question.

### Q31 (OWN-C10, L03/L02 (own))

**Sample answer:** (1) Keep each country's data in a region (or sovereign cloud) in that country and route each university's users to their country's regional service, with access control and encryption. (2) Put a load balancer and auto-scaling in each region so capacity scales out for the exam periods and back in afterwards, so there is no idle cost.

**Marking:** 1 mark for a residency design (in-region storage and routing users to region-specific services). 1 mark for a scaling design that also scales back DOWN. A single global region fails the residency rule; 'horizontal scaling' alone ignores scaling in (Mock A Q25 slip).

### Q32 (24S2 Q25, L02)

**Sample answer:** It depends. The main issue is data security and privacy and whether you require it. If not required, go public cloud; if it is, a hybrid or private model would work.

**Marking:** Must tie the choice to the security/privacy requirement and give both branches.

### Q33 (OWN-C7, L07 (own))

**Sample answer:** The upload server only saves the raw video to storage (S3) and leaves a job message in a queue (SQS), then replies at once; the encoders pick jobs from the queue when free, so the delay is just the backlog. Waiting for encoding would tie up the upload server and the user for the whole conversion, cause time-outs when encoders are busy (e.g. a viral spike), and a job running only inside one server would be lost if that server died, whereas a queued message reappears and another encoder takes it.

**Marking:** 1 mark: current design explained (save, queue, reply; encoders work from the backlog; delay is only conversion time). 1 mark: consequence of waiting (uploads block and time out under load, or job lost if the server dies). Naming 'asynchronous' without the mechanism earns at most 1.

### Q34 (25S2 Q21, L04)

**Sample answer:** Availability; cost of the cloud by region; location for latency; location for legal requirements. The question is about hosting cloud resources globally, not about deployment or service models.

**Marking:** 1 mark per factor with a reason. Deployment/service model answers do not count.

### Q35 (24S2 Q21, L10)

**Sample answer:** Reserved: typically used to run 24/7 over the long term, and the cost is lower than on-demand.

**Marking:** Reserved + reason (steady/long-running; cheaper than on-demand).

