# L03 Scenario Log

A record of each scenario, what you answered, how it was graded, and the correct answer. Reference only: the concepts live in `L03-Architectures.md` and the index. Answers are lightly trimmed from your spoken replies.

---

## S1. Ticketing site: sources of fluctuation and what the provider must achieve

**Scenario:** A ticketing company runs its booking site on a public cloud. Normally a few hundred bookings an hour. When a popular concert goes on sale, each customer session also gets heavier (seat maps, payment retries) and demand jumps about 50x. During one sale the company's own load is no higher than expected, yet it still struggles to get the extra servers it asked for.

**Q (a, open):** Name the two kinds of fluctuation the company copes with, and say which is behind each of the two problems.
**Your answer:** "The number of jobs and the resource demand within a job. The number of jobs going up 50 times is the demand rising; each session getting heavier is the resource demand within a job."
**Grade: partly right.** You matched the surge (number of jobs) and heavier sessions (demand within a job) correctly. But both are the *same* kind: fluctuation in the consumer's own demand over time. You missed the second kind, **fluctuation in available cloud resources**: the provider serves many customers, so other tenants can take the capacity this company expected. That is the problem "own load is normal, yet extra servers are hard to get". (The slide lists the demand sub-types under the first kind; the scenario's second problem pointed at the second kind.)

**Q (b, open):** What must the provider's design achieve, for this customer and across all customers?
**Your answer:** "Elasticity to cope with changing demand. And balanced utilisation: if this company needs more resources per job, the provider should allocate accordingly."
**Grade: half right.** **Elasticity** is correct (grow and shrink with the consumer's changing demand). **Balanced utilisation** is the right name but wrongly applied: it is not about giving one customer more. It is about the provider spreading and reallocating shared capacity across all customers so nothing is over-utilised (one tenant's spike starving others) or under-utilised (idle capacity). Giving this customer more resources is the elasticity half.

**Overall: about 50%.**

---

## S2. Food-delivery app: one big server vs four small behind an entry point

**Scenario:** A food-delivery app has one large server, overloaded at lunch peak, nearly idle at night. The architect proposes four smaller identical servers with a single entry point that receives every order and hands each to one of the four. The provider's managed entry point keeps working when one server crashes.

**Q (a, open):** What problem does the entry point solve, and what is the "four small instead of one large" approach called?
**Your answer:** "The problem it solves is the underutilisation of the single large server at night, and at peak time it's not enough. The approach is horizontal scaling."
**Grade: half right.** **Horizontal scaling** is correct. But you described the problems of the *single server*, not what the entry point (a **load balancer**) does. It distributes incoming workload across the available servers so none is **over-utilised** while another is **under-utilised**. (The night-time idle cost is solved by having several small servers you can add or remove, not by the balancer itself.)

**Q (b, open):** Engineer says service continues after a crash only because a standby copy takes over. Correct?
**Your answer:** "Not too correct. No standby copy; the load balancer shifts the load to the remaining three servers while a new one is spun up to replace the crashed one."
**Grade: correct.** No standby is needed: the balancer stops sending to the failed server and spreads traffic over the remaining healthy ones, which is the fault tolerance the Amazon ELB slide (s8) credits to automatic traffic distribution. Spinning up a replacement is a separate scaling step that the scenario did not state.

**Q (c, MCQ):** Which statement is false? (C: replacing the four servers with one even larger server is the same scaling direction.)
**Your answer:** "C is false."
**Grade: correct.** One bigger server is **vertical** scaling, the opposite direction.

**Overall: about 80%.**

---

## S3. Exam portal: unhealthy target, and which AWS balancer type

**Scenario:** An exam portal runs behind an AWS load balancer with five servers. One server's application hangs; one student gets an error, later students do not.

**Q (MCQ):** Why were later students not affected? (B: the balancer checked target health and stopped routing to the unhealthy one.)
**Your answer:** "B. It's not a copy, it's just how it routes."
**Grade: correct.** AWS routes traffic only to healthy targets (s9).

**Q (open):** Which of the four AWS balancer types for routing HTTP requests by URL path to different server groups, and which should a new design avoid, and why?
**Your answer:** "The network load balancer, because on a network level the roads and cars are the HTTP requests."
**Grade: wrong, and half the question unanswered.** The answer is the **Application Load Balancer**: its rules have conditions (such as a URL path) and send matching requests to a chosen target group (s10). You also did not say which type to avoid: the **Classic Load Balancer**, kept only for backward compatibility. The slide's "roads and cars" note labels application and network balancers alike as network level, so it does not separate them; do not use it to pick between them.

**Overall: about 35%.**

---

## S4. ALB with /api, /images and default routing

**Scenario:** An ALB fronts a web site: `/api/...` goes to API servers, `/images/...` to image servers, everything else to main web servers.

**Q (a, open):** Describe how the ALB handles one request, naming its parts in order.
**Your answer:** "The load balancer receives each request. The request is evaluated and an appropriate rule is applied, then a target is selected from the target group for the rule action."
**Grade: partly right (about 60%).** The three steps are the slide's (s10). But you did not name the **listener**, the part that checks for requests on the configured protocol and port and is the entry point. Order: load balancer → listener → rules → target group → target.

**Q (b, open):** What does a rule consist of, and what happens to `/checkout`, which matches no rule?
**Your answer:** "A priority, one or more actions and one or more conditions. `/checkout` goes to the main web servers."
**Grade: mostly right (about 70%).** The rule parts are correct. The destination is correct, but you did not name why: the **default rule**, which is mandatory and catches whatever no other rule matched.

**Q (c, open):** Where does the health check sit in this structure?
**Your answer:** "Between the load balancer and each service."
**Grade: not quite (about 40%).** On the slide's hierarchy (s11) the health check belongs to each **target group**: it checks that group's targets, and only healthy ones are chosen.

**Overall: about 55%.**

---

## S5. Photo-sharing upload service: independent vs built-in balancer

**Scenario:** Upload service replicated on servers A, B, C. Design X: a separate component in front forwards each request to A, B or C. Design Y: no separate component; requests go to the service on A, whose own logic passes some on to B and C.

**Q1 (open):** Name each design, where the request lands first, and whether that first stop does real processing.
**Your answer:** "X is the independent load balancer, Y is the built-in load balancer. In X the request lands first on the load balancer and no processing is done there; it routes to one of the three servers. In Y it lands first on [server A] and some real processing may be done there, then it passes other processing to B and C."
**Grade: correct.** (You said "E"; taken as server A, a speech slip.)

**Q2 (MCQ):** Which statement about service load balancing is false? (C: the balancer distributes among different cloud services that each do a different job.)
**Your answer:** "C is false."
**Grade: correct.** Service load balancing balances redundant copies of the same service (s12); the option is false because service load balancing is about redundant copies of the same service. (An earlier version of this note wrongly said slide 8 shows different services; it shows the same Cloud Service A on two virtual servers.)

**Overall: about 95%.**

---

## S6. Provider data centre with CPU, memory, storage and network groups

**Scenario:** A provider keeps separate groups of CPUs, memory, storage and network devices; customers' virtual servers are built from them; identical resources inside each group are kept automatically in step.

**Q1 (open):** A student says this is the same as the "resource pool" in service load balancing (a set of duplicate service copies). Right? What does each pool contain, and what is this design for?
**Your answer:** "I guess this is a sibling resource pool because the resources are co-located. Each pool contains multiple copies of each type of resource."
**Grade: wrong (about 10%).** You did not say whether the student is right (they are not) and did not name the aim. This is the **resource pooling architecture** (s16): it aggregates cloud resources of **different types** (server, CPU, memory, storage, network pools) to serve the diverse needs of consumers, keeping identical resources synchronised. It is not a sibling pool: that is a separate, later idea (co-located, isolated pools per consumer, s18). The service load balancing "pool" is a set of duplicate copies of one service; here each pool holds identical resources of one *type*.

**Q2 (MCQ):** Which statement is false? (D: each pool must mix CPU, memory and storage.)
**Your answer:** "D is false."
**Grade: correct.** Pools are per resource type.

**Overall: about 45%.**

---

## S7. Isolated firms, departments, and the 30-customer pool setup

**Scenario:** Firm X and Firm Y in one data centre must be isolated; Firm X splits its CPUs among three departments (same kind of CPU, different numbers); the provider gives each of 30 big customers a full private set of CPU, memory, storage and network sub-pools and finds it hard to manage.

**Q1 (open):** (i) arrangement keeping X and Y isolated, (ii) arrangement for departments, (iii) name and problem of the operations team's setup.
**Your answer:** "(i) Sibling resource pool: co-located resources isolated from each other so each consumer gets its own pool. (ii) Nested: like a template assigned to departments, same template in different numbers. (iii) The operations setup is the resource pooling architecture, and the problem is it is difficult to manage multiple pools without some structure."
**Grade: about 65%.** (i) correct. (ii) correct: add that a nested pool is a larger pool divided into smaller pools of the **same resource type**. (iii) wrong name: it is a **dedicated pool** (one pool with sub-pools per resource type, set aside for one consumer or application, s17). The problem is that it **becomes complex, leading to multiple pools for a specific consumer or application**; "without some structure" is not on the slide.

**Q2 (MCQ):** Which is true? (B: a nested pool splits a larger pool into smaller pools of the same resource type.)
**Your answer:** "D."
**Grade: wrong.** D said nested pools combine *different* resource types, which contradicts what you said in (ii): nested pools are the *same* type.

**Overall: about 60%.**

---

## S8. Streaming service: scaling on pre-set CPU thresholds

**Scenario:** Platform adds copies of its streaming service from shared server pools when average CPU stays above 70% for 5 minutes, and removes copies below 30% for 10 minutes. Engineers set the thresholds in advance.

**Q1 (MCQ, five architectures):** Which architecture? (C: Dynamic Scalability.)
**Your answer:** "Dynamic scalability, because it relies on predefined thresholds."
**Grade: correct.** Allocation of extra instances from pools on predefined scaling conditions (s21); elastic resource capacity would resize one virtual server vertically through an automation engine (s24).

**Q2 (open):** Original design used a single 50% threshold checked every minute and capacity kept flipping. What went wrong, and why do 70/30 with time windows fix it?
**Your answer:** "If the CPU fluctuates around 50% it keeps flipping up and down. 70/30 thresholds with time windows minimise this fluctuation."
**Grade: about 50%.** You named the problem (capacity oscillating). You did not give the mechanism, only restated that it "minimises fluctuation". The gap between 70 and 30 means CPU has to move a long way before the opposite action triggers, and adding a copy spreads the load so CPU drops without reaching the removal threshold straight away; the time windows ignore short blips. (Reasoning from the past-paper key, not slide text.)

**Overall: about 70%.**

**Your meta-feedback:** several earlier scenarios (S4, S7) can be answered by re-saying the slides. From S9 on, scenarios test reasoning on facts the slides do not spell out.

---

## S9. Three scaling problems: stateless front end, one-instance legacy app, exhausted host

**Scenario:** P1 stateless web front end, traffic 10x. P2 legacy accounting program limited to one instance, short of memory, host has spare RAM. P3 same program, host now has no spare RAM/CPU and slow disk.

**Q1 (open):** Pick horizontal, vertical or relocation for each and justify.
**Your answer:** "P1 horizontal: replicate resources to take the traffic, and since it is stateless no request is tied to a server. P2 vertical: stick to that single resource and the host has spare RAM. P3 relocation: the machine is limited and the disk is too slow, so no point getting more of those machines; move to an entirely new machine."
**Grade: correct.** All three, with reasons drawn from the scenario facts.

**Q2 (open):** One concrete reason always using relocation is a poor rule.
**Your answer:** "You may get a more powerful host than you need and underutilise it."
**Grade: mostly right (about 75%).** Over-sizing wastes money and leaves capacity idle: valid. Stronger reasons: relocating means moving the whole resource (migration effort and possible interruption) when a cheaper in-place vertical step would have done (P2). (Reasoning, beyond slides.)

**Overall: about 90%.**

---

## S10. Overloaded service, no scaling events

**Scenario:** Two instances behind a load balancer at 90%+ CPU; a scaling policy exists; the pool has free capacity; no scaling event in the logs.

**Q1 (open):** Which component is missing or failing, and why can't the load balancer or the policy fix it alone?
**Your answer:** "The listener. The load balancer is only for routing and can't spin up instances. The policy can't execute itself; the listener monitors and decides to replicate resources or scale down."
**Grade: correct.**

**Q2 (open):** One difference between the scaling listener and the load balancer.
**Your answer:** "Two distinct jobs: the listener monitors and decides to scale; the balancer only distributes traffic."
**Grade: correct.**

**Overall: about 95%.**

**Your meta-feedback:** keep to key concepts, no nitpicking on specific terms; no more than one or two extra questions per weak concept; questions are tiring when multi-part. Scenarios from S11 are at most two short questions; the three gap scenarios were merged into one mixed set.

---

## S11. Database VM given extra CPU/RAM before its limit; broken chain after hypervisor update

**Q1 (MCQ, five architectures):** Scripts from a management component give one database VM extra CPU/RAM before its limit, no new servers. (B: Elastic Resource Capacity.)
**Your answer:** "Elastic resource capacity."
**Grade: correct.**

**Q2 (open):** After a hypervisor update the VM stays starved every spike though monitoring and scripts work. Which link is broken, what does the team see, why do earlier steps look fine?
**Your answer:** "The step where the engine's script signals the hypervisor to allocate more resources. The database returns slower and slower results because it lacks resources. The earlier steps are fine because the hypervisor only comes in at the end."
**Grade: correct (about 90%).** Detail to add: the listener still detects the spike and the engine still runs the script (which looks successful), so monitoring and logs look normal while no extra resources arrive.

**Overall: about 95%.**

---

## S12. Retailer's Black Friday overflow to the cloud

**Q1 (MCQ):** On-premise overflow to idle pre-deployed cloud copies past a threshold, back afterwards. (B: Cloud Bursting.)
**Your answer:** "Cloud bursting."
**Grade: correct.**

**Q2 (open):** Shoppers on the cloud copies see wrong stock and lose orders. What was missing and what does it do?
**Your answer:** "The resource replication system: it keeps the state management databases synchronised so the on-premise and cloud copies match."
**Grade: correct.**

**Overall: about 95%.**

---

## Gap set: re-test of earlier mistakes (5 MCQs)

**Your answers:** 1B, 2A, 3C, 4C, 5D.
**Grade: 3/4 (75%) on the valid questions.** Q5 is excluded from the score: both A and D fit the slides, so it cannot be graded fairly.
- 1 (available-resource fluctuation): **correct**, fixes S1.
- 2 (ALB for URL-path routing): **correct**, fixes S3.
- 3 (full private set of sub-pools per customer): **wrong, same mistake as S7**. You chose resource pooling architecture; the answer is **E, dedicated pool**. Slide 17's heading reads "Resource Pooling Architecture / Dedicated Pools", which makes the mix-up understandable: the pooling architecture is the whole design (pools by resource type, kept synchronised); a dedicated pool is one arrangement inside it, giving one consumer its own set.
- 4 (balanced utilisation): **correct**, fixes S1.
- 5 (three copies of one service behind a balancer): **excluded: ambiguous question.** You asked how A (workload distribution) differs from D (service load balancing). I first said slide 8 shows two different services; that was wrong (you caught it: slide 8 shows the same Cloud Service A on two virtual servers). The slides draw only a thin line: service load balancing is the specialised variation stressing redundant deployments and the independent/built-in balancer, workload distribution the general idea. A scenario like this one is not safely answerable from the slides alone.
