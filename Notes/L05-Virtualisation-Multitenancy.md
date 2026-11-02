# L05 Virtualisation and Multitenancy

Cards: `Notes/cards/L05-cards.md` (C01-C34). Past-paper questions: 24S2 Q5, Q10, Q14, Q15; 25S1 Q6, Q18; 25S2 Q3, Q10 (see `PAST-PAPER-MAP.md`).

## Scenario Plan

| # | Idea (hidden from Joshua until review) | Cards | Past-paper link |
|---|---|---|---|
| 1 ✅ | Why virtualise (1:1 to many:1) and what it costs: diagnose a symptom (hypervisor failure, overhead) | C01-C04 | 25S2 Q3, 24S2 Q10 |
| 2 ✅ | Which resource is virtualised and what the VM sees (processor, memory, storage, network pools) | C05-C09 | - |
| 3 ✅ | Full vs para vs hardware-assisted: choose for a situation (unmodifiable guest OS, performance, migration to physical hardware) | C10-C16 | 24S2 Q5 |
| 4 ✅ | Full virtualisation vs containers: look-alike MCQ (guest OS unaware, kernel sharing, isolation) | C11, C23 | 24S2 Q5, Q15; 25S1 Q18; 25S2 Q10 |
| 5 ✅ | Type 1 vs Type 2 hypervisor for a setting, merged with hypervisor attacks (host OS vs guest OS compromised) | C18-C22 | - |
| 6 ✅ | Docker: client, daemon, registry, image, container; trace a "run" and diagnose a symptom | C24-C29 | 25S2 Q10 |
| 7 ✅ | Multitenancy vs virtualisation: what each is, how they relate, single tenancy security | C31-C32 | 25S1 Q6, 24S2 Q14 |
| 8 ✅ | Multitenancy characteristics (tenant isolation, data tier isolation, metered usage) | C34 | - |
| 9 ✅ | Virtualisation technologies vs service models (VMs, Docker, multitenancy against IaaS/PaaS/SaaS) | C30 | - |
| Gap ✅ | One mixed set (4-5 short questions) on concepts he actually got wrong | - | - |

## Detailed Notes

### Concept 1: Why virtualise, and what it costs (C01-C04)

- Before virtualisation, one workload runs on one physical machine (1:1). Virtualisation lets a single physical infrastructure act as several logical ones, so many workloads share the hardware (many:1) and utilisation rises **(slides, s3-s5)**.
- The virtualisation layer sits between the VMs and the physical hardware; every access to processor, memory, storage and network passes through it. That extra step is the **performance overhead** **(slides, s6 and s12)**.
- Pros: hardware independence, resource consolidation (higher utilisation, load balancing), resource replication (rapid scaling, because VMs are created from **virtual disk images**) **(slides, s6)**.
- Cons: performance overhead, and a **single point of failure**: the virtualisation software and host are shared, so one failure takes down every VM on that host (before consolidation, a failure hit one application) **(slides, s6)**.
- Fast provisioning only works while the hosts have spare capacity (low average CPU use leaves room) **(beyond slides)**.

**Key one-liner:** consolidation raises utilisation and speeds provisioning (copy a disk image), but it concentrates failures on shared hosts and adds a layer that costs some performance.

### Concept 2: The four resources that are virtualised (C05-C09)

- Four resources are virtualised: **processor, memory, storage, network** **(slides, s7)**. Each follows the same pattern: the virtualisation layer pools the physical resource and hands each VM a virtual slice; the VM sees only the virtual slice **(slides, s8-s11)**.
- **Processor:** physical cores (P1..P4) form a shared pool; the layer builds a **virtual processor pool** (VP1..VP8) and VMs get virtual processors. So a VM can be shown more processors than the host has physical cores **(slides, s8)**.
- **Memory:** VMs get virtual main memory (Vmem) from a **virtual main memory pool** built over the physical memory modules. The guest OS never touches the physical modules directly; the layer maps them **(slides, s9)**.
- **Storage:** VMs get virtual disks (VDisks) from a **virtual disk storage pool** built from several physical drives. One virtual disk can sit across several drives, and a physical drive can be replaced underneath without the VM's disk changing **(slides, s10; the drive-swap consequence is beyond slides)**.
- **Network:** the layer provides software versions of network gear (vNICs, vSwitches, vRouters, vFirewalls, virtual load balancers) over the physical network, so tenants get their own **virtual private networks** over shared switches **(slides, s11)**.

> [!WARNING]
> **Mistake:** treating "which kind of virtualisation" as full vs para virtualisation. Those are two separate questions. *Which resource* is virtualised (processor, memory, storage, network) is one axis; *how the guest OS is run* (full, para, hardware-assisted) is another. A failed physical drive swapped out with the VM noticing nothing is **storage virtualisation** (the VM's disk is a virtual disk from a pool over several drives), not full virtualisation. Full virtualisation's "easy migration to native hardware" means running the guest OS with no hypervisor at all.

**Key one-liner:** each resource is pooled and handed out as virtual slices, so the VM's view (8 vCPUs, one disk, its own firewall) is decoupled from the physical parts underneath.


### Concept 3: Full, para and hardware-assisted virtualisation (C10-C16)

- The hypervisor (also called the VMM, virtual machine manager) sits between the VMs and the hardware. Only privileged (OS) instructions should reach the hardware, so each approach answers one question: **how does the guest OS's privileged request get there?** Lower ring number = higher privilege **(slides, s12)**.
- **Full virtualisation:** the guest OS is **unmodified and unaware** it is virtual. The VMM runs at ring 0, mimics the hardware, and **translates** the guest's instructions (binary translation) **(slides, s13)**.
  - Pros: best isolation and security; different OSs at once; the guest OS **can easily move to native hardware** (run with no hypervisor); easy to install, no guest changes **(slides, s14)**.
  - Cons: **binary translation overhead** (lower performance); needs the right hardware and software combination (the hardware may lack drivers for the virtualisation software) **(slides, s14)**.
- **Para virtualisation (OS-assisted):** the guest OS is **modified and aware**. It replaces OS requests with **hypercalls**, privileged calls straight to the hypervisor with no translation **(slides, s15)**.
  - Pros: no translation overhead, so better performance; **no special hardware** needed **(slides, s16)**.
  - Cons: guest kernel modification; the modified OS **cannot run on physical hardware**; poor backward compatibility, **hard to migrate to other hosts** **(slides, s16)**.
- **Hardware-assisted virtualisation:** the **processor has virtualisation extensions**. Guest OS requests **trap** to the hypervisor in hardware, so there is **no translation and no guest modification** ("best of both worlds"). The hypervisor has root privilege; the guest OS and user applications share the same non-root level **(slides, s17-s18)**.
- Choosing: unmodifiable guest OS or a planned move to bare metal → full; patchable guest, performance, no CPU extensions → para; CPU extensions available → hardware-assisted **(slides, s14-s18)**.

**Key one-liner:** full translates (no guest changes, slower), para modifies the guest to make hypercalls (faster, locked to the hypervisor), hardware-assisted lets the CPU trap requests (neither cost, needs CPU extensions).


### Concept 4: Containers vs VMs (C23)

- A VM carries its own guest OS on top of a hypervisor. A **container** has **no guest OS and no hypervisor**: it is an **isolated user space instance** that **shares the host system's kernel** with the other containers, so it is lightweight and starts fast ("quickly develop, deploy, test") **(slides, s27)**.
- The **kernel** is the core of an OS: the part that runs in the highest privilege and manages the CPU, memory and devices. An OS is the kernel plus everything around it (libraries, tools, shell). Containers share the kernel but can each have their own libraries and tools, so two containers can use different library versions or even different Linux distributions **(beyond slides)**.
- Consequences of sharing a kernel **(inferred from s27, beyond slides)**:
  - A container can only run software for the host's kernel: a Windows-only app cannot run in a container on a Linux host.
  - The boundary is weaker than between VMs: a kernel flaw exploited from one container can affect the others. For the strongest separation (e.g., a bank client), keep the workload in its own VM; the slides give full virtualisation the "best isolation and security" (s14).
- Containers are separated inside the one kernel by **namespaces** **(slides, s28)**.

**Key one-liner:** a container is not a small VM; it is an isolated user space on a shared kernel, so it is light and fast but limited to the host's kernel and less isolated than a VM.

### Concept 5: Type 1 vs Type 2 hypervisors, and what an attack reaches (C18-C22)

- **Type 1 (bare metal, native):** the hypervisor runs **directly on the hardware, with no host OS**. Slide: for **larger scale** applications, i.e., datacenters. Examples: Xen, VMware ESXi, Hyper-V, KVM **(slides, s20-s21, s23)**.
- **Type 2 (hosted, embedded):** the hypervisor runs **on a host OS** and needs it to reach the hardware; normal apps keep running on the host OS beside the VMs. Slide: for **smaller** applications, e.g., a laptop. Examples: VirtualBox, Parallels, VMware Workstation **(slides, s20, s22-s23)**.
- Choose by what must sit under the hypervisor: if the machine must keep working as a normal computer (the student keeps using macOS apps), the host OS stays and the hypervisor is Type 2. The guest OS (Linux here) does not decide the type **(slides, s20-s22)**.
- **Attacks:** the hypervisor itself is "less likely" to be compromised; the targets are the host OS and the guest OS **(slides, s24)**.
  - **Host OS compromised:** the host OS sits below the hypervisor with the highest privilege, so it can compromise the hypervisor and then **every guest** **(slides, s25)**. Only Type 2 has a host OS, so a Type 1 datacenter has no host OS to attack this way **(inferred from s21)**.
  - **Guest OS compromised:** the hypervisor is not compromised; the infection is **isolated** to that guest **(slides, s26)**.

**Key one-liner:** Type 1 sits on bare hardware (datacenters), Type 2 sits on a host OS (laptops); a compromised host OS reaches every guest, a compromised guest stays contained.


### Concept 6: Docker components and what happens on a run (C24-C29)

- Docker packages and runs an app in a loosely isolated **container** that holds everything the app needs, so it is portable; isolation comes from **namespaces**, and it relies on **Linux kernel features** **(slides, s28)**. On a Mac, Docker therefore runs its containers inside a Linux VM (slide annotation "how does Docker run on Mac?... virtualization") **(slides, s28; the Linux VM detail is beyond slides)**.
- Client-server architecture **(slides, s29, s31)**:
  - **Client:** how users interact with Docker (the `docker` command); can talk to more than one daemon.
  - **Daemon:** background process that listens for Docker API requests, builds, runs and distributes containers, and manages images, containers and networks; can talk to other daemons.
  - Client and daemon talk over a **REST API**, through a UNIX socket or a network interface.
- **Registry:** stores images; **Docker Hub** is the public default **(slides, s32)**.
- **Image:** a **read-only template** for creating a container, often based on another image or built from a **Dockerfile** **(slides, s32)**.
- **Container:** a **runnable instance** of an image; can be created, started, stopped, moved or deleted through the Docker API **(slides, s33)**.
- Trace of `docker run <image>` on a fresh machine: client sends the request → daemon checks for the image locally → not found, pulls it from the registry → creates a container from the image → starts it **(slides, s29-s33)**.
- An image is never edited in place. Changes made inside a container belong to that container and are lost when it is deleted. Rebuilding from an edited Dockerfile, or `docker commit`, makes a **new** image, often under the same name, which is why it can feel like editing **(beyond slides)**.

> [!WARNING]
> **Mistake:** tracing `docker run` as starting at the daemon, and thinking a fresh machine skips the local image check. The `docker` command you type **is the client**; it sends the request to the daemon over the REST API. The daemon **always** checks for the image locally first; only if it is missing does it **pull from the registry**. With a cached image, the pull is the step that is skipped.

**Key one-liner:** the client asks, the daemon does the work (pull image from registry, create and start container); images are read-only templates, containers are their disposable running copies.


### Concept 7: Multitenancy vs virtualisation (C31-C32)

- **Multitenancy**, provider view: **a single instance of software runs on a server and serves multiple tenants** (e.g., Dropbox, email). Consumer view: each tenant sees a **dedicated instance with a customised view**. Same arrangement, two sides **(slides, s35)**.
- **Tenant isolation:** a tenant cannot access data and configuration it does not own **(slides, s35)**.
- **Virtualisation** = abstraction of **physical resources**; **multitenancy** = a dedicated consumer instance of **software**. Multitenancy is possible **because of** virtualisation (the dependence runs that way) **(slides, s36)**.
- Single tenancy (a separate application copy per customer) **(beyond slides)**:
  - The customer gains: no shared application instance or data, so a bug or misconfiguration in a shared instance cannot expose its data, and other tenants' load cannot affect it.
  - The provider gives up: the efficiency of one instance; it must run, patch, upgrade and monitor a separate copy, using more resources and work.
  - Both designs can still share physical hardware through VMs; that sharing is virtualisation, not multitenancy.

> [!WARNING]
> **Mistake:** treating multitenancy as sharing physical resources, so that giving a customer its own copy means "no longer sharing hardware". Sharing hardware is **virtualisation**; a separate application copy in its own VM still shares the physical host. **Multitenancy** is sharing **one instance of the software** (and often its database) among tenants. Moving a customer to its own copy removes the shared software instance and data, not the shared hardware.

**Key one-liner:** virtualisation shares hardware; multitenancy shares one software instance among tenants who each see their own dedicated view, and it is built on virtualisation.


### Concept 8: Multitenancy characteristics (C34)

- Six characteristics **(slides, s38)**:
  - **Usage/tenant isolation:** one tenant's behaviour does not affect the others (a bulk upload must not slow everyone).
  - **Data security:** separate procedures for each tenant.
  - **Recovery:** backup and restore (per tenant: restoring one tenant must not roll back the rest).
  - **Scalability:** both the tenants' usage and the number of tenants can grow.
  - **Metered usage:** each tenant is charged only for the features it uses; tenants have different agreements (e.g., Dropbox: 500 MB vs 1 TB).
  - **Data tier isolation:** databases and tables **can be isolated or shared** among tenants; sharing is allowed.
- A shared database is a **cause** that makes per-tenant recovery hard; recovery is the property that fails. Separate databases per tenant make one tenant's restore easy but cost more to run; the app is still multitenant, because the application instance is still shared **(beyond slides)**.
- Real examples **(beyond slides)**: Slack, Gmail, Salesforce, Dropbox run one application for all customers, tagging each record with a tenant ID. In March 2023 a bug in a shared component of ChatGPT showed some users other users' chat titles: one software bug crossing tenants, which hardware separation would not have stopped.

**Key one-liner:** a multitenant app must keep tenants from affecting each other (usage), from seeing each other (data security, tenant isolation), and lets each be restored, scaled and billed on its own; whether the database is shared is a design choice.


### Concept 9: Virtualisation technologies against service models (C30)

- All three service models sit on a virtualisation layer over shared physical infrastructure; what differs is what the consumer is handed **(slides, s34)**:
  - **IaaS** (infrastructure architects): **VMs**; each customer gets its own VM on a shared host.
  - **PaaS** (application developers): application runtime and database instances, a development platform; **Docker** containers, each packaging the customer's code with its own runtime on a shared kernel.
  - **SaaS** (application consumers): a hosted application with database instances and configuration files; **multitenancy**, one application instance shared by many companies.
- Many VMs on one host is virtualisation, not multitenancy (see Concept 7) **(slides, s36)**.

**Key one-liner:** IaaS hands out VMs, PaaS hands out containers and runtimes, SaaS hands out a seat in one shared application; all rest on virtualisation.


## Reference only (not tested)

- Hypervisor vendor table (C21), Docker Desktop (C26), the privilege rings wording (C10).
- Where the virtualisation layer sits (C17, a transition slide), the Docker architecture diagram (C25, covered by Concept 6), the multitenancy example diagram (C33: two organisations' consumers using one multitenant application on one hosting virtual server).

## Not yet tested

None. All concepts C01-C34 checked against the cards: tested in S1-S9 and the gap set, or listed under Reference only.
