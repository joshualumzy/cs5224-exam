# Mixed Mock Log (L01-L05)

## Mock A (31 Oct 2026): 21.5/30 (72%), 31 of 90 minutes

Format: 20 MCQ (1 mark) + 5 short answers (2 marks), past-paper questions from all three papers plus one own (Q23), shuffled across L01-L05.

**MCQ: 14/20.** Wrong:
- **Q4 (trust boundaries, false statement):** chose (b) "A has its own organisational boundary". Both consumer and provider have organisational boundaries; the false one is (d): only the consumer extends its *trust* boundary to cover the provider, never the reverse.
- **Q7 (energy order, lowest to highest):** chose (c) Disk → DRAM → Cooling. Answer (e) Disk → Cooling → CPU: the slide chart shows storage small, cooling large, servers (CPU) largest. The slides give no separate DRAM share.
- **Q9 (VM vs Docker distinguishing factor):** chose (a) isolation. Both isolate, so isolation cannot distinguish them. Answer (e) separate namespaces: containers isolate via namespaces on a shared kernel; VMs use hardware virtualisation.
- **Q11 (tax SaaS deadline spike):** chose (d) lease hardware for the peak. Answer (a) robust load balancing: the real peak cannot be estimated, and leased hardware is expensive and slow to provision.
- **Q17 (different OSs on one host):** chose (c) containerization. Containers share the host kernel, so they cannot run a different OS, and they are not VMs. Answer (a) virtualisation. Repeat of the L05 "container = lightweight VM" model (starred in INDEX L05-6).
- **Q18 (scaling that adjusts resources to load):** chose (c) horizontal. Answer (e) elastic: horizontal is the direction (more instances, can be manual); elastic is automatic and follows load. Repeat of L01 elasticity vs scaling (already starred).

**Short answers: 7.5/10.**
- **Q21 backup time (2/2):** False; named data amount, bandwidth, latency. Note: server location is its own factor; latency is delay (distance is one cause).
- **Q22 vendor lock-in (2/2):** portable tech such as Docker; interoperable, non-proprietary services.
- **Q23 two isolation layers (1.5/2):** multitenancy keeps other SaaS clients out: right. Named a VPC for the provider's other customers: a VPC isolates network traffic, but what stops a co-located VM on the same physical server is the **hypervisor**, which logically separates VMs (a compromised guest stays isolated).
- **Q24 data residency across countries (1/2):** gave only a sovereign cloud that blocks foreign access. The question needs managed cross-border access across several countries: keep each country's data in-region and route users to region-specific services; plus access control/encryption and auditing.
- **Q25 healthcare SaaS (1/2):** community cloud is defensible for shared governance, but the outbreak spike was not handled. Key: private or hybrid (sensitive data private), with cloud bursting or controlled dynamic scaling that scales **up and back down**. "Horizontal scaling" names a direction, not an architecture, and ignores scaling in.

**Unused L01-L05 past questions (for Mock B):** 24S2 Q1, 3, 7, 9, 10, 13, 14, 15, 20, 22, 23, 25; 25S1 Q1, 7, 8, 12, 14, 15, 18, 23, 25; 25S2 Q1, 3, 5, 17, 18, 19, 20, 21, 24.

## Mock C: full paper written 3 Nov 2026 (Mock B papers written 2 Nov)

Mock C not yet sat. Papers and keys are in `Notes/mocks/` (see HANDOVER.md, "Mock papers"). Results to be logged below after each sitting, in the Mock A format (MCQ wrong with the reason, short answers with marks).

## Mock B (2 Nov 2026): 27/36 (75%); time not reported

Format: 24 MCQ (1 mark) + 6 short answers (2 marks). 26 real + 4 own (OWN-B1..B4).

**MCQ: 19/24.** Wrong:
- **Q9 (24S2 Q9, best fit for hybrid):** chose (a) government agency hosting sensitive data. Hybrid needs two kinds of demand: a large enterprise with varying workloads (d). A body whose data is all sensitive and steady is private (or sovereign). His Q25 answer shows he knows the idea; the slip is "sensitive means hybrid".
- **Q13 (OWN-B3, hypervisor):** chose (a) VPC rules. Answer (b) hypervisor. **Second miss of the same idea (Mock A Q23 was the first): star in INDEX L05 after Mock C.** A VPC only controls network traffic; VM memory access happens inside the machine and is separated by the hypervisor.
- **Q15 (24S2 Q18, most maintenance):** chose (a) PaaS and VMs. Answer (d) containers and VMs: PaaS puts the runtime and OS on the provider.
- **Q18 (25S2 Q3, virtualisation):** chose (c) "in hardware-assisted virtualisation the guest talks directly to hardware". Answer (d). In hardware-assisted virtualisation the CPU traps guest requests to the hypervisor (slides s17-18); the guest never reaches hardware directly.
- **Q22 (24S2 Q19, stateless computation):** chose (b) REST. Answer (d) Lambda. REST is a style for programs to talk to each other, not a place that runs code.

**Short answers: 8/12.**
- **Q25 hybrid security (2/2):** hybrid, sensitive part private, cheaper than full private.
- **Q26 instance choice (0.5/2):** chose g4 ($50,000), correct for that row, but said "lowest amongst all" without working out the other rows. c5a is $43,200 (21,600 s x $2). Method right; conclusion wrong because only one row was done.
- **Q27 ticket spike (1.5/2):** autoscaling with scale-in: full mark. "Cloud bursting" named but nothing on spilling over past a threshold and bursting back in: half mark. "Horizontal" adds nothing.
- **Q28 Singapore data (1.5/2):** data in Singapore plus copies and a load balancer. Missing: copies must stay in separate zones within Singapore, a load balancer spreads requests and does not store extra copies, nothing on cost.
- **Q29 bank (0.5/2):** chose IaaS + private. Key: hybrid (only *some* data sensitive, so full private costs more) + PaaS for the new build, IaaS for the legacy. His own Q25 reasoning (hybrid because only part is sensitive) was not applied here.
- **Q30 two VM cost ways (2/2):** Savings Plan (slide s9) and spot.

**Pattern:** wrong answers cluster in L06 (Q15, Q22) and L05 (Q13, Q18). Short answers lose marks by naming an architecture without saying how it works (bursting) or by not applying a reason he had already used in another answer (Q25 vs Q29).

## Mock C (3 Nov 2026, exam day): 32/44 (73%); time not reported

Format: 26 MCQ + 9 short answers. 25 real + 10 own gotchas (OWN-C1..C10).

**MCQ: 18/26.** Wrong:
- **Q2 (OWN-C8, manual Friday servers):** chose (e) elastic resource capacity. Answer (b) horizontal scaling done manually: more instances = horizontal; by hand on a fixed schedule = not elastic. Elastic resource capacity resizes ONE server vertically.
- **Q5 (OWN-C5, log2 centroids 4 and 10):** chose (b) 2.5x (10/4). Answer (c) 64x: centroids are in log2, so a difference d means 2^d, 2^6 = 64. Arithmetic/recall slip on a known L07 rule.
- **Q6 (25S1 Q14, major cloud security threat):** chose (a) unauthorized physical access. Answer (b) data breaches due to multi-tenancy (shared resources, overlapping trust boundaries). Physical access is the provider's datacentre problem.
- **Q8 (24S2 Q17, multi-cloud sync loss):** chose (c) incompatible APIs. Key: (d) uneven resource provisioning (one cloud runs short of space). Loosely supported by the slides (L10 s19), weak question.
- **Q13 (25S1 Q19, "which service model gives scalability"):** chose (c) auto-scaling. Answer (d) PaaS: auto-scaling is a feature, not a service model. Same pattern as Mock B Q22 (REST): answering with a technology when the question asks for a model/kind.
- **Q17 (25S1 Q16, encryption, "most choice"):** chose (e) (iii) or (iv). Answer (c) (ii) or (iii) or (iv): third-party tools are valid too; "most choice" means pick the option that lists every valid method. Not covered by any slide.
- **Q21 (25S1 Q12, e-commerce past-sales analysis):** chose (a) public only. Answer (d) either: nothing in the scenario forces private or hybrid, so "only" makes (a) wrong.
- **Q26 (25S1 Q15, NOT true statement):** chose (b) spam detection as MapReduce use case (true). Answer (d): elastic scaling follows load, not a specific period. Same idea as Q2.

**Short answers: 14/18.**
- Q27 MRT (2/2): async offloading + auto-scaling behind a load balancer, up and down.
- Q28 port 8080 (2/2): apply reverts it; put the change in the code.
- Q29 web farm availability (1/2): load-balanced duplicate servers; second way left blank (key: auto-scaling + redundancy across zones).
- Q30 two other methods (1.5/2): vertical scaling valid; cloud bursting assumes an on-prem base the question does not have. Key: caching, CDN, database optimisation.
- Q31 residency + exam peaks (2/2): in-country storage with routing, auto-scaling with scale-in.
- Q32 collaboration tools deployment (1.5/2): public, but only one branch; key: "it depends" on whether security/privacy is required (public if not; hybrid or private if so).
- Q33 upload design (1.5/2): async, no waiting; consequence correct (web servers pile up). Mechanism (S3 + queue + encoders) not stated.
- Q34 global hosting factors (0.5/2): gave cost (no region link) and security/trust boundary (a deployment-model answer). Key: availability, cost by region, latency/location, legal requirements.
- Q35 steady workload pricing (2/2): reserved, with the reason.

**Pattern:** elastic = automatic and follows load, not a schedule or one resized server (Q2, Q26; same as Mock A Q18). The question asks for a model or kind, not a feature (Q13, Mock B Q22). L09 went well: 3/3 MCQ and the port question 2/2.

**Scores over time:** Mock A 72%, Mock B 75%, Mock C 73%.
