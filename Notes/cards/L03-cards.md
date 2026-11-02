# L03 Concept Cards

Built by DeepSeek V4.1 Flash from the slide text plus diagram facts (transcribed by Claude Haiku, spot-checked against the slide images). Cards are the source for writing scenarios. 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide. For past-paper links, trust Notes/PAST-PAPER-MAP.md over the card's Past-paper line (cards miss some, e.g. sovereign cloud 24S2 Q16, 25S2 Q23).

### L03-C01 Rapid elasticity: why it matters
- **Slides:** 3, 4
- **Type:** Application
- **What it is:** NIST's fourth essential characteristic (the recap lists the five: on-demand self-service, broad network access, resource pooling, **rapid elasticity**, measured service). Slide 4 gives its importance: it responds to **fluctuation in the cloud consumer's demand over time** — the **number of jobs**, and the **resource demand within a job** — and to **fluctuation in available cloud resources**, because the provider provides services to **many** cloud customers.
- **Look-alikes:** Rapid elasticity vs resource pooling — elasticity is the ability to grow and shrink with demand, pooling is why one provider's shared capacity can be re-allocated; "fluctuation in consumer demand" vs "fluctuation in available resources" — the first is *your* workload changing, the second is *other tenants* taking capacity from the same provider.
- **Limits / trade-offs:** None stated; the two fluctuation sources are the reason elasticity is hard to deliver (inferred).
- **Situation cues:** "demand spikes at month-end", "jobs vary in count and in size", "the provider's other customers can consume the capacity we expected".
- **Past-paper Qs:** 25S1 Q15

### L03-C02 Resource organisation: objectives and five methods
- **Slides:** 5, 6
- **Type:** Application
- **What it is:** Objectives: **achieve elasticity or scaling**, **achieve balanced utilisation of cloud resources**, and answer "how is this done in practice?". Methods split by level — **application level:** workload distribution, service load balancing; **resource level:** resource pooling, dynamic scalability, elastic resource capacity.
- **Look-alikes:** Workload distribution vs service load balancing — service LB is a *specialised variation* of workload distribution (slide 12); dynamic scalability vs elastic resource capacity — scalability adds or removes resource instances, elastic capacity resizes a *single virtual server* (slide 24); the two objectives — elasticity is about changing capacity at all, balanced utilisation is about not over- or under-using what already exists.
- **Limits / trade-offs:** None stated on the slide; note that the application/resource split is the slide's own grouping, not a ranking.
- **Situation cues:** "which methods are application level", "name the resource-level methods", "we need both elasticity and balanced utilisation".
- **Past-paper Qs:** none

### L03-C03 Workload distribution architecture
- **Slides:** 7
- **Type:** Application
- **What it is:** **Aim:** distribute the consumer's workload over available cloud resources — it **uses horizontal scaling**. **Key component:** the **load balancer**, which distributes workload to **reduce over-utilisation or under-utilisation** of resources.
- **Look-alikes:** Workload distribution vs horizontal scaling — distribution is the architecture, horizontal scaling is the direction of scaling it relies on (more instances of the same size); horizontal vs vertical scaling — vertical grows one server instead of spreading across several; workload distribution vs service load balancing — the latter adds redundant *copies of the service* (slide 12).
- **Limits / trade-offs:** None stated; the aim names both over-utilisation and under-utilisation as the problems to remove.
- **Situation cues:** "spread the workload across the available servers", "no server idle while another is saturated", "add more servers of the same size rather than bigger ones".
- **Past-paper Qs:** 24S2 Q11, 25S1 Q8

### L03-C04 Amazon Elastic Load Balancing as workload distribution
- **Slides:** 8
- **Type:** Application
- **What it is:** The worked example of the architecture: the **Amazon Elastic Load Balancing Service** **automatically distributes incoming application traffic**, achieves **greater levels of fault tolerance** for applications, and **seamlessly provides the required amount of load balancing capacity**. Diagram: cloud service consumers → load balancer → two instances of Cloud Service A, one on Virtual Server A and one on Virtual Server B (the same service twice; corrected from an earlier mis-transcription).
- **Look-alikes:** ELB's fault tolerance vs replication — the slide attributes tolerance to *spreading traffic*, not to keeping a standby copy (inferred); "seamless load balancing capacity" vs auto-scaling the application — the balancer's own capacity grows with traffic, which is separate from adding application servers (inferred); this vs service load balancing — the slide-8 diagram already shows the same service on two virtual servers, so the slides draw little difference between them; service load balancing (slide 12) is the specialised variation that adds redundant deployments and the independent/built-in placement of the balancer.
- **Limits / trade-offs:** None stated on the slide.
- **Situation cues:** "traffic spread over two cloud services on separate virtual servers", "one server fails and users notice nothing", "balancing capacity that grows with the traffic".
- **Past-paper Qs:** 24S2 Q22

### L03-C05 AWS load balancer: health checks and the four types
- **Slides:** 9
- **Type:** Application
- **What it is:** AWS **uses elastic load balancing**, i.e. it **automatically distributes incoming traffic across multiple targets**, and it **routes traffic only to healthy targets**. Types: **Application Load Balancer**, **Network Load Balancer**, **Gateway Load Balancer**, **Classic Load Balancer** (classic exists **for backward compatibility**). Lecture annotations: application/network are **network level** ("like roads and cars"); gateway is **gateway level** ("you want the right traffic on your roads").
- **Look-alikes:** Health check vs the balancing decision — balancing is about even spread, health checking is what *removes* a failing target from the spread; Application vs Network LB — ALB routes on application-level request detail (protocol, port, rules, slide 10) while NLB is network level; Classic vs the other three — classic is kept only for backward compatibility, so it is not the choice for a new design.
- **Limits / trade-offs:** None stated beyond health filtering; choosing the wrong type is the practical pitfall (inferred).
- **Situation cues:** "one target is unhealthy, stop sending it requests", "which balancer for HTTP request routing", "we still run a legacy setup", "gateway-level traffic inspection".
- **Past-paper Qs:** 25S2 Q1

### L03-C06 ALB listeners, rules and target groups
- **Slides:** 10, 11
- **Type:** Application
- **What it is:** The ALB **serves as a single point of contact for clients** and contains **one or more listeners**. A **listener** checks for requests from clients using the **protocol** and **port** you configure. **User-defined rules** route requests to registered targets in **target groups**; a rule consists of **priority**, **one or more actions** and **one or more conditions**, and a **default rule is necessary**. Steps: (1) the load balancer receives a request; (2) the request is evaluated and the appropriate rule applied; (3) a target is selected from the target group for the rule's action. Slide 11 shows the **hierarchy**: load balancer → listeners → rules → target groups (each with a **health check**) → targets.
- **Look-alikes:** Listener vs rule — the listener is the entry point on a protocol/port, the rule is the conditional decision applied to what arrives; rule vs target group — the rule decides *where*, the target group is *the set of targets* to choose from; default rule vs an ordinary rule — the default catches whatever no other rule matched, which is why it is mandatory.
- **Limits / trade-offs:** Every ALB needs a default rule, so a request is never left unrouted (inferred); target groups carrying health checks can shrink at run time (inferred from slide 11).
- **Situation cues:** "requests to /api go to the API servers", "no rule matched, where does the request go", "which port is the listener watching", "what sits between the listener and the target".
- **Past-paper Qs:** none

### L03-C07 Service load balancing architecture
- **Slides:** 12
- **Type:** Application
- **What it is:** A **specialised variation of the workload distribution architecture**. **Key feature:** **redundant cloud service deployments** are created and a load balancer **dynamically distributes workloads**. The slide writes "**resource pool ⇔ duplicate cloud service**". Load balancers can be **independent** of the cloud services and their host servers, or **built-in** to the cloud service as part of the application or server environment.
- **Look-alikes:** Service load balancing vs workload distribution — same aim; the slides call it a specialised variation that emphasises **redundant deployments of one cloud service** and where the balancer sits (independent or built-in), while workload distribution is the general idea of spreading workload (the slide-8 diagram also shows the same service on two servers); "resource pool" here vs resource pooling architecture (slide 16) — this is a pool of identical service copies, not pooled hardware resources.
- **Limits / trade-offs:** Replication has to exist before balancing helps, so the service must be safely duplicable (inferred).
- **Situation cues:** "run three copies of the service behind a balancer", "redundant deployments of the same service", "the same application on servers A, B and C".
- **Past-paper Qs:** none

### L03-C08 Independent vs built-in load balancer
- **Slides:** 13, 14
- **Type:** Application
- **What it is:** Both variants replicate **cloud service A** across different virtual servers. **Independent:** the load balancer **intercepts requests from cloud consumers and forwards them to the virtual servers**, so workload processing is **horizontally scaled** — the balancer is its own element in front of servers A, B and C. **Built-in:** the cloud consumer's request is **sent to cloud service A on virtual server A**, and the service's **built-in load balancing logic** means requests are **distributed to virtual servers B and C** — there is no separate balancer element.
- **Look-alikes:** Independent vs built-in — independent means the request always lands on the balancer first; built-in means it lands on one service instance, which then forwards, so that first server also does real work; both vs workload distribution (slides 7-8) — the same service on several servers appears in both, so the slides do not give a sharp difference.
- **Limits / trade-offs:** Built-in puts balancing logic inside the application/server environment and makes the first instance a de facto entry point (inferred); independent adds a component that must itself be run and scaled (inferred).
- **Situation cues:** "the balancer is its own tier", "no separate balancer, the app shares the requests itself", "requests hit server A and are then spread to B and C".
- **Past-paper Qs:** 25S1 Q11

### L03-C09 Resource pooling architecture
- **Slides:** 16
- **Type:** Application
- **What it is:** **Aim:** **aggregate cloud resources of different types** to serve the diverse needs of cloud consumers. **Key feature:** **automatically maintain identical IT resources to ensure they remain synchronised**. **Common resource pools:** **server pool** (physical/virtual), **CPU pool**, **memory pool**, **storage pool**, **network pool**.
- **Look-alikes:** This architecture vs the NIST resource-pooling characteristic (L02) — the characteristic is the property, this is the architecture that implements it (link inferred); pooling vs virtualisation — pooling aggregates resources of the same type, virtualisation carves instances out of them (inferred); resource pooling vs service load balancing's "resource pool" — that one is a pool of duplicate service copies.
- **Limits / trade-offs:** Keeping identical resources synchronised is the stated requirement, i.e. ongoing work, not a one-off setup.
- **Situation cues:** "separate pools for CPU, memory, storage and network", "resources of one type kept identical and in sync", "different consumer needs served from the same aggregate".
- **Past-paper Qs:** none

### L03-C10 Dedicated pools and their complexity
- **Slides:** 17
- **Type:** Application
- **What it is:** A **dedicated pool** holds sub-pools of the different resource types — the example is one dedicated pool with **4 sub-pools** of **CPUs, memory, storage and network devices**. **Issue:** it **becomes complex**, leading to **multiple pools for a specific consumer or application**.
- **Look-alikes:** Dedicated pool vs nested pool — a dedicated pool is set aside for one consumer or application, a nested pool subdivides one pool by the *same* resource type for departments (slide 18); dedicated pool vs private cloud — the pool is a slice of resources, private cloud is a deployment model (inferred).
- **Limits / trade-offs:** Complexity: you end up maintaining a separate set of sub-pools per consumer or application.
- **Situation cues:** "each customer gets its own pool", "four sub-pools, one per resource type", "the pool layout is getting hard to manage".
- **Past-paper Qs:** none

### L03-C11 Hierarchical pools: sibling vs nested
- **Slides:** 18, 19, 20
- **Type:** Application
- **What it is:** Pools are arranged as a **hierarchical structure of parent, sibling and nested pools** to meet diverse requirements. **Sibling resource pool:** drawn from **physically grouped IT resources** and **not spread out across data centres** (co-located); **isolated from one another**, so each cloud consumer gets access to its respective pool. **Nested resource pool:** a **larger pool divided into smaller pools with the same type** of IT resources; used for assigning pools to **different departments and groups within the same organisation**. Examples: **Pools B and C are sibling pools of Pool A**, from the same datacentre; **Pools A.1 and A.2 are nested pools of Pool A** — "same template, only different numbers".
- **Look-alikes:** Sibling vs nested — siblings are separate pools *side by side*, co-located and isolated, each for a different consumer; nested is *one pool subdivided*, same resource type, for departments of one organisation; parent vs sibling — the slide names a parent/sibling/nested hierarchy but only illustrates siblings (B and C are siblings of A, same datacentre) and nested pools (A.1, A.2 inside A); the parent role is not drawn (inferred); sibling vs dedicated — a dedicated pool is a whole pool per consumer, sibling pools are the co-located, isolated siblings inside one hierarchy.
- **Limits / trade-offs:** Siblings must be co-located, so they cannot span data centres; nested pools can only split resources of the same type.
- **Situation cues:** "two customers, each isolated, in the same datacentre", "split the CPU pool per department", "same template, different numbers", "resources must not be spread across data centres".
- **Past-paper Qs:** none

### L03-C12 Dynamic scalability architecture
- **Slides:** 21
- **Type:** Application
- **What it is:** **Aim:** enable **variable resource utilisation** to meet **usage demand fluctuations**. **Key feature:** **dynamic allocation of resources from resource pools based on predefined scaling conditions**.
- **Look-alikes:** Predefined scaling conditions vs the intelligent automation engine — slide 21 allocates on fixed, pre-set conditions, slide 24's engine runs workflow logic and can act *before* the threshold (L03-C15); dynamic scalability vs resource pooling — pooling supplies the resources, scalability decides when to draw on them; dynamic scalability vs workload distribution — distribution spreads load over what exists, scalability changes how much exists.
- **Limits / trade-offs:** Behaviour is only as good as the pre-set conditions; the 25S2 Q18 answer credits predefined thresholds with damping oscillation versus purely reactive scaling (see PAST-PAPER-MAP). No trade-off is stated on the slide itself.
- **Situation cues:** "allocate capacity when demand rises, release it when demand falls", "the rules were defined in advance", "resources come out of the pools on demand".
- **Past-paper Qs:** 25S1 Q20, 25S2 Q18

### L03-C13 Three dynamic scaling methods: horizontal, vertical, relocation
- **Slides:** 22
- **Type:** Application
- **What it is:** **Dynamic horizontal scaling** — the **same resource instance scaled dynamically** with fluctuating workloads, e.g. **replicating resources**. **Dynamic vertical scaling** — scale the **processing capacity of a single IT resource**, e.g. **increase memory dynamically when a virtual server is loaded**. **Dynamic relocation** — the resource is **relocated to a host with larger capacity**, e.g. a faster storage device with better I/O capacity ("move to an entirely new machine").
- **Look-alikes:** Horizontal vs vertical — horizontal adds or removes copies, vertical resizes one instance; vertical vs relocation — vertical adds capacity to the *same* machine, relocation moves the workload to a *different, bigger* machine; horizontal scaling vs workload distribution — distribution spreads load over existing instances, horizontal scaling creates more.
- **Limits / trade-offs:** Relocation moves the whole resource, so it implies migration work the slide does not discuss (inferred).
- **Situation cues:** "add another replica", "give the virtual server more memory", "move it to a host with faster storage".
- **Past-paper Qs:** none

### L03-C14 Automated scaling listener and horizontal dynamic scaling
- **Slides:** 23
- **Type:** Application
- **What it is:** The worked horizontal example in three steps: **(1)** the **automated scaling listener monitors capacity**; **(2)** the listener **takes a decision based on a predefined scaling policy** — it notifies cloud service instances that are overloaded with requests; **(3)** the listener **replicates resources** (resource replication), adding another cloud service instance so processing is spread over more instances.
- **Look-alikes:** Automated scaling listener vs load balancer — the listener watches utilisation and triggers scaling, the load balancer spreads requests over whatever instances exist (inferred from the diagrams); scaling policy vs scaling condition — the policy is the rule set, the condition is the trigger inside it (inferred); "replicates resources" here vs resource replication in cloud bursting — same mechanism, local replication versus on-premise/cloud replication.
- **Limits / trade-offs:** None stated on the slide.
- **Situation cues:** "who notices the service is overloaded", "a policy decides to add instances", "the listener creates a copy of the service".
- **Past-paper Qs:** none

### L03-C15 Elastic resource capacity architecture
- **Slides:** 24
- **Type:** Application
- **What it is:** **Aim:** **dynamic provisioning of virtual servers**. **Key features:** fluctuating **processing** requirements; **allocates and reclaims CPUs, RAMs**, etc.; the **run-time virtual server is monitored**; **additional resources are leveraged before the capacity threshold is reached**; the virtual server and its IT resources are **vertically scaled**; it uses an **Intelligent Automation Engine** (with **administration workflow logic** and **scripts**).
- **Look-alikes:** Elastic resource capacity vs dynamic scalability — ERC resizes **one virtual server vertically**, dynamic scalability adds **horizontal** instances; intelligent automation engine vs predefined scaling conditions — the engine executes workflow logic/scripts rather than a fixed threshold rule, and acts before the threshold; ERC vs resource pooling — it *draws from* CPU/memory sub-pools rather than creating them.
- **Limits / trade-offs:** Vertical scaling is bounded by what the host can give (inferred); it also depends on the automation engine and its scripts being in place.
- **Situation cues:** "give the busy VM more CPU and RAM", "act before the threshold is hit", "reclaim resources when the load drops", "no new servers, just a bigger one".
- **Past-paper Qs:** 25S1 Q20

### L03-C16 Elastic resource capacity in operation (listener → engine → hypervisor)
- **Slides:** 25, 26
- **Type:** Application
- **What it is:** Steady state: **(1)** cloud consumers send requests to a cloud service; **(2)** requests are monitored by an **automated scaling listener**; **(3)** the **intelligent automation engine** is deployed with **workflow logic**; **(4)** the workflow logic can notify the **resource pool** using **allocation requests**. On a spike: **(5)** consumer requests increase dramatically; **(6)** the listener **signals the intelligent automation engine to execute the script**; **(7)** the script runs workflow logic that **signals the hypervisor to allocate more resources from the resource pools**; **(8)** the **hypervisor allocates** the additional resources.
- **Look-alikes:** Listener vs engine — the listener detects and signals, the engine executes scripted workflow; engine vs hypervisor — the engine decides and signals, the hypervisor actually allocates; slide 25 vs slide 26 — same architecture, steady state versus spike.
- **Limits / trade-offs:** The chain listener → engine → script → hypervisor is long and every link must work for scaling to happen (inferred).
- **Situation cues:** "trace the request from the listener to the hypervisor", "who actually hands out the extra CPU", "workflow logic vs the monitoring component".
- **Past-paper Qs:** none

### L03-C17 Scaling on-premise provisioning and cloud bursting
- **Slides:** 27, 28
- **Type:** Application
- **What it is:** **Aim:** **scale on-premise IT resources into the cloud whenever capacity thresholds have been reached**; the example is **cloud bursting**. **Burst out:** to meet higher usage demand, **dynamic scaling of on-premise resources to cloud-based resources**. **Burst in:** on lower demand, **revert back to on-premise and release the cloud resources**. Cloud services are **redundant, pre-deployed and inactive** until bursting. **Features required:** an **automated scaling listener**, and **resource replication** so that **cloud and on-premise resources are synchronised**.
- **Look-alikes:** Burst out vs burst in — out grows into the cloud, in retreats and *releases* the cloud resources; cloud bursting vs hybrid cloud (L02-C31) — bursting is a temporary overflow using pre-deployed idle services, hybrid is a standing combination of distinct clouds; cloud bursting vs dynamic scalability — bursting crosses the on-premise/cloud boundary, dynamic scalability stays inside the provider's pools.
- **Limits / trade-offs:** It needs redundant services pre-deployed and state synchronised, so the cloud side costs while idle (inferred); it only starts once the threshold is crossed.
- **Situation cues:** "our datacentre is full at peak, rent cloud capacity for the peak", "release the cloud when the peak passes", "services already in the cloud but idle", "on-premise and cloud copies must stay in sync".
- **Past-paper Qs:** 25S2 Q6, 25S2 Q22

### L03-C18 Cloud bursting in operation
- **Slides:** 29
- **Type:** Application
- **What it is:** The **automated scaling listener monitors the usage of on-premise service A**. **(1)** When the **usage threshold is exceeded**, **Service Consumer C is redirected** to Service A's **redundant implementation on the cloud**. **(2)** The **resource replication system ensures the state management databases are synchronised**.
- **Look-alikes:** Redirecting the consumer vs replicating the service — redirection moves traffic, replication keeps both copies' state consistent; this vs the ELB example (slide 8) — both spread load, but here the overflow target sits in a different environment (on-premise versus cloud), not just another virtual server.
- **Limits / trade-offs:** Correctness depends on the state databases being synchronised; only the overflowing consumer is redirected, on-premise service A keeps serving (inferred).
- **Situation cues:** "traffic crosses from our datacentre to the cloud", "the state database must match on both sides", "which consumer gets moved, and when".
- **Past-paper Qs:** none

---

## Coverage

| Slide | Card(s) |
|---|---|
| 3 | L03-C01 |
| 4 | L03-C01 |
| 5 | L03-C02 |
| 6 | L03-C02 |
| 7 | L03-C03 |
| 8 | L03-C04 |
| 9 | L03-C05 |
| 10 | L03-C06 |
| 11 | L03-C06 |
| 12 | L03-C07 |
| 13 | L03-C08 |
| 14 | L03-C08 |
| 15 | none ("Take a Break" slide, no content) |
| 16 | L03-C09 |
| 17 | L03-C10 |
| 18 | L03-C11 |
| 19 | L03-C11 |
| 20 | L03-C11 |
| 21 | L03-C12 |
| 22 | L03-C13 |
| 23 | L03-C14 |
| 24 | L03-C15 |
| 25 | L03-C16 |
| 26 | L03-C16 |
| 27 | L03-C17 |
| 28 | L03-C17 |
| 29 | L03-C18 |
