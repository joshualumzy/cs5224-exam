# Mock C, Part 1: answer key and source map

Do not open before sitting the paper. Source codes: 24S2 = 2425-Sem2 paper, 25S1 = 2526-Sem1, 25S2 = 2526-Sem2, OWN = written for this mock. Question wording is the past paper's own, except arrows fixed, a stray backtick removed (25S2 Q6 not used here) and the `deployment*` correction in 24S2 Q25 applied.

Marks: 19 MCQ x 1 + 6 short answers x 2 = 31. Time: 90 min.

## MCQ

| # | Source | Lecture | Answer | Official note |
|---|---|---|---|---|
| 1 | 25S2 Q13 | L09 | (b) | Option (b). Copy-paste leads to issues; one environment is error-prone because it is monolithic; hardcoding is not an option; separate code repositories are harder to manage. |
| 2 | 24S2 Q10 | L05 | (e) | Option (e). Adding more physical servers may help, but it depends more on how the virtualisation is set up. |
| 3 | 25S1 Q1 | L02 | (c) | Option (c). (a) and (d) are not guaranteed. |
| 4 | 25S2 Q18 | L03 | (b) | Option (b). The rest are not practical. A cooldown period gives resources time to adjust before any further change. |
| 5 | 24S2 Q17 | L10 | (d) | Option (d). You could end up with less space for the data on one of the clouds. |
| 6 | 25S1 Q14 | L01 | (b) | Option (b). |
| 7 | 25S2 Q2 | L06 | (d) | Option (d). PaaS enables the fastest building and deployment. IaaS takes time while SaaS is too restrictive since you wish to build your own application. |
| 8 | 24S2 Q13 | L02 | (a) | Option (a). Not much extra maintenance, since the extra resources come from the cloud, which is managed by the cloud provider. There are likely extra running costs. |
| 9 | 25S1 Q19 | L06 | (d) | Option (d), as it provides scaling. (a) and (c) are not service models. |
| 10 | 25S2 Q15 | L06 | (d) | Option (d). Security and keeping software updated do not directly translate into availability. |
| 11 | 24S2 Q20 | L01 | (e) | Option (e). (b) is not an issue if you choose the right cloud. |
| 12 | 25S1 Q16 | UNMAPPED | (c) | Option (c). All of these are fine. Asking clients is risky in case they forget. (Not covered by any lecture slide.) |
| 13 | 24S2 Q14 | L05 | (b) | Option (b). |
| 14 | 25S2 Q14 | L09 | (e) | Option (e). |
| 15 | 25S1 Q12 | L02 | (d) | Option (d), as either would be fine depending on your needs. |
| 16 | 24S2 Q3 | L02 | (a) | Option (a). |
| 17 | 25S2 Q19 | L02 | (d) | Option (d). (b) may not be a choice depending on the application. The rest all take much more time and effort. (e) is not really an option. |
| 18 | 25S1 Q2 | L06 | (d) | Option (d). SaaS gives the least manual work, but the data processing cannot be real-time and data privacy is also a concern. PaaS minimises work while meeting the privacy and real-time requirements. |
| 19 | 25S1 Q15 | L03 | (d) | Option (d). There is no specific time period; elastic scaling depends on the load. |

## Short answer

### Q20 (25S2 Q25, L06)

**Sample answer:** The primary issue is the sequence of operations before the gate opens. Do only what is necessary to let the user through and do the other operations later: asynchronous processing, where FaaS or a similar element helps. Scalability must be elastic, scaling up and down with the number of users.

**Marking:** Needs (1) asynchronous offloading of non-essential steps and (2) elastic scaling that also scales down.

### Q21 (24S2 Q22, L03)

**Sample answer:** Availability = high probability the system is operational at a given time. Use scaling (auto-scaling in particular), and have redundancy where server instances are in multiple zones/locations.

**Marking:** 1 mark per valid way. Load balancer with health checks routing away from failed instances also fits.

### Q22 (25S1 Q23, L04)

**Sample answer:** Use caching, CDNs, optimise the database for faster query processing, etc.

**Marking:** 1 mark per valid way; auto-scaling and load balancing are excluded by the question.

### Q23 (24S2 Q25, L02)

**Sample answer:** It depends. The main issue is data security and privacy and whether you require it. If not required, go public cloud; if it is, a hybrid or private model would work.

**Marking:** Must tie the choice to the security/privacy requirement and give both branches.

### Q24 (25S2 Q21, L04)

**Sample answer:** Availability; cost of the cloud by region; location for latency; location for legal requirements. The question is about hosting cloud resources globally, not about deployment or service models.

**Marking:** 1 mark per factor with a reason. Deployment/service model answers do not count.

### Q25 (24S2 Q21, L10)

**Sample answer:** Reserved: typically used to run 24/7 over the long term, and the cost is lower than on-demand.

**Marking:** Reserved + reason (steady/long-running; cheaper than on-demand).

