# L02 Concept Cards

Built by DeepSeek V4.1 Flash from the slide text plus diagram facts (transcribed by Claude Haiku, spot-checked against the slide images). Cards are the source for writing scenarios. 'Type: Application' = can be tested in a scenario; 'Reference-only' = lookup. '(inferred)' = not stated on a slide. For past-paper links, trust Notes/PAST-PAPER-MAP.md over the card's Past-paper line (cards miss some, e.g. sovereign cloud 24S2 Q16, 25S2 Q23).

### L02-C01 NIST 5-4-3 key components
- **Slides:** 3, 5
- **Type:** Reference-only
- **What it is:** NIST 2011 splits cloud into **five essential characteristics**, **four deployment models** (public, private, community, hybrid) and **three service models** (SaaS, PaaS, IaaS).
- **Look-alikes:** 5/4/3 counts swapped (e.g. "3 deployment, 4 service models"); variants such as DBaaS/FaaS counted as the three service models — the slide lists only SaaS, PaaS, IaaS as the models and puts the rest under "Variants of Service Models" (slide 18).
- **Limits / trade-offs:** None stated on the slide; it is a taxonomy, not a design.
- **Situation cues:** "how many essential characteristics does NIST define", "list the deployment models", "is function-as-a-service one of the three service models".
- **Past-paper Qs:** 24S2 Q2

### L02-C02 Essential characteristics: self-service, elasticity, metering
- **Slides:** 4
- **Type:** Application
- **What it is:** **On-demand self-service** (provision via a service portal), **rapid elasticity** (time to market / fast deployment) and **measured service** (pay-per-use).
- **Look-alikes:** On-demand self-service vs rapid elasticity — self-service is *who/when you request* capacity, elasticity is *how fast capacity changes*; rapid elasticity vs resource pooling — elasticity is about scaling with demand, pooling is about sharing one pool across customers.
- **Limits / trade-offs:** None stated; note pooled/elastic services are what make pay-per-use metering meaningful.
- **Situation cues:** "no human intervention", "self-service portal", "scale up for a spike then back down", "billed only for what is used".
- **Past-paper Qs:** 24S2 Q4

### L02-C03 Essential characteristics: broad access, resource pooling
- **Slides:** 4
- **Type:** Application
- **What it is:** **Broad network access** (ubiquitous access) and **resource pooling** (location independent, multi-tenancy).
- **Look-alikes:** Broad network access vs resource pooling — access is about *reach over the network*, pooling is about *shared underlying resources*; broad access vs location independence — the slide binds location independence to pooling, not to access.
- **Limits / trade-offs:** Pooling implies multi-tenancy, which the slide elsewhere links to overlapping trust boundaries (slide 32).
- **Situation cues:** "users in several countries reach the same service", "provider pools servers across customers", "consumer does not know where the resource is".
- **Past-paper Qs:** 24S2 Q12, 24S2 Q16

### L02-C04 Single-tenancy vs multi-tenancy
- **Slides:** 6
- **Type:** Application
- **What it is:** **Single tenant:** each cloud consumer has a separate IT resource instance. **Multi-tenancy:** the provider pools IT resources to serve multiple consumers, and one instance of the program serves multiple consumers (tenants).
- **Look-alikes:** Multi-tenancy vs resource pooling — pooling is the provider-side act of sharing resources, multi-tenancy is the resulting shared instance visible to several consumers; multi-tenancy vs virtualisation — virtualisation gives separate VMs on one host, multi-tenancy can mean one *application instance* shared (difference inferred).
- **Limits / trade-offs:** The slide does not list a downside; slide 32 links multi-tenancy to overlapping trust boundaries and increased security vulnerability (inferred link).
- **Situation cues:** "same application instance serves several customers", "separate instance per customer", "provider pools resources", "tenant A's data must not be visible to tenant B".
- **Past-paper Qs:** 24S2 Q14, 25S1 Q6

### L02-C05 Service model pyramid and the abstraction ladder
- **Slides:** 7, 9
- **Type:** Application
- **What it is:** Stacked from bottom to top **IaaS, PaaS, SaaS**; going up raises levels of abstraction, ease of use, management effort borne by the provider and speed of deployment. Different models exist because of "different levels of abstraction and management – use depending on need".
- **Look-alikes:** IaaS vs PaaS vs SaaS (who manages more); "higher = better" — the slide says higher ease of use but also **lowest flexibility** for SaaS (slide 20), so "better" depends on need.
- **Limits / trade-offs:** More abstraction trades away flexibility and control (slide 20 corroborates).
- **Situation cues:** "wants to avoid managing servers", "needs only to deploy code", "weighs ease of use against control", "which layer gives the least management burden".
- **Past-paper Qs:** none

### L02-C06 SaaS
- **Slides:** 8, 16
- **Type:** Application
- **What it is:** Use the provider's applications over a network; the SaaS provider **installs and maintains** the software and the consumer **remotely runs** it on the cloud. Examples: Salesforce.com, Google apps, Microsoft 365. Contract shape: SLA response time 0.5ms, $0.05 per 100 requests.
- **Look-alikes:** SaaS vs PaaS — SaaS delivers a finished application to an end user, PaaS delivers a platform for developers to build applications; SaaS vs IaaS — IaaS rents raw compute/storage/network as VM instances.
- **Limits / trade-offs:** Lowest flexibility (slide 20); consumer controls only its data (slide 19); portability of data between SaaS providers is a concern (slide 30, 24S2 Q2).
- **Situation cues:** "staff need email and office productivity immediately", "no in-house software maintenance", "per-request billing for a hosted application", "provider upgrades the software for us".
- **Past-paper Qs:** 24S2 Q1, 24S2 Q7

### L02-C07 PaaS
- **Slides:** 8, 12, 13
- **Type:** Application
- **What it is:** Two parts: **platform software** and the **computing resources needed to run it**. The provider develops the platform software and decides where to host/run the PaaS; the consumer **incorporates the ready-made PaaS into the application being developed**. Contract shape: application server + DBMS platforms, SLA 99.9% with auto-scaling, $0.45/hour for 500,000 requests. Examples: Google App Engine, Heroku, Azure App Service.
- **Look-alikes:** PaaS vs IaaS — PaaS includes the runtime/platform (app server, DBMS) so the consumer does not manage OS/runtime, IaaS gives only virtual machines; PaaS vs SaaS — PaaS consumers are *developers building* software, SaaS consumers *use* finished software.
- **Limits / trade-offs:** Vendor lock-in (slide 20); consumer still manages data and application (slide 19); limited to the languages/frameworks the ready-made environment supports (inferred).
- **Situation cues:** "ready-made environment", "developers want to deploy without managing the OS or database", "auto-scaling built in", "middleware and frameworks already provided".
- **Past-paper Qs:** 24S2 Q3, 25S1 Q2, 25S1 Q13, 25S2 Q2, 25S1 Q19

### L02-C08 IaaS
- **Slides:** 8, 10, 11
- **Type:** Application
- **What it is:** **Lowest level of abstraction**; physical resources are abstracted as **virtual resources** — servers, storage, networks, applications & middleware. Rent processing, storage and network capacity. Contract shape: virtual server with 32GB RAM and 4GB local storage, SLA 99.5% availability, **no failover**, $0.95/hour plus $0.05/GB transferred out of the cloud. Examples: Amazon EC2, DigitalOcean, Linode, Alibaba ECS.
- **Look-alikes:** IaaS vs PaaS — IaaS stops at virtual machines (consumer installs OS and everything above), PaaS supplies the platform software; IaaS vs on-premise — both give high control, but IaaS removes hardware procurement (slide 20).
- **Limits / trade-offs:** Most consumer responsibility (slide 19); privacy listed as the IaaS con (slide 20); example SLA has no failover (slide 10); egress charged per GB.
- **Situation cues:** "lift-and-shift existing systems", "needs full control of the OS", "no hardware procurement", "contract specifies vCPU/RAM and availability".
- **Past-paper Qs:** 25S2 Q9, 25S2 Q19, 25S2 Q4

### L02-C09 Combining the service models (layering)
- **Slides:** 14, 17
- **Type:** Application
- **What it is:** Layers stack: PaaS platform software (ready-made environments A, B, C, each with server + database) runs on IaaS compute (virtual servers A, B on physical server A); a SaaS can be developed using PaaS, which runs on IaaS — cloud services on ready-made environments on virtual servers on physical servers.
- **Look-alikes:** "Combining models" vs "hybrid cloud" — this is *stacking service models in one provider chain*, hybrid is *multiple deployment models networked together* (difference inferred); PaaS on IaaS vs PaaS alone — the provider must still source compute somewhere.
- **Limits / trade-offs:** Each extra layer adds a dependency and a provider whose SLA/region must be checked (inferred from slide 15).
- **Situation cues:** "the platform is itself hosted on virtual machines", "a vendor's SaaS is built on another vendor's PaaS", "which layer does each provider own".
- **Past-paper Qs:** none

### L02-C10 Cross-provider hosting to meet legal/data-storage requirements
- **Slides:** 15
- **Type:** Application
- **What it is:** The consumer subscribes to PaaS from provider X (Cloud A), but to meet a requirement provider X's services are physically hosted on provider Y (Cloud B), and Cloud B is in the **same region as the cloud consumer**.
- **Look-alikes:** This vs sovereign cloud — both keep data in a jurisdiction, but sovereign cloud is a *deployment/storage model*, this is an *arrangement between two providers*; this vs hybrid — no second deployment model is involved, just re-hosting (difference inferred).
- **Limits / trade-offs:** The consumer's SLA and contract are with provider X while the data physically sits with provider Y — responsibility and audit must span both (inferred).
- **Situation cues:** "data must stay in the country", "the chosen provider sub-contracts hosting", "legal requirement for physical location", "same region as the customer".
- **Past-paper Qs:** 25S2 Q23

### L02-C11 Variants of service models (XaaS)
- **Slides:** 18
- **Type:** Reference-only
- **What it is:** Storage-as-a-Service, Database-as-a-Service, Security-as-a-Service, Communication-as-a-Service, Integration-as-a-Service, Testing-as-a-Service, **Function-as-a-Service (serverless computing)**, … i.e. "Everything-as-a-Service".
- **Look-alikes:** DBaaS vs PaaS — DBaaS offers just the database, PaaS offers a whole ready-made development/runtime environment including a DBMS; FaaS vs PaaS — FaaS is serverless and runs functions without managing servers or provisioning, PaaS still gives you an environment to deploy an application into (differences inferred from the one-line list).
- **Limits / trade-offs:** None stated — the slide is a list.
- **Situation cues:** "managed database only", "serverless", "as-a-service for a single capability rather than a whole platform".
- **Past-paper Qs:** 25S1 Q1, 25S2 Q4

### L02-C12 Consumer vs provider responsibility by model
- **Slides:** 19
- **Type:** Application
- **What it is:** Stack (bottom→top): Network, Storage, Server, Virtualization, OS, Database, Integration, Runtime, Application, Data. **On-premise:** consumer manages all. **IaaS:** consumer manages Data, Application, Runtime, Integration, Database; provider manages OS, Virtualization, Server, Storage, Network. **PaaS:** consumer manages Data, Application; provider manages Runtime down. **SaaS:** consumer manages Data only; provider manages the rest. *Record both versions:* the 2526-Sem2 Q9 model answer says the **IaaS user manages the OS**, whereas this slide puts the OS with the IaaS provider.
- **Look-alikes:** IaaS vs PaaS responsibility — the boundary sits at the OS for IaaS and at Runtime for PaaS; "SaaS = zero responsibility" — the consumer still owns Data in every model.
- **Limits / trade-offs:** The more the provider manages, the less the consumer controls (mirrors slide 20 flexibility).
- **Situation cues:** "who patches the operating system", "who is responsible for the database", "the customer keeps only its own data", "which model leaves the customer with the most responsibility".
- **Past-paper Qs:** 25S2 Q9, 24S2 Q18

### L02-C13 Pros and cons of each model
- **Slides:** 20
- **Type:** Application
- **What it is:** On-premise: highest flexibility / long time-to-market. IaaS: scalability, no H/W procurement / privacy. PaaS: DB, frameworks, middleware ready / vendor lock-in. SaaS: reduce time-to-market / lowest flexibility.
- **Look-alikes:** IaaS "privacy" con vs private cloud — private cloud is chosen *for* control of sensitive data, IaaS privacy is a *concern*; PaaS vendor lock-in vs SaaS lowest flexibility — lock-in is about difficulty moving providers, flexibility is about how much you can customise.
- **Limits / trade-offs:** Every model has an explicit cost: time-to-market, privacy, lock-in or flexibility.
- **Situation cues:** "fastest to market", "avoid buying hardware", "locked into the provider's runtime", "needs maximum flexibility".
- **Past-paper Qs:** 24S2 Q1, 25S2 Q19

### L02-C14 NIST reference model: what, not how
- **Slides:** 21
- **Type:** Reference-only
- **What it is:** Focuses on the **what** (what cloud services provide), not the **how** (design solution and implementation); does not represent the system architecture of a specific cloud; provides a common reference framework to describe, discuss and develop system-specific architectures; **vendor and implementation independent**.
- **Look-alikes:** Reference model vs reference architecture — the model is the abstract framework, the architecture (slide 22) is the actor/layer picture built on it (difference inferred); reference architecture vs a real system architecture — the reference one is not any specific cloud's design.
- **Limits / trade-offs:** Deliberately not prescriptive: it cannot be used as an implementation blueprint.
- **Situation cues:** "vendor-neutral framework", "describes what is offered rather than how it is built", "common vocabulary across providers".
- **Past-paper Qs:** none

### L02-C15 Cloud computing reference architecture layout
- **Slides:** 22
- **Type:** Reference-only
- **What it is:** Cloud Consumer; Cloud Auditor (Security Audit, Privacy Impact Audit, Performance Audit); Cloud Provider = Service Orchestration [Service Layer (SaaS, PaaS, IaaS) / Resource Abstraction and Control Layer / Physical Resource Layer (Hardware, Facility)] + Cloud Service Management [Business Support, Provisioning/Configuration, Portability/Interoperability] + Security and Privacy bars spanning all; Cloud Broker (Intermediation, Aggregation, Arbitrage); Cloud Carrier across the bottom.
- **Look-alikes:** Cloud Service Management vs Service Orchestration — management is the business/operational functions, orchestration is the arrangement and coordination of the resource layers; Security and Privacy vs Cloud Auditor — the bars are cross-cutting functions, the auditor is the independent actor that checks them.
- **Limits / trade-offs:** None stated — it is a reference picture, not a specific design (slide 21).
- **Situation cues:** "which bar spans every layer", "where does the carrier sit", "which actor is independent of provider and consumer".
- **Past-paper Qs:** none

### L02-C16 The five actors and their roles
- **Slides:** 23, 25
- **Type:** Application
- **What it is:** An **actor** is an entity (person/organisation) that participates in a transaction or process and/or performs tasks. Five actors: **Cloud Consumer** (maintains a business relationship with, and uses services from, providers), **Cloud Provider** (offers a cloud service), **Cloud Auditor** (independent assessment of services, operations, performance and security), **Cloud Broker** (manages use, performance and delivery, and negotiates relationships between providers and consumers), **Cloud Carrier** (connectivity and transport between providers and consumers).
- **Look-alikes:** Broker vs Carrier — broker manages/negotiates services, carrier only moves the traffic; Auditor vs Broker — auditor is independent assessment, broker is a commercial intermediary; Consumer vs Provider — consumer uses services, provider offers them.
- **Limits / trade-offs:** None stated.
- **Situation cues:** "an independent body reviews compliance", "a third party negotiates between several providers", "who provides the network link", "who uses the service under a business relationship".
- **Past-paper Qs:** none

### L02-C17 Cloud consumer use cases by service model
- **Slides:** 26
- **Type:** Application
- **What it is:** **SaaS consumer:** ERP, HR, Billing, Social Networks, Sales, Financials, CRM, Content Mgmt, Collaboration, Email & Office Productivity, Document Mgmt. **PaaS consumer:** Business Intelligence, Database, Application Deployment, Development & Testing, Integration. **IaaS consumer:** Storage, CDN, Backup & Recovery, Compute, Services Management, Platform Hosting.
- **Look-alikes:** PaaS "Application Deployment / Development & Testing" vs IaaS "Platform Hosting" — PaaS is building/deploying *your app* on a ready platform, IaaS is hosting a *platform* on raw infrastructure; SaaS CRM/ERP vs PaaS Business Intelligence — SaaS is a finished business application, BI on PaaS is something you build.
- **Limits / trade-offs:** None stated — a categorisation list.
- **Situation cues:** "wants CRM without building it", "needs a development and testing environment", "needs backup and recovery capacity", "needs storage and CDN".
- **Past-paper Qs:** 24S2 Q1, 24S2 Q7

### L02-C18 Cloud provider types and service orchestration
- **Slides:** 27, 28
- **Type:** Application
- **What it is:** Three provider types depending on service model: SaaS, PaaS, IaaS cloud provider. **Service orchestration** composes system components to support the provider's activities in **arrangement, coordination and management** of computing resources, across three layers: Service Layer (SaaS, PaaS, IaaS) over Resource Abstraction and Control Layer over Physical Resource Layer (Hardware, Facility).
- **Look-alikes:** Service orchestration vs cloud service management — orchestration arranges/coordinates resources, management runs the business and operational functions for consumers; Resource Abstraction and Control Layer vs Virtualization — the layer is an architectural tier, virtualisation is the mechanism beneath it (inferred).
- **Limits / trade-offs:** None stated.
- **Situation cues:** "how the provider arranges and coordinates its resources", "which layer sits between the service layer and the hardware", "provider categorised by the model it sells".
- **Past-paper Qs:** none

### L02-C19 Cloud service management: three categories
- **Slides:** 29, 30
- **Type:** Application
- **What it is:** Service-related functions for the management and operation of services provided to consumers, used by Cloud Consumers and Cloud Brokers: **Business Support** (Customer Mgmt, Contract Mgmt, Inventory Mgmt, Accounting & Billing, Reporting & Auditing, Pricing & Rating), **Provisioning/Configuration** (Rapid Provisioning, Resource Change, Monitoring & Reporting, Metering, SLA Management), **Portability/Interoperability** (data portability, service interoperability, system portability).
- **Look-alikes:** Business Support vs Provisioning/Configuration — business support is client-facing commerce (billing, pricing, contracts), provisioning is technical delivery (rapid provisioning, resource change); Metering (provisioning) vs Accounting & Billing (business support) — metering measures usage, billing charges for it; Rapid provisioning vs resource change — provisioning deploys new systems on request, resource change adjusts existing configuration for repairs/upgrades/new nodes.
- **Limits / trade-offs:** None stated.
- **Situation cues:** "automatically deploying the requested resources", "adding a node for an upgrade", "invoice and rating", "measuring consumption", "managing the SLA".
- **Past-paper Qs:** none

### L02-C20 Portability and interoperability
- **Slides:** 30
- **Type:** Application
- **What it is:** The reference model should provide mechanisms for **data portability, service interoperability and system portability**; the listed functions are Data Portability, Copy Data To-From, Bulk Data Transfer, Service Interoperability, Unified Management Interface, System Portability, VM Images Migration, App/Svc Migration.
- **Look-alikes:** Portability vs interoperability — portability is moving data/system to another provider, interoperability is services from different providers working together; data portability vs system portability — data leaves as data, system portability moves the running system (VM images, apps/services); portability vs vendor lock-in — lock-in is what you suffer without portability.
- **Limits / trade-offs:** Without these mechanisms the consumer is locked in (slide 20 PaaS con; 25S1 Q22).
- **Situation cues:** "export our data and leave the provider", "move VM images to another cloud", "two providers' services must work together", "unified management interface".
- **Past-paper Qs:** 24S2 Q2, 25S1 Q22

### L02-C21 Security and privacy in the reference model
- **Slides:** 31
- **Type:** Application
- **What it is:** **Security** is cross-cutting and spans across all layers of the reference model, and concerns **all relevant actors**. **Privacy:** for cloud providers, Personal Information (PI) and Personally Identifiable Information (PII).
- **Look-alikes:** Security vs privacy — security is protection of the system across all layers, privacy specifically concerns PI/PII held by providers; security as a layer vs security as a cross-cutting bar — the slide says it is *not* a layer but spans all layers.
- **Limits / trade-offs:** Because it spans all layers and all actors, no single party can be made solely accountable (inferred).
- **Situation cues:** "which actor is responsible for security", "security applies to every layer", "personal data held by the provider", "privacy impact".
- **Past-paper Qs:** 24S2 Q25

### L02-C22 Trust boundary
- **Slides:** 32
- **Type:** Application
- **What it is:** A **logical perimeter** representing which IT resources are trusted by an organisation. Implications of cloud: **increased security vulnerabilities**, **reduced operational governance control**, **multi-tenancy means overlapping trust boundaries**.
- **Look-alikes:** Trust boundary vs security in the reference model — the boundary is the perimeter definition, security is the cross-cutting control set; overlapping trust boundaries vs multi-tenancy — multi-tenancy is the sharing arrangement, overlapping trust boundaries are its security consequence; trust boundary vs private cloud — private cloud is a way to keep the boundary small (inferred).
- **Limits / trade-offs:** The three listed implications are all costs: more vulnerability, less governance control, boundaries that overlap other tenants.
- **Situation cues:** "which resources does the organisation trust", "shared host exposes data to another tenant", "loss of governance control", "logical perimeter".
- **Past-paper Qs:** 25S1 Q7, 24S2 Q8, 25S1 Q14, 25S1 Q16

### L02-C23 Cloud auditor
- **Slides:** 33
- **Type:** Application
- **What it is:** **Independent examination of cloud service controls** — Security Controls, Privacy Impact, Performance, … — verifying compliance with regulation and security policy, and conformance to standards, **through review of objective evidence**.
- **Look-alikes:** Auditor vs broker — auditor is independent and does not sell or negotiate; auditor vs provider's own monitoring — monitoring is operational self-reporting (Provisioning/Configuration), audit is independent examination of objective evidence.
- **Limits / trade-offs:** Its value depends on evidence being objective and the auditor being independent (inferred).
- **Situation cues:** "independent assessment", "review of objective evidence", "prove conformance to standards", "privacy impact audit".
- **Past-paper Qs:** none

### L02-C24 Cloud broker
- **Slides:** 34
- **Type:** Application
- **What it is:** Helps consumers manage integration of cloud services. Three services: **Service Intermediation** (provides value-added services to consumers), **Service Aggregation** (combines and integrates multiple services into one or more new services, provides data integration, ensures secure data movement between consumers and multiple providers), **Service Arbitrage** (flexibility to choose services from multiple agencies).
- **Look-alikes:** Aggregation vs intermediation — aggregation *combines several services into a new one*, intermediation *adds value on top of an existing service*; arbitrage vs aggregation — arbitrage is *choosing* among providers/agencies, aggregation is *merging* them into one offering; broker vs carrier — broker manages services and relationships, carrier only transports.
- **Limits / trade-offs:** None stated on the slide.
- **Situation cues:** "one bill/one integrated service from several providers", "value-added layer on top of a provider's service", "pick the best provider per component", "secure data movement across providers".
- **Past-paper Qs:** 25S1 Q10

### L02-C25 Cloud carrier
- **Slides:** 35
- **Type:** Application
- **What it is:** Provides **connectivity and transport** of cloud services between consumers and providers; cloud providers set up **SLAs with a cloud carrier** to provide consistent services; may be required to provide **dedicated and secured connections**.
- **Look-alikes:** Carrier vs broker — carrier moves bits, broker manages/negotiates services; carrier vs provider — the provider sells the service, the carrier only delivers it; carrier SLA vs provider SLA — the provider's promise to its consumer depends on the carrier's separate SLA.
- **Limits / trade-offs:** The provider's service quality is bounded by a third party's SLA (inferred).
- **Situation cues:** "network link between provider and customer", "dedicated secured connection", "the provider has an SLA with the network operator", "transport of the service".
- **Past-paper Qs:** none

### L02-C26 Four deployment models defined
- **Slides:** 36, 37
- **Type:** Application
- **What it is:** **Public** — available to the general public, shared by all consumers. **Private** — solely for use by an organisation, suitable for enterprises with large-scale IT. **Community** — shared by multiple organisations based on **common operational and regulatory requirements**. **Hybrid (Federated)** — two or more public and private clouds that interoperate. All are reached via network connectivity.
- **Look-alikes:** Private vs community — private is one organisation, community is several with shared regulation/operations; public vs community — public is open to everyone, community is restricted to participating organisations; hybrid vs community — hybrid joins *different deployment types*, community is a single shared cloud (difference inferred).
- **Limits / trade-offs:** None stated at this level; the individual model slides carry the costs.
- **Situation cues:** "shared by all", "exclusive to our organisation", "several hospitals with the same regulator", "a mix of clouds that interoperate".
- **Past-paper Qs:** 25S1 Q12, 24S2 Q25

### L02-C27 Public cloud
- **Slides:** 38
- **Type:** Application
- **What it is:** The most commonly used cloud infrastructure; organisations act as consumers of resources made available by different providers. Needs met: **low upfront costs with potentially pay-as-you-go**, **available anytime, anywhere**, **maintenance handled by the provider**. Providers: Amazon, Microsoft, Google, Oracle, IBM, Alibaba, Zoho, DigitalOcean, …
- **Look-alikes:** Public vs private — public is shared with all and provider-maintained, private is exclusive with in-house maintenance; public vs out-sourced private — a VPC lives inside public infrastructure but is isolated for one organisation (slide 41, difference inferred).
- **Limits / trade-offs:** Implied loss of control from provider-handled maintenance and shared infrastructure (inferred; slide 32 lists governance loss).
- **Situation cues:** "low upfront cost", "no infrastructure team", "available anywhere", "provider handles maintenance".
- **Past-paper Qs:** 24S2 Q13

### L02-C28 Private cloud
- **Slides:** 39, 40, 42
- **Type:** Application
- **What it is:** The consumer's organisation has **exclusive access and usage** of cloud resources. Needs met: **high level of control, especially for sensitive data**, **restricted access often limited to the organisation**, **maintenance handled predominantly in-house**. Can be managed **on-site** or by a **third party (out-sourced)**. Concerns: **limited SLA, reliability, security, availability, trust**. Providers: Amazon VPC, Cisco Private Cloud Solutions, Google Cloud VPC, Azure Dedicated Host, …
- **Look-alikes:** Private vs public — exclusive control and in-house maintenance vs shared and provider-maintained; on-site vs out-sourced private — same exclusivity, different hosting location and therefore a different security question; private cloud vs VPC — a VPC is a private slice inside public infrastructure (slide 41).
- **Limits / trade-offs:** Limited SLA, reliability, security, availability and trust; suits enterprises with large-scale IT (slide 36).
- **Situation cues:** "exclusive to our organisation", "sensitive data must stay under our control", "maintenance done in-house", "we worry about SLA and trust".
- **Past-paper Qs:** 24S2 Q25, 25S2 Q22

### L02-C29 On-site vs out-sourced private cloud (and VPC)
- **Slides:** 40, 41
- **Type:** Application
- **What it is:** **On-Site Private Cloud** runs on the organisation's own premises; **Out-Sourced Private Cloud** is **dedicated IT resources hosted by a third-party provider**, accessed from the enterprise network. The slide's callout asks "**Security? On-site vs out-sourced**". A **Virtual Private Cloud** is a secure, isolated environment **within a public cloud** that is customisable by you.
- **Look-alikes:** Out-sourced private vs public — both use a provider's facility, but out-sourced private is dedicated to one organisation; VPC vs fully private cloud — a VPC is isolation *inside* shared public infrastructure, a private cloud is dedicated infrastructure; on-site vs out-sourced — same exclusivity, different physical control.
- **Limits / trade-offs:** Out-sourcing moves physical control to a third party, which is exactly the open security question the slide poses (inferred).
- **Situation cues:** "on our own premises", "hosted by a provider but dedicated to us", "isolated environment inside a public cloud", "security of hosting location".
- **Past-paper Qs:** none

### L02-C30 Community cloud
- **Slides:** 43, 44
- **Type:** Application
- **What it is:** Positioned **between public and private** clouds. Needs met: **cost of private cloud is prohibitive**, **shared needs and regulatory compliance with other organisations**, **restricted access often limited to participating organisations**. Requires a **clear governance structure for management**. Examples: government departments, educational institutions, health care. Architecture: ORG 1–3 linked by shared policies and shared protocols, IAM, a cloud manager, and a cloud community holding storage, applications & services, security controls, data governance tool, reporting engine, logging engine.
- **Look-alikes:** Community vs public — community is restricted to participating organisations with common regulation, public is open to all; community vs private — community is multi-organisation and cheaper, private is single-organisation; community vs hybrid — community is one shared cloud, hybrid joins distinct clouds (inferred).
- **Limits / trade-offs:** Private cloud cost is prohibitive (the reason it exists); needs a clear governance structure, and members are bound by shared policies/protocols.
- **Situation cues:** "several universities under the same regulator", "cannot afford a private cloud alone", "shared policies and protocols", "access limited to member organisations".
- **Past-paper Qs:** none

### L02-C31 Hybrid cloud
- **Slides:** 45, 46
- **Type:** Application
- **What it is:** Two or more clouds (**on-site private, on-site community, off-site private, off-site community or public**) that **remain distinct entities**, connected to allow **data and application interoperability**. Needs met: **balance control and cost**, flexible approach per data/application — e.g. **sensitive data on the private cloud while the application runs on the public cloud**. Slide 46 contrasts the simple picture ("2 different clouds": one public + one private) with "5 different clouds" interconnected.
- **Look-alikes:** Hybrid vs community — hybrid joins different deployment types, community is a single cloud shared by organisations with common requirements; hybrid vs combining service models (slide 17) — hybrid is about deployment models, slide 17 is about SaaS/PaaS/IaaS stacking; hybrid vs cloud bursting — bursting adds capacity temporarily, hybrid is the standing arrangement (L03).
- **Limits / trade-offs:** Requires connectivity and interoperability between distinct clouds; only balances control and cost, it does not maximise either (inferred).
- **Situation cues:** "sensitive data private, the rest public", "balance control and cost", "keep existing private cloud and add public capacity", "two clouds must interoperate".
- **Past-paper Qs:** 24S2 Q9, 24S2 Q23, 25S2 Q24, 25S2 Q22

### L02-C32 Sovereign cloud
- **Slides:** 47
- **Type:** Application
- **What it is:** Exists to **meet regulatory and compliance needs of a country or jurisdiction** and **stores data (including metadata) within national borders**. Needs met: **adhere to local data protection laws**, **prevent foreign access to data under all circumstances**. Providers: Microsoft Sovereign Cloud, Oracle Sovereign Cloud, SAP Sovereign Cloud, …
- **Look-alikes:** Sovereign vs private cloud — private is about *exclusive organisational* control, sovereign is about *national/jurisdictional* control of data and metadata; sovereign vs community — community shares common regulatory requirements among organisations, sovereign answers to a country's law; sovereign vs choosing a region — a region keeps data in a geography, sovereignty also demands no foreign access under any circumstances (differences inferred).
- **Limits / trade-offs:** Constrained to providers operating within the jurisdiction, which narrows choice (inferred).
- **Situation cues:** "data must not leave the country", "local data protection law", "metadata too", "no foreign access under any circumstances".
- **Past-paper Qs:** 25S1 Q25, 25S2 Q5

---

**Slides with no card (and why):**
- 1 title, 2 outline, 48 "Next Week", 49 references, 50 continuous feedback — no examinable content.
- 24 — image only ("24/50"); it illustrates the actors already covered by L02-C16 (slides 23, 25).
- 11 folded into L02-C08, 13 into L02-C07, 14/17 into L02-C09, 27/28 into L02-C18, 29/30 into L02-C19 and L02-C20, 37 into L02-C26, 40/41/42 into L02-C28 and L02-C29, 44 into L02-C30, 46 into L02-C31.
