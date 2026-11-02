# L04 Scenario Log

A record of each scenario, what you answered, how it was graded, and the correct answer. Reference only: the concepts live in `L04-Resource-Hosting.md` and the index. Answers are lightly trimmed from your spoken replies.

---

## S1. Truck-tracking firm: moving from its own server room to a public cloud

**Scenario:** A logistics firm runs truck tracking from a server room in its own office. Positions must show on dispatcher screens within a contractual time limit. It is considering a public cloud provider.

**Q1 (open):** After the move, name two things the firm no longer owns, and what each means for keeping the time limit.
**Your answer:** "The firm no longer owns the latency and the bandwidth. Latency: may not keep to the fixed time limit. Bandwidth: if the load is too high and the server can't transfer enough bits per unit time, it may not show every truck's position in time."
**Grade: about 50%.** Latency and bandwidth are measurements of a connection, not things the firm owned. What the firm gives up is (1) the **internet connectivity** (deploying, operating, maintaining it) and (2) **complete control over QoS**; with the cloud, traffic crosses **multiple carriers**, so QoS depends on them. Your consequence for latency was right. Your bandwidth point blamed server overload, which is a capacity problem on-premise too; the move-specific risk is losing control of the link capacity to the users. Security is also no longer solely the firm's (Q2).

**Q2 (MCQ):** Security officer says "the cloud makes us less secure". Best response?
**Your answer:** "C."
**Grade: correct.** Cloud is not inherently insecure, just more actors involved.

**Overall: about 75%.**

---

## S2. Video-review company: Singapore editors, Frankfurt datacenter, tenfold link upgrade

**Scenario:** Singapore editors upload 40 GB raw files (takes hours) and scrub clips in the browser (each click waits about 0.5 s). App hosted in Frankfurt. The company buys a tenfold capacity upgrade.

**Q1 (open):** For each complaint, will the upgrade help, and why?
**Your answer:** "Complaint one yes, more capacity, I can transfer more GB per unit time. Complaint two no, that's latency, the time for data to travel from Singapore to Frankfurt, a physical property that can't be changed just by increasing capacity."
**Grade: correct.**

**Q2 (MCQ):** Make scrubbing feel instant: faster link / more CPU cores / serve from a datacenter near Singapore / compress uploads / more carriers.
**Your answer:** "C."
**Grade: correct.** Only moving the app closer shortens the distance that sets the latency.

**Overall: 100%.**

---

## S3. News site: Virginia datacenter, slow for Singapore readers, low CPU

**Scenario:** News site served from one Virginia datacenter. Singapore readers see slow page loads. Servers at 15% CPU, spare memory, first-carrier link lightly loaded. Traffic crosses three carrier networks.

**Q1 (MCQ):** Best single fix? (D: keep copies of the articles near Singapore.)
**Your answer:** "D."
**Grade: correct.** Server resources and the first link are fine, so the delay is distance; a CDN keeps versions of the content closer to consumers.

**Q2 (open):** Editor: "We pay all three carriers, so we can demand they speed up." Reasonable?
**Your answer:** "Not reasonable, the limitation is latency not bandwidth, a physical property that carriers can't change. Also it depends on the SLA between you and the carrier."
**Grade: about 75%.** Latency as a physical limit is right; the SLA point is valid (beyond slides). Missing: with the cloud/carrier path, **QoS depends on the carriers** and the firm has no control over networks beyond its own. (The scenario's "we pay all three carriers" was unrealistic wording.)

**Overall: about 85%.**

---

## S4. Fraud check: 200 small reads across datacenters

**Scenario:** Fraud-detection code in Datacenter A reads about 200 small records from a database in Datacenter B, thousands of km away. A check takes 8 s. Engineer proposes a faster CPU.

**Q (open):** (a) Why will the faster CPU barely help? (b) What should change instead, and how does that behave differently?
**Your answer:** "It's a latency problem, which a faster CPU can't help with. The records are small, so it's not bandwidth. The team should cache the results nearer to Datacenter A, or choose a closer datacenter."
**Grade: about 80%.** Latency diagnosis and the bandwidth check were right; fixes right. Missed: 200 sequential round trips each cost the network delay (cost scales with the number of trips, not the data size), and the second half of (b): after the change, reads are local so each is fast (keep workloads local). A cache can serve stale copies (beyond slides). Best fix: run the code next to its data.

**Overall: about 80%.** Scenarios 2–4 overlapped heavily; remaining new idea (keep workloads local) moved into S5.

---

## S5. Startup's first private datacenter: commodity racks, chatty workers

**Scenario:** Architect wants a few custom high-end machines; vendor offers cheap identical servers in standard racks, grown by adding racks. The job's workers exchange a lot of data.

**Q1 (MCQ):** Best description of build-out and worker placement? (B: identical commodity servers in racks, racks replicated; keep workers in the same rack.)
**Your answer:** "B."
**Grade: correct.** (C, spreading workers across racks for fault isolation, is sensible in practice but beyond slides and adds network latency for a chatty job.)

**Q2 (open):** 42 1U servers per rack, 500 servers needed: how many racks, and what lets servers talk to each other and the rest of the datacenter?
**Your answer:** "About twelve racks, and the rack level switch."
**Grade: about 80%.** 500 / 42 = 11.9, so 12 racks: correct. Rack-level (Top Of Rack) switch correct, but only half the job given: it connects IT resources within the rack **and** connects the rack to the datacenter network. Rack also provides power and battery backup.

**Overall: about 90%.**

---

## S6. Image-resizing job: scratch buffer, shared table, original photos

**Scenario:** Three data kinds: (i) a worker's scratch buffer, (ii) a shared table of processed images read and updated by every worker, (iii) original photos in a storage system reached by all servers.

**Q1 (MCQ):** Best placement? (B: (i) local DRAM, (ii) distributed storage network, (iii) storage system reached over a network.)
**Your answer:** "B."
**Grade: correct.**

**Q2 (open):** Order fastest to slowest: other rack's memory, own DRAM, own disk, same-rack memory. Then gain and loss of keeping the table in another rack's memory instead of own DRAM.
**Your answer:** "Own DRAM, own disk, same-rack memory, other rack's memory. Slower is what's lost; what's gained is more space."
**Grade: about 50%.** Own DRAM fastest and "slower" and "more space" are right. Missed the main gain: the table becomes **shared state** that every worker can see and update; local DRAM is private to one server. The ordering is not answerable from the slides (flaw in the question, not counted against you): the standard datacenter reference figures (beyond slides) put memory reached across the rack/datacenter ahead of a spinning local disk.

**Overall: about 75%.**

---

## S7. Streaming company's datacenter links

**Scenario:** (1) datacenter-to-viewers link over the internet, (2) rack servers to a storage cabinet, (3) duplicated links among servers in a rack. Then peak-hour requests overwhelm one front-end server.

**Q1 (MCQ):** Name (1), (2), (3). (B: carrier interconnection, SAN, LAN.)
**Your answer:** "B."
**Grade: correct.**

**Q2 (open):** Which component spreads requests, and what two things does it depend on knowing about the servers?
**Your answer:** "A load balancer, probably an application load balancer because it routes user requests. I'm not sure about the last part."
**Grade: about 50%.** Load balancer is right. The "two things" half was outside L04 (health and load/capacity of targets belong to L03 on health checks), so not counted against you. L04 slide 21 names a network load balancer that manages data movement.

**Overall: about 75%.**

---

## S8. Dense racks: air cooling failing, water and seawater options

**Scenario:** Singapore operator, dense servers, nearly all electricity ends as heat, air cooling can't keep up. Options: (i) piped fresh water, (ii) site on the sea with seawater. Water authority later caps freshwater use.

**Q1 (open):** Why would water help, and what drawback follows?
**Your answer:** "Water is a thousand times more efficient than air at removing heat." (No drawback given.)
**Grade: about 50%.** Reason correct. Missing the drawback: **water usage is very high**.

**Q2 (open):** Freshwater capped: what option remains, and what does it address?
**Your answer:** "Move to seawater; it solves the problem of using the nation's potable water."
**Grade: correct.**

**Overall: about 75%.**

---

## S9. Monthly power breakdown and the efficiency ratio

**Scenario:** Servers 600 kW, storage 80 kW, network 70 kW, cooling 180 kW, distribution losses and lighting 70 kW. Goal: ratio as close to ideal as possible.

**Q1 (MCQ):** Which action brings it closest to ideal? (C: redesign cooling and power distribution.)
**Your answer:** "C."
**Grade: correct.** Cutting IT power (A, B) shrinks numerator and denominator and worsens the ratio. E was a weak distractor (more servers would add cooling load in practice).

**Q2 (open):** Current ratio, the ideal, and why a real datacenter can't reach it.
**Your answer:** "1.33, ideal is 1, there will always be unavoidable cooling, lighting and power distribution overhead."
**Grade: correct.** (750 kW IT, 1000 kW total, 1000 / 750 = 1.33.)

**Overall: 100%.**

---

## S10. 200 idle servers overnight

**Scenario:** 200 servers, 400 W peak each, idle nights and weekends. Management: idle servers cost nothing.

**Q1 (open):** Is management right? Idle fleet power? Ideal fleet power?
**Your answer:** "Wrong. 50% of peak = 200 W x 200 servers = 40,000 W while idle. Ideal would draw 0."
**Grade: correct.** (40 kW; slide says an ideal energy-proportional system draws *almost* no power when idle.)

**Q2 (MCQ):** Which describes an energy-proportional server? (C: almost no power idle, very little at light load, gradually more as load rises.)
**Your answer:** "C."
**Grade: correct.**

**Overall: 100%.**

---

## S11. Payments datacenter: choosing a tier

**Scenario:** Must service any power or cooling path without downtime; management wants every component duplicated; tolerance about 2 hours downtime per year; higher resilience costs more.

**Q1 (MCQ):** Lowest tier meeting the maintenance requirement? (C: Tier 3.)
**Your answer:** "C."
**Grade: correct.**

**Q2 (open):** Is Tier 4 justified given the tolerable downtime?
**Your answer:** "It's justified because it still satisfies the downtime requirement, but it is overkill."
**Grade: about 40%.** Self-contradictory, and the numbers were not used. Tier 3 (99.982%, about 1.6 h/year) already meets the 2-hour tolerance; Tier 4 (99.995%, about 26 min/year) adds cost for availability not needed. Not justified.

**Overall: about 70%.**

---

## Gap set (5 short questions)

1. MCQ on-premise vs cloud (QoS control, carriers): **B, correct.**
2. Why a shared total can't live in each worker's local DRAM: "private to each worker, no way to get the total." **Correct.**
3. Air to water cooling, benefit and cost: "increase in efficiency; water consumption still very high." **Correct.**
4. Tier 2 (99.741%) downtime vs 2 h tolerance: "22 hours, does not meet." **Correct** (about 22.7 h).
5. MCQ latency vs bandwidth (Singapore users, Frankfurt): **B, correct.**

**Overall: 100%.** L04 complete.
