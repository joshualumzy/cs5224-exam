# L03 — Cloud Architectures

Source: `Lecture 03 - Cloud Architectures.pdf` (slides 3–29; slide 15 is a break slide). Cards: `cards/L03-cards.md`. Past-paper mapping from `PAST-PAPER-MAP.md`.

---

## Scenario Plan (12 scenarios + 1 mixed gap set) — all done

| # | Topic | Cards | Slides | Format | Past-paper link | Status |
|---|-------|-------|--------|--------|-----------------|--------|
| 1 | Why elasticity matters (two sources of fluctuation) + resource organisation objectives and levels | C01, C02 | 3–6 | Open + MCQ | 2526S1 Q15 | ✅ |
| 2 | Workload distribution: load balancer, horizontal vs vertical, fault tolerance | C03, C04 | 7–8 | Production scenario | 2425S2 Q11, Q22; 2526S1 Q8 | ✅ |
| 3 | AWS load balancing: health checks, four balancer types | C05 | 9 | MCQ | 2526S2 Q1 | ✅ |
| 4 | ALB listeners, rules, target groups, default rule | C06 | 10–11 | Open | — | ✅ |
| 5 | Service load balancing: independent vs built-in balancer | C07, C08 | 12–14 | MCQ + open | 2526S1 Q11 | ✅ |
| 6 | Resource pooling architecture: pool types, synchronised identical resources | C09 | 16 | Application scenario | — | ✅ |
| 7 | Dedicated vs sibling vs nested pools | C10, C11 | 17–20 | Production scenario | — | ✅ |
| 8 | Dynamic scalability: predefined conditions, damping oscillation | C12 | 21 | Application scenario | 2526S1 Q20; 2526S2 Q18 | ✅ |
| 9 | Horizontal vs vertical vs relocation | C13 | 22 | Production scenario | — | ✅ |
| 10 | Automated scaling listener and horizontal scaling steps | C14 | 23 | Open | — | ✅ |
| 11 | Elastic resource capacity vs dynamic scalability; listener → engine → hypervisor chain | C15, C16 | 24–26 | MCQ (five architectures) + diagnose | 2526S1 Q20 | ✅ |
| 12 | Cloud bursting: burst out/in, pre-deployed services, state sync, redirecting consumers | C17, C18 | 27–29 | Production scenario | 2526S2 Q6, Q22 | ✅ |

Gap set after scenario 12 (one mixed set of 4 to 5 short questions, only on concepts that went wrong in testing, plus five-option "which architecture is this?" MCQs): the two kinds of fluctuation and balanced utilisation (S1), ALB vs NLB vs Classic (S3), typed pools vs sibling/nested/dedicated (S6, S7).

---

## Detailed Notes

### Concept 1: Rapid elasticity and the two sources of fluctuation (S1)

**Core idea:** Rapid elasticity is NIST's fourth essential characteristic. It matters because two kinds of fluctuation hit a cloud consumer **(slides, s4)**:

1. **Fluctuation in the consumer's own demand over time.** This has two parts: the **number of jobs**, and the **resource demand within a job** (each job getting heavier).
2. **Fluctuation in available cloud resources**, because the provider serves **many** customers who all draw on the same capacity.

> [!WARNING]
> **Mistake:** Treating "number of jobs" and "demand within a job" as the two kinds of fluctuation. Both belong to the first kind (your own demand). The second kind is the provider side: other tenants can take capacity you expected, so extra servers can be hard to get even when your own load is normal.

**Key one-liner:** Elasticity must absorb both your own demand swings (jobs and job size) and swings in what capacity is available because the provider is shared.

### Concept 2: Resource organisation: objectives and methods (S1)

**Core idea:** The slides give two objectives, **achieve elasticity or scaling** and **achieve balanced utilisation of cloud resources** **(slides, s5)**. Methods are split by level **(slides, s6)**: application level = workload distribution, service load balancing; resource level = resource pooling, dynamic scalability, elastic resource capacity.

- **Elasticity** = capacity follows one consumer's changing demand (grow and shrink).
- **Balanced utilisation** = the provider spreads shared capacity across all customers so nothing is over-utilised (one tenant's spike starving others) or under-utilised (idle capacity) **(beyond slides, s4/s7 wording)**.

> [!WARNING]
> **Mistake:** Describing balanced utilisation as "give this customer more resources". That is elasticity. Balanced utilisation is about the spread across everything the provider runs.

**Key one-liner:** Elasticity is per consumer; balanced utilisation is across the provider's shared resources.

**Where the five methods sit (slides, s6):** application level = workload distribution and service load balancing (spreading requests over copies); resource level = resource pooling (grouping resources by type), dynamic scalability (adding or removing instances) and elastic resource capacity (resizing one virtual server).

### Concept 3: Workload distribution architecture and the load balancer (S2)

**Core idea:** The aim is to distribute the consumer's workload over available cloud resources, using **horizontal scaling** **(slides, s7)**. The key component is the **load balancer**, which spreads workload to reduce **over-utilisation and under-utilisation** of the resources behind it.

- **Horizontal scaling** = more identical servers side by side. **Vertical scaling** = one bigger server. Replacing four servers with one larger server is vertical, the opposite direction.
- **Fault tolerance** comes from spreading traffic over several servers, not from a standby copy: if one fails, the balancer sends traffic to the remaining ones. The Amazon Elastic Load Balancing example says it automatically distributes incoming traffic, gives greater fault tolerance and provides the needed balancing capacity seamlessly **(slides, s8)**.

> [!WARNING]
> **Mistake:** Saying the load balancer solves the single server's problems (idle at night, too small at peak). The balancer spreads work over the servers that exist. Having several small servers you can add or remove is what fixes the cost and capacity problem.

**Key one-liner:** A load balancer spreads requests over identical servers so none is overloaded while another sits idle, and failed servers simply stop receiving traffic.

### Concept 4: AWS load balancing: health checks and the four types (S3)

**Core idea:** AWS uses elastic load balancing: it automatically distributes incoming traffic across multiple targets and **routes traffic only to healthy targets** **(slides, s9)**. A failing server is taken out of the spread by its health check, with no standby copy involved.

The four types **(slides, s9)**: **Application Load Balancer (ALB)**, **Network Load Balancer (NLB)**, **Gateway Load Balancer** and **Classic Load Balancer**. The Classic exists **for backward compatibility**, so a new design should not choose it.

- **Pick the ALB to route by request content**: it has listeners with rules whose conditions (for example a URL path) send matching requests to a target group **(slides, s10)**.
- The slide's note "like roads and cars" calls both application and network balancers network level, so it does not tell them apart, and the slide gives the Gateway only "you want the right traffic on your roads". **(Beyond slides, AWS documentation from memory):** **ALB** = request level (HTTP/HTTPS), routes on content; **NLB** = connection level (TCP/UDP), no content routing, very high throughput and low latency; **Gateway** = inserts third-party virtual appliances (firewalls, inspection) into the traffic path; **Classic** = older generation.

> [!WARNING]
> **Mistake:** Choosing the Network Load Balancer to route HTTP requests by URL path because "HTTP requests are the cars on the network roads". Routing on request content (path) is the ALB's job through rule conditions. Also name the type to avoid for new designs: Classic.

**Key one-liner:** Balancers send traffic only to healthy targets; use the ALB when routing depends on the request, and avoid Classic for new designs.

### Concept 5: ALB structure: listeners, rules, target groups (S4)

**Core idea:** The ALB is a **single point of contact for clients** and contains one or more **listeners** **(slides, s10)**. Hierarchy **(slides, s11)**: load balancer → **listeners** → **rules** → **target groups** (each with a **health check**) → **targets**.

- **Listener**: checks for requests from clients on the **protocol** and **port** you configure. It is the entry point.
- **Rule**: user-defined; consists of a **priority**, **one or more actions** and **one or more conditions** (for example a URL path). Matching requests go to the rule's target group.
- **Default rule**: necessary. It catches any request no other rule matched, so no request is left unrouted.
- **Target group**: the set of targets to choose from. The **health check** is attached to the target group; only healthy targets are selected.
- Three steps: receive the request; evaluate it and apply the right rule; select a target from the target group in the rule's action.

> [!WARNING]
> **Mistake:** Describing the request path without the listener, and placing the health check "between the balancer and the servers". The listener is the first part that sees the request, and the health check belongs to each target group.

**Key one-liner:** Listener takes the request in, a rule decides which target group, the target group's health check decides which target; the default rule catches the rest.

### Concept 6: Service load balancing: independent vs built-in balancer (S5)

**Core idea:** Service load balancing is a **specialised variation of workload distribution** **(slides, s12)**. Redundant deployments of the **same cloud service** are created and a load balancer dynamically distributes the workload. The slide writes "resource pool ⇔ duplicate cloud service". The Amazon ELB diagram (s8) also shows the same Cloud Service A on two virtual servers, so the slides draw only a thin line between the two.

Where the balancer lives **(slides, s12-14)**:

- **Independent**: a separate load balancer intercepts consumer requests and forwards them to the virtual servers. Every request lands on the balancer first, which does no service processing; processing is horizontally scaled.
- **Built-in**: the request is sent to cloud service A on virtual server A, and the service's built-in load balancing logic distributes requests to virtual servers B and C. The first server does real processing and also passes work on.

- **Versus workload distribution (s7-8):** the slides draw only a thin line. Workload distribution is the general idea: spread the consumer's workload over available resources by horizontal scaling (the s8 diagram already shows the same service on two virtual servers). Service load balancing is its specialised variation, stressing **redundant deployments** of a service and where the balancer sits (independent or built-in). The textbook the slides cite (Erl, Chapter 11) draws the line by scope **(beyond slides)**: workload distribution is the general pattern for any IT resource; service load balancing is a specialised variation for cloud service implementations (redundant copies of the same service in a resource pool; balancer external or built into the hosting servers). Checked against Arcitura's pattern page for service load balancing; the "general vs specialised" framing comes from secondary study material, not the Erl book itself. A past-paper question separates them by the placement cue (balancer separate vs inside the service), not by "same vs different service".

**Key one-liner:** Independent = the request hits a separate balancer first; built-in = it hits a service instance that shares the work out itself.

### Concept 7: Resource pooling architecture (S6)

**Core idea:** The aim is to **aggregate cloud resources of different types** to serve the diverse needs of cloud consumers **(slides, s16)**. Common pools: **server pool** (physical or virtual), **CPU pool**, **memory pool**, **storage pool**, **network pool**. Key feature: **identical IT resources are maintained automatically so they stay synchronised**.

- Each pool holds identical resources of **one type** (a CPU pool of CPUs). Consumers' virtual servers draw from several pools.
- This is a different "pool" from service load balancing's "resource pool ⇔ duplicate cloud service" (s12), which is a set of copies of one service.

> [!WARNING]
> **Mistake:** Calling the typed hardware pools (CPU, memory, storage, network) a "sibling pool". Sibling and nested pools describe how pools are arranged and isolated (s18); the pooling architecture itself is about aggregating resources by type.

**Key one-liner:** Pooling groups identical resources by type (CPU, memory, storage, network) and keeps them in step so consumers' needs can be met from the aggregate.

### Concept 8: Dedicated, sibling and nested pools (S7)

**Core idea:** Pools are organised in a hierarchy of parent, sibling and nested pools to meet diverse requirements **(slides, s18)**.

- **Dedicated pool**: set aside for one consumer or application, holding sub-pools of the different resource types (example: one pool with 4 sub-pools of CPUs, memory, storage and network devices). **Issue: it becomes complex, leading to multiple pools for a specific consumer or application** **(slides, s17)**.
- **Sibling pools**: drawn from physically grouped IT resources, **not spread across data centres** (co-located), and **isolated from one another** so each consumer gets access to its own pool. Example: Pools B and C are siblings of Pool A, from the same data centre **(slides, s18-19)**.
- **Nested pools**: a larger pool divided into smaller pools of the **same type** of IT resources, used for different departments and groups in the same organisation. Example: A.1 and A.2 inside Pool A, "same template, only different numbers" **(slides, s18, s20)**.

> [!WARNING]
> **Mistake:** Choosing "nested pools combine different resource types". Nested pools split one pool into smaller pools of the *same* type. Also, a per-consumer set of CPU/memory/storage/network sub-pools is a **dedicated pool**, not "the resource pooling architecture".

- **Slide gap (s17):** the slide heading reads "Resource Pooling Architecture: Dedicated Pools". The resource pooling architecture is the whole design (pools by resource type, kept synchronised, s16); a dedicated pool is one arrangement inside it that gives one consumer or application its own set of sub-pools. Tripped on twice in testing (S7 and the gap set).

**Key one-liner:** Siblings are co-located isolated pools for different consumers; nested pools split one pool by the same type for departments; dedicated pools give one consumer a full set and get complex.

### Concept 9: Dynamic scalability architecture (S8)

**Core idea:** Aim: enable **variable resource utilisation** to meet usage demand fluctuations. Key feature: **dynamic allocation of resources from resource pools based on predefined scaling conditions** **(slides, s21)**. It scales by adding or removing instances (horizontal), unlike elastic resource capacity, which resizes one virtual server (s24).

- **Why thresholds are paired with a gap and time windows** **(beyond slides; matches the past-paper answer)**: a single threshold makes capacity oscillate (flip up and down) when load hovers around it. Separate scale-out and scale-in thresholds (70% / 30%) leave a gap, adding a copy spreads the load so CPU falls without reaching the removal threshold, and time windows ignore short blips.

> [!WARNING]
> **Mistake:** Saying the thresholds and windows "minimise fluctuation" without the mechanism. Name the problem (oscillation around one threshold) and the reasons the gap and the windows stop it.

**Key one-liner:** Dynamic scalability draws instances from the pools on pre-set conditions; a gap between scale-out and scale-in thresholds, plus time windows, stops it oscillating.

### Concept 10: Horizontal, vertical and relocation scaling (S9)

**Core idea:** Three dynamic scaling methods **(slides, s22)**:

- **Dynamic horizontal scaling**: the same resource instance is scaled with fluctuating workloads, e.g. by **replicating** resources.
- **Dynamic vertical scaling**: scale the capacity of a **single IT resource**, e.g. add memory dynamically to a loaded virtual server.
- **Dynamic relocation**: the resource is **moved to a host with larger capacity**, e.g. a faster storage device with better I/O.

**How to choose (reasoning from the facts; beyond slides):**

- **Stateless** or freely copyable service, load rising: horizontal (any copy can answer any request).
- **Must stay one instance** and the current host still has spare capacity: vertical.
- **Must stay one instance** and the host itself is exhausted (no spare RAM/CPU, slow disk): relocation.
- Relocation is not a universal rule: it moves the whole resource (migration effort, possible interruption) and may give more host than needed, wasting cost, when a cheaper in-place vertical step suffices.

**Key one-liner:** Copy it if it can be copied; grow it in place if the host has room; move it only when the host itself is the limit.

### Concept 11: Automated scaling listener and horizontal dynamic scaling (S10)

**Core idea:** Worked horizontal example **(slides, s23)**: (1) the **automated scaling listener monitors capacity**; (2) it **takes a decision based on a predefined scaling policy**, notifying instances that are overloaded; (3) it **replicates resources**, adding another service instance.

- **Listener** = monitors and decides (and triggers scaling out or in). **Load balancer** = only routes traffic over the instances that exist. A policy is just a rule; something has to act on it.
- Symptom of a missing or failing listener: instances stay overloaded, no scaling events appear, even though the policy and free pool capacity exist and the load balancer works.

**Key one-liner:** The load balancer spreads traffic; the automated scaling listener watches load, applies the policy and triggers new instances.

### Concept 12: Elastic resource capacity architecture and the scaling chain (S11)

**Core idea:** Aim: **dynamic provisioning of virtual servers**. It **allocates and reclaims CPUs, RAM, etc.** for one virtual server, the run-time virtual server is monitored, extra resources are leveraged **before the capacity threshold is reached**, scaling is **vertical**, and it uses an **Intelligent Automation Engine** **(slides, s24)**.

- **Versus dynamic scalability:** dynamic scalability adds or removes instances on predefined conditions (s21); elastic resource capacity resizes one virtual server through an automation engine that acts before the threshold. Past papers ask for exactly this difference.
- **Chain on a spike (slides, s25-26):** the automated scaling listener monitors requests → signals the intelligent automation engine to execute the script → the script's workflow logic signals the **hypervisor** → the hypervisor allocates more resources from the pools. The listener detects, the engine decides and runs the script, the hypervisor actually hands out the resources.
- **Failure in the last link** (for example the hypervisor will not accept the allocation): the listener still sees the spike and the script still runs without errors, so monitoring looks normal, but the virtual server stays starved and its response times worsen **(reasoning, beyond slides)**.

**Key one-liner:** Elastic resource capacity grows one virtual server in place, ahead of the threshold, via listener → automation engine script → hypervisor allocation.

### Concept 13: Scaling on-premise provisioning and cloud bursting (S12)

**Core idea:** Aim: scale on-premise IT resources into the cloud whenever capacity thresholds are reached; the example is **cloud bursting** **(slides, s27-28)**.

- **Burst out**: to meet higher demand, scale on-premise resources dynamically to cloud-based resources. **Burst in**: on lower demand, revert to on-premise and release the cloud resources.
- The cloud services are **redundant, pre-deployed and inactive** until bursting. Required: an **automated scaling listener** and **resource replication**, so cloud and on-premise resources stay synchronised.
- In operation **(slides, s29)**: the listener monitors on-premise service A; when the threshold is exceeded, the consumer is redirected to A's redundant implementation in the cloud; the **resource replication system** keeps the state management databases synchronised.
- **Without replication:** the two sides hold different state, so shoppers see wrong stock and lose orders **(reasoning from the slide)**.
- **Versus hybrid cloud (L02):** bursting is temporary overflow using pre-deployed idle services, hybrid is the standing combination of clouds. **Versus dynamic scalability:** bursting crosses the boundary between on-premise and cloud.

**Key one-liner:** Cloud bursting overflows on-premise load to pre-deployed cloud copies past a threshold and returns afterwards, with replication keeping both sides' state in step.

---

## Reference only (not tested)

- Common pool names (slide 16): server, CPU, memory, storage, network.
- ALB hierarchy wording (slide 11) beyond what concepts 4 and 5 state.
- The parent pool role in the parent / sibling / nested hierarchy (named on slide 18, not drawn on slides 19-20).

## Coverage check

Every card C01-C18 was tested at least once (C01-C02 in S1; C03-C04 S2; C05 S3; C06 S4; C07-C08 S5; C09 S6; C10-C11 S7; C12 S8; C13 S9; C14 S10; C15-C16 S11; C17-C18 S12), plus the mixed gap set. Left untested: only the reference-only items above.

## Mistakes to watch

- Dedicated pool vs resource pooling architecture (S7, gap set Q3).
- Balanced utilisation vs elasticity (S1).
- Application vs network load balancer (S3).
