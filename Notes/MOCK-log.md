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

## Mock B and Mock C Part 1: papers written 2 Nov 2026

Not yet sat. Papers and keys are in `Notes/mocks/` (see HANDOVER.md, "Mock papers"). Results to be logged below after each sitting, in the Mock A format (MCQ wrong with the reason, short answers with marks).

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
