# L02 Scenario Log

A record of each scenario, what you answered, how it was graded, and the correct answer. Reference only: the concepts live in `L02-Concepts-Models.md` and the index. Answers are lightly trimmed from your spoken replies.

---

## S1. LAMP retailer moves to the cloud (SaaS / PaaS / IaaS)

**Scenario:** A Singapore online retailer runs its shop on its own server room on a LAMP stack (Linux, Apache, MySQL, PHP) installed by a two-person IT team. The hardware is ageing and they want to move to a public cloud.

**Q1 (MCQ):** Move the shop as it is, with the least change to code and setup. Which model? (A SaaS, B PaaS, C IaaS, D none: the stack can't move unchanged.)
**Your answer:** "Probably platform as a service, because they probably already have the code. They just need to publish it to an environment that supports the LAMP stack."
**Grade: wrong.** Correct is **C, IaaS**. The team installs and manages the OS, Apache, MySQL and PHP themselves, so they need virtual machines they control (lift-and-shift). PaaS supplies the runtime and database, so the app must fit what the platform supports: more change, not less.

**Q2 (open):** Six months later they switch to the provider's managed MySQL service (backups and patching included) and leave the rest as it is. Which model is that database part, and what stops being their job?
**Your answer:** "Software as a service, because the managed MySQL database is software provided as a service. What stops is the installing, patching and maintenance of the software, backups and patching."
**Grade: half right.** Model wrong, job right. It is **PaaS** (a database service is platform software that developers put inside their own app). SaaS is a finished application used by an end user. The patching, maintenance and backups moving to the provider were correct. They still own their data and application code.

**Q3 (MCQ):** Finance moves to a provider's finished accounting application. Which statement is false? (B: the finance team still manages the application's operating system.)
**Your answer:** "B is wrong. That is taken care of by the provider."
**Grade: correct.** In SaaS the consumer manages only its data (slide 19).

**Overall: about 50% (1.5 of 3).**

---

## S2. Clinic booking system (responsibility split, pros and cons)

**Scenario:** A 30-person clinic group with no developers or IT staff wants an online patient-booking system. Three quotes: X = rent virtual machines and have a contractor build and run the software; Y = rent a ready-made application server and database and have a contractor write the booking logic; Z = subscribe to a vendor-hosted booking application.

**Q1 (MCQ):** Live in 3 weeks, standard features enough. Which option, and which drawback is accepted?
**Your answer:** "A."
**Grade: correct.** Z (SaaS), accepting the lowest flexibility to customise.

**Q2 (open):** "With Z the vendor handles everything, so we carry no responsibility for the patient records." Right or wrong? Name one thing the clinic looks after under Y that it does not under Z.
**Your answer:** "It's not right. The clinic still has to handle the management of the patient's data. Under Y, the application code, the code of the actual booking application."
**Grade: correct.** The consumer keeps its data in every model. Under Y the clinic also owns the application (its contractor writes it). Slide 19: PaaS consumer = Data, Application; SaaS consumer = Data only.

**Q3 (MCQ):** Moving from X to Y to Z, which statement is false? (D: the provider takes on less of the stack.)
**Your answer:** "D is false."
**Grade: correct.** The provider takes on more, the consumer less, speed rises and flexibility falls.

**Overall: 100% (3 of 3).**

---

## S3. Tutoring company compares providers (NIST essential characteristics, 5/4/3)

**Scenario:** An online tutoring company compares cloud providers for its lesson platform.

**Part A (open):** Provider Q's sales sheet: "Email your account manager and we provision more storage within 2 working days. Flat monthly fee whatever you use." Which two of the five essential characteristics is Q missing, and why?
**Your answer:** "Q is missing the essential characteristics of measured service and rapid elasticity."
**Grade: about 50%.** Measured service is correct (flat fee, not pay per use). The second is **on-demand self-service**: the sheet provisions through an account manager by email, with no portal and no self-provisioning. Rapid elasticity is not the giveaway. Ground truth is the official NIST definition (slide 4 is shorthand): self-service = the consumer provisions capability by themselves without human interaction with the provider. No reasons were given, although the question asked for them. (Briefly regraded to 75% after the slide's terse wording was raised, then restored: the NIST definition decides.)

**Part B (MCQ):** Provider P pools servers across customers; students in three countries use phones and laptops with a browser; the company doesn't know which datacenter runs it. Which pair?
**Your answer:** "C, showing broad network access from anywhere and resource pooling."
**Grade: correct.**

**Part C (MCQ):** Which consultant statement about 5/4/3 is correct?
**Your answer:** "B."
**Grade: correct.** SaaS, PaaS and IaaS are the three service models. DBaaS and FaaS are variants (slide 18). FaaS is not a deployment model.

**Overall: about 83%.**

---

## S4. Shop with no servers (variants of service models)

**Scenario:** A small online shop wants to run no servers of its own. Needs: (1) store invoice PDFs for years, (2) hold order records its app reads and writes constantly, (3) run a small piece of code that resizes each uploaded product photo with no machine to look after, (4) have an outside company scan the site for vulnerabilities monthly.

**Part A (open):** Name the "as-a-Service" offering that matches each need.
**Your answer:** "One and two feel like infrastructure as a service, where the database is provided for you. Three feels like platform as a service, running my code on a platform provided to me. Four feels like software as a service, where the outside company provides that software."
**Grade: about 25%.** Named the three base models, not the variants asked for. Expected: (1) Storage-as-a-Service, (2) Database-as-a-Service, (3) Function-as-a-Service, (4) Security-as-a-Service. Calling a managed database IaaS repeats the S1 error: a managed database is platform software (PaaS side).

**Part B (MCQ):** Founder claims NIST now has more than three service models. Best response? (B: the three are SaaS, PaaS, IaaS and these are single-capability variants.)
**Your answer:** "B."
**Grade: correct.**

**Part C (open):** Which need is serverless computing, and what does serverless mean for the team day to day? Is a server really absent?
**Your answer:** "Number three. Serverless means it's lightweight, it triggers upon something and then finishes that thing fast. There is still a server in the back end, but it is taken care of by the provider."
**Grade: about 85%.** Need 3 is correct. Key point correct: servers exist but the provider provisions and manages them, so the team has nothing to look after. "Triggered, short-lived" is event-driven behaviour, which is L06 material (beyond L02 slides).

**Overall: about 70%.**

---

## S5. Health-tech launches in Indonesia (combining service models, data residency)

**Scenario:** A Singapore health-tech company launches an app in Indonesia; law requires patient data to stay in Indonesia. It subscribes to a platform service from Provider X, which has no Indonesian datacenter, so X runs its platform on virtual servers rented from Provider Y in Jakarta. (Format: MCQ, MCQ, open. Reshaped from an earlier open, MCQ, open draft at Joshua's request.)

**Q1 (MCQ):** Who supplies what? (A: company writes the app; X supplies the platform software; Y supplies the virtual servers to X.)
**Your answer:** "A."
**Grade: correct.**

**Q2 (MCQ):** Where is the patient data physically stored? (B: Jakarta, because X's platform runs on Y's infrastructure in the same region as the users.)
**Your answer:** "B."
**Grade: correct.**

**Q3 (open):** "Stacking a platform on rented virtual servers is just hybrid cloud." Agree?
**Your answer:** "I don't think that's hybrid cloud. Hybrid cloud consists of two or more clouds that remain as distinct entities, not stacking a platform on top of infrastructure. That's just the cloud broken down into different levels and different as-a-service."
**Grade: about 85%.** Correct. Hybrid = two or more distinct clouds, connected for data and application interoperability (slide 45). Stacking PaaS on IaaS is layering of service models. Loose wording: "stacking clouds" should be "stacking service models". Service models say what layer is offered; deployment models say how and for whom clouds are set up.

**Overall: about 95%.**

---

## S6. Bank, consultant, telco and auditor (the five actors, purpose of the reference model)

**Scenario:** Bank B uses cloud services offered by Company P. Firm C negotiates contracts with P and a second provider R and manages the bank's use of both. Telco T provides the network link. Independent Firm A assesses P's security, privacy handling and performance. (Format: four MCQs, no open question.)

**Q1 (MCQ):** Map C, T, A to NIST actors. (A: C broker, T carrier, A auditor.)
**Your answer:** "A."
**Grade: correct.**

**Q2 (MCQ):** Pages load slowly but P's servers show normal response times. Whose responsibility is the first place to check?
**Your answer:** "The assessment of performance falls on the cloud auditor."
**Grade: wrong.** Correct is **the cloud carrier (C)**. P's servers are fine, so the slowness is in the connectivity between provider and consumer, which is the carrier's job (connectivity and transport). The auditor assesses performance independently, as a review, not as the first place to look for a live slowdown.

**Q3 (MCQ):** Firm A's report covers (i) lawful handling of personal data, (ii) meeting contract response times, (iii) whether P could be talked into a lower price. Which belong to the auditor?
**Your answer:** "One and two" (speech-to-text wrote "eight" for A).
**Grade: correct.** (i) privacy and (ii) performance are auditor work. (iii) is the broker's job.

**Q4 (MCQ):** "NIST's reference model is the blueprint for exactly how to build a compliant cloud." Best response? (B: it describes what services provide, not how; vendor-independent; not any specific cloud's architecture.)
**Your answer:** "B. It is vendor independent and not the architecture of any specific cloud."
**Grade: correct.**

**Overall: 75% (3 of 4).**

---

## S7. Retailer hires a broker (intermediation, aggregation, arbitrage)

**Scenario:** A retailer hires a broker firm. Offerings: (a) Provider 1's storage plus single sign-on and a reporting dashboard, resold to the retailer; (b) Provider 1's storage and Provider 2's analytics combined into one service with a single login and secure data movement between them; (c) each month, run batch jobs on whichever of several providers is cheapest. (Format: MCQ then open.)

**Q1 (MCQ):** One integrated offering from both providers with secure data movement between them. Which broker service? (B: service aggregation.)
**Your answer:** "B, service aggregation."
**Grade: correct.**

**Q2 (open):** Name the broker services behind (a) and (c), and say what makes (c) different from (b).
**Your answer:** "A is service intermediation, value-added services. C is service arbitrage, the flexibility to choose services from multiple providers. B is service aggregation: it involves more than one provider, but it's not choosing between two providers, it's combining and integrating multiple services from different providers."
**Grade: correct.** (a) intermediation, (c) arbitrage; aggregation merges services into something new, arbitrage chooses among providers without merging them.

**Overall: 100%.**

---

## S8. CloudCo's operations (cloud service management, portability, security and privacy)

**Scenario:** A new CTO reviews how provider CloudCo runs its service day to day. (Format: open, open, MCQ.)

**Q1 (open):** Sort four activities into Business Support, Provisioning/Configuration, Portability/Interoperability: (1) automatically deploying a requested virtual server, (2) setting prices and sending invoices, (3) measuring each customer's storage and compute use, (4) letting a departing customer bulk-export data.
**Your answer:** "(1) provisioning/configuration, rapid deploying. (2) business support. (3) business support, because it's consumer facing. (4) portability and interoperability, a mechanism that supports data portability."
**Grade: 75%.** (1), (2), (4) correct. (3) wrong: **metering is Provisioning/Configuration** (slide 29–30 lists Rapid Provisioning, Resource Change, Monitoring & Reporting, Metering, SLA Management). Billing, pricing and invoicing are Business Support. "Consumer facing" is not a reliable test: measuring is technical, charging is commercial.

**Q2 (open):** A customer wants to leave CloudCo for a rival and have CloudCo's service work with the rival's during the move. Which two needs, and what is the difference?
**Your answer:** "Portability to move the data out of CloudCo, and interoperability to use the two services together during the move. One is movement, the other is using the two together."
**Grade: about 90%.** Correct. Portability = moving data or a system (VM images, apps) to another provider; interoperability = services from different providers working together.

**Q3 (MCQ):** "Security is its own layer below the physical resources." Correct response? (B: security is cross-cutting, spans all layers and all relevant actors; privacy concerns PI/PII.)
**Your answer:** "B. Security spans all layers."
**Grade: correct.**

**Overall: about 88%.**

---

## S9. Hospital moves patient records to a public cloud (trust boundary, carrier, auditor)

**Scenario:** A hospital group moves its patient-records system from its own server room to Provider P's shared public cloud. P reaches the hospital through network operator N. The board wants proof P is trustworthy. (Format: MCQ, open, open.)

**Q1 (MCQ):** Which statement about the move is false? (C: the hospital keeps the same level of governance control.)
**Your answer:** "C is false, because the level of governance control that the hospital has goes down."
**Grade: correct.**

**Q2 (open):** P promises 99.9% availability but the hospital had a long outage while P's servers stayed up. How can that happen, and what arrangement should P have?
**Your answer:** "If P is fine but the hospital is not, it has to be a problem with the cloud carrier, the network. P should have an SLA with their cloud carrier."
**Grade: about 90%.** Correct. Missing: slide 35 also lists a dedicated, secured connection as an arrangement. P's promise is bounded by the carrier's SLA.

**Q3 (open):** What does the cloud auditor do that makes its opinion more credible than P's own statement?
**Your answer:** "It takes an independent stance, an independent examination of controls, and it's objective. P is the provider and may be biased, but the auditor is an independent unbiased body."
**Grade: about 80%.** Independence and objectivity correct. Missing the mechanism: the auditor examines controls through review of **objective evidence** to verify compliance with regulation and security policy and conformance to standards (slide 33).

**Overall: about 90%.**

---

## S10. Booking app for 500 clinics (single vs multi-tenancy)

**Scenario:** A software vendor sells an appointment-booking app to 500 small clinics, running one copy of the app that serves all of them, with each clinic's data kept separate inside it. A large hospital group asks for its own separate copy instead. (Format: open, MCQ.)

**Q1 (open):** Why does the shared arrangement lower the vendor's cost, and what might a cautious clinic worry about?
**Your answer:** "Multi-tenancy. Low cost because the vendor doesn't need to customize the app for every clinic. The worry: if one clinic is compromised, that may compromise all 500 clinics' data, like a single point of failure."
**Grade: about 60%.** Multi-tenancy correct. Cost reason wrong: the saving comes from **pooling**: one instance serves many tenants, so the vendor runs and maintains one thing and uses resources more fully (slide 6), not from skipping customisation. The worry is right (shared exposure, overlapping trust boundaries, slide 32). "Single point of failure" is loose: it is shared exposure, a single point of compromise.

**Q2 (MCQ):** The hospital wants its own separate copy. Which statement is correct? (C: shared copy is multi-tenant, own copy is single-tenant; the hospital pays for more isolation and typically more cost.)
**Your answer:** "C."
**Grade: correct.**

**Overall: about 80%.**

---

## S11. Choosing deployment models for five organisations

**Scenario:** For each organisation, name the deployment model and one reason. (a) two-person app start-up, no IT staff, unpredictable usage, little upfront spend; (b) large bank, big in-house IT team, highly sensitive data, wants exclusive access; (c) five regional hospitals under the same regulator, same compliance needs, none can afford its own private cloud; (d) retailer wanting customer records under its own control but a public web shop on cheap flexible capacity; (e) the bank later wants exclusive access without running a server room: name two ways, how they differ, and what question the lecture raises. (Format: one question, five parts, no MCQ.)

**(a)** **Your answer:** "Public cloud. It's a general public thing, it has no specific requirements."
**Grade: model correct, reason about 60%.** Slide 38 reasons: low upfront cost with pay-as-you-go, available anytime and anywhere, maintenance handled by the provider. No IT staff plus unpredictable usage fits those.

**(b)** **Your answer:** "Private cloud: large scale, exclusive access, a private place for the sensitive data."
**Grade: about 90%.** Correct. Slides 36, 39: high control for sensitive data, restricted access, maintenance mainly in-house, suited to large-scale IT.

**(c)** **Your answer:** "Community cloud. The five hospitals form a community with similar operational and regulatory needs, and it is more affordable than each having its own private cloud."
**Grade: 100%.**

**(d)** **Your answer:** "Hybrid: private cloud for customer records, public cloud for the web shop."
**Grade: 100%.** Slide 45: balance control and cost.

**(e)** **Your answer:** "An outsourced private cloud, operated by a third party. Another is a virtual private cloud, a secure environment within the public cloud. The question is security; it's obviously less secure than an on-site private cloud."
**Grade: about 65%.** Both options correct and each described correctly. Missing the key difference: out-sourced private = **dedicated** resources hosted by a third party, reached from your enterprise network; VPC = an isolated environment **inside shared public infrastructure**. The slide's question is "Security? On-site vs out-sourced": it only poses the question; "obviously less secure" overclaims.

**Overall: about 83%.**

---

## S12. Health ministry and a sovereign cloud (sovereign cloud, data residency)

**Scenario:** A European health ministry stores citizens' health records in the cloud. Law: records and their metadata stay inside the country; no foreign authority or staff may access them under any circumstances. (Format: two MCQs, each with a follow-up.)

**Q1 (MCQ + follow-up):** Which offering is designed for this? (C: sovereign cloud.) Why is the closest wrong option not enough?
**Your answer:** "C, sovereign cloud. The closest wrong option is private cloud, because it is also meant for sensitive data, but it is not enough because of the scale of this data; private cloud would be extremely costly at that scale."
**Grade: MCQ correct; follow-up about 35%.** Cost is not the reason. Private cloud is exclusive control by one organisation and can sit in another country or be run by foreign staff, so it does not guarantee that data **and metadata** stay in the country or that foreign access is prevented. Region choice (D) is the other close wrong option: it keeps data in a geography but does not stop foreign access. Sovereign = national or jurisdictional control (slide 47).

**Q2 (MCQ + follow-up):** A global vendor offers a dedicated private cloud in an in-country datacenter run by its engineers worldwide. Which statement is correct? (C: it does not necessarily satisfy the ministry.) Name the two things to ask the vendor to guarantee.
**Your answer:** "C. Ask whether it prevents foreign access under all circumstances and whether it adheres to all local data protection laws."
**Grade: MCQ correct; follow-up about 90%.** Both are the slide's organisational needs. Add: data and metadata stored within national borders.

**Overall: about 80%.**

---

## G1. Provider architecture (service orchestration vs cloud service management)

**Scenario:** A provider's engineer describes the architecture under Service Orchestration: Service Layer holds buildings, power and cooling; Resource Abstraction and Control Layer offers SaaS, PaaS and IaaS; Physical Resource Layer holds the software that splits servers into VMs; billing, pricing and SLA management belong in these three layers. (Format: one question, two open parts. Note: the question said "three mistakes" but the description contains four; the error was mine.)

**Part A (open):** Find the mistakes and give the correct statements.
**Your answer:** "The service layer consists of SaaS, PaaS or IaaS. The middle layer, resource abstraction and control, contains the software that splits our servers into VMs and controls allocation. The bottom physical resource layer holds the buildings, power and cooling. And billing, pricing and SLA don't belong in these three layers."
**Grade: full marks.** All four found. Detail: the Physical Resource Layer holds Hardware and Facility (slide 28).

**Part B (open):** What is service orchestration and how does it differ from cloud service management?
**Your answer:** "Service orchestration is orchestrating the resources to provide the service to the consumer; cloud service management is related to the actual provisioning of the service, which is where billing, pricing and SLA management fall."
**Grade: about 85%.** Orchestration correct (arrangement, coordination and management of computing resources). Cloud service management is wider than provisioning: Business Support (billing, pricing), Provisioning/Configuration (metering, SLA management) and Portability/Interoperability (slide 29).

**Overall: about 90%.**

---

## G2. Operations manager's six requests (consumer use cases by service model)

**Scenario:** Classify six requests as SaaS, PaaS or IaaS consumer use cases with a short reason: (1) ready-made CRM, (2) environment to build and test an internal app without setting up servers, (3) managed database and BI tooling for analysts to build dashboards, (4) CDN for worldwide video, (5) backup and recovery capacity for servers, (6) own application-server stack on rented machines with full platform control. (Format: one question, six parts.)

**Your answer:** "1 SaaS, a ready-made software. 2 PaaS, an environment for developers. 3 PaaS, tooling for analysts to build on. 4 IaaS, seems to be infrastructure. 5 IaaS, server related. 6 IaaS, the provider just provides rented machines."
**Grade: about 90%.** All six correct. Reasons for 4 and 5 were guesses: slide 26 lists CDN and Backup & Recovery under IaaS consumer use cases. #6 is IaaS "Platform Hosting": you install and run the platform software yourself, unlike #2 where the provider supplies the platform.

**Overall: about 90%.**

---

## G3. FreshCart's cloud review (re-test of six earlier mistakes)

**Scenario:** Eight claims from a grocery-delivery company's cloud review; mark each correct or incorrect and fix the incorrect ones. (Format: one list, eight parts.) Claims 1 (managed PostgreSQL = IaaS), 2 (create a server in minutes with no one at the provider = rapid elasticity), 3 (FreshCart still holds responsibility for its own data under SaaS), 4 (usage counters that measure compute hours = Business Support), 5 (slow pages, provider dashboards normal: first look at the auditor), 6 (shared app instance cheaper because no per-customer customisation), 7 (private cloud in a home-country datacentre makes data sovereign), 8 (private customer records plus public web shop = hybrid).

**Your answers:** 1 wrong, PaaS. 2 true, "stuff can spin up and spin down fast". 3 true. 4 true. 5 wrong, the carrier. 6 not true, resource pooling and higher utilisation. 7 not true, needs compliance, local data protection law and no foreign access. 8 true.
**Grade: 75% (6 of 8).**
- 1, 3, 5, 6, 7, 8: correct. For 7 add: data **and metadata** within national borders.
- **2: wrong.** Creating a server through a portal in minutes with no one at the provider is **on-demand self-service** (official NIST: the consumer provisions by themselves without human interaction with the provider). Rapid elasticity is capacity scaling out and in with demand. Slide 4's wording is shorthand and misleading here; the NIST definition decides. (Briefly half credit, then restored.)
- **4: wrong (repeat of S8).** Measuring compute hours is **metering**, Provisioning/Configuration. Billing and pricing are Business Support.

**Overall: 75%.**
