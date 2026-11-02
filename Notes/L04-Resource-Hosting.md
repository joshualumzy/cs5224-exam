# L04 — Resource Hosting and Datacenter

Source: `Lecture 04 - Resource Hosting and Datacenter.pdf` (slides 3–28; slide 17 is a break slide). Cards: `cards/L04-cards.md`. Past-paper mapping from `PAST-PAPER-MAP.md`.

---

## Scenario Plan (11 scenarios + 1 mixed gap set) — all done

| # | Topic | Cards | Slides | Format | Past-paper link | Status |
|---|-------|-------|--------|--------|-----------------|--------|
| 1 | Hosting choice: on-premise vs cloud-based (QoS control, carriers, security) | C01 | 3 | Open + MCQ | 2526S2 Q21 | ✅ |
| 2 | Slow access diagnosis: latency vs bandwidth, what fixes which | C02 | 4 | Open + MCQ | 2425S2 Q6, Q24 | ✅ |
| 3 | Latency up but CPU low; CDN and carriers | C02, C04 | 4, 6 | MCQ (five options) + open | 2526S2 Q17; 2526S1 Q23 | ✅ |
| 4 | Why a network hop dwarfs local access; keep workloads local | C03, C09 | 5, 16 | Open | — | ✅ (merged into S2–S3; locality moves to S5) |
| 5 | Commodity modular hardware: build-out by racks, rack capacity | C07, C08, C09 | 10–16 | MCQ + open | — | ✅ |
| 6 | Storage: private vs shared state, storage hierarchy | C10, C11 | 18, 19 | MCQ | — | ✅ |
| 7 | Datacenter network: carrier interconnection, LAN, SAN, load balancer | C12, C13 | 20, 21 | MCQ + open | — | ✅ |
| 8 | Heat and cooling: air vs water vs sea, the water trade-off | C06, C14, C15 | 8, 9, 22–24 | Open | — | ✅ |
| 9 | PUE: what to cut, what the ideal means; energy breakdown order | C16 | 25, 26 | MCQ (five options) | 2526S1 Q9; 2526S2 Q11 | ✅ |
| 10 | Energy proportionality: idle cost of a lightly used fleet | C17 | 27 | Open + MCQ | — | ✅ |
| 11 | Datacenter tiers: choosing a tier, cost vs availability | C18 | 28 | Scenario choice | — | ✅ |
| Gap | Mixed set (4–5 short questions on concepts missed) | — | — | Mixed | — | ✅ |

Reference only (not tested, see below): Singapore datacenter counts (C05), the Supermicro spec figures (C08), the exact scaled-time table values (C03).

---

## Detailed Notes

### Concept 1: On-premise vs cloud-based hosting (S1)

**Core idea (slides, s3):**
- **On-premise:** the organisation is responsible for **deploying, operating and maintaining its internet connectivity**, has **complete control over Quality of Service (QoS)**, and provides its own security.
- **Cloud-based:** traffic crosses **multiple cloud carriers**, so **QoS depends on the carriers**. Easier to adopt for applications with **relaxed bandwidth and latency** needs. Security: the cloud is **not inherently insecure, just more actors** involved.

**What moving to the cloud gives up:** ownership of the connectivity and control over QoS. A strict response-time guarantee (latency) can no longer be enforced by the firm alone, and latency is a physical property, so it is the harder one to fix **(slides, s4)**. Latency and bandwidth are what QoS is judged on, not things the firm "owns".

> [!WARNING]
> **Mistake:** Saying the firm "no longer owns the latency and bandwidth". They are measurements of a connection. What is lost is ownership of the **connectivity** and **control over QoS** (carriers now sit in between). An overloaded server is a capacity problem that exists on-premise too; it is not the cost of moving.

**Key one-liner:** On-premise = you own the connectivity and control QoS; cloud = carriers decide QoS, so it suits apps with relaxed latency and bandwidth, and security is not worse, just shared among more actors.

### Concept 2: Latency vs bandwidth (S2)

**Core idea (slides, s4):**
- **Latency:** the time a packet takes to travel from one node to another. Matters when **response time is key**.
- **Bandwidth:** bits transferred per unit time. Matters when a **substantial amount of data** must be moved.
- **Easier to increase bandwidth than latency**, because latency is a **physical property**.

**Diagnosing which one a symptom is (beyond slides, worked example):** bulk transfers (large uploads and downloads) are limited by bandwidth, so more capacity speeds them up. Many small interactions (each click waits for a round trip) are limited by latency, so more capacity does not help; only a shorter path does, for example hosting closer to the users. Faster servers do not help either, because the delay is in the network.

**Key one-liner:** Big transfers are slow = add bandwidth; each small action is slow = latency, which more capacity cannot fix, only distance can.

### Concept 3: Latency up but CPU low; CDN and carriers (S3)

**Core idea:** If response time is slow while the servers are idle (low CPU, spare memory, an uncongested first link), the delay is in the network path, not the servers **(beyond slides, reasoning from s4)**. Adding server resources does not help.

**CDN (slides, s6):** keeps **versions of the content closer to the consumers**, so readers are served from a nearby copy instead of crossing the carrier networks to the origin datacenter. This is the fix for a distance-driven latency problem.

**Carriers (slides, s3, s6):** between consumers and the datacenter sit carriers/ISPs, and QoS depends on them. The hosting company cannot make other carriers' networks faster; what it owes or is owed by its own carrier is set by contract (SLA, beyond slides).

**Key one-liner:** Slow response with idle servers means network distance; a CDN fixes it by moving copies of the content near the consumers, because you cannot make the carriers' networks faster.

### Concept 4: A network hop dwarfs local access (S4)

**Core idea:** On the scaled-time view (slide 5, reference only), one cross-region internet round trip is orders of magnitude slower than DRAM, SSD or disk. A task that makes **many small remote reads** pays the full network delay **once per read**, so total time = number of trips x per-trip latency. A faster CPU or more bandwidth does not help **(slides, s4, s5; the multiplication is beyond slides)**.

**Fixes:** bring the data to the compute (cache nearby, with the risk of stale copies, beyond slides), choose a closer datacenter, or move the code next to its data **(keep workloads local, slides, s16)**.

**Key one-liner:** Many small remote reads multiply the network delay; fix it by making the reads local, not by adding CPU or bandwidth.

### Concept 5: Commodity modular hardware, racks and rack-level locality (S5)

**Core idea:** Datacenters use **commodity hardware with a modular architecture** ("like lego, building blocks") **(slides, s10-12)**. Servers are packed into racks as a cluster, and **racks are replicated** to scale up the datacenter. The standard sizing unit is the **rack unit**; a typical rack holds **42 1U servers** of 1.75 in each **(slides, s12, s16)**. Racks needed = servers / 42, rounded up (500 servers = 12 racks).

**The rack (slides, s16):** supports servers, storage and networking equipment, with provision for **power, battery backup and a rack-level switch (Top Of Rack, TOR)**. The TOR **connects IT resources within the rack and connects the rack to the datacenter network**.

**Keep workloads local (slides, s16):** workers that exchange a lot of data should share a rack so the traffic stays on the TOR instead of crossing the datacenter network and adding latency. Spreading across racks for fault isolation is a valid opposing consideration (beyond slides).

**Key one-liner:** Build big from identical commodity servers packed into racks and replicate racks; the TOR links the rack's servers and connects the rack outward, and chatty workloads should stay in one rack.

### Concept 6: Private vs shared storage, and the storage hierarchy (S6)

**Core idea (slides, s18):** datacenter storage is of **two categories**:
- **Private to an individual running task**: resides in **local DRAM or disk** of the server.
- **Part of the shared state of a distributed workload**: reached through a **distributed storage network**.

**Hierarchy (slides, s19):** **one server** (caches, DRAM, disks, flash disks); **each rack** (local and distributed memory); **across racks** (local and distributed memory). The hierarchy says where capacity sits; the two categories say who the data belongs to.

> [!WARNING]
> **Mistake:** Seeing remote memory as only "more space but slower". Its main advantage is that data in a distributed store is **shared**: every worker can read and update it. Local DRAM is private to one server, so shared state cannot live there.

**Speed order (beyond slides):** own DRAM is fastest. Memory reached over the datacenter network (same rack, then other racks) answers sooner (lower latency) than a spinning local disk, because a network round trip within the datacenter is far shorter than a disk seek; but a local disk can stream large data faster (higher bandwidth). With flash/SSD the gap is much smaller. The slides give no figures for this.

**Key one-liner:** Per-task scratch data stays in local DRAM or disk; state that every worker must see lives in a distributed storage network, trading speed for sharing and capacity.

### Concept 7: Datacenter networks and the load balancer (S7)

**Core idea (slides, s20):** three network roles.
- **Carrier interconnection:** between the datacenter (LAN) and cloud consumers (WAN).
- **LAN:** within a rack, with **redundant connectivity**.
- **SAN:** between servers and storage systems.

**Topology (slides, s21):** Internet, then border and access routers (Layer 3), then load balancers and switches (Layer 2), then racks of servers. A **network load balancer manages data movement**, spreading incoming requests across servers. The slide's housing analogy: rack = HDB, machine = house, house-to-house = corridor, HDB-to-HDB = main road, neighbourhood-to-neighbourhood = road. What a balancer must know about its servers (health, load) is L03 material.

**Key one-liner:** Carrier interconnection faces the consumers (WAN), the LAN links servers inside a rack redundantly, the SAN links servers to storage, and a load balancer spreads incoming requests across the servers.

### Concept 8: Datacenter heat and cooling (S8)

**Core idea:** Datacenters consume a lot of energy and **most of it is converted into heat, so cooling is a big issue (slides, s22)**. The three parts of a datacenter: **main server hall** (compute, storage, networking), **mechanical yard** (cooling systems), **electrical yard** (generators and power distribution) **(slides, s8-9, reference only)**.

**Cooling progression (slides, s23-24):** air to liquid cooling (**water is 1000x more efficient than air at removing heat**); then portable water to **seawater**, with the **Singapore Floating Datacenter Park** (Keppel) planned and **Microsoft Project Natick** as the first proof of concept for a datacenter in the sea.

> [!WARNING]
> **Mistake:** Giving the benefit of water cooling without its cost. The trade-off is that **water usage is very high**, which is what pushes the move from potable water to seawater and to siting at sea.

**Key one-liner:** Almost all datacenter power ends up as heat; water cools about 1000x better than air but uses a lot of water, so the next step is seawater and siting the datacenter at sea.

### Concept 9: Power Usage Effectiveness (S9)

**Core idea (slides, s25):** **PUE = total power used by the datacenter / power used by IT equipment.** The **ideal is 1** (no overhead). The overhead is cooling, power distribution and other infrastructure, and **cooling is a significant portion**. Worked example: IT 750 kW, total 1000 kW, PUE = 1.33.

**What to cut:** to approach 1, reduce the **overhead** (cooling, power distribution). Reducing IT equipment power (CPUs, DRAM, disks, networking) lowers both numerator and denominator, so it cannot bring PUE toward 1 and can make it worse. PUE measures overhead, not how efficiently the IT equipment itself uses power (beyond slides).

**Where the electricity goes (slides, s25 chart):** servers are by far the largest share, cooling is next, and storage and network are the smallest slivers. **Trend (slides, s26, Google):** average PUE fell from about 1.22 (2008) to about 1.10 and has flattened.

**Key one-liner:** PUE = total power / IT power, ideal 1; only cutting the overhead (cooling, distribution) moves it toward 1, because cutting IT power lowers both terms.

### Concept 10: Energy proportionality (S10)

**Core idea (slides, s27):** energy efficiency is **not a linear function of load**: an **idle system uses about 50% of peak power**. An **energy-proportional system** consumes almost no power when idle, very little under light load, and gradually more as load increases. Worked example: 200 servers at 400 W peak idle at 200 W each, so 40 kW is drawn all night while doing no work.

**Do not confuse with PUE:** PUE is an overhead ratio for the whole datacenter; energy proportionality is about how an IT system's power tracks its load.

**Key one-liner:** Real servers draw about half their peak power doing nothing, so a lightly used fleet is expensive; an energy-proportional system would draw almost nothing when idle.

### Concept 11: Datacenter tiers (S11)

**Core idea (slides, s28):** a ranking of datacenter **reliability**. Availability and cost both rise: **Tier 1 < Tier 2 < Tier 3 < Tier 4**.
- **Tier 1:** single path for power distribution, UPS and cooling, no redundant components. 99.671% uptime (about 28.8 h downtime/year).
- **Tier 2:** partial redundancy for power and cooling. 99.741% (about 22.7 h/year).
- **Tier 3:** multiple paths for power and cooling, each path with redundant components, **concurrently maintainable**. 99.982% (about 1.6 h/year).
- **Tier 4:** redundancy for every component. 99.995% (about 26 min/year).

**Choosing:** **Tier 3 is typically the industry standard; Tier 4 might be overkill.** Convert the uptime figures to downtime per year (x 8760 h) and compare with what the business can tolerate; pay for a higher tier only if the cheaper one fails that tolerance. Downtime hours are a worked conversion (beyond slides).

> [!WARNING]
> **Mistake:** Calling Tier 4 "justified" while also calling it overkill, without checking the numbers. If Tier 3's downtime already fits the tolerance, the extra cost of Tier 4 is not justified.

**Key one-liner:** Pick the cheapest tier whose yearly downtime fits what the business can tolerate; Tier 3 (multiple redundant paths, maintainable without downtime) is the usual choice and Tier 4 is often overkill.


---

## Reference only (not tested)

- **Singapore datacenters (slide 7):** 145 locations, 50 providers (datacenters.com).
- **1U server example (slides 13–15):** Supermicro AS-1127H7-N, dual AMD EPYC, up to 512 cores / 1024 threads, 32 DIMM slots, 3 PCIe slots, AIOM networking. Generic, not specialised hardware.
- **Scaled-time table (slide 5):** 1 CPU cycle 0.3 ns = 1 s; L1 0.9 ns = 3 s; DRAM 120 ns = 6 min; SSD 50–150 µs = 2–6 days; disk 1–10 ms = 1–12 months; Singapore–Hong Kong 40 ms = 4 years; Singapore–London 155 ms = 16 years; flight Singapore–Tokyo 7 hrs = 2.5 million years.

---

## Not yet tested

All concepts with an Application card were tested. Only reference-only items were not: the Singapore datacenter counts (C05), the datacenter anatomy (C06, server hall / mechanical yard / electrical yard), the Supermicro 1U spec (C08), the scaled-time table (C03) and the housing analogy details (C13).
