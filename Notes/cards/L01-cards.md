# L01 Concept Cards

Built by DeepSeek V4.1 Flash from the slide text plus diagram facts (transcribed by Claude Haiku, spot-checked against the slide images). Cards are the source for writing scenarios. 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide. Slides 1-16 are course admin. The last list is claims in L01-Principles.md not supported by slides: label them 'beyond slides' or fix them (sunk-cost line is WRONG, see 2526-S2 Q8).

### L01-C01 Cloud computing definitions (Gartner 2025 vs NIST 2011)
- **Slides:** 17
- **Type:** Application
- **What it is:** Gartner: "a style of computing in which scalable and elastic IT-enabled capabilities are delivered as a service using Internet technologies." NIST 2011: "a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources … rapidly provisioned and released with minimal management effort or service provider interaction." Slide's own summary of both: "on-demand service + elastic resource".
- **Look-alikes:** Scalability vs elasticity — Gartner says "scalable and elastic", NIST says "rapidly provisioned and released"; they are not the same property (inferred). Utility computing — one of the enabling technologies (slide 26), not a definition of cloud (inferred). NIST's five essential characteristics (L02) — the definition paragraph does not enumerate them.
- **Limits / trade-offs:** Neither quote mentions cost savings; "reduces cost" is a separate claim on slides 22-23/30.
- **Situation cues:** "delivered as a service using Internet technologies"; "shared pool of configurable resources"; "provisioned and released with minimal provider interaction"; "which definition does this wording come from".
- **Past-paper Qs:** 24S2 Q2
- **Already tested:** 7

### L01-C02 Program = cloud service, platform = datacenters
- **Slides:** 18
- **Type:** Application
- **What it is:** The two-layer mental model: "Program is an Internet (cloud) service" and "platform are datacenters" ("service" and "platform" highlighted).
- **Look-alikes:** SaaS (program consumed as a service) vs IaaS/PaaS (the platform capability the datacenter provides) — the slide does not name them (inferred). "Cloud service" (s39: any IT resource made remotely accessible) vs "datacenter" (the physical facility, s19 infrastructure item).
- **Limits / trade-offs:** None stated; it is a one-line model with no cost/risk discussion.
- **Situation cues:** "user only ever touches the service"; "provider owns the machines behind it"; "classify each item as service or datacenter".
- **Past-paper Qs:** none
- **Already tested:** no

### L01-C03 Defining attributes of cloud (six)
- **Slides:** 19
- **Type:** Application
- **What it is:** The slide lists six: 1 on-demand self service, 2 broad network access, 3 resource pooling, 4 rapid elasticity, 5 measured service, 6 resiliency.
- **Look-alikes:** NIST's five essential characteristics — the slide's six include resiliency, which NIST's list omits (inferred; L02). Measured service vs pay-as-you-go/pay-per-use pricing (L10) — metering vs billing model (inferred). Resource pooling (attribute) vs multi-tenancy (s19 infrastructure item) — slides list both without distinguishing (inferred).
- **Limits / trade-offs:** Slide gives the names only, no definitions or disadvantages.
- **Situation cues:** "no human interaction to get a resource"; "reachable from anywhere over the network"; "many customers share one pool"; "usage is metered"; "keeps working when a component fails".
- **Past-paper Qs:** 24S2 Q2
- **Already tested:** 7 (definitions only)

### L01-C04 Cloud infrastructure: datacenters, virtualization, multi-tenancy
- **Slides:** 19
- **Type:** Application
- **What it is:** The slide's INFRASTRUCTURE list: 1 datacenters, 2 virtualization, 3 multi-tenancy.
- **Look-alikes:** Enabling technologies (s26) — a longer academic list (parallel/distributed computing, programming models, utility computing, virtualization, web technologies, storage/network technologies, Internet); only virtualization overlaps. Multi-tenancy vs resource pooling — mechanism vs defining attribute (inferred). Virtualization vs multi-tenancy — partitioning one machine vs serving many customers (L05, inferred).
- **Limits / trade-offs:** Multi-tenancy is also the stated source of overlapping trust boundaries and malicious co-tenants (s42, s44).
- **Situation cues:** "same physical host serves several customers"; "hypervisor splits one server"; "provider's building full of machines".
- **Past-paper Qs:** 24S2 Q12, 25S1 Q6
- **Already tested:** no (3 touches sharing only)

### L01-C05 Cloud resources and the cloud boundary (symbols)
- **Slides:** 34
- **Type:** Application
- **What it is:** Legend: physical server, virtual server, software program, service, storage device, network device; "PaaS, SaaS" group = software program + service. A cloud symbol marks the boundary of a cloud environment. Example: a cloud hosting 8 IT resources = 3 virtual servers, 2 cloud services, 3 storage devices; these are "cloud-based IT resources".
- **Look-alikes:** Cloud-based IT resource vs cloud service — a cloud service is one such resource made remotely accessible, so a resource inside the boundary need not be a cloud service. Physical vs virtual server symbols — a virtual server sits on a physical host (s36).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "count the resources inside the cloud boundary"; "which item is drawn outside the cloud"; "label the diagram"; "is this device a cloud-based IT resource".
- **Past-paper Qs:** none
- **Already tested:** no

### L01-C06 Service models: SaaS, PaaS, IaaS
- **Slides:** 19, 39
- **Type:** Application
- **What it is:** Slide 19 names the service models SaaS, PaaS, IaaS. Slide 39: "Multitude of service usage models – next lecture: IaaS, PaaS, SaaS."
- **Look-alikes:** Deployment models (public/private/hybrid/community, s19) — who may use the cloud vs how much of the stack the provider manages (inferred). SaaS vs on-premise licensed software; PaaS vs IaaS — detail is L02, not L01.
- **Limits / trade-offs:** L01 gives no definitions or trade-offs; all detail is deferred to L02.
- **Situation cues:** "uses the application, manages nothing"; "deploys code to a managed runtime"; "rents virtual machines"; "which service model".
- **Past-paper Qs:** 24S2 Q1, 24S2 Q7, 24S2 Q3, 25S2 Q9
- **Already tested:** no

### L01-C07 Cloud deployment models
- **Slides:** 19
- **Type:** Reference-only
- **What it is:** The slide lists "cloud deployment models" as a category; names are given in L02 (public, private, hybrid, community).
- **Look-alikes:** Service models (SaaS/PaaS/IaaS) — deployment = exclusivity/ownership, service = managed layer (inferred). Hybrid vs multi-cloud — mixing on-prem with cloud vs using several providers (inferred, L02).
- **Limits / trade-offs:** Not discussed on this slide.
- **Situation cues:** "only our staff may use it"; "mix of own datacenter and public cloud"; "shared by several agencies with common requirements".
- **Past-paper Qs:** 24S2 Q25, 25S1 Q12
- **Already tested:** no

### L01-C08 Cloud history milestones 1961-2011
- **Slides:** 20, 21
- **Type:** Reference-only
- **What it is:** 1961 McCarthy: computing as a public utility. 1996 "cloud computing" coined at Compaq (MIT Technology Review). 1999 Salesforce.com delivers enterprise applications via a website. Jul 2002 AWS suite (computation, storage, Amazon Mechanical Turk). May 2006 S3 pay-per-use storage. Aug 2006 EC2, commercial IaaS, rent computers to run own applications. Apr 2008 Google App Engine (PaaS), Bigtable, GFS, MapReduce. Nov 2009 Windows Azure, manages large pools, handles spikes in demand. 2011 onwards: many providers.
- **Look-alikes:** Order traps: S3 (May 2006) precedes EC2 (Aug 2006); Salesforce 1999 (SaaS pioneer) precedes AWS 2002; "cloud computing" coined 1996 at Compaq, not by Amazon or Google. Azure is described as an "operating environment" here, not a service model name.
- **Limits / trade-offs:** None stated.
- **Situation cues:** "which came first"; "who coined the term"; "match the year to the milestone"; "which event was IaaS".
- **Past-paper Qs:** none
- **Already tested:** no

### L01-C09 Why cloud: innovation and matching elastic demand to elastic supply
- **Slides:** 22
- **Type:** Application
- **What it is:** Technology (cloud-enabled platforms and services) for current/future innovations and disruptions; next wave delivers advanced capability around AI and IoT; reduces business cost by "improves match between elastic resource demand and elastic computing resource".
- **Look-alikes:** Organisational agility (s32) — responsiveness to change vs raw cost. Cost reduction (s30) — the mechanism here is matching supply to demand, not a lower unit price. Elasticity (s35) — the property that makes the match possible.
- **Limits / trade-offs:** "Reduces business cost" is qualified on s30 as "cost efficiency at scale"; s24 shows the availability downside.
- **Situation cues:** "demand swings through the year"; "AI/IoT workload"; "stop paying for capacity that sits idle"; "match spend to actual usage".
- **Past-paper Qs:** 24S2 Q4
- **Already tested:** 1

### L01-C10 Benefits: improves availability and elasticity, reduces cost
- **Slides:** 23
- **Type:** Application
- **What it is:** The slide's benefit list: "Improves availability and elasticity", "Reduces cost", followed by "However . . ." leading into the outage slides.
- **Look-alikes:** Availability vs resiliency (attribute 6, s19) — slides use both without defining either (inferred). Elasticity vs scaling (s35) — scaling is the ability to change capacity, elasticity the on-demand property (inferred). "Reduces cost" vs s30's "cost efficiency at scale".
- **Limits / trade-offs:** The slide itself signals a caveat ("However . . .") resolved on s24: provider outages and concentration risk.
- **Situation cues:** "keeps serving through a node failure"; "capacity follows the peak and the trough"; "cheaper than owning hardware".
- **Past-paper Qs:** 25S1 Q15, 24S2 Q22
- **Already tested:** 7, 2 (partly)

### L01-C11 Concentration and outage risk
- **Slides:** 24
- **Type:** Application
- **What it is:** Two BBC screenshots of cloud outages: an AWS outage (21 Oct 2025) that "made the internet fall apart", and a Cloudflare outage (18 Nov 2025) that took down X and ChatGPT. Point: reliance on a few providers means one failure spreads widely.
- **Look-alikes:** Technical challenge "Internet dependence" (s40) — dependence on the public Internet vs dependence on one provider's platform. Reduced operational governance (s45) — provider reliability and SLA recourse. Availability as a benefit (s23) — the same property, opposite direction.
- **Limits / trade-offs:** The slide states no mitigation; concentration is the cost of the availability/cost benefits.
- **Situation cues:** "one provider outage broke many unrelated services"; "third-party dependency widens the blast radius"; "single-provider concentration".
- **Past-paper Qs:** none
- **Already tested:** 9 (internet dependence only)

### L01-C12 Enabling technologies ("under the hood")
- **Slides:** 26
- **Type:** Reference-only
- **What it is:** "To help deliver computing as-a-service": parallel and distributed computing, programming models, utility computing, virtualization, web technologies, storage and network technologies, Internet.
- **Look-alikes:** Cloud infrastructure (s19: datacenters, virtualization, multi-tenancy) — what the cloud is built from vs the technologies that enable delivery as-a-service (inferred). Utility computing vs cloud computing — utility is one listed enabler, not a synonym (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "which is an enabling technology, not a service model"; "list-matching"; "what sits under the hood".
- **Past-paper Qs:** none
- **Already tested:** no

### L01-C13 Elastic resource
- **Slides:** 17, 22, 27
- **Type:** Application
- **What it is:** Listed as key term 1 ("Elastic resource"); used in the slide summaries "on-demand service + elastic resource" and "match between elastic resource demand and elastic computing resource". The slide never defines it.
- **Look-alikes:** Scaling (s35) — the ability of an IT resource to handle increased or decreased usage demands, which can be manual. Elasticity — automatic provisioning/release (inferred; not defined on L01 slides). Availability — staying up vs resizing (inferred).
- **Limits / trade-offs:** No definition or drawback on the slide — flag this when a question assumes a definition.
- **Situation cues:** "grows with demand and shrinks back"; "released as soon as the peak passes"; "pay only while it exists"; "capacity follows load automatically".
- **Past-paper Qs:** 25S1 Q17, 25S1 Q15
- **Already tested:** 7

### L01-C14 Availability
- **Slides:** 23, 27
- **Type:** Application
- **What it is:** Listed as key term 2; the only substantive claim is "Improves availability and elasticity" (s23). No definition or measurement on the slide.
- **Look-alikes:** Resiliency (attribute 6, s19) — surviving failure vs being reachable (inferred). Elasticity — resizing vs staying up (inferred). Uptime percentage in an SLA (s45) — a contract metric, not the slide's term (inferred).
- **Limits / trade-offs:** Slide gives no availability target; s24 shows provider outages can remove it.
- **Situation cues:** "service stays usable while a component fails"; "uptime"; "continues through a zone failure".
- **Past-paper Qs:** 24S2 Q22, 25S2 Q15
- **Already tested:** no

### L01-C15 Capacity planning: definition and challenges
- **Slides:** 29
- **Type:** Application
- **What it is:** "Process of determining and fulfilling future demands of an organisation's IT resources, products and services." Challenges: usage/demand fluctuations, peak usage, cost of resource provisioning. Parenthetically equated with "resource provisioning".
- **Look-alikes:** Scaling (s35) — reacting to current demand vs planning future demand. Elasticity — automatic response, i.e. not planning at all (inferred). Over/under-provisioning — the two failure outcomes of planning (s29).
- **Limits / trade-offs:** "Should ideally avoid under-provisioning and over-provisioning"; cost of provisioning is itself a challenge.
- **Situation cues:** "forecast next quarter's load"; "size the estate before launch"; "peak season is 5x normal"; "how much capacity to commit to".
- **Past-paper Qs:** none
- **Already tested:** 8, 1 (capacity risk)

### L01-C16 Lead strategy
- **Slides:** 29
- **Type:** Application
- **What it is:** "Add capacity in anticipation of demand."
- **Look-alikes:** Match strategy — adds in small increments as demand increases (follows actual demand); lead acts on a forecast. Lag strategy — adds only when resources are already at full capacity.
- **Limits / trade-offs:** Pays for capacity before it is needed; over-provisioning if demand does not materialise (the slide only says over-provisioning should be avoided).
- **Situation cues:** "buy ahead of the festive peak"; "capacity ready before launch day"; "based on a demand forecast".
- **Past-paper Qs:** none
- **Already tested:** 8

### L01-C17 Lag strategy
- **Slides:** 29
- **Type:** Application
- **What it is:** "Add capacity when resources reach its full capacity."
- **Look-alikes:** Match strategy — also reactive but adds in small increments as demand rises, before the ceiling. Lead strategy — proactive.
- **Limits / trade-offs:** Capacity is added only after the resource is saturated, so demand is unmet at the ceiling (inferred from the definition).
- **Situation cues:** "add servers only after CPU hits 100%"; "react once the queue is full"; "no capacity added until saturation".
- **Past-paper Qs:** none
- **Already tested:** 8

### L01-C18 Match strategy
- **Slides:** 29
- **Type:** Application
- **What it is:** "Add capacity in small increments as demand increases."
- **Look-alikes:** Lead — one large commitment ahead of demand; match tracks demand in steps. Lag — waits for full capacity; match does not.
- **Limits / trade-offs:** Requires many incremental additions and continuous tracking; reacts step-by-step rather than ahead of a spike (inferred).
- **Situation cues:** "add one node for every 10% growth"; "closely track demand and top up"; "capacity grows in small steps".
- **Past-paper Qs:** none
- **Already tested:** 8

### L01-C19 Under-provisioning vs over-provisioning
- **Slides:** 29
- **Type:** Application
- **What it is:** Capacity planning "should ideally avoid under-provisioning and over-provisioning"; the slide names both but defines neither.
- **Look-alikes:** Lead strategy failure mode = over-provisioning (capacity bought, demand absent); lag strategy failure mode = under-provisioning at the ceiling. Measured service / pay-per-use (s19, L10) — paying for what is used, the opposite of idle over-provisioning.
- **Limits / trade-offs:** Over-provisioning wastes spend on idle resources; under-provisioning leaves demand unmet (inferred — the slide only says to avoid both).
- **Situation cues:** "paying for servers nobody uses"; "requests queue at peak"; "right-sizing the estate"; "capacity sits at 15% utilisation".
- **Past-paper Qs:** 25S1 Q24
- **Already tested:** 8, 1

### L01-C20 On-premise cost structure and cost reduction
- **Slides:** 30
- **Type:** Application
- **What it is:** "Difficult to directly align IT costs and business performance." On-premise: the IT department is a big cost — up-front investment costs, plus operational costs: technical staff (manpower), utility bills (power and cooling), security and access control to protect infrastructure, admin/account cost (software licences, etc.). "Cloud computing typically offers cost efficiency at scale."
- **Look-alikes:** Cost model graph (s31) — the same split drawn as fixed vs variable curves. CapEx/OpEx (inferred labels; slides say "up-front investment costs" and "operational costs"). TCO comparisons (L10) — adds migration, integration, egress (inferred).
- **Limits / trade-offs:** "Typically … at scale" — no guarantee, and small workloads may not benefit (inferred). Cost-to-business-performance alignment is hard either way.
- **Situation cues:** "budget includes cooling, security staff and licences"; "finance wants IT cost tied to revenue"; "small pilot — is cloud actually cheaper?"; "which on-prem cost is usually forgotten".
- **Past-paper Qs:** 24S2 Q4
- **Already tested:** 1

### L01-C21 Cost model: fixed + variable vs variable only
- **Slides:** 31
- **Type:** Application
- **What it is:** Cost model (Hwang p199): x = number of users, y = costs. (a) Traditional on-premise IT: a large block of fixed costs in capital equipment at the base, with variable operational costs growing above it. (b) Cloud: only variable operational costs, starting from zero, no fixed block.
- **Look-alikes:** s30's prose cost list — same idea, no graph. "Cloud is always cheaper" — the graph shows two lines, so a low-user and a high-user regime differ (inferred, not stated on the slide). Reserved/committed pricing (L10) reintroduces a fixed commitment into the cloud line (inferred).
- **Limits / trade-offs:** No numbers or break-even point printed; excludes migration, egress and integration costs (inferred).
- **Situation cues:** "no upfront hardware purchase"; "cost per user at low volume"; "when does owning become cheaper"; "fixed base cost vs pay-per-use".
- **Past-paper Qs:** 24S2 Q4, 25S2 Q8
- **Already tested:** 1

### L01-C22 Organisational agility
- **Slides:** 32
- **Type:** Application
- **What it is:** "A measure of an organisation's responsiveness to change." On-premise: up-front investment and infrastructure ownership costs "may be prohibitive". Cloud: elastic IT resources respond to business cycles beyond what was previously predicted or planned; software fixes/updates — update datacenters vs millions of clients; the datacenter allows faster introduction of new hardware innovations.
- **Look-alikes:** Elasticity (s35) — a technical property; agility is the business responsiveness it enables (inferred). Cost reduction (s30) — cheaper vs faster to change.
- **Limits / trade-offs:** On-premise blockers are cost and ownership ("may be prohibitive"); cloud agility depends on the provider's update and hardware cadence.
- **Situation cues:** "match a competitor's launch within days"; "patch all users at once"; "business cycle beyond the plan"; "faster access to new hardware".
- **Past-paper Qs:** none
- **Already tested:** 1 (mentions agility)

### L01-C23 Cloud-based IT resources (inventory)
- **Slides:** 34
- **Type:** Application
- **What it is:** IT resources hosted inside a cloud environment — the worked example has 8 resources: 3 virtual servers, 2 cloud services, 3 storage devices. The cloud symbol is the boundary of the cloud environment.
- **Look-alikes:** Cloud service (s39) — one cloud-based IT resource that is made remotely accessible; not every cloud-based IT resource is a cloud service. Resources outside the boundary — on-premise equivalents (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "which of these sit inside the cloud boundary"; "count the virtual servers / services / storage"; "classify each symbol".
- **Past-paper Qs:** none
- **Already tested:** no

### L01-C24 Cloud service
- **Slides:** 39
- **Type:** Application
- **What it is:** "Any IT resource made remotely accessible via a cloud." The slide notes a multitude of service usage models — IaaS, PaaS, SaaS — covered next lecture.
- **Look-alikes:** Cloud-based IT resource (s34) — hosted in the cloud but possibly not remotely accessible. Service model (IaaS/PaaS/SaaS) — a category of usage, not the definition. Web service/API — narrower (inferred).
- **Limits / trade-offs:** The definition is deliberately broad: a VM, a storage bucket or an application all qualify once remotely accessible (inferred).
- **Situation cues:** "consumer reaches it over the network"; "made remotely accessible"; "is a rented VM a cloud service?"; "resource offered by the provider".
- **Past-paper Qs:** 24S2 Q2
- **Already tested:** no

### L01-C25 Horizontal scaling (scale out / in)
- **Slides:** 35, 36
- **Type:** Application
- **What it is:** Scaling "out or in" by adding "more of the same resource type". Diagram: pooled physical servers host virtual servers; as demand rises, Virtual Server A is scaled out by adding Virtual Servers B and C.
- **Look-alikes:** Vertical scaling — replaces the resource with a more powerful one (s37). Elasticity — automatic add/release in response to load, not just adding nodes (inferred). Load balancing — spreads requests across the added nodes (L03, inferred). Replication for redundancy — same node count, different purpose (inferred).
- **Limits / trade-offs:** s38: less expensive using commodity hardware; not limited by hardware capacity; needs "resource replication and automated scaling".
- **Situation cues:** "add three identical web servers behind a load balancer"; "distribute reads across more nodes"; "scale in by removing nodes"; "commodity boxes".
- **Past-paper Qs:** 25S1 Q17, 24S2 Q20, 25S2 Q20
- **Already tested:** 2

### L01-C26 Vertical scaling (scale up / down)
- **Slides:** 35, 37
- **Type:** Application
- **What it is:** Scaling "up or down" — "replace resource with higher or lower capacity or add resources to a single node". Diagram: Virtual Server A with 2 CPUs is scaled up by replacing it with a more powerful resource, Server B with 4 CPUs.
- **Look-alikes:** Horizontal scaling — more nodes of the same type vs one bigger node. Resizing an instance to a larger type — the same thing in L10 pricing language (inferred). Adding CPU/RAM to the same node — explicitly allowed by s35 and still vertical.
- **Limits / trade-offs:** s38: more expensive, specialised hardware; "may need additional setup"; "limited by maximum hardware capacity". Replacement implies the old server is swapped out (inferred).
- **Situation cues:** "upgrade the database server from 2 vCPU to 4 vCPU"; "move to a bigger instance type"; "single node needs more RAM"; "can't split the workload".
- **Past-paper Qs:** 25S1 Q17
- **Already tested:** 2

### L01-C27 Scaling comparison table
- **Slides:** 38
- **Type:** Application
- **What it is:** Horizontal vs vertical on four rows — Cost: less expensive with commodity hardware vs more expensive with specialised hardware. Availability: "Resources instantly available" vs "Resources normally instantly available". Ease of setup: "Resource replication and automated scaling" vs "May need additional setup". Hardware capacity: "Not limited by hardware capacity" vs "Limited by maximum hardware capacity".
- **Look-alikes:** Availability here means the new resource is instantly available, not system uptime (inferred) — do not read it as a redundancy claim. Single point of failure — not mentioned on the slide (Notes concept 2 adds it).
- **Limits / trade-offs:** Both rows concede vertical's ceiling; horizontal's setup depends on replication and automated scaling being in place.
- **Situation cues:** "which option is limited by the largest machine available"; "which needs commodity hardware"; "which needs replication and automation"; "which is only 'normally' instant".
- **Past-paper Qs:** 25S1 Q17, 24S2 Q20
- **Already tested:** 2

### L01-C28 Trust boundary and its expansion
- **Slides:** 27, 42, 43
- **Type:** Application
- **What it is:** Key term 7 is "trust boundary". Slide 43: Organisation X and Organisation Y each have their own trust boundary; when each uses the cloud service, X's trust boundary "expands" to organisation + cloud service provider. Slide 42: "Expansion of trust boundary introduces new vulnerabilities."
- **Look-alikes:** Overlapping trust boundaries (s44) — expansion adds the provider; overlap adds other consumers. Resource pooling (s19) — the performance benefit of the same sharing. Network/security-group boundary (L03) — a technical control, not the slide's term (inferred).
- **Limits / trade-offs:** New vulnerabilities; the slide does not define the boundary formally (definition inferred).
- **Situation cues:** "who must you now trust"; "provider staff and hypervisor fall inside the boundary"; "the boundary grew when we moved to cloud"; "which direction does it expand".
- **Past-paper Qs:** 24S2 Q8, 25S1 Q7
- **Already tested:** 3

### L01-C29 Overlapping trust boundaries
- **Slides:** 42, 44
- **Type:** Application
- **What it is:** The cloud service sits in the overlap of Organisation X's and Organisation Y's trust boundaries (shaded area with diagonal lines). Slide 42: shared IT resources across different cloud consumers create overlapping trust boundaries — "opportunities for malicious cloud consumers to steal or damage data".
- **Look-alikes:** Expanded trust boundary — includes the provider, not other tenants. Resource pooling / multi-tenancy — the same sharing seen as efficiency rather than exposure. Tenant isolation (L05) — the mitigation, absent from this slide (inferred).
- **Limits / trade-offs:** Exposure to malicious co-tenants; slide states no isolation guarantee or mitigation.
- **Situation cues:** "two competitors use the same provider"; "co-tenant on the same physical host"; "shared storage or network"; "shaded overlap in the diagram".
- **Past-paper Qs:** 25S1 Q14, 25S1 Q7
- **Already tested:** 3

### L01-C30 Increased security vulnerabilities (shared responsibility)
- **Slides:** 42
- **Type:** Application
- **What it is:** Responsibility over data security becomes shared with cloud providers; expansion of the trust boundary introduces new vulnerabilities; shared IT resources across consumers create overlapping trust boundaries and opportunities for malicious consumers to steal or damage data.
- **Look-alikes:** Technical challenge "Security" (s40) — a one-word list item, same topic. Non-technical challenge "Increased security vulnerabilities" (s41) — same heading repeated under a different list; do not treat them as different mechanisms. "Provider is responsible for all security" — contradicted by "shared".
- **Limits / trade-offs:** No mitigation stated; security responsibility is divided, not removed.
- **Situation cues:** "who patches what"; "shared responsibility"; "co-tenant can damage our data"; "boundary expansion adds vulnerabilities".
- **Past-paper Qs:** 25S1 Q7, 24S2 Q8
- **Already tested:** 3

### L01-C31 Technical challenges
- **Slides:** 40
- **Type:** Application
- **What it is:** Software development — different cloud platforms and services across cloud providers; tools continuously evolving; moving large data is still expensive; security; Internet dependence; quality of service; energy costs; "…" (open list).
- **Look-alikes:** Non-technical challenges (s41) — governance, legal/privacy, lock-in, SLA. Security appears in both lists (s40 item, s41 heading) — a trap. "Application compatibility" is the software-development item, not a separate challenge. Latency/bandwidth from provider distance is filed under governance (s45), not here.
- **Limits / trade-offs:** List is non-exhaustive (trailing "…"); no mitigations given.
- **Situation cues:** "app written for one provider won't run on another"; "petabyte migration is too expensive"; "ISP outage takes the app down"; "QoS / energy bill".
- **Past-paper Qs:** 24S2 Q20, 25S2 Q16, 24S2 Q24, 24S2 Q6
- **Already tested:** 9

### L01-C32 Non-technical challenges (list)
- **Slides:** 41
- **Type:** Application
- **What it is:** Increased security vulnerabilities; reduced operational governance control; privacy/legal issues — data localization, multi-regional compliances; vendor lock-in; service level agreement; "…".
- **Look-alikes:** Technical challenges (s40) — pick by "contract/legal/organisational" vs "engineering". Data localization (legal) vs vendor lock-in (commercial/technical dependency) — both non-technical but different remedies. SLA — listed as a challenge here, used as the governance lever on s45.
- **Limits / trade-offs:** Non-exhaustive; no mitigations on the slide.
- **Situation cues:** "regulator requires in-country data"; "contract renegotiation"; "can't exit the provider"; "who is accountable".
- **Past-paper Qs:** 25S2 Q23, 25S1 Q25, 25S2 Q5, 25S1 Q22
- **Already tested:** 4, 5, 6, 9 (individually)

### L01-C33 Vendor lock-in
- **Slides:** 41
- **Type:** Application
- **What it is:** Listed as a non-technical challenge: "Vendor lock-in". The slide offers no definition and no mitigation.
- **Look-alikes:** Data localization/residency (s46) — legal constraint on location vs dependency on a provider's technology. SLA (s41) — contractual commitment vs technical coupling. Application compatibility (s40) — the technical face of lock-in (inferred).
- **Limits / trade-offs:** Slide states only that it is a challenge; mitigations (portable technology, multi-cloud, exit clauses) are not on L01.
- **Situation cues:** "switching providers means a rewrite"; "proprietary APIs everywhere"; "exit cost too high"; "we are effectively tied to one vendor".
- **Past-paper Qs:** 25S1 Q22
- **Already tested:** 5

### L01-C34 Reduced operational governance control
- **Slides:** 45
- **Type:** Application
- **What it is:** For cloud consumers there are "different levels of IT resource governance between on-premise and cloud"; an unreliable cloud provider "may not maintain/meet SLA guarantees"; physical distance between provider and consumer introduces additional latency and bandwidth constraints.
- **Look-alikes:** SLA (s41) — the contract, not the loss of control. Technical challenge "quality of service" (s40) — QoS as a general challenge. Latency vs bandwidth (L04) — two separate distance effects, both named here. Provider-managed maintenance (L02) — the upside of the same handover.
- **Limits / trade-offs:** No direct control over provider infrastructure; the only levers named are the SLA and distance/placement choices (inferred).
- **Situation cues:** "provider's status page is our only visibility"; "no access to hypervisor logs"; "SLA credits are the only remedy"; "far region adds delay".
- **Past-paper Qs:** 24S2 Q13
- **Already tested:** 6

### L01-C35 Data localization / residency and privacy-legal issues
- **Slides:** 46
- **Type:** Application
- **What it is:** Datacenters are usually set up in "affordable/convenient locations". Data Localization/Residency — industry or government regulations on data privacy or storage policies ("very important"), e.g. "Data belonging to Singapore citizens to be kept within Singapore". Legal issues on accessibility and disclosure of data (laws require data to be disclosed appropriately). Tension between personal rights (privacy) and society, e.g. location and proximity data.
- **Look-alikes:** Latency (performance) vs residency (legal) — a nearby region is not automatically compliant. Multi-regional compliance (s41) — several jurisdictions at once. Sovereign cloud (L02 s47) — a delivery model built around this requirement. Cost-driven region choice (s46) — datacenters sit where it is affordable, which is exactly the conflict.
- **Limits / trade-offs:** Convenient/affordable locations conflict with legal requirements; disclosure laws may compel access to data.
- **Situation cues:** "must keep data in Singapore"; "regulator forbids offshore storage"; "government can demand disclosure"; "which region is legal".
- **Past-paper Qs:** 25S2 Q23, 25S1 Q25, 25S2 Q5
- **Already tested:** 4

### L01-C36 Cloud repatriation (note of caution)
- **Slides:** 47
- **Type:** Application
- **What it is:** A "Note of Caution" slide linking a Forbes council article titled "The rise of cloud repatriation — why companies are bringing data in-house". No text beyond the heading and link.
- **Look-alikes:** Vendor lock-in (s41) — an exit barrier, one reason repatriation is hard (inferred). Cost model (s31) — the fixed-cost argument for owning again (inferred). Hybrid cloud (L02) — partial return vs full return (inferred).
- **Limits / trade-offs:** The slide asserts nothing itself; everything about reasons and costs is external to it (inferred).
- **Situation cues:** "bringing workloads back in-house"; "cloud bill exceeded owning hardware"; "repatriation trend".
- **Past-paper Qs:** none
- **Already tested:** 9

**Slides with no card (and why)**
- 1-16: title, who am I, course info/LMS, TAs, teaching style, lecture schedule, assessments, quizzes, labs, group project, STePS, AI & plagiarism I-III, resources, "previously on CS5224" — course administration, no examinable concept.
- 25: blank ("25/50").
- 27, 33: key-term index lists; the terms themselves are carded where they are taught (C13, C14, C15, C28).
- 28: "Key Business Drivers!" names only capacity planning / cost reduction / organisation agility; each is carded at its own slide (C15, C20, C22).
- 48: "Next Week / Things get serious! Concepts and Models".
- 49: references list.
- 50: continuous feedback QR/link.

**Claims in Notes/L01-Principles.md that the slides do not support**
- Concept 1: cloud's advantage is "risk reduction, not guaranteed cost savings" — slides claim "reduces business cost" (s22) and "cost efficiency at scale" (s30); no risk-reduction statement.
- Concept 1: "Over 3+ years at stable load, on-premise often wins on pure price" — no such comparison, horizon or numbers on any L01 slide.
- Concept 1: "CapEx / OpEx" labels — slides say "up-front investment costs" / "operational costs".
- Concept 1: "Hours to provision vs weeks" — provisioning time is not mentioned on L01 slides.
- Concept 2: vertical scaling creates a "single point of failure" and horizontal removes it — s38 gives "resources instantly available" for both and mentions no SPOF.
- Concept 2: "Horizontal: failure of one node doesn't kill the system" — not stated; s38 only says "not limited by hardware capacity".
- Concept 3: side-channel attacks, VM escape, shared memory bus — not on any slide; s42 says only "steal or damage data".
- Concept 3: "Trust boundary = the boundary within which you trust and control IT resources" — s27 lists the term only, s43/44 only draw it.
- Concept 4: "Singapore's PDPA and sector regulations apply to patient data" — s46 gives only "data belonging to Singapore citizens to be kept within Singapore".
- Concept 4: region choice driven by "cost of cloud resources" and "availability of specific services in that region" — neither is on L01 s46.
- Concept 5: mitigation list (Kubernetes, standard SQL, multi-cloud, SLA exit terms) — s41 lists "Vendor lock-in" with no mitigations.
- Concept 6: SLA must include latency/throughput metrics, remedy clauses, right-to-audit — s45 says only that an unreliable provider "may not maintain/meet SLA guarantees".
- Concept 7: "Scaling can be manual" and "elasticity = automatic, real-time, demand-driven" — s35 defines scaling only as the ability to handle increased/decreased demand; elasticity is never defined on L01.
- Concept 7: "Pre-provisioning a fixed pool is scaling, not elasticity, you pay for idle capacity" — not stated anywhere in L01.
- Concept 8: risk column "over-provisioning if demand doesn't materialise", "requires close monitoring; slow to respond to spikes" — s29 gives the three definitions only.
- Concept 9: "data egress costs" — s40 says "moving large data is still expensive"; egress fees are an interpretation.
- Concept 9: repatriation criteria ("stable workload", "team has on-prem capability", "SLA continuity", "elasticity lost") — s47 is a heading and a Forbes link with no criteria.
- Concept 9: "documented real-world trend" — supported only by the linked article's title, not by slide content.
