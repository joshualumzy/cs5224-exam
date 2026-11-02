# L04 Concept Cards

Built by DeepSeek V4.1 Flash from the slide text; diagram facts transcribed by Claude Haiku and the slide 22 and 25 charts read by Claude Sonnet from the slide images. Slide 17 is a break slide (no content). 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide.

### L04-C01 Resource hosting: on-premise vs cloud-based
- **Slides:** 3
- **Type:** Application
- **What it is:** Two hosting choices. **On-premise:** organisations are **responsible for deploying, operating and maintaining internet connectivity**, have **complete control over Quality of Service (QoS)**, and are **providing security**. **Cloud-based:** use **multiple cloud carriers**, so **QoS is dependent on carriers**; **easier to adopt for applications with relaxed bandwidth and latency**; on security, the slide's point is that cloud is **not inherently insecure — just more actors**.
- **Look-alikes:** Control over QoS vs dependence on carriers — on-premise owns the connectivity, cloud hands it to several carriers; "relaxed bandwidth and latency" vs the latency/bandwidth definitions (slide 4) — the hosting choice is judged against those two requirements; "more actors" vs "insecure" — the slide explicitly separates the two.
- **Limits / trade-offs:** Cloud hosting is only "easier" for applications that can tolerate relaxed bandwidth and latency; on-premise carries the deployment, operating and maintenance burden to get full QoS control (inferred from what on-premise is responsible for).
- **Situation cues:** "we must guarantee response time ourselves", "our own team runs the connectivity", "several carriers sit between us and the users", "the app can tolerate variable latency so hosting is easier".
- **Past-paper Qs:** 25S2 Q21

### L04-C02 Latency vs bandwidth
- **Slides:** 4
- **Type:** Application
- **What it is:** **Latency** — the **time it takes a packet to travel from one data node to another**; **important when response time is key** for applications. **Bandwidth** — the **number of bits transferred per unit time**; **important when a substantial amount of data transfer is required** by the application. The decisive line: **easier to increase bandwidth than latency (physical property)**.
- **Look-alikes:** Latency vs bandwidth — one is delay for a packet to cross, the other is volume per unit time; both get called "speed" in casual use (inferred); improving bandwidth vs improving latency — bandwidth can be added, latency is a physical property and therefore harder.
- **Limits / trade-offs:** Latency cannot be bought away the way bandwidth can, because it is a **physical property**; so an application whose response time is key is constrained by distance, not by link capacity (inferred).
- **Situation cues:** "users complain the page takes seconds to respond", "we need to move terabytes", "we doubled the link but the round trip is unchanged", "the two nodes are far apart".
- **Past-paper Qs:** 24S2 Q6, 24S2 Q24, 25S2 Q17

### L04-C03 Time scales of computing latencies
- **Slides:** 5
- **Type:** Reference-only
- **What it is:** A table scaling each latency so one **CPU cycle (0.3 ns)** becomes **1 second**: **L1 cache 0.9 ns → 3 seconds**; **main memory (DRAM, from CPU) 120 ns → 6 minutes**; **solid-state disk I/O (flash) 50–150 µs → 2–6 days**; **rotational disk I/O 1–10 ms → 1–12 months**; **internet Singapore–Hong Kong (2555 km) 40 ms → 4 years**; **internet Singapore–London (10856 km) 155 ms → 16 years**; **flight Singapore–Tokyo (5322 km) 7 hrs → 2.5 million years**.
- **Look-alikes:** Cache vs DRAM vs flash vs rotational disk — each step is orders of magnitude apart; local device access vs an internet round trip — on the scaled view one internet hop dwarfs a disk read (inferred comparison from the table); the latency column vs the scaled-time column — the second is an analogy for human intuition, not a measurement.
- **Limits / trade-offs:** The values are the slide's reference figures; the scaled column is illustrative only (inferred).
- **Situation cues:** "why a network hop hurts more than a disk read", "put these latencies in order of magnitude", "the scaled-time analogy".
- **Past-paper Qs:** none

### L04-C04 Cloud connectivity and CDN
- **Slides:** 6
- **Type:** Application
- **What it is:** Cloud connectivity between consumers and the datacenter, with **CDN** annotated as: **have versions of the content closer to the consumers**. Diagram (slide 6): consumer networks (enterprise) connect through carrier/ISP networks ("importance of cloud carriers or ISPs") to the provider's network and datacenter.
- **Look-alikes:** CDN vs cloud hosting — the CDN keeps *versions of the content* near consumers rather than serving everything from the datacenter (inferred from the annotation); CDN vs a single central copy — the point is proximity to the consumer.
- **Limits / trade-offs:** None stated on the slide; keeping versions implies copies must be managed (inferred).
- **Situation cues:** "users in another region wait too long", "serve the content from somewhere near the user", "the same content is needed in many places".
- **Past-paper Qs:** 25S1 Q23

### L04-C05 Singapore datacenter landscape
- **Slides:** 7
- **Type:** Reference-only
- **What it is:** Singapore datacenter locations, from datacenters.com: **145 locations**, **50 providers**.
- **Look-alikes:** Number of locations vs number of providers — one provider can run several locations, so the two counts answer different questions (inferred).
- **Limits / trade-offs:** A snapshot of one directory's listing (inferred).
- **Situation cues:** "how many datacenters are in Singapore", "how many providers".
- **Past-paper Qs:** none

### L04-C06 Datacenter anatomy: server hall, mechanical yard, electrical yard
- **Slides:** 8, 9
- **Type:** Reference-only
- **What it is:** The datacenter's three parts: **main server hall** — **compute, storage, and networking equipment**; **mechanical yard** — **hosts cooling systems**; **electrical yard** — **generators and power distribution centers**. Diagram (slide 8): cooling equipment (water storage, fan coil/air handling units, chillers, cooling towers) and power equipment (utility power, transformers, power bus, backup generators) surround the networking room, racks and servers.
- **Look-alikes:** Mechanical yard vs electrical yard — cooling versus power; server hall vs the other two — the only part holding IT equipment, the yards exist to keep it running (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "where do the generators sit", "which area holds the cooling plant", "what is in the server hall".
- **Past-paper Qs:** none

### L04-C07 Commodity, modular servers built into racks
- **Slides:** 10, 11, 12
- **Type:** Application
- **What it is:** Datacenters use **commodity hardware with a modular architecture**; **servers are modularized and packed as a cluster in server racks**; **server racks are replicated as scaled up computational resources to form a datacenter**. Lecture annotation: **"like lego -> building blocks"**, and the sizing unit is **1 rack unit — a standardized amount of space**. Slide 10's annotation is **"organization: layering"**. Diagrams: slide 10 shows the Core / Aggregation / Access network layers above the servers ("layering"); slide 12 shows 1U server (1.75 in) → 42U rack (cluster) → multiple clusters joined by a cluster switch → datacenter.
- **Look-alikes:** Server vs rack vs datacenter — the same modular idea repeated at three levels (inferred from "replicated as scaled up"); commodity vs specialised — the example server is **generic hardware, not specialized** (slide 14); "modularized and packed" vs "scaled up" — packing builds a rack, replication of racks builds the datacenter.
- **Limits / trade-offs:** None stated on the slides.
- **Situation cues:** "build the datacenter out of identical blocks", "what is the standard unit of space", "why commodity rather than bespoke hardware".
- **Past-paper Qs:** none

### L04-C08 The 1U server: Supermicro AS-1127H7-N
- **Slides:** 13, 14, 15
- **Type:** Reference-only
- **What it is:** The worked example of commodity hardware: **Supermicro AS-1127H7-N — 1U Hyper Server**, **actually generic hardware, not specialized**; **2 CPUs connected by buses**; **blue → memory slots**; **dual AMD EPYC 9006 SP7 Series processors, up to 512C/1024T (512 cores / 1024 threads)**; **32 DIMM slots**; **3 PCIe expansion slots for networking and storage**; **flexible networking via AIOM (Advanced I/O Module)**. Slides 13–15 carry the photo and spec text.
- **Look-alikes:** 1U vs rack unit — the same standardized unit of height; 512C vs 1024T — threads are twice cores in the quoted spec; "generic" vs specialized — the slide stresses this is off-the-shelf, not purpose-built.
- **Limits / trade-offs:** None stated; the spec is one model's configuration, not a datacenter-wide rule (inferred).
- **Situation cues:** "what fits in one rack unit", "how much memory can one server take", "which slot takes the network card".
- **Past-paper Qs:** none

### L04-C09 The machine rack and rack-level locality
- **Slides:** 16 (slide 17 is a break slide)
- **Type:** Application
- **What it is:** A **machine rack supports servers, storage and networking equipment**; it **has provision for power, battery backup and a rack-level switch (e.g., Top Of Rack — TOR)**. The **rack-level switch connects IT resources within the rack and also connects the rack to the datacenter network**. A **typical commodity rack can house 42 1U servers, each of 1.75 in height**. Lecture annotations: **"rack -> connections"** and **"reduce latency -> keep workloads local"**.
- **Look-alikes:** Rack-level switch vs datacenter network — TOR is the rack's own switch and its doorway outward; keeping workloads local vs spreading them — locality cuts latency while distribution balances load, so the two pull in opposite directions (inferred).
- **Limits / trade-offs:** Capacity per rack is bounded (42 1U servers); the locality hint trades away spreading work across the datacenter (inferred).
- **Situation cues:** "servers in the same rack talk constantly", "a top-of-rack switch", "move the workload next to its data to cut latency", "how many 1U servers fit".
- **Past-paper Qs:** none

### L04-C10 Datacenter storage: private vs shared
- **Slides:** 18
- **Type:** Application
- **What it is:** Storage comes in **two categories**: **private to individual running tasks — resides in local DRAM or disk**; and **part of the shared state of a distributed workload — a distributed storage network**.
- **Look-alikes:** Private storage vs shared state — one belongs to a single task, the other is common state for a distributed workload; local DRAM/disk vs distributed storage network — where the data physically sits.
- **Limits / trade-offs:** Shared state depends on a storage network rather than a local device (inferred).
- **Situation cues:** "each task has its own scratch data", "every node must see the same state", "data lives on one server's disk".
- **Past-paper Qs:** none

### L04-C11 Storage hierarchy
- **Slides:** 19
- **Type:** Application
- **What it is:** Three levels of storage: **one server — caches, DRAM memory, disks, flash disks**; **each rack — local and distributed memory**; **across racks — local and distributed memory**. (slide 19 has text only)
- **Look-alikes:** The storage hierarchy vs the two storage categories (slide 18) — the hierarchy says *where* capacity sits (server, rack, across racks), the categories say *who it belongs to* (one task vs shared state); "local" vs "distributed" at rack and cross-rack level.
- **Limits / trade-offs:** None stated.
- **Situation cues:** "what memory is available inside one server vs across racks", "where should this data live".
- **Past-paper Qs:** none

### L04-C12 Datacenter network: carrier interconnection, LAN, SAN
- **Slides:** 20
- **Type:** Application
- **What it is:** Three network roles. **Carrier interconnection** — **between the datacenter (LAN) and cloud consumers (WAN)**. **Local Area Network (LAN)** — **within a rack**, with **redundant connectivity**. **Storage Area Network (SAN)** — **between servers and storage systems**.
- **Look-alikes:** LAN vs WAN vs SAN — inside the rack, out to consumers, and to storage respectively; carrier interconnection vs LAN — the boundary where consumer traffic enters; SAN vs the distributed storage network (slide 18) — SAN is the network between servers and storage systems, the distributed storage network is how shared state is reached (inferred distinction).
- **Limits / trade-offs:** Redundancy is stated for the LAN within a rack; nothing is said about redundancy of the other two (inferred from what the slide lists).
- **Situation cues:** "which network connects servers to the storage systems", "redundant links inside the rack", "consumer traffic arrives over the WAN".
- **Past-paper Qs:** none

### L04-C13 Datacenter network topology and the housing analogy
- **Slides:** 21
- **Type:** Application
- **What it is:** The network topology with a **network load balancer** that **manages data movement**, explained by an analogy: **rack → HDB**, **machine → house**, **house connected to house by corridor**, **HDB connected to HDB by main road**, **neighbourhood connected to neighbourhood by road**. Diagram (slide 21): Internet → Layer 3 (border routers BR, access routers AR) → Layer 2 (load balancers LB and L2 switches S) → racks of servers (A), grouped as a single layer 2 domain.
- **Look-alikes:** The four analogy levels map to rack, machine, rack-to-rack and neighbourhood-to-neighbourhood links (inferred from the annotations); network load balancer vs rack-level switch — the balancer manages data movement across the topology, the TOR connects within and out of a rack (inferred).
- **Limits / trade-offs:** The analogy is illustrative, not a technical claim (inferred).
- **Situation cues:** "explain the datacenter network in plain terms", "what sits between racks and between neighbourhoods", "who manages data movement".
- **Past-paper Qs:** none

### L04-C14 Datacenter energy demand and heat
- **Slides:** 22
- **Type:** Application
- **What it is:** **Datacenters consume a lot of energy**, and **most of this is converted into heat — cooling is a big issue!** Chart (slide 22): electricity use of data centres 2010–2030 in TWh under three scenarios (best, expected, worst); the worst case rises steeply to about 8,000 TWh by 2030, expected to about 3,000, best to about 1,000.
- **Look-alikes:** Energy consumed vs heat produced — the slide treats almost all consumed energy as becoming heat, which is why cooling follows immediately as a topic (inferred); this card vs PUE (slide 25) — this is the demand and heat problem, PUE is the ratio used to measure the overhead.
- **Limits / trade-offs:** Cooling is named as the big issue that follows from the heat; no efficiency figure is given on this slide.
- **Situation cues:** "the power bill is dominated by the datacenter", "why is cooling the hard part", "energy turned into heat".
- **Past-paper Qs:** 25S2 Q11 (energy breakdown)

### L04-C15 Cooling: air to water, freshwater to seawater
- **Slides:** 23, 24
- **Type:** Application
- **What it is:** The move **from air to liquid (water) cooling — water is 1000x more efficient than air to remove heat**; then **from portable water to seawater**, with the **planned Singapore Floating Datacenter Park** (Keppel) as the example; **in the sea** is affirmed, with **Microsoft Project Natick as the first Proof of Concept** — "the 'Cloud' in the Ocean". The cost: **water usage is very high**. Lecture annotation: **"data center in space? possible"**. Slide 23 shows hot-cold aisle cooling in a raised-floor datacenter: cool air from CRAC units rises through floor tiles into cool aisles, passes through the racks and returns as hot air from the hot aisles; liquid supply feeds the heat exchange.
- **Look-alikes:** Air vs water cooling — water is quoted as 1000x more efficient at removing heat; freshwater vs seawater — the next step in sourcing; floating/undersea vs land-based — siting choice, with Natick as proof of concept.
- **Limits / trade-offs:** **Water usage is very high**, which is the trade-off for more effective cooling.
- **Situation cues:** "air cooling cannot keep up", "water consumption is a concern", "put the datacenter on the sea", "cool with seawater".
- **Past-paper Qs:** none

### L04-C16 Power Usage Effectiveness (PUE)
- **Slides:** 25, 26
- **Type:** Application
- **What it is:** **PUE = total power used by datacenter ÷ power used by IT equipment**, so **in the ideal case PUE is 1**. Context on the same slide: **cooling is a significant portion of power used**, and a chart shows the **share of electricity consumption by data centre and equipment type**. Slide 26 shows **average PUE for all data centers**. Chart (slide 25, IEA 2024): stacked bars of the share of data-centre electricity by equipment type for four kinds of data centre (enterprise, colocation and service provider, hyperscale, and one more), segments Servers, Storage, Network, Cooling, Other infrastructure. **Servers are by far the largest share (roughly 30–75%), Cooling is next (roughly 10–30%), and Storage and Network are the smallest slivers** — so storage (disks) < cooling < servers (CPU) in consumption (this is what 25S2 Q11 tests). Chart (slide 26, Google): average PUE falls from about 1.22 (2008) to about 1.10 (recent years) and has flattened.
- **Look-alikes:** Total datacenter power vs IT equipment power — the ratio's two terms; PUE vs energy proportionality (slide 27) — PUE is an overhead ratio, energy proportionality is how consumption tracks load (inferred); PUE = 1 vs a real datacenter — 1 is the ideal with no overhead.
- **Limits / trade-offs:** Ideal is 1; cooling overhead is what pushes it above 1. PUE says nothing about how efficiently the IT equipment itself uses power, and it is a ratio rather than a load-dependent curve (inferred).
- **Situation cues:** "how much power goes to cooling versus computing", "compare datacenter efficiency", "what is the best possible PUE".
- **Past-paper Qs:** 25S1 Q9

### L04-C17 Energy-proportional systems
- **Slides:** 27
- **Type:** Application
- **What it is:** **Energy efficiency is not a linear function of load — an idle system uses 50% power.** An **energy proportional system consumes almost no power when idle, very little power under light load, and gradually more power as the load increases**.
- **Look-alikes:** Energy proportionality vs PUE — proportionality is about the curve as load changes, PUE is a single overhead ratio (inferred); "idle at 50%" vs "almost no power when idle" — the gap between today's systems and the energy-proportional ideal.
- **Limits / trade-offs:** Real systems idle at **50% power**, so low utilisation is expensive; energy proportionality is described as the target, not the norm (inferred).
- **Situation cues:** "servers sit idle but still draw half their power", "efficiency at light load", "power should track utilisation".
- **Past-paper Qs:** none

### L04-C18 Datacenter tiers
- **Slides:** 28
- **Type:** Application
- **What it is:** A **ranking system to indicate the reliability of a datacenter**. **Tier 1:** **single path for power distribution, UPS, and cooling distribution, no redundant components** — **99.671%** uptime. **Tier 2:** **partial redundancy for power and cooling** — **99.741%**. **Tier 3:** **multiple paths for power and cooling, and each path with redundant components, concurrently maintainable** — **99.982%**. **Tier 4:** **redundancy for every component** — **99.995%**. **Availability & cost: Tier 1 < Tier 2 < Tier 3 < Tier 4**; **Tier 3 is typically industry standard**, **Tier 4 might be overkill**.
- **Look-alikes:** Tier 3 vs Tier 4 — Tier 3 has multiple paths each with redundant components and is concurrently maintainable, Tier 4 adds redundancy for every component; tier ranking vs uptime percentage — the tier is the label, the percentage is the expected uptime behind it; redundancy vs multiple paths — Tier 1 has neither, Tier 2 partial redundancy, Tier 3 both paths and redundant components.
- **Limits / trade-offs:** Cost rises with tier while availability rises with it; Tier 4 **might be overkill**, and Tier 3 is the typical industry choice.
- **Situation cues:** "we must maintain the datacenter without downtime", "how many nines do we need", "is Tier 4 worth the cost", "single path for power and cooling".
- **Past-paper Qs:** none

---

## Coverage

| Slide | Card(s) |
|---|---|
| 3 | L04-C01 |
| 4 | L04-C02 |
| 5 | L04-C03 |
| 6 | L04-C04 |
| 7 | L04-C05 |
| 8 | L04-C06 |
| 9 | L04-C06 |
| 10 | L04-C07, L04-C08 |
| 11 | L04-C07 |
| 12 | L04-C07 |
| 13 | L04-C08 |
| 14 | L04-C08 |
| 15 | L04-C08 (spec text) |
| 16 | L04-C09 |
| 17 | L04-C09 (diagram only, no text) |
| 18 | L04-C10 |
| 19 | L04-C11 |
| 20 | L04-C12 |
| 21 | L04-C13 |
| 22 | L04-C14 |
| 23 | L04-C15 |
| 24 | L04-C15 |
| 25 | L04-C16 |
| 26 | L04-C16 |
| 27 | L04-C17 |
| 28 | L04-C18 |

