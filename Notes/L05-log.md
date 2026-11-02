# L05 Scenario Log

A record of each scenario, what you answered, how it was graded, and the correct answer. Reference only: the concepts live in `L05-Virtualisation-Multitenancy.md` and the index. Answers are lightly trimmed from your spoken replies.

---

## S1. Twenty applications consolidated onto four hosts

**Scenario:** A company runs 20 small applications, each on its own physical server (average CPU use about 8%). The IT team moves all 20 onto 4 physical hosts as virtual machines. Weeks later: (a) at 2am the virtualisation software on one host crashes and the 5 applications on it go down together; (b) each application benchmarks slightly slower than it did on its own server.

**Q1 (open):** Explain why (a) and (b) happened, in terms of what the move changed.
**Your answer:** "A looks like a single point of failure: the one host went down and the five applications on it go down together. B is performance overhead, probably because there is some infrastructure that goes on top of the virtualisation layer."
**Grade: about 80%.** (a) correct: single point of failure. Before the move one failure hit one application; now it hits every VM on that host. (b) the label (performance overhead) is right but the mechanism is wrong: the virtualisation layer sits between the VMs and the physical hardware, and every access to processor, memory, storage and network goes through it. That extra step is the overhead.

**Q2 (open):** Management wants 3 more application servers by Friday with no hardware order. How, and why is it fast?
**Your answer:** "It's fast because it's reusing the same physical hardware, just spinning up more virtual infrastructure on top of it."
**Grade: about 50%.** Right direction (no new hardware). Missed: (1) new VMs are made from **virtual disk images** (resource replication), files that can be copied in minutes, versus weeks to buy and install hardware; (2) it only works because the hosts have **spare capacity** (8% average CPU leaves plenty of room).

**Overall: about 70%.** No misconception box: the idea was right, the slip was in the mechanism wording.

---

## S2. What the VM sees vs what the host has

**Scenario:** A tenant's VM shows 8 processors, 32 GB of main memory, one 500 GB disk, and a private network with its own firewall. The physical host has 4 physical cores, memory across several modules, 4 physical drives, and one physical switch and firewall, all shared with other tenants' VMs.

**Q1 (MCQ, spot the false one):** A. 8 processors on a 4-core host come from a virtual processor pool built from the physical cores. B. The 500 GB disk may be spread over several physical drives. C. The firewall can be a software component of the virtualisation layer. D. The VM's OS reads and writes the physical memory modules directly, bypassing the virtualisation layer. E. Two tenants can each have a private network over the same physical switch.
**Your answer:** "D, because it always has to go through the virtualisation layer."
**Grade: 100%.** The VM sees virtual memory (Vmem) from a virtual main memory pool; the layer maps it onto the physical modules.

**Q2 (open):** A physical drive fails; the provider swaps it and the tenant notices nothing. Which kind of virtualisation made that possible, and why?
**Your answer:** "The guest OS can easily be migrated to different hardware, so I'd assume full virtualisation, because para virtualisation cannot migrate to run on physical hardware."
**Grade: 0%.** Wrong axis. The question asks *which resource* is virtualised, and the answer is **storage virtualisation**: the VM sees a virtual disk drawn from a virtual disk storage pool that the layer builds from several physical drives, so a physical drive can be replaced under it without the VM's disk changing. Full vs para is a different question (*how* the guest OS is run), and "migrate to native hardware" means running the guest OS with no hypervisor at all, not swapping a drive.

**Overall: about 50%.** Misconception box added: resource type vs virtualisation approach. Your comment afterwards: you read "kind of virtualisation" as the approach (full, para, hardware-assisted), not the resource. Fair point: the question should have said "which resource". The answer still had to explain a drive swap, which only storage virtualisation does.

---

## S3. Three customers, three virtualisation approaches

**Scenario:** X runs a licensed closed-source OS that must not be modified and plans to move it onto its own physical servers with no hypervisor next year. Y runs a patchable open-source Linux, wants the best performance, on old servers whose CPUs have no virtualisation extensions. Z runs an unmodified OS on new servers whose CPUs have virtualisation extensions.

**Q1 (open):** Which approach for X and for Y? Reason and one accepted cost each.
**Your answer:** "X is full virtualisation, because it can easily be migrated to native hardware, which is what it plans to do. Y is para virtualisation, because on old servers the binary translation overhead may lead to poor performance, and there's no need for special hardware, which fits CPUs with no virtualisation extensions."
**Grade: about 60%.** Both choices and the reasons you gave are right. Missed: (1) X's other reason: the OS cannot be modified, and full virtualisation needs no guest OS changes; (2) the cost of each choice, which the question asked for. X (full) accepts **binary translation overhead** (lower performance). Y (para) accepts **modifying the guest OS kernel**, and the modified OS **cannot run on physical hardware** and is **hard to migrate to other hosts**.

**Q2 (MCQ, true statement about Z):** A. must be modified to issue hypercalls. B. requests are caught by the processor and handed to the hypervisor, so no translation and no guest changes. C. guest knows it is virtualised. D. hypervisor still translates, extension makes it faster. E. guest OS and hypervisor run at the same privilege level.
**Your answer:** "B, hardware-assisted, the hardware steps in. E is never possible: the guest OS and hypervisor can't run at the same privilege level."
**Grade: 100%.** On E: right. In hardware-assisted virtualisation the hypervisor has root privilege and the guest OS runs non-root, at the **same level as user applications**, not as the hypervisor. In full virtualisation the VMM is at ring 0 and the guest above it.

**Overall: about 75%.** No misconception box: the choices were right, the costs were left out.

---

## S4. VMs or containers

**Scenario:** 30 small Linux services, each in its own full VM (own OS, minutes to boot), redeployed many times a day. The same hosts must also run a Windows-only reporting tool and a bank client's workload whose contract demands the strongest separation from other tenants.

**Q1 (open):** Move the 30 services to containers? Why, in terms of what a container does differently. Should the Windows tool and the bank workload move too?
**Your answer:** "Yes. A container is a lightweight virtual machine; taking minutes to boot tells me this is a lightweight VM. Each full VM carrying its own OS is very heavy; in containers they all share the host system's kernel, so there isn't so much redundancy. The Windows tool should not move, because you can't share the same OS. The bank: there is isolation through namespaces, but I'm not sure it's secure enough. Probably not."
**Grade: about 65%.** Right: move the services, kernel sharing removes the OS per instance; Windows tool stays out (it needs a Windows kernel, the containers share a Linux one). Wrong: a container is **not a lightweight VM**: it has no guest OS and no hypervisor, it is an isolated user space on the host's kernel. "Minutes to boot" describes the current heavy VMs, a reason to move. Missed: fast start and quick deploys for a team that redeploys many times a day. Bank: hedged; the answer is keep it in a VM, because a shared kernel is a weaker boundary than separate VMs and full virtualisation gives the best isolation.

**Q2 (MCQ, false statement):** A. container uses the host's kernel instead of booting its own OS. B. starts faster and packs denser, no OS per instance. C. a container's guest OS is unaware it is containerised, like full virtualisation. D. a kernel flaw exploited from one container can affect others on the host. E. containers are isolated user spaces, so can use different library versions.
**Your answer:** "C."
**Grade: 100%.** A container has no guest OS.

**Overall: about 80%.** No misconception box: the MCQ shows the container model is understood; "lightweight VM" was loose wording.

---

## S5. Datacenter and laptop (hypervisor types and attacks)

**Scenario:** A university needs virtualisation in (1) a datacenter of 200 servers hosting VMs for every department, and (2) a student's macOS laptop that needs a Linux VM while the student keeps using normal Mac apps.

**Q1 (open):** Which hypervisor type for each, and why, in terms of what sits directly beneath the hypervisor?
**Your answer:** "Type 1 for the datacenter, because it can run directly on the physical infrastructure. For the laptop, it requires the help of macOS to communicate with the underlying infrastructure, because it's trying to run Linux."
**Grade: about 65%.** Datacenter right: Type 1 (bare metal), the hypervisor sits directly on the hardware with no host OS, the slide's choice for larger scale. Laptop: Type 2 (hosted) is right, but the reason is wrong. Running Linux is not the reason: Linux is the guest under either type. The reason is that the student keeps using macOS and its apps, so macOS stays as the host OS and the hypervisor runs on top of it, using macOS to reach the hardware (slide: "for smaller applications").

**Q2 (MCQ, true statement):** On the laptop, malware infects (i) the host macOS, (ii) the Linux guest. A. both contained equally. B. (i) reaches the guests through the hypervisor; (ii) stays inside the guest. C. (ii) spreads to macOS because Type 2 runs inside the host OS. D. (i) guests safe, guests have higher privilege. E. datacenter equally exposed to (i).
**Your answer:** "B: a host OS compromise is worse than a guest OS compromise."
**Grade: 100%.** The host OS sits below the hypervisor, so a compromised host OS can compromise the hypervisor and then every guest. A compromised guest is isolated; the hypervisor is not compromised. E is false because a Type 1 datacenter has no host OS to attack.

**Overall: about 80%.** No misconception box.

---

## S6. A Docker run on a fresh laptop

**Scenario:** A developer types `docker run myteam/api:2.1` on a new laptop with nothing Docker-related downloaded yet. Seconds later the API is running.

**Q1 (open):** Trace what happened, naming each Docker component and what it did.
**Your answer:** "The Docker daemon must have been running in the background, listening for requests, and it received the docker run request via the REST API, and that's how it ran."
**Grade: about 35%.** Right: the daemon runs in the background, listens for API requests, and receives them over the REST API. Missed most of the trace: (1) the `docker` command is the **client**, which sends the request to the daemon; (2) the daemon looks for the **image** locally and does not find it; (3) it **pulls** the image from a **registry** (Docker Hub by default); (4) it creates a **container**, a runnable instance of the image, and starts it.

**Q2 (MCQ):** A change made inside a running container is gone after deleting it and running a new container from the same image. Why? A. registry overwrote it. B. the image is a read-only template; a new container starts from it unchanged; build a new image to keep the change. C. host kernel reset. D. client connected to several daemons. E. changes held in the shared kernel.
**Your answer:** "B, from the notes, but I've worked with Docker and felt I could modify the image."
**Grade: 100%.** On the doubt: you never edit an image in place. Editing a Dockerfile and rebuilding, or saving a container's changes with `docker commit`, both make a **new** image, often under the same name and tag, so it feels like an edit (beyond slides).

**Overall: about 65%.** No misconception box: the trace was incomplete, not wrong.

---

## S7. One app, 2,000 firms

**Scenario:** An accounting SaaS serves 2,000 small firms. Option 1: a separate copy of the application per firm, each in its own VM. Option 2: one running instance serves all firms, each seeing its own logo, data and settings.

**Q1 (MCQ, true statement):** A. Option 2 is virtualisation, not multitenancy. B. Option 1 is the multitenant design. C. Option 2: single instance, each firm sees a dedicated instance, tenant isolation stops cross-firm access to data and settings. D. Option 2 removes the need for virtualisation. E. multitenancy and virtualisation are the same idea from two sides.
**Your answer:** "C."
**Grade: 100%.**

**Q2 (open):** A large firm wants its own copy. What does it gain, and what does the company give up?
**Your answer:** "The firm gains isolation, because it no longer has to share the physical resources. Well, actually it's still sharing, because it's virtual machines. What they give up is also the sharing of physical resources: the company now needs to secure more hardware."
**Grade: about 40%.** You framed both sides as hardware sharing; your self-correction (still shared, because VMs) was right. Multitenancy is about sharing the **software instance**, not hardware. Gain: the firm no longer shares the application and its data with other tenants, so a bug or misconfiguration in the shared instance cannot expose its data, and other tenants' load cannot affect it. Give up: the efficiency of one instance; the company must run, patch, upgrade and monitor a separate copy for one customer (more resources and work, not necessarily new hardware).

**Overall: about 70%.** Misconception box added: hardware sharing (virtualisation) vs software-instance sharing (multitenancy).

---

## S8. A multitenant file-sharing service

**Scenario:** One application serves thousands of tenant companies. (a) One tenant's huge bulk upload slows every other tenant. (b) A 1 TB-plan tenant is billed the same as a 500 MB-plan tenant. (c) A tenant wants only its own data restored from yesterday, but the provider can only restore the whole shared database, rolling back every tenant.

**Q1 (open):** Which multitenancy property failed in each?
**Your answer:** "(a) usage/tenant isolation, (b) metered usage, (c) data tier isolation."
**Grade: about 85%.** (a) and (b) right. (c): the property that failed directly is **recovery** (per-tenant backup and restore); the shared database (no data tier isolation) is the cause.

**Q2 (MCQ, true statement):** fix (c) with one database per tenant. A. must give each tenant a separate database. B. databases and tables can be isolated or shared; separate makes one tenant's restore easier but costs more. C. per-tenant database = single tenancy. D. data tier isolation = usage isolation. E. shared database means tenants can necessarily read each other's data.
**Your answer:** "B."
**Grade: 100%.**

**Overall: about 90%.** You also asked for real examples of sharing a software instance: Slack, Gmail, Salesforce, Dropbox (one app, tenant ID on every record); the March 2023 ChatGPT bug where a shared component showed some users other users' chat titles; self-hosted Jira or GitLab as single tenancy.

---

## S9. One provider, three products

**Scenario:** (1) server rental: customers install their own software; (2) code platform: customers upload code, platform supplies runtime and database; (3) ready-made CRM used as-is by thousands of companies.

**Q1 (open):** Which of VMs, containers, multitenancy serves many customers on the same hardware for each, and why?
**Your answer:** "(1) VMs let the provider serve many customers on the same hardware, the server itself. (2) Docker containers, because the containers can all share the host runtime. (3) Multitenancy: thousands of companies share the same software instance."
**Grade: about 85%.** All three choices right. (2) reason off: containers share the host **kernel**, not a runtime; each container carries its own runtime packaged with the customer's code, which is why containers suit a code platform.

**Q2 (MCQ, false statement):** A. all three on a virtualisation layer. B. CRM shares one instance; rental gives each a VM. C. multitenancy belongs to server rental because VMs share a host. D. CRM users are application consumers, rental users infrastructure architects. E. containers suit the code platform.
**Your answer:** "C."
**Grade: 100%.** VMs sharing a host is virtualisation, not multitenancy (the S7 distinction, now applied correctly).

**Overall: about 90%.**

---

## Gap set (G1-G5)

**G1 (open):** A VM's traffic moves to a different physical switch during maintenance; the VM keeps its private network and firewall rules. Which resource virtualisation? Would para to full change anything?
**Your answer:** "Network virtualisation. Switching from para to full changes nothing."
**Grade: 100%.** The resource axis and the approach axis kept apart (the S2 mistake, now fixed).

**G2 (MCQ):** A hospital gets its own copy of a multitenant SaaS app in its own VM. True statement?
**Your answer:** "B: it has its own copy of the application, but the VM still runs in the provider's datacenter, so it may still share physical hosts."
**Grade: 100%.** (The S7 mistake, now fixed.)

**G3 (open):** `docker run nginx` where the image was pulled last week. Trace it; which fresh-machine step is skipped?
**Your answer:** "The daemon listens, a request comes in, it searches the local images, finds nginx, and runs the image, that's the instance. On a fresh machine the local search is skipped and it goes to the registry."
**Grade: about 50%.** Right: daemon, local image found, container created from it. Missed again: the `docker` command is the **client**, which sends the request to the daemon over the REST API. Reversed: the daemon **always** checks locally first. The step skipped here is the **pull from the registry**, because the image is already local; on a fresh machine the local check runs, finds nothing, and then the pull happens.

**G4 (MCQ):** Windows laptop, Ubuntu VM, keep using Outlook and Excel. Choice and reason?
**Your answer:** "Type 2. It needs the help of the host OS, Windows, to communicate with Outlook and Excel."
**Grade: about 75%.** Type 2 is right (option C). The reason is slightly off: the hypervisor does not talk to Outlook and Excel. Windows stays as the host OS so those apps keep running, and the hypervisor runs on top of Windows and uses it to reach the hardware.

**G5 (open):** Team A full, Team B para; one downside each after six months?
**Your answer:** "Full: system performance is reduced over time. Para: the modified guest OS is difficult to migrate to other hosts or physical hardware; it can only run on a VM."
**Grade: about 85%.** Para fully right. Full: the cost is **binary translation overhead**, a constant slowdown on every privileged instruction, not a slowdown that grows over time (the other possible downside: hardware without drivers for the virtualisation software).

**Overall: about 80%.** Misconception box added: leaving the Docker client out of the trace (twice, S6 and G3) and the fresh vs cached reversal.

Also re-answered: the kernel is the core of the OS (highest privilege; manages CPU, memory, devices); the OS is the kernel plus libraries, tools and shell.
