# L10 Log

---

## S1. One app, three workloads

**Scenario:** PhotoBox on EC2. A: web backend, 4 servers 24/7, traffic flat for a year, expected to run 2+ more years. B: viral spikes without warning, extra servers for 20 min to a few hours, a few times a month. C: nightly 3-hour thumbnail batch that can resume after interruption; a day's delay is fine. Q1: pricing model for each, and why? Q2: a teammate wants to reserve enough servers to cover B's spikes because reserved is cheaper per hour. What goes wrong?

**Your answer:** Q1: "A: reserved, because the workload is steady (traffic flat); maybe combined with a Savings Plan because I can commit for two years. B: on-demand, because the workload is spiky. C: spot, because the job is not critical, so I get a lower cost; nobody minds late thumbnails and we can resume if interrupted." Q2: "I'm reserving enough for peak workloads, so I'm paying for more than I need during normal times."

**Grade: about 85%.** Q1 about 90%: all three picks right with the right reasons, and C correctly uses the fact that the job can be interrupted. Small slip: reserved and a Savings Plan are two alternative ways to commit for the same steady servers, not two things to stack on them. Q2 about 75%: the core idea (paying for idle capacity) is right, but the mechanism was not spelled out: a reservation is a commitment paid for the whole term, used or not, so the cheaper hourly rate only saves money on hours you actually use.

**Correct:** Q1: A: reserved (one-time upfront cost + a lower hourly rate than on-demand, s9) or, as an alternative, a Savings Plan (low prices for a commitment to consistent usage over a longer term, s9). Both pay off because the 4 servers really run every hour of the 2 years. B: on-demand: no commitment, billed per second (60 s minimum) only while the extra servers run (s9, s20), which suits short, unpredictable spikes. C: spot: unused capacity at a lower price, for jobs that are "not time critical" (s9). Spot capacity can be taken back, which is fine here because the job resumes and a delay costs nothing. Q2: a reservation runs from start date to expiry date with an upfront fee (s20), so you pay for every hour of the term whether the server is busy or not. Spike servers are busy a few hours a month, so almost all the reserved hours are wasted. Illustration (my numbers): on-demand $1/h vs reserved effectively $0.60/h. Reserved: about 730 h × $0.60 ≈ $438 per server per month. On-demand for 10 spike hours: $10. Also, viral spikes vary in size, so a fixed reservation can still be too small on a big spike and too big on a small one.

---

## S2. Which instance is cheaper for the job

**Scenario:** Encode 1,000 equal videos on on-demand EC2. X general purpose $0.20/h, 10 videos/h; Y compute optimised $0.34/h, 20/h; Z memory optimised $0.50/h, 12/h. Q1: cheapest for the whole job, total cost of each, why the cheapest per hour is not cheapest overall? Q2: 1,000 small jobs of 30 s each on Y: one new instance per job (shut down after) vs one instance running all back to back. Cost of each and why they differ?

**Your answer:** Q1: "$20, $17 and $41. General purpose is cheapest per hour but compute optimised encodes more videos per hour, so it runs for less time overall and costs less. Choosing the right type of server matters." Q2: "On-demand charges to the nearest second with a 60-second minimum, so each job is billed 60 s if I launch one instance per job: $16.66; back to back: $8.33."

**Grade: about 85%.** Q1 100%. Q2 about 70%: the 60-second-minimum mechanism is right, but both totals are hours, not dollars (the $0.34/h rate was never applied). Second arithmetic slip of this kind (L07 G5 was off by 100x).

**Correct:** Q1: cost per video = price per hour ÷ videos per hour: X $0.020, Y $0.017, Z ≈ $0.042, so totals X $20, Y $17, Z $41.67. Y wins because the job needs a fixed amount of work, and Y's speed (compute optimised for CPU-heavy encoding, s7) more than offsets its higher hourly price. Q2: on-demand bills to the second with a 60 s minimum (s9). One instance per job: each 30 s job is billed 60 s → 1,000 × 60 s = 16.67 h × $0.34 = **$5.67**. Back to back: 1,000 × 30 s = 8.33 h × $0.34 = **$2.83**. Short-lived instances pay for time they never use, so batching short jobs on one instance halves the bill.

---

## S3. Who sends you the bill

**Scenario:** A school wants QuizHub (SaaS on Cloud B's IaaS). Offer 1: $3 per registered student per month to QuizHub, which pays Cloud B itself. Offer 2: $1 per student per month to QuizHub, and the school pays Cloud B directly for QuizHub's servers under its own account. Q1: which pricing model is each; under Offer 2, one advantage and one risk vs Offer 1? Q2: in exam week, student count unchanged, usage triples and QuizHub needs 3× the servers. What happens to the school's bill under each offer, and why?

**Your answer:** Q1: "Offer 1 integrated, Offer 2 separate. Advantage: it probably pays less because it pays each provider directly. Risk: with Offer 1 it could lock in a preferential rate; with Offer 2 there are two separate contracts, so payments are less predictable: if the IaaS provider changes its prices you can't lock in the rate." Q2: "Under integrated pricing it's still one price; as long as it falls under the contract, the SaaS provider is obliged to pay it. Under Offer 2 the school pays more to the IaaS provider because it needs three times the servers, so the bill spikes. Not predictable, which is also the risk in Q1."

**Grade: about 75%.** Q1 about 70%: names right; risk right (unpredictable bill, two contracts). Advantage vague: not said why it is cheaper (no SaaS markup or safety margin on hosting; pays actual usage; sees the hosting cost). Q2 about 85%: outcomes right, but not tied to the price drivers (Offer 1 is per registered student, which did not change; the $1 part of Offer 2 also stays; the Cloud B part is priced by number of servers).

**Correct:** Q1: Offer 1 = integrated pricing (consumer pays SaaS provider, which pays the IaaS provider, s10-11); Offer 2 = separate pricing (consumer pays both, s10, s12). Advantage of Offer 2 (my reasoning): the fixed $3 under Offer 1 includes QuizHub's markup and a margin for heavy months; under Offer 2 the school pays Cloud B's actual usage price, so a normal month is cheaper and the hosting cost is visible. Risks: the hosting bill varies with usage and Cloud B's prices, and the school must manage a second contract and its own Cloud B account. Q2: Offer 1: bill = $3 × registered students (SaaS priced by number of nominated consumers, s6), unchanged; QuizHub absorbs its tripled Cloud B bill. Offer 2: the $1 × students part is unchanged; the Cloud B part is priced by number of virtual servers, data transferred and storage (IaaS pricing, s6), so it roughly triples. Integrated pricing puts the usage risk on the SaaS provider; separate pricing puts it on the consumer.

---

## S4. Building a monthly bill

**Scenario:** Inbound and intra-cloud traffic free. Outbound, totalled over the month: first 100 GB free, next 9,900 GB $0.09/GB, above 10,000 GB $0.05/GB. Storage $0.10 per GB-month, charged only for days allocated. Month (30 days): 3,000 GB uploads, 12,100 GB downloads, 5,000 GB between own servers, 2,000 GB replicated to a backup at a different provider; 500 GB storage all month plus 3,000 GB for the last 10 days. Q1: network bill (what counts, what doesn't)? Q2: storage bill?

**Your answer:** Q1: "Outbound is 12,100 + 2,000 GB. The first 100 GB is free, leaving 14,000; above 10,000 costs $0.05/GB, so $700. Uploads and intra-cloud traffic are free, so they are not considered." Q2: "$150."

**Grade: about 70%.** Q1 about 50%: classification fully right (downloads and inter-cloud replication count as outbound; uploads and intra-cloud do not). Calculation wrong: applied the top tier's rate to all 14,000 GB instead of charging each band at its own rate. Q2 100%.

**Correct:** Q1: outbound = 12,100 + 2,000 = 14,100 GB (inter-cloud replication leaves this cloud, s19; inbound and intra-cloud often not charged, s19). Tiered pricing charges each band at its own rate: 100 GB free; 9,900 × $0.09 = $891; 4,100 × $0.05 = $205; total **$1,096**. Check: charging everything at the top rate would make 10,001 GB cheaper than 9,999 GB. Q2: storage is charged for the time it is allocated (allocation to release, s21): 500 × $0.10 = $50, plus 3,000 × $0.10 × 10/30 = $100; total **$150**.

---

## S5. Should we move to the cloud?

**Scenario:** Firm P bought new servers and licences 6 months ago for $400k (5-year life); its core system is a 15-year-old custom program talking directly to warehouse barcode scanners. Firm Q is 2 years old, short of cash, bank charges 12% interest; second-hand servers failing; off-the-shelf software. Q1: for each, which cost factors push toward and against the cloud, and what do you recommend? Q2 (false statement): A. cloud replaces a large up-front cost with ongoing costs; B. high cost of borrowing makes leasing cloud resources more attractive; C. lock-in costs are paid when a company first moves its own servers to a cloud provider; D. integration costs include making existing systems work on the new platform; E. ongoing costs (licensing, electricity, maintenance) are usually higher on-premise.

**Your answer:** Q1: "P: against the cloud: they just bought new hardware lasting five years, that is their depreciation; the core system is so custom it probably needs to run on their own servers. Recommend not moving. Q: short of cash, can't afford heavy investment in hardware, and the bank charges high interest, so borrowing for high capex makes no sense; the cloud converts capex to opex; off-the-shelf software runs easily on the cloud; servers are failing, so it's a perfect push to the cloud, spreading spending over the years." Q2: "C."

**Grade: about 85%.** Q1 about 80%: Q fully right (cost of capital, capex to opex, low integration cost, failing servers). P right in substance but not in the slide's terms or mechanism: the recent $400k is a **sunk cost** (not "depreciation"), and the custom scanner system is a high **integration cost** (it can move, but making it work on a cloud platform takes a lot of effort), not something that "needs" its own servers. Recommendation better as "not now; reconsider when the servers reach end of life". Q2 100%.

**Correct:** Q1: P: sunk costs: a significant prior investment in existing IT that still has 4.5 years of use; moving now means paying for the cloud while that hardware sits unused, so the move cannot be justified (s15). Integration costs: the effort to make the custom scanner system inter-operate on a new cloud platform is high, which makes the cloud less appealing (s16). Toward the cloud: only lower ongoing costs (s14), small next to the above. Recommend: stay on-premise for now and re-evaluate when the hardware is due for replacement. Q: cost of capital is high (12% interest), so leasing cloud resources is justified (s15); the cloud has low up-front Capex instead of buying hardware (s14); off-the-shelf software means low integration cost (s16); failing second-hand servers mean no significant sunk cost to protect, and replacing them would be a new Capex. Recommend the cloud; keep in mind lock-in costs if Q later wants to change provider (s16). Q2: C. Lock-in costs are the cost of moving from one cloud provider to another (s16); the first move is an integration cost.

---

## S6. Owning a datacenter

**Scenario:** Own datacenter, two designs, shares of TCO. Design 1 (expensive high-end servers): server depreciation 66%, power 7%, building (depreciation + interest + Opex) 16%, other 11%. Design 2 (cheap, higher-power servers): 30%, 26%, 39%, 5%. Q1: a manager says Design 2 is worse because power and building are a much bigger part of costs. What is wrong, and what would you need to decide? Q2: Design 2 chosen; building designed for 1,000 servers, only 500 run. What happens to building cost per running server, and why does the building's share grow while power's shrinks?

**Your answer:** Q1: "Servers are usually more expensive, so the datacenter building would be less in absolute dollars than the server depreciation. To decide I'd need the absolute cost first, and second whether we really need the high-end servers or can stick to cheaper ones." Q2: "The building cost per running server goes up, and correspondingly the depreciation cost of the building goes up; even though power cost comes down, depreciation goes up more than power, so the building's share grows while the power share shrinks."

**Grade: about 55%.** Q1 about 60%: "need the absolute cost" is the key, but the reason was not stated: each percentage is a share of a different total, so a bigger share of a smaller total can be fewer dollars. "Do we need high-end servers" points the right way but should be "total cost for the same amount of work". The first sentence (building less than server depreciation) is off the point. Q2 about 50%: cost per running server rising is right, but the mechanism was wrong: the building's total depreciation does **not** go up. It is fixed (built for 1,000, written off per year whether used or not); what changes is that it is spread over 500 servers and the total shrinks around it.

**Correct:** Q1: the pie charts give shares of each design's own total (s26-27), not dollars. Design 2's servers are much cheaper, so its total is smaller, and 26% of a small total can be fewer dollars than 7% of a large one. Its power and building shares look big largely because the server slice shrank (s27: "server depreciation went down"). To decide: the total TCO of each design per year (datacenter depreciation + datacenter Opex + server depreciation + server Opex, s24), divided by the work each delivers (TCO per unit of useful work). Q2: datacenter Capex is an up-front investment depreciated over a set time frame (s23), so the yearly building charge is the same at 500 or 1,000 servers. Per running server it doubles. Power and server costs scale with the servers actually running, so they roughly halve. The total TCO shrinks, the fixed building charge stays, so the building's share rises (s28: DC amortisation 18.5% → 32.4%) and the power share falls (server power 14.3% → 8.4%).

**Follow-up question (S6):** "If the total shrinks but the building charge doesn't, do all the other rows apart from power go up too?" **Answer:** no. Only the rows tied to the building (DC amortisation 18.5% → 32.4%, DC interest 10.3% → 18.1%, DC Opex 10.6% → 12.4%) grow, because they are fixed. Every row tied to the number of running servers shrinks in dollars and in share: server amortisation 29.5% → 17.3%, server interest 3.8% → 2.2%, server Opex 1.5% → 0.9%, server power 14.3% → 8.4%, PUE overhead 11.5% → 8.4% (s27-28).

---

## Gap set

**Questions:** G1: outbound first 50 GB free, up to 5,000 GB total at $0.08/GB, above 5,000 GB at $0.04/GB; 7,050 GB out, 2,000 GB in (free). Bill? G2: building $1.2M/yr depreciation; each server $500/yr depreciation + $300/yr power. Building cost per running server and building share of TCO at 1,000 and at 500 servers? G3: name the cost: (a) university bought a $2M storage system last year, weighing cloud storage; (b) company on Cloud A wants cheaper Cloud B but its app relies on A's own message-queue service; (c) bank wants its 20-year-old mainframe system to work with a new cloud platform. G4: X TCO $1M/yr, 10% power; Y TCO $300k/yr, 25% power; same workload. Which spends more on power, which is cheaper overall?

**Your answer:** G1: "$480." G2: "$1,200 and $2,400 per server; 60% and 75%." G3: "(a) sunk, (b) locked-in, (c) integration." G4: "Y spends more on power, but X is cheaper overall."

**Grade: about 70%.** G1 about 90%: band method right; $2 off because the $0.08 band is 4,950 GB (from 50 to 5,000), not 5,000 GB. G2 100%. G3 100%. G4 0%: both parts wrong. Joshua: a calculation slip, not a misconception (S6 Q1 did say absolute costs are needed), so no star.

**Correct:** G1: 50 GB free; 4,950 × $0.08 = $396; 2,050 × $0.04 = $82; total **$478**. G2: 1,000 servers: building $1.2M ÷ 1,000 = $1,200 per server; servers 1,000 × $800 = $0.8M; total $2.0M; building share 60%. 500 servers: $2,400 per server; servers $0.4M; total $1.6M; share 75%. G3: (a) sunk cost (s15); (b) locked-in cost (moving between providers, s16); (c) integration cost (s16). G4: convert shares to dollars first: X power = 10% × $1M = **$100k**; Y power = 25% × $300k = **$75k**. X spends more on power, and Y is cheaper overall ($300k vs $1M for the same work). Y's power share is bigger only because its total is much smaller.
