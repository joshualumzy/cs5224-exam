# Past-Paper Map (all 75 questions)

Built by DeepSeek V4.1 Flash, cross-checked by GLM 5.3. Checks run: 75/75 rows, no duplicates; all cited slides exist; GLM agreed on the main lecture for 64/75; disputed rows settled by searching slide text; 6 random rows read against their slide (5 exact; the 6th was read against the wrong slide by my script, not re-checked). **Also** = a second lecture (or GLM's pick) that also covers it.

| Paper | Q | Main | Also | Concept tested | Slide ref | Conf |
|---|---|---|---|---|---|---|
| 2425-S2 | 1 | L02 | L06 P1, L01 | SaaS use case: avoid on-prem Capex | L02 s8 | H |
| 2425-S2 | 2 | L02 | L05, L03, L10, L01 | SaaS portability/interoperability + NIST 5/4/3 counts | L02 s30 (also s3) | M |
| 2425-S2 | 3 | L02 | L06 P1 | PaaS = development/deployment environment | L02 s12 | H |
| 2425-S2 | 4 | L01 | L10, L02 | Pay-as-you-go lowers experimentation risk | L01 s30 | H |
| 2425-S2 | 5 | L05 | L05 (s20) | Full virtualisation: guest OSs unaware, Type 1 vs containers | L05 s13 | H |
| 2425-S2 | 6 | L04 | L01 | Latency vs bandwidth as cause of slow access | L04 s4 | H |
| 2425-S2 | 7 | L02 | L06 P1 | SaaS examples (Google Photos) vs IaaS/PaaS | L02 s8 | H |
| 2425-S2 | 8 | L01 | L02 | Trust boundary expansion is one-directional (consumer→provider) | L01 s42 | M |
| 2425-S2 | 9 | L02 | — | Hybrid = balance control and cost for varying workloads | L02 s45 | H |
| 2425-S2 | 10 | L05 | L03 | VM resource allocation/consolidation under contention | L05 s6 | L |
| 2425-S2 | 11 | L03 | L02 | Workload distribution / elastic load balancing for spikes | L03 s7 | H |
| 2425-S2 | 12 | L02 | L05 | Resource pooling by provider → cost savings | L02 s6 | M |
| 2425-S2 | 13 | L02 | L10 | Provider-managed maintenance means overhead does not scale | L02 s38 | L |
| 2425-S2 | 14 | L05 | L02 | Tenant isolation → security/isolation benefit of single tenancy | L05 s38 | M |
| 2425-S2 | 15 | L05 | — | Containers share host kernel; VM isolation is stronger | L05 s27 | H |
| 2425-S2 | 16 | L02 | L01 | Broad network access / location-independent access | L02 s4 | M |
| 2425-S2 | 17 | L10 | L01 | Inter-cloud replication/synchronisation; provisioning mismatch | L10 s19 | L |
| 2425-S2 | 18 | L06 P2 | L02 | Consumer vs provider responsibility across IaaS/PaaS/CaaS/FaaS | L06 P2 s24 | H |
| 2425-S2 | 19 | L06 P2 | L02 | FaaS/Lambda: stateless, event-driven, no provisioning | L06 P2 s20 | H |
| 2425-S2 | 20 | L01 | L10 | Application compatibility / differing cloud platforms | L01 s40 | M |
| 2425-S2 | 21 | L10 | — | Reserved pricing for steady 24/7 workloads | L10 s9 | H |
| 2425-S2 | 22 | L03 | L06 P1 | Auto-scaling + redundancy across zones for availability | L03 s8 | M |
| 2425-S2 | 23 | L02 | L01 | Hybrid: sensitive data private, rest public (cheaper than all-private) | L02 s45 | H |
| 2425-S2 | 24 | L04 | L01 | Performance = f(location, latency, bandwidth, data amount) | L04 s4 | H |
| 2425-S2 | 25 | L02 | — | Deployment model choice driven by security/privacy need | L02 s36 (and s45) | H |
| 2526-S1 | 1 | L02 | L01 | Database-as-a-Service variant: accessibility and scalability | L02 s18 | L |
| 2526-S1 | 2 | L06 P1 | L02 | PaaS: provider maintains stack, consumer keeps control of deployment | L06 P1 s26 | M |
| 2526-S1 | 3 | L06 P2 | — | Too many workers overload master; optimal worker count | L06 P2 s12 | H |
| 2526-S1 | 4 | L06 P2 | L10 | FaaS/Lambda: no idle cost, bursty event-driven workload | L06 P2 s21 | H |
| 2526-S1 | 5 | L06 P2 | — | Map writes to local disk; system shuffles/sorts/merges | L06 P2 s7 (and s9) | H |
| 2526-S1 | 6 | L05 | L02 | Virtualisation abstracts hardware; multitenancy shares one app instance | L05 s36 | H |
| 2526-S1 | 7 | L01 | L02 | Security/trust boundary is the dominant concern | L01 s42 | H |
| 2526-S1 | 8 | L03 | — | Distribute incoming requests across servers | L03 s7 | H |
| 2526-S1 | 9 | L04 | — | PUE = total power / IT power ⇒ cut overhead (cooling/power) | L04 s25 | H |
| 2526-S1 | 10 | L02 | L03 | Cloud Broker – Service Aggregation | L02 s34 | H |
| 2526-S1 | 11 | L03 | — | Built-in load balancer (vs independent) | L03 s14 | H |
| 2526-S1 | 12 | L02 | L01 | Deployment model selection depends on needs — public or private | L02 s36 | M |
| 2526-S1 | 13 | L06 P1 | L02 | PaaS is used by application developers | L06 P1 s19 | H |
| 2526-S1 | 14 | L01 | L05, L02 | Shared resources/overlapping trust boundaries → data breach | L01 s42 | M |
| 2526-S1 | 15 | L03 | L10, L06 P2 | Elastic scaling responds to load, not a fixed period | L03 s4 | M |
| 2526-S1 | 16 | UNMAPPED | L02, L05 | No lecture slide covers client/app encryption (searched 'encrypt': 0 slides) | — (closest L02 s31) | L |
| 2526-S1 | 17 | L01 | L03 | Horizontal/elastic scaling definition | L01 s35 | H |
| 2526-S1 | 18 | L05 | — | Containers isolate app from OS/other apps while sharing kernel | L05 s27 | H |
| 2526-S1 | 19 | L06 P1 | L02 | PaaS built-in scalability (not a service model: ELB/auto-scaling) | L06 P1 s20 | M |
| 2526-S1 | 20 | L03 | — | Predefined scaling conditions vs intelligent automation engine | L03 s21 (and s24) | H |
| 2526-S1 | 21 | L10 | — | EC2 instance families and price/performance computation | L10 s7 (and s9) | H |
| 2526-S1 | 22 | L01 | L10 | Vendor lock-in mitigation (portability, multi-provider, Docker) | L01 s41 | M |
| 2526-S1 | 23 | L04 | L06 P1 | CDN/caching to cut latency and load | L04 s6 | M |
| 2526-S1 | 24 | L10 | L01 | Reserved/spot instances, avoid over-provisioning, scale down | L10 s9 | H |
| 2526-S1 | 25 | L02 | L01 | Sovereign cloud / region selection and in-region replication | L02 s47 | H |
| 2526-S2 | 1 | L03 | — | Routes traffic only to healthy targets | L03 s9 | H |
| 2526-S2 | 2 | L06 P1 | L02 | PaaS: fastest build/deploy ("all in one" IDE to deploy) | L06 P1 s20 | M |
| 2526-S2 | 3 | L05 | — | Virtualisation isolates apps on same server / one-to-many | L05 s3 | H |
| 2526-S2 | 4 | L02 | L06 P1 | Database-as-a-Service in PaaS vs LAMP stack on IaaS | L02 s18 | M |
| 2526-S2 | 5 | L02 | L01 | Sovereign cloud | L02 s47 | H |
| 2526-S2 | 6 | L03 | — | Cloud bursting (burst out / burst in) | L03 s28 | H |
| 2526-S2 | 7 | L06 P2 | — | FaaS cannot persist connections/state (stateless) | L06 P2 s24 | H |
| 2526-S2 | 8 | L10 | — | Sunk costs and integration costs in TCO comparison | L10 s15 | H |
| 2526-S2 | 9 | L02 | L06 P1 | IaaS = most control, most consumer responsibility | L02 s19 | M |
| 2526-S2 | 10 | L05 | — | Containers use namespaces/shared kernel vs hardware virtualisation | L05 s28 (and s27) | H |
| 2526-S2 | 11 | L04 | — | Energy breakdown: disks < cooling < CPU | L04 s25 | M |
| 2526-S2 | 12 | L06 P2 | — | Serverless: no provisioning/managing servers | L06 P2 s21 | H |
| 2526-S2 | 13 | L09 | — | Separate state files / modules per environment | L09 s26 | M |
| 2526-S2 | 14 | L09 | — | terraform plan + alert; configuration drift | L09 s28 (and s35) | M |
| 2526-S2 | 15 | L06 P1 | L03, L04 | Reliability: autoscaling + multi-region redundancy | L06 P1 s6 | M |
| 2526-S2 | 16 | L01 | L10 | Application compatibility with cloud platforms | L01 s40 | M |
| 2526-S2 | 17 | L04 | L01 | Network bottleneck vs latency/bandwidth | L04 s4 | H |
| 2526-S2 | 18 | L03 | L01 | Predefined scaling conditions/thresholds to damp oscillation | L03 s21 | L |
| 2526-S2 | 19 | L02 | L06 P1 | IaaS lift-and-shift as least-effort migration | L02 s20 | M |
| 2526-S2 | 20 | L01 | L03 | Horizontal scaling distributes reads/writes across nodes | L01 s35 | H |
| 2526-S2 | 21 | L04 | L02, L10 | Resource hosting: availability, region cost, latency, legal | L04 s3 | M |
| 2526-S2 | 22 | L03 | L02 | Hybrid/private cloud + cloud bursting (L03 s27-29) / dynamic scaling | L03 s28 | M |
| 2526-S2 | 23 | L01 | L02 | Data localisation/residency; region-pinned storage | L01 s46 | M |
| 2526-S2 | 24 | L02 | L06 P1 | Hybrid (private for sensitive) + PaaS for new build | L02 s45 | H |
| 2526-S2 | 25 | L06 P2 | L03 | FaaS/async offloading of fare calc; elastic scaling | L06 P2 s20 | M |

## By lecture (main only)

- **L01** (10): 24S2 Q4, 24S2 Q8, 24S2 Q20, 25S1 Q7, 25S1 Q14, 25S1 Q17, 25S1 Q22, 25S2 Q16, 25S2 Q20, 25S2 Q23
- **L02** (19): 24S2 Q1, 24S2 Q2, 24S2 Q3, 24S2 Q7, 24S2 Q9, 24S2 Q12, 24S2 Q13, 24S2 Q16, 24S2 Q23, 24S2 Q25, 25S1 Q1, 25S1 Q10, 25S1 Q12, 25S1 Q25, 25S2 Q4, 25S2 Q5, 25S2 Q9, 25S2 Q19, 25S2 Q24
- **L03** (10): 24S2 Q11, 24S2 Q22, 25S1 Q8, 25S1 Q11, 25S1 Q15, 25S1 Q20, 25S2 Q1, 25S2 Q6, 25S2 Q18, 25S2 Q22
- **L04** (7): 24S2 Q6, 24S2 Q24, 25S1 Q9, 25S1 Q23, 25S2 Q11, 25S2 Q17, 25S2 Q21
- **L05** (8): 24S2 Q5, 24S2 Q10, 24S2 Q14, 24S2 Q15, 25S1 Q6, 25S1 Q18, 25S2 Q3, 25S2 Q10
- **L06 P1** (5): 25S1 Q2, 25S1 Q13, 25S1 Q19, 25S2 Q2, 25S2 Q15
- **L06 P2** (8): 24S2 Q18, 24S2 Q19, 25S1 Q3, 25S1 Q4, 25S1 Q5, 25S2 Q7, 25S2 Q12, 25S2 Q25
- **L09** (2): 25S2 Q13, 25S2 Q14
- **L10** (5): 24S2 Q17, 24S2 Q21, 25S1 Q21, 25S1 Q24, 25S2 Q8
- **UNMAPPED** (1): 25S1 Q16
