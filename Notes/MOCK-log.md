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
