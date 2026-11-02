# L01 — Principles of Cloud Computing ✅

Tags: **(slides)** = stated on an L01 slide (slide number given). **(beyond slides)** = reasonable explanation or a past-paper-key point, not on an L01 slide. Slides 1-16 are course admin. Your answers and grades for every scenario are in `L01-log.md`.

## Scenario Plan

| # | Topic | Status |
|---|-------|--------|
| O1 | Reduced investment risk & CapEx vs OpEx | ✅ |
| O2 | Horizontal vs. vertical scaling | ✅ |
| O3 | Trust boundaries & shared infrastructure | ✅ |
| O4 | Data residency & region selection | ✅ |
| O5 | Vendor lock-in | ✅ |
| O6 | Reduced operational governance / SLA | ✅ |
| O7 | Elasticity vs scaling | ✅ |
| O8 | Capacity planning strategies (Lead / Lag / Match) | ✅ |
| O9 | Cloud repatriation | ✅ |
| G1 | Availability and single points of failure | ✅ |
| G2 | Cloud-based IT resource vs cloud service | ✅ |
| G3 | Capacity planning challenges + full cost picture | ✅ |
| G4 | Diagnosing slow performance (latency vs bandwidth) | ✅ |
| G5 | Technical vs non-technical challenges | ✅ |
| G6 | Trust-boundary direction + shared security responsibility | ✅ |
| G7 | Privacy, legal disclosure, multi-regional compliance | ✅ |

Not yet tested (short notes at the end): concentration/outage risk, organisational agility, program = service / platform = datacenter. An async/FaaS scenario was also run but belongs to L06 (see `L01-log.md`, G8).

---

## Detailed Notes

### Concept 1: Cost Model & Reduced Investment Risk

**Core idea:** On-premise has a large fixed up-front cost plus operational costs; cloud has only variable operational costs starting from zero (s31). Cloud "typically offers cost efficiency at scale" (s30) and improves the match between elastic demand and elastic supply (s22).

| | On-Premise | Cloud |
|--|--|--|
| Cost shape (s31) | Large fixed block (capital equipment) + variable operational costs | Variable operational costs only, from zero |
| Capacity risk | Must commit before knowing demand | Scale on demand (beyond slides: defers the commitment) |
| Failure risk | Money already spent on hardware | Costs stop when usage stops (beyond slides) |
| Agility (s32) | Up-front investment and ownership costs "may be prohibitive" | Elastic resources respond to business cycles beyond what was planned |

- "CapEx / OpEx" are the conventional labels; the slides say "up-front investment costs" and "operational costs".
- "Cloud is cheaper over 3+ years" or "on-premise wins at stable load" is **beyond the slides**.
- **Existing on-premise investment is not ignored in the course's answer key.** 2526-S2 Q8: a company already invested in on-premise and would face substantial integration costs to migrate. Correct answer: *cloud adoption may be less attractive due to high migration and integration costs*.

> [!WARNING]
> **Mistake:** arguing cloud suits a startup only because "we might fail before the hardware pays for itself". That is one of three reasons. The other two: capacity-planning risk (on-premise buys hardware before demand is known, so you over- or under-buy) and agility (hours to provision instead of weeks).

> [!CAUTION]
> **Exam Trap (MCQ):** "Cloud is always cheaper because it reduces upfront capital expenditure" is wrong (2526-S2 Q8 option a).

> [!CAUTION]
> **Exam Trap (MCQ):** "Past investments should not be considered when evaluating future decisions" is wrong in this course's key (2526-S2 Q8 option d), even though textbook economics says to ignore sunk costs.

**Key one-liner:** Cloud turns a fixed up-front block into pay-for-use cost and defers capacity commitment, but migration and integration costs can still tip the decision.

---

### Concept 2: Scaling — Horizontal vs. Vertical

**Core idea:** Two ways to handle more (or less) demand (s35).

| | Vertical (scale up/down) | Horizontal (scale out/in) |
|--|--|--|
| What it does (s36-37) | Replace the resource with a higher/lower capacity one, or add resources to a single node | Add (or remove) more of the same resource type |
| Cost (s38) | More expensive (specialised hardware) | Less expensive (commodity hardware) |
| Availability of new capacity (s38) | Normally instantly available | Instantly available |
| Setup (s38) | May need additional setup | Resource replication and automated scaling |
| Ceiling (s38) | Limited by maximum hardware capacity | Not limited by hardware capacity |
| Single point of failure (beyond slides) | Yes: one machine | No: loss of one node does not take everything down |

- "Availability" in the s38 table means how quickly the new capacity appears, **not** system uptime.

> [!WARNING]
> **Mistake:** treating a bigger server as the fix for both capacity and reliability. A bigger single machine adds capacity only, and has a hard ceiling. It is still one machine, so if its host fails the whole service is down. Availability comes from redundancy (more machines, or failover).

**Key one-liner:** Horizontal scaling adds commodity nodes with no hardware ceiling and removes the single point of failure; vertical scaling is bounded by the biggest machine and stays a single point of failure.

---

### Concept 3: Trust Boundaries & Cloud Security (s42-44)

**Core idea:** Using the cloud widens your security exposure in two different ways. Responsibility for data security becomes **shared** with the provider (s42).

- **Trust boundary:** the boundary around the IT resources you trust and control. (s27 lists the term; s43-44 draw it. The one-line definition is beyond slides.)
- **Expanded trust boundary (s43):** when Organisation X uses a cloud service, X's trust boundary expands to X + the cloud provider. "Expansion of trust boundary introduces new vulnerabilities" (s42). The direction is one-way: the consumer's boundary extends to the provider.
- **Overlapping trust boundaries (s44):** shared IT resources across different consumers put the cloud service in the overlap of their boundaries, giving "opportunities for malicious cloud consumers to steal or damage data" (s42).
- Concrete attack routes (side channels, VM escape, shared network/storage) are **beyond slides**.
- On-premise you control who shares your hardware, so this overlap does not exist.

> [!WARNING]
> **Mistake:** picturing an outside attacker breaking in through another customer's VM. The threat from sharing is lateral: a malicious or compromised co-tenant on the same shared platform. On-premise you choose who shares your hardware; in cloud you cannot vet your neighbours.

**Key one-liner:** Moving to cloud expands your trust boundary to include the provider, overlaps it with co-tenants, and leaves data-security responsibility shared.

---

### Concept 4: Data Residency, Latency & Region Selection (s46)

- **Data localization / residency (s46):** industry or government rules on where data may be stored; "very important". Example on the slide: data belonging to Singapore citizens kept within Singapore.
- Datacenters are usually built in "affordable/convenient locations", which can conflict with these rules.
- **Latency (performance):** physical distance between region and users adds delay (s45).
- Region cost and per-region service availability are common practical factors but are **beyond L01 slides**.

> [!WARNING]
> **Mistake:** answering a region-choice question with latency and ignoring the law. For regulated data (for example patient records), residency is a legal requirement that overrides cost and performance. A cheap, fast region that breaks the rule is not an option; lead with compliance.

**Key one-liner:** Check residency law first; a cheaper or faster region that breaks it is not an option.

---

### Concept 5: Vendor Lock-In (s41)

- Listed on the slide as a non-technical challenge with no definition. Deep reliance on provider-specific services makes leaving very costly.
- Mitigations (not on the slide; 2526-S1 Q22 key): portable technologies, using multiple providers, containers such as Docker. Also standard SQL and open data formats, negotiated exit terms (beyond slides).
- Trade-off: provider-specific services are often faster to build with, so lock-in is a conscious weighing.

> [!WARNING]
> **Mistake:** treating lock-in as a buying problem ("pick the cheapest provider at the start"). It is an architecture problem: the cost of leaving comes from how deeply the system is built on one provider's own services, so the fix is portable design from day one.

**Key one-liner:** Lock-in builds silently through convenience; mitigate through portable architecture.

---

### Concept 6: Reduced Operational Governance Control (s45)

- Consumers have "different levels of IT resource governance between on-premise and cloud".
- An unreliable provider "may not maintain/meet SLA guarantees".
- Distance between provider and consumer adds latency and bandwidth constraints.
- Your lever is the contract. What a strong SLA contains (measurable metrics, remedies, audit rights) is **beyond slides**.

> [!WARNING]
> **Mistake:** assuming a provider that meets its SLA poses no risk. If the SLA was weak (only a loose uptime figure, no performance metrics, no remedies), the provider can let performance degrade while staying within the contract. The failure is in the contract you signed.

**Key one-liner:** In cloud your contract is your governance.

---

### Concept 7: Elasticity vs. Scaling (s35, s17, s22)

- **Scaling (s35):** the ability of an IT resource to handle increased or decreased usage demands. May be manual.
- **Elastic resource:** a key term (s27) that L01 never defines; slide summaries say "on-demand service + elastic resource".
- **Elasticity** (defined in L02 as NIST "rapid elasticity"; consistent with NIST wording "rapidly provisioned and released"): automatic, on-demand resizing that follows demand, releasing resources when not needed.
- Pre-provisioning a fixed pool is scaling, not elasticity (beyond slides).

> [!WARNING]
> **Mistake:** treating scaling and elasticity as the same thing, or calling elasticity a property of the demand. Scaling is the ability to resize and may be manual. Elasticity is resizing that is automatic and follows demand. A fixed pool of servers is scaled, not elastic.

**Key one-liner:** Elasticity is scaling that is automatic and tracks actual demand.

---

### Concept 8: Capacity Planning (s29)

**Capacity planning** = process of determining and fulfilling future demands for IT resources, products and services. Challenges: usage/demand fluctuations, peak usage, cost of resource provisioning. It should ideally avoid **under-provisioning** and **over-provisioning**.

| Strategy | Definition (s29) | Failure mode (beyond slides) |
|----------|-----------------|-----------------------------|
| **Lead** | Add capacity in anticipation of demand | Over-provisioning if demand does not arrive |
| **Lag** | Add capacity **when resources reach full capacity** (not whenever demand changes) | Under-provisioning at the ceiling |
| **Match** | Add capacity in small increments as demand increases | Needs close tracking; steps may trail a sharp spike |

- Business meaning: **under** = site slow or down, lost sales; **over** = paying for capacity that sits idle.
- A long provisioning time (for example 8 weeks for servers) rules out a reactive strategy for a short peak: the decision has to be made ahead of time.

> [!WARNING]
> **Mistake:** naming only the outage when asked what bad capacity planning risks. There are two: too little capacity (outage, lost sales) and too much (paying for idle capacity). A full answer names both.

**Key one-liner:** Lead anticipates, Lag waits until full, Match adds in small steps; the aim is to avoid under- and over-provisioning.

---

### Concept 9: Cloud Repatriation (s47)

- **Repatriation (s47):** a "Note of Caution" slide linking an article on companies bringing data in-house. The slide gives no reasons. It is a real trend.
- Whether to move back depends on (beyond slides): how stable and predictable the workload is, the cost of moving large data back (s40: "moving large data is still expensive"), how deeply the system is built on the provider's services (lock-in), and whether on-premise can match the cloud-grade availability and SLA promised to customers.
- Savings are plausible for stable, predictable workloads; variable demand loses the benefit of elasticity.
- A good answer gives a verdict, not only a list of factors.

**Key one-liner:** Repatriation can pay off for stable workloads, but variable demand, the cost of moving data back, lock-in and SLA continuity can outweigh the saving.

---

### Concept 10: Availability and Single Points of Failure (s23)

- The slide lists the benefit as "Improves availability and elasticity" and "Reduces cost", then "However . . ." (provider outages, s24).
- Availability is lost when the service depends on one component. A single server on a single physical host is a **single point of failure**: when the host fails, the service is down however big the server is.
- Keeping the service up (beyond slides): run more than one server on different physical hosts with traffic routed between them, and/or automatic failover or replacement.
- Elasticity is a different benefit. A host failure is an availability problem, not an elasticity problem.

**Key one-liner:** Availability needs redundancy; one server, however large, is a single point of failure.

---

### Concept 11: Cloud-Based IT Resource vs Cloud Service (s34, s39)

- **Cloud-based IT resource (s34):** any IT resource hosted inside the cloud environment (virtual servers, storage devices, services, software). The cloud symbol marks the boundary.
- **Cloud service (s39):** "any IT resource made remotely accessible via a cloud". It is the subset that is **offered** for consumers to use.
- Every cloud service is a cloud-based IT resource; not every cloud-based IT resource is a cloud service (for example a provider-internal log server, or storage used only behind an application).

> [!WARNING]
> **Mistake:** calling everything inside the cloud boundary a cloud service because it is reachable over a network. A cloud service is a resource that has been made accessible to consumers. Internal supporting resources are cloud-based IT resources only.

**Key one-liner:** In the cloud means cloud-based IT resource; offered to consumers over the network means cloud service.

---

### Concept 12: The Full Cost Picture (s30-31)

- **On-premise costs (s30):** up-front investment, plus operational costs: technical staff, utility bills (power and cooling), security and access control, admin/licences. "Difficult to directly align IT costs and business performance."
- **Cloud:** "cost efficiency at scale" (s30). Why per-unit cost can be lower: the provider spreads purchase and running costs across many customers (economies of scale; beyond slides).
- A comparison that counts only the hardware already bought is incomplete: it omits running costs and ignores capacity fit (hardware sized for normal load cannot carry a 5x peak).
- See Concept 1 for how the course key treats prior on-premise investment.

**Key one-liner:** On-premise has hidden running costs and a fixed capacity; cloud spreads those costs across customers and tracks demand.

---

### Concept 13: Latency vs Bandwidth (s45; detail in L04)

- **Latency:** delay for data to travel between user and service; grows with physical distance. Symptom: every small action is slow even when the server is idle.
- **Bandwidth:** how much data the link can carry per second. Symptom: large transfers take very long. Example: 4 TB over 100 Mbps takes about 3.7 days.
- Fixes: latency → move the service (and its database) closer to users. Bandwidth → bigger or dedicated link, send only new/changed data, compress, ship bulk data physically.
- Low CPU and memory use means compute is not the bottleneck, so extra servers will not help.

> [!WARNING]
> **Mistake:** adding or parallelising servers to fix a slow transfer. If the office link carries 100 Mbps, ten extra cloud servers still receive data at 100 Mbps. Identify whether the limit is distance (latency), the link (bandwidth) or compute before choosing a fix.

**Key one-liner:** Slow small actions over distance = latency; slow bulk transfer = bandwidth; neither is fixed by adding servers.

---

### Concept 14: Technical vs Non-Technical Challenges (s40, s41)

| Technical (s40) | Non-technical (s41) |
|---|---|
| Software development: different platforms/services across providers (**application compatibility**) | Increased security vulnerabilities |
| Tools continuously evolving | Reduced operational governance control |
| Moving large data is still expensive | Privacy/legal issues: data localization, multi-regional compliances |
| Security | Vendor lock-in |
| Internet dependence | Service level agreement |
| Quality of service | |
| Energy costs | |

- Both lists end with "…" (non-exhaustive). **Security** appears in both lists.
- Quick test: if the fix is a design or engineering change → technical. If the fix is a contract, law or policy → non-technical.
- Examples: legacy app tied to specific OS/hardware → technical (compatibility). Branch loses Internet and cannot reach the system → technical (Internet dependence). Regulator requires in-country data → non-technical. Provider guarantees only 99.5% uptime, no audit rights → non-technical (SLA / governance), even though "quality of service" is on the technical list.

---

### Concept 15: Privacy, Legal Disclosure and Multi-Regional Compliance (s41, s46)

- **Residency (where data sits)** and **disclosure (when it must be handed over)** are separate legal issues. Storing data in the required country settles residency only; "legal issues on accessibility and disclosure of data" mean the data may still have to be disclosed to authorities as laws require (s46).
- Privacy has a tension between personal rights and society, for example location and proximity data (s46).
- **Multi-regional compliance (s41):** each country has its own storage, privacy and disclosure laws. Data copied to several countries falls under each country's laws, so satisfying the home-country rule does not cover the other copies.

> [!WARNING]
> **Mistake:** answering "how secure the cloud is" when asked for the legal challenge of storing data in several countries. Security and legal compliance are separate items. The legal challenge is multi-regional compliance: each country's own laws apply to its copy.

**Key one-liner:** Residency is not disclosure, and every extra region brings its own laws.

---

## Reference only (not tested)

- **Definitions (s17):** Gartner 2025: "a style of computing in which scalable and elastic IT-enabled capabilities are delivered as a service using Internet technologies." NIST 2011: "a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources … rapidly provisioned and released with minimal management effort or service provider interaction." Slide summary: on-demand service + elastic resource.
- **Six defining attributes (s19):** on-demand self service, broad network access, resource pooling, rapid elasticity, measured service, resiliency. NIST's five omit resiliency.
- **Infrastructure (s19):** datacenters, virtualization, multi-tenancy. **Service models:** SaaS, PaaS, IaaS (detail in L02). **Deployment models:** public, private, hybrid, community (L02).
- **Enabling technologies (s26):** parallel and distributed computing, programming models, utility computing, virtualization, web technologies, storage and network technologies, Internet.
- **History (s20-21):** 1961 McCarthy (computing as a utility); 1996 "cloud computing" coined at Compaq; 1999 Salesforce.com; Jul 2002 AWS; May 2006 S3; Aug 2006 EC2; Apr 2008 Google App Engine; Nov 2009 Windows Azure; 2011 onwards many providers. Order traps: S3 before EC2; Salesforce before AWS.
- **Resource symbols (s34):** physical server, virtual server, software program, service, storage device, network device. Example cloud: 3 virtual servers + 2 cloud services + 3 storage devices = 8 cloud-based IT resources.

## Not yet tested (short notes)

- **Concentration / outage risk (s24):** AWS outage (21 Oct 2025) and Cloudflare outage (18 Nov 2025) show that reliance on a few providers lets one failure spread widely. The cost side of the availability and cost benefits.
- **Organisational agility (s32):** a measure of responsiveness to change. Cloud: elastic resources respond to business cycles beyond what was planned; fixes and updates applied once at the datacenter instead of on millions of clients; faster access to new hardware.
- **Program = Internet (cloud) service, platform = datacenters (s18):** a two-layer model.
- **Innovation (s22):** cloud platforms enable current and future innovation, with the next wave around AI and IoT.
