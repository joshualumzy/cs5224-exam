# Mock B: answer key and source map

Do not open before sitting the paper. Source codes: 24S2 = 2425-Sem2 paper, 25S1 = 2526-Sem1, 25S2 = 2526-Sem2, OWN = written for this mock. Question wording is the past paper's own, except arrows fixed, a stray backtick removed (25S2 Q6 not used here) and the `deployment*` correction in 24S2 Q25 applied.

Marks: 24 MCQ x 1 + 6 short answers x 2 = 36. Time: 110 min.

## MCQ

| # | Source | Lecture | Answer | Official note |
|---|---|---|---|---|
| 1 | 24S2 Q1 | L02 | (d) | Option (d). For the rest, SaaS is not a practical application to use. |
| 2 | 25S1 Q3 | L06 | (a) | Option (a). (b) is wrong as more workers usually reduces latency up to a point. (c) is wrong because some CPUs would sit idle and network is not the only overhead. (d) is wrong because the number of workers does affect latency. (e) is wrong because fewer workers mean each gets more tasks, which decreases idle time. |
| 3 | 25S2 Q17 | L04 | (d) | Option (d). Most probable cause for increased latency. |
| 4 | 24S2 Q15 | L05 | (b) | Option (b). Each VM is isolated, while containers can be impacted by the OS being compromised. |
| 5 | OWN-B1 | L07 (own) | (a) | Option (a). The mapper only labels: for each point it finds the nearest current centroid and emits (clusterID, point). N points in, N pairs out, only k distinct keys. Averaging the points into a new centroid and counting them is the reducer's job ((b) describes the reducer's output). Source: L07 k-means slides (s8-10). |
| 6 | 25S1 Q8 | L03 | (c) | Option (c). |
| 7 | 25S2 Q5 | L02 | (d) | Option (d). Bookwork. |
| 8 | 25S2 Q7 | L06 | (b) | Option (b). The rest all work fine for FaaS. |
| 9 | 24S2 Q9 | L02 | (d) | Option (d). Hybrid clouds allow balancing between private and public clouds. |
| 10 | 25S1 Q18 | L05 | (c) | Option (c). |
| 11 | 25S2 Q1 | L03 | (b) | Option (b). |
| 12 | 25S1 Q13 | L06 | (b) | Option (b). |
| 13 | OWN-B3 | L05 (own) | (b) | Option (b). The hypervisor logically separates the VMs and gives each its own share of CPU, memory and storage. A VPC only isolates network traffic. Application-level multitenancy separates customers inside one app instance, not VMs on a server. This was Mock A's Q23 weak spot. Source: L05 virtualisation slides; 24S2 Q2 option (d) wording. |
| 14 | 25S2 Q20 | L01 | (a) | Option (a). Horizontal scaling lets you distribute these reads and writes across multiple nodes. |
| 15 | 24S2 Q18 | L06 | (d) | Option (d). PaaS is managed by the provider, while FaaS requires low maintenance. |
| 16 | 25S1 Q4 | L06 | (e) | Option (e). Traffic is bursty during festive periods but not otherwise. Lambda has no continuous cost when idle. EC2 and EBS incur continuous cost even when idle. CloudFront and S3 are only for static content and do not handle app logic. |
| 17 | 24S2 Q7 | L02 | (d) | Option (d). Rest are all cloud provisions, either PaaS or IaaS. |
| 18 | 25S2 Q3 | L05 | (d) | Option (d). Comes directly from the definition in some ways. |
| 19 | 25S1 Q7 | L01 | (b) | Security. The rest depend on SLAs and what you can get, but by going to the cloud your data is no longer under your control to some extent. |
| 20 | 25S2 Q8 | L10 | (e) | Option (e). (a) ignores sunk costs: it may be cheaper later, but there is no guarantee. (b) and (c) are not really options. (d) cannot ignore sunk costs. |
| 21 | OWN-B2 | L07 (own) | (c) | Option (c). Encoding is CPU-heavy, uploading is I/O-heavy; on shared servers the encodings use all the CPU and uploads time out. Separate groups scale independently, and the queue lets an upload finish as soon as the file is saved, so a spike only lengthens the conversion backlog. (d) is synchronous, so uploads would still wait on busy encoders. (b) and (a) do not touch the CPU contention. (e) is vertical scaling and still shares one pool. Source: L07 video-app slides (s20-30) and my reasoning. |
| 22 | 24S2 Q19 | L06 | (d) | Option (d). Use FaaS: computations are simple and no state is maintained. |
| 23 | 25S2 Q12 | L06 | (d) | Option (d). |
| 24 | 25S1 Q5 | L06 | (d) | Option (d). Bookwork. |

## Short answer

### Q25 (24S2 Q23, L02)

**Sample answer:** Move to a hybrid cloud: sensitive data on a private cloud, less sensitive workloads on the public cloud. You could also move everything to a private cloud, but that would be more expensive overall.

**Marking:** Must reach hybrid and give the cost reason (private only costs more).

### Q26 (25S1 Q21, L10)

**Sample answer:** c5a, total $43,200. Time = FLOPs / speed + I/O ops x latency; cost = time x price. m7: 60000/1 = 60000 s + 800000 x 3 ms = 2400 s = 62400 s x $1 = $62,400. i8: 60000 + 800 = 60800 s x $2 = $121,600. c5a: 60000/3 = 20000 + 1600 = 21600 s x $2 = $43,200. r7: 62400 s x $2 = $124,800. g4: 60000/30 = 2000 + 8000 = 10000 s x $5 = $50,000.

**Marking:** 2 marks: correct instance (c5a) with working. Slips seen before: giving seconds instead of dollars; mis-scaling Tera/Peta (60 PFLOP = 60,000 TFLOP).

### Q27 (OWN-B4, L03/L01 (own))

**Sample answer:** Any two of: (1) move to the cloud with a load balancer plus automatic (elastic) scaling that adds servers during the sale and removes them afterwards; (2) hybrid with cloud bursting: keep the normal load on-premise and spill over to pre-deployed cloud resources only past a threshold, then burst back in; (3) put a CDN/cache in front for static pages and a queue or serverless functions behind the checkout so extra work is absorbed and billed per use; (4) pay-as-you-go on-demand instances only for sale windows.

**Marking:** 1 mark per way. Each way must say how capacity comes back DOWN after the spike (scale in, burst in, per-use billing). 'Horizontal scaling' alone, or 'buy more servers', earns nothing: it names a direction and ignores scaling back down (Mock A Q25 slip).

### Q28 (25S1 Q25, L02)

**Sample answer:** Use a sovereign cloud, or select specific regions for data storage, and ensure that data replication occurs only within those regions.

**Marking:** Must cover both: compliance (data stays in Singapore) AND availability (replicate, but only within the allowed region/zones).

### Q29 (25S2 Q24, L02)

**Sample answer:** Hybrid cloud: sensitive workloads on private cloud, non-sensitive on public cloud. Build the new application through PaaS for the modern services; any legacy infrastructure can stay on IaaS. Key points: not all data is sensitive, and the application has to be rebuilt, which implies PaaS.

**Marking:** Needs both a deployment model (hybrid, with the reason) AND a service model (PaaS for the new build, IaaS for legacy). One without the other loses marks.

### Q30 (25S1 Q24, L10)

**Sample answer:** Eliminate over-provisioning; use reserved instances for predictable workloads; use spot instances for non-critical workloads; use auto-scaling to scale down as necessary.

**Marking:** 1 mark per valid way, two needed.

