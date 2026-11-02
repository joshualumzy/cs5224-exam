# L01 Scenario Log

A record of each scenario, what you answered, how it was graded, and the correct answer. Reference only: the concepts live in `L01-Principles.md` and the index. Answers are lightly trimmed from your spoken replies.

Scenarios O1-O9 were the original nine, graded in an earlier session (grades are that session's). G1-G8 were the gap scenarios, graded in a later session. G8 is not an L01 topic and moves to the L06 notes.

---

## O1. Startup dilemma (cost vs risk)

**Scenario:** A healthcare analytics startup has $200K to build an MVP in 4 months. Option A: buy 4 servers ($60K), rent colo space, hire a sysadmin. Option B: pay-as-you-go cloud, scale down to near zero if the MVP fails. An advisor says on-premise is often 40% cheaper over 3 years. Why still pick B?

**Your answer:** "I should still pick option B just in case we don't last three years. If we don't last three years then the cloud will not be cheaper."

**Grade: about 30%.** You gave survival risk only. Missing: capacity-planning risk (on-premise commits money before demand is known, so you over-provision or under-provision) and organisational agility (hours to provision vs weeks).

**Correct:** Cloud turns an up-front commitment into variable cost and defers the capacity guess, and it lets the company move quickly. It is not about being cheaper.

## O2. Black Friday meltdown (scaling)

**Scenario:** One 64-CPU, 512 GB server, the largest the provider offers, goes down for 2 hours at 8,000 req/s (normal 500). The manager says: get a bigger server. What is wrong with that, and what instead?

**Your answer:** "I can't upgrade anymore, it's the most powerful machine. There are limits to the physical capacity of a machine, so I should do horizontal scaling. I should buy more machines."

**Grade: about 60%.** Hard ceiling and horizontal scaling: correct. Missing: a single server is a single point of failure, and the 2-hour outage was a reliability failure, not only a capacity one.

**Correct:** Two problems with "bigger server": a hard hardware ceiling and one machine failing takes everything down.

## O3. The neighbour problem (trust boundaries)

**Scenario:** A bank's customer data sits on shared cloud infrastructure, with other companies' VMs on the same physical server. Is this a real security concern, and what makes it different from on-premise?

**Your answer:** "Yes, because if that infrastructure gets hacked, maybe through the other company's VMs, the whole server can be compromised. So I have to widen my trust boundary to include everything else on that shared infrastructure."

**Grade: partial.** You named the trust boundary, but you framed the threat as an outside attacker going through another company's VM. The threat is lateral: a malicious or compromised co-tenant on the same host attacking you directly. You also didn't say what differs from on-premise.

**Correct:** Shared hardware makes trust boundaries overlap with unknown co-tenants. On-premise you control who shares your hardware.

## O4. The Singapore clinic (region choice)

**Scenario:** A healthcare startup is building patient records for Singapore clinics. The CTO wants to deploy everything in the US east region because it is cheapest and has the most services. What is the problem and what should the CTO consider?

**Your answer:** "The US is far from Singapore, so it could introduce massive latency and very slow retrieval of records, affecting the clinic. The CTO should consider a region closer to Singapore."

**Grade: partial.** Latency: correct. Missing the bigger issue: data residency law may require patient data to stay in Singapore, which makes the US region possibly illegal, not just slow.

**Correct:** Lead with the legal requirement (data residency), then latency, then cost and service availability.

## O5. The exit that wasn't (vendor lock-in)

**Scenario:** A logistics company has been on one provider for 4 years, deeply integrated with its functions, database, storage and CDN services. Switching to another provider would take 18 months and $4M. What risk is this and what should they have done from day one?

**Your answer:** "The risk is vendor lock-in. On day one they should have evaluated which vendor offers the best pricing up front."

**Grade: wrong remedy.** Lock-in is named correctly, but you gave a procurement answer. It is an architecture problem.

**Correct:** Use portable technology, avoid deep coupling to provider-specific services, design so workloads can run on more than one provider, and negotiate exit terms. (These mitigations are from the past-paper key, not the L01 slides.)

## O6. The governance gap (SLA)

**Scenario:** A company moved its ERP to a third-party provider. Six months later performance has degraded and uptime has dipped, but the provider says everything is within contractual limits. What structural risk is this, and what should the company have done when signing?

**Your answer:** "This is the cloud not meeting the SLAs. Actually they have met the SLAs, so I'm not sure why there's a risk. Conceptually I don't understand."

**Grade: concept not understood.** Explained afterwards.

**Correct:** The provider met the contract, and that is the problem. In cloud the contract is your only lever, so a weak contract (loose uptime, no performance metrics, no remedies, no audit access) leaves you with no recourse. This is reduced operational governance control.

## O7. Definitions and elasticity (elasticity vs scaling)

**Scenario:** (A) What is the difference between elasticity and scaling? (B) A news site runs at 100 req/s, spikes to 50,000 req/s for under an hour, and the company pre-provisions 500 servers. Is that elastic? Scalable?

**Your answer:** (A) "Elastic means resources can be scaled up and down, whereas scaling means providing more or less of such resource. They're very interconnected." (B) "It's elastic because traffic can spike and drop back, but not scalable because I've provisioned 500 servers and can't expand. Elastic is a property of the demand, scalable a property of the resources."

**Grade: mostly wrong.** (A) described the same thing twice. (B) backwards.

**Correct:** Scaling is the ability to resize and can be manual. Elasticity is automatic resizing that follows actual demand and releases resources when not needed. Pre-provisioning 500 servers is scaling, not elasticity, because you pay for idle capacity.

## O8. Capacity planning strategies

**Scenario:** A company adds server capacity in small increments as actual user numbers grow. Which strategy is it, and what are the other two, with a one-line description of each?

**Your answer:** "Match. The other two are lead and lag. Match incrementally allocates resources based on demand, lead pre-allocates and anticipates a change, and lag is more reactive: it sees a change and then responds."

**Grade: about 80%.** One imprecision: lag adds capacity only when resources reach full capacity, not whenever it sees a change in demand.

## O9. The homecoming (repatriation)

**Scenario:** A fintech has been fully on one provider for 5 years and its bill has tripled. A competitor moved its core database back on-premise and cut costs by 35%. The CFO wants to do the same. Is the reasoning sound, what would you evaluate, and what are the risks?

**Your answer:** "I would not just look at cost, but at the availability and the elasticity, and how necessary they are for the fintech. They'd have established SLAs with customers, and on-prem I don't know if it can keep that same SLA, because on-prem you can't just spin up additional resources."

**Grade: about 50%.** Right factors (availability, elasticity, SLA), but no verdict on the CFO. Missing: the cost of moving large data back, lock-in and migration cost, and acknowledging repatriation is a real trend that can pay off for stable workloads.

**Correct:** The CFO's reasoning has merit only for stable, predictable workloads. Weigh variable demand, the cost of moving data back, how deeply the system is coupled to the provider, and whether on-premise can match the SLA.

---

## G1. Availability and single points of failure

**Scenario:** A ticketing company runs its web shop on one large virtual server. At 10:05 on concert-ticket day the physical host fails, and the shop is down for 40 minutes. Management says "we moved to the cloud so this wouldn't happen." (a) Which expected benefit did they fail to get, and why? (b) Name two changes that would have kept it up, and the scaling direction.

**Your answer:** (a) "Availability, because it relied on a single server." (b) "Horizontal scaling across multiple datacenters, so if one fails another is still running. Maybe vertical scaling, so my one server is sufficient for the increased load."

**Grade: about 50%.** (a) correct. (b) horizontal: correct. Vertical: wrong, because a bigger single server is still one machine and fails the same way. Vertical scaling adds capacity, not availability.

**Correct:** Redundancy: more than one server on different hosts, or automatic failover or replacement.

## G2. Cloud service vs cloud-based IT resource

**Scenario:** A provider's cloud hosts three virtual servers (two run the public booking app, one is used only for internal log processing), two storage devices (one holds bookings accessed through the app, one holds the log server's temp files), and customers subscribe to the booking app over the Internet. Which statement is correct?

**Your answer:** "A cloud service is something made remotely accessible via the cloud. I would think all six are cloud services because they are all remotely accessible."

**Grade: 0%.** You recalled the definition correctly but applied it wrongly. The correct option: all six are cloud-based IT resources, but only the booking application, which is made remotely accessible to consumers, is a cloud service.

## G3. Capacity planning challenges and the full cost picture

**Scenario:** A retailer bought S$2M of servers two years ago (3 years of life left). Normal traffic uses about 20% of capacity; the year-end sale needs 5x for 3 weeks; servers take 8 weeks to order. The CFO says the hardware is already paid for so running it costs nothing more. (a) Two flaws in that reasoning. (b) Two risks of bad capacity planning and what the business sees. (c) One reason cloud cost per unit can be lower.

**Your answer:** (a) "The sunk cost fallacy: it doesn't matter how much you paid, it's whether the hardware can support the demand. Also, running the hardware takes manpower, electricity, so there's additional cost on top of the fixed cost." (b) "The site can go down and lose profits at the sale. The other is that a lag strategy can't work because servers take 8 weeks to install." (c) "It's a shared resource among many people, so the cost per user is less: economy of scale."

**Grade: about 75%.** (a) running costs: correct. Sunk-cost wording: see note below. (b) under-provisioning: correct; the second risk should have been over-provisioning (idle capacity). Your 8-week lead-time point is good but isn't the second risk. (c) correct.

**Note on sunk cost:** I told you the CFO's mistake was the sunk-cost fallacy. The course's answer key (2526-S2 Q8) marks "past investments should not be considered" as wrong. Under this course, existing investment and migration costs count.

## G4. Diagnosing slow performance

**Scenario:** An insurer moves its reporting app to a US cloud region. Singapore staff see each click take about 1.5 seconds while server CPU is 10% and memory 30%. A nightly upload of 4 TB over a 100 Mbps office link takes about 4 days. (a) Cause and fix of the slow clicks. (b) Cause and fix of the upload. (c) Would adding 10 identical servers fix either?

**Your answer:** (a) "Latency: it takes time for data to travel between Singapore and the US. Move the web server closer." (b) "No parallelization: one large server, so it's slow. Have multiple servers, like MapReduce." (c) "It can only fix problem two, not problem one, because problem one is limited by distance."

**Grade: about 40%.** (a) correct. (b) wrong: the cause is bandwidth; 4 TB over 100 Mbps takes about 3.7 days, so the office link is the bottleneck. (c) problem 1: right. Problem 2: wrong, because extra cloud servers still receive data through the same 100 Mbps link.

**Correct:** Bandwidth fixes: bigger or dedicated link, send only changes, compress, or ship bulk data physically.

## G5. Technical vs non-technical challenges

**Scenario:** A bank lists five concerns about moving its loan system: (1) legacy app tied to specific OS and hardware, (2) 300 TB of records to move, (3) regulator requires data to stay in Singapore, (4) a branch loses Internet and cannot reach the system, (5) provider guarantees only 99.5% uptime with no audit rights. Classify each as technical or non-technical, and pick the one hardest to fix by engineering alone.

**Your answer:** "One is technical, two is technical, three is non-technical, four is technical, five is technical. The hardest to fix by engineering is five, because the control just goes to the provider and no amount of engineering on the user side takes it back."

**Grade: about 80%.** 1-4 correct. Concern 5 is non-technical (SLA and governance), and your own reasoning in (b) says why.

## G6. Trust-boundary direction and shared security responsibility

**Scenario:** A health-tech startup stores patient records in a public storage service also used by a competitor. (a) Which of four statements about trust boundaries and security responsibility is false? (b) Give one security risk it did not have on-premise.

**Your answer:** (a) "C is the false statement." (b) "Some other service in the same public cloud gains access to the patient records. That wouldn't happen on-premise. It's a lateral risk."

**Grade: 100%.** C reversed the direction (it claimed the provider's boundary expands to cover the customer's data and the provider is responsible). The customer's boundary expands to include the provider, and responsibility is shared.

## G7. Privacy, legal disclosure, multi-regional compliance

**Scenario:** A ride-hailing company stores trip and location data in a Singapore region to comply with a localization rule, then expands abroad. (a) Which statement is correct? (b) An engineer proposes replicating all trip data to a cloud region in each new country for low latency. What legal challenge does this create?

**Your answer:** (a) "B." (b) "Again how secure the cloud is. If the cloud is not secure it could lead to vulnerabilities, even though I'm storing all the data locally." (Afterwards you asked what multi-regional compliance means.)

**Grade: about 50%.** (a) correct: residency (where data sits) and disclosure (when authorities can demand it) are separate legal issues. (b) wrong: you answered security, which is not a legal challenge. The legal challenge is multi-regional compliance: each country's own laws apply to the data stored there.

## G8. Scalable, low-latency design (moves to L06)

**Scenario:** A photo-sharing app's single server receives the upload, creates thumbnails, runs moderation, then replies, which takes 8 seconds. Traffic spikes 50x during campaigns and is near zero most nights; the team pays for servers sized for the peak. (a) Why the wait, and what change gives a near-immediate reply? (b) What change makes cost follow usage? (c) Scaling direction, and why not the other?

**Your answer:** (a) "It bundles the upload and moderation together. Separate them, or have checkpoints in between." (b) "Allow for horizontal scaling." (c) "Not vertical: 50x the rate may not fit one server, and even if it does it is a single point of failure."

**Grade: about 55%.** (a) cause correct, fix vague: reply immediately and process in the background (asynchronous). (b) only half: cost follows usage with automatic scaling plus pay-per-use, such as serverless functions (FaaS). (c) correct.
