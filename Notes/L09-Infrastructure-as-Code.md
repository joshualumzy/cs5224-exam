# L09 — Infrastructure as Code

Source: `Lecture 09 - Infrastructure as Code.pdf` (41 slides; s22 break, s40-41 admin). Two past-paper questions map to L09; they stay unseen for the mocks, so the scenarios below are my own.

## Scenario Plan

| # | Scenario | Concepts | Slides |
|---|---|---|---|
| 1 | Prod and staging behave differently | limits of manual GUI/CLI management, what IaC fixes and why, IaC in DevOps (version control, CI/CD, production-like test environments) | s3-9 |
| 2 | Steps vs desired state | imperative vs declarative: rerunning, starting point, drift, idempotency, control | s10-13 |
| 3 | A server fails at 3 a.m. | pets vs cattle, why IaC fits cattle | s19-21 |
| 4 | Choosing a tool | provider tools (CloudFormation, CDK, ARM, Infra Manager) vs independent (Terraform, Pulumi); multi-cloud; language choice | s14-18, s23-24, s33-34 |
| 5 | Terraform in a team | write/plan/apply, state file, resource graph and parallel creation, modules, separate environments, version control | s25-32 |
| 6 | Drift and security after IaC | why drift still happens, detecting it, credentials in code, compliance, self-healing (monitor/analyse/remedy), Policy-as-Code, GitOps | s35-39 |

Then one mixed gap set (4-5 short questions) on what he gets wrong.

## Annotations on the slides (Joshua's handwriting, checked)

- **s8 "deterministic"** next to "Repeatable and Consistent": correct. The same code gives the same infrastructure every run.
- **s15 "imperative" over CDK, "declarative" over CloudFormation:** half right. CloudFormation is declarative (a template describing the end state). CDK code is written in an ordinary programming language, so it *looks* imperative, but it only generates a CloudFormation template, and CloudFormation then works out the changes. The result is still desired-state management (standard AWS CDK docs).
- **s35 "drift is reduced, but still not 0, e.g. Git merge conflicts":** first half right, example wrong. Drift means the live infrastructure no longer matches the code, typically because someone changed it by hand in the console, outside the code. A Git merge conflict is a version-control problem (the separate "Version Control" pitfall on the same slide) and does not change live infrastructure.

## Detailed Notes

### Concept 1. Why IaC: manual management vs code (S1)

- **Infrastructure (slides, s3):** VMs, networks, databases, load balancers and other cloud resources.
- **Manual management (slides, s4-5):** by GUI (clicking buttons) or CLI scripts. Limitations: manual and time-consuming, complex and error-prone, does not scale, configuration drift.
- **How drift creeps in (reasoning):** fixes are clicked straight into one environment and never written down, so documentation describes an older system; rebuilding by hand invites a skipped step or a different default. Nothing records what is actually running, so differences cannot be found.
- **IaC (slides, s6):** "provision and support your computing infrastructure using code instead of manual processes and settings": express the desired infrastructure as code.
- **Mechanism (reasoning):** every environment is built by running the same code (only parameters such as size differ), so they match by construction. Changes are made by editing the code and re-applying, never by clicking, so the code is always the true record and version history shows every change.
- **Why code (slides, s7-9):** software practices apply: version control, CI/CD pipelines, testing, documentation. Key DevOps practice: automated setup, rapid deployment, repeatable and consistent, easy scaling. In DevOps it plugs into CI/CD pipelines, enables production-like test environments, and keeps app code and IaC together for collaboration.

> [!WARNING]
> **Mistake:** IaC prevents differences between environments mainly through version control ("everyone has the latest version"). The core mechanism is that every environment is *built by running the same code*, and changes are made only by editing that code and re-applying; version control then records those changes. A version-controlled document that people still follow by hand would drift just the same.

**Key one-liner:** build every environment by running the same code and change it only through the code, so environments match by construction and the code always describes what is running.

### Concept 2. Imperative vs declarative (S2)

- **Imperative = task management (slides, s10):** the developer writes the exact steps, and must keep track of the system state and manage any changes. Dinner analogy (s11): turn-by-turn directions from COM2 versus just "go to West Coast hawker centre".
- **Declarative = state management (slides, s10):** the developer describes the required state; the tool handles the updates and changes automatically.
- **Mechanism (reasoning):** the declarative tool reads what actually exists, compares it with the file, and makes only the difference. So rerunning changes nothing (idempotent), a half-built or hand-modified system is repaired, and changing the target (3 → 5 VMs) is a one-number edit. An imperative script blindly repeats its steps: rerun it and you get duplicates; to change the system you must first find out its current state and write new steps for that exact starting point.
- **Imperative advantages (slides, s12):** control over every step; ideal for small tasks. **Disadvantages (s13):** difficult to maintain, more prone to human error, less idempotent.
- **Declarative advantages (slides, s12):** less coding skill needed, highly repeatable, adapts well to configuration drift, starting point does not matter, changes to the destination handled automatically. **Disadvantages (s13):** less control (the tool decides the order), can overcomplicate simple tasks.

> [!WARNING]
> **Mistake:** describing declarative as just "I state the end state" and stopping there. The point is what the tool does with it: compare the stated state with what actually exists and create, change or delete only the difference. That comparison is why rerunning is safe and why the starting point does not matter.

**Key one-liner:** imperative replays fixed steps and needs you to know the current state; declarative compares desired with actual and applies only the difference, so it is safe to rerun from any starting point.

### Concept 3. Pets vs cattle (S3)

- **Pets (slides, s19):** servers individually managed and cared for, named and treated as important; maintenance and recovery need manual intervention. E.g. a dedicated web server.
- **Cattle (slides, s20):** interchangeable servers, configured identically, replaced when they fail with no manual repair. E.g. web servers behind a load balancer that can be swapped quickly.
- **IaC uses the cattle model (slides, s21):** it allows rapid, consistent deployment and management of cloud resources.
- **What happens when a cattle server dies (reasoning; health checks and auto-scaling: beyond slides, AWS docs):** (1) the load balancer's health check sees it stop answering and stops sending it traffic; (2) the other identical servers keep serving, so users notice nothing; (3) the auto-scaling group sees one server fewer than wanted and launches a fresh one from the same definition; (4) the dead one is thrown away. This works only if no server holds unique data (state in a separate database, L06).
- **Who does what (reasoning):** IaC defines the server so any copy is identical and quick to build. It does not watch servers; detection and replacement come from health checks and auto-scaling. Automatic detect-and-fix inside IaC is "self-healing IaC", a future trend (s38-39).
- **Cost trade-off (reasoning):** a stored definition costs nothing. One running server that is auto-replaced from its definition costs one server but gives a few minutes of downtime while the new one boots; several running servers cost more but give no downtime. Pick by how much an outage costs.
- **When a pet is right (reasoning):** something that cannot be rebuilt from a definition, e.g. a one-of-a-kind legacy server.

> [!WARNING]
> **Mistake:** IaC's role in surviving a server failure is "self-healing" (it detects the dead server and replaces it). IaC describes the server in code so identical copies can be built in minutes; the load balancer's health checks and auto-scaling do the detecting and replacing.

**Key one-liner:** cattle = several identical servers built from the same code behind a load balancer; a dead one is dropped and replaced automatically, never repaired, and IaC is what makes the replacement identical and fast.

### Concept 4. Choosing a tool (S4)

- **Cloud provider tools (slides, s14-18):** AWS CloudFormation (declarative templates) and AWS CDK (familiar programming languages in the IDE); Azure Resource Manager (declarative templates, manage resources as a group, redeploy in a consistent state, Azure RBAC built in); Google Infrastructure Manager (uses Terraform configurations and deploys them onto Google Cloud; application deployment via Cloud Build and Cloud Deploy). Each works only on its own cloud.
- **Terraform (slides, s23-24):** declarative, cloud agnostic, multi-cloud; works with any platform that has an API through providers from the Terraform registry.
- **Pulumi (slides, s33-34):** infrastructure code in familiar languages (TypeScript, Python, Go, C#), flexibility for more complex logic; multi-cloud (beyond slides, Pulumi docs).
- **Picking (reasoning):** several clouds → Terraform or Pulumi; one cloud and want its native service → that provider's tool; complex logic in a language the team already knows → Pulumi (or CDK if AWS only).

**Key one-liner:** provider tools lock you to one cloud; Terraform and Pulumi cover many clouds, and Pulumi lets you write the infrastructure in an ordinary programming language.

### Concept 5. Terraform in a team (S5)

- **Core workflow (slides, s25, s27-30):** Write (configuration files, kept in Git; `terraform init` loads providers) → Plan (`terraform plan` previews the changes Terraform will make) → Apply (`terraform apply` shows the plan, asks for "yes", provisions the infrastructure and updates the state file).
- **Configuration vs state file (slides, s25-26; reasoning):** the configuration (`.tf` files) is what you want, written by you. The state file is Terraform's record of what it has actually created. Plan compares the two (refreshed against the real cloud) to work out the difference.
- **What plan and apply actually check (beyond slides, Terraform docs):** the state file does not update itself when someone changes the cloud by hand. Plan and apply first refresh: for each resource listed in the state, they look up that real resource by its ID, then compare with the configuration and act on the difference (e.g. one VM deleted by hand → "1 to add" → recreated → state updated). They do not scan the whole cloud, so a resource created by hand that is not in the state is invisible to Terraform.
- **Why the state file is needed (beyond slides, Terraform docs):** it is used by Terraform itself. (1) It maps each resource in the configuration to one real resource ID, so Terraform knows which of the account's many VMs are its own and never duplicates or touches others'. (2) It remembers what Terraform created, so removing a resource from the configuration leads to destroying it. (3) Terraform checks only its own resources instead of scanning everything. (4) It defines what one folder owns, which is why separate state files separate environments.
- **Different settings per environment (beyond slides, Terraform docs):** the module declares input variables (e.g. `server_count`, `instance_size`, `enable_backups`); each environment passes its own values. Something only one environment has is either a module input that switches it on (`count = var.enable_cdn ? 1 : 0`) or an extra resource written only in that environment's folder.
- **Resource graph (slides, s26):** Terraform works out which resources depend on which and creates or modifies non-dependent ones in parallel (network first, then subnets in parallel; unrelated buckets in parallel from the start).
- **Modules (slides, s26):** reusable, configurable collections of infrastructure; from the Terraform Registry or your own. Encourage best practices.
- **Collaborate (slides, s26):** configuration in version control; HCP Terraform to manage workflow across teams.
- **Layout (reasoning):** the module is its own folder of `.tf` files with input variables (e.g. `server_count`); each environment is its own small folder whose configuration calls the module with its values, and each has its own state file.
- **Separate environments (reasoning):** write the infrastructure once as a module; each environment calls the module with its own settings and has its own state file. One definition means environments cannot diverge and a fix reaches all; separate state means an apply in dev can only touch dev. Copying the folder per environment lets the copies diverge; one shared state means every apply covers production too.

> [!WARNING]
> **Mistake (twice):** mixing up the configuration and the state file, and assuming the state file tracks the live system by itself (so a VM deleted by hand would go unnoticed). The configuration is what you want; the state file is Terraform's record of what it created; plan and apply re-read the real cloud first, so a hand deletion is found and recreated. Separate environments need separate state files; putting them in different modules but one state does not separate them.

**Key one-liner:** one module defines the infrastructure, each environment uses it with its own settings and its own state file, so environments stay alike and changing one can never touch another.

### Concept 6. Drift, security and the future (S6)

- **Pitfalls (slides, s35-37):** learning curve, many tools, code complexity, version control, configuration drift (reduced but still possible), security and compliance.
- **Drift after IaC (reasoning):** someone changes the live system by hand (e.g. an emergency fix in the console), so it no longer matches the code.
- **Detecting drift (reasoning; plan s28):** run `terraform plan` automatically on a schedule (e.g. nightly in CI/CD). Plan reads the real infrastructure, compares it with the configuration and lists the changes needed; any listed change means drift, so alert the team.
- **What the next apply does (slides, s29; reasoning):** apply makes its own plan first, checking the real cloud. It sees a hand change to any resource it tracks and its plan lists the reversal, so an emergency fix is undone unnoticed if whoever approves (or an auto-approving pipeline) does not read the plan, possibly during an unrelated change. A resource created by hand is not in the state and is left alone. The habit: put every emergency hand change into the code (or revert it) through normal review.
- **Security and compliance (slides, s37):** misconfigurations need continuous monitoring (a mistake in code is copied into every environment built from it); protect the code and the credentials or access keys, or risk a data breach; drift can break compliance standards.
- **Future (slides, s38-39):** AI-driven deployment; Policy-as-Code (pipelines check changes against policy); GitOps (changes deployed from Git to the system automatically); self-healing IaC: monitor (collect workload and server state), analyse (compare with baselines and prediction models), remedy (create a fix plan and carry it out).

> [!WARNING]
> **Mistake:** "`terraform apply` without a plan might assume the port is still closed." Apply always makes its own plan first, checking the real cloud, so it sees the hand-made change and reverts it to match the code. That is the danger: a forgotten emergency fix is silently undone at the next apply.

**Key one-liner:** IaC reduces drift but hand changes still cause it; a scheduled `plan` detects it, and the next `apply` reverts it, so emergency fixes must go back into the code.

## Reference only (not tested)

- Tool names and dates: Terraform 2014, HashiCorp, Business Source Licence from 2023 (s23); Pulumi 2018, Pulumi Neo (s33); Google Deployment Manager discontinued, replaced by Infra Manager (s18); the tool list on s36.
- Terraform language elements: blocks, arguments, expressions (s31); the S3 bucket examples (s32, s34).
- Azure Resource Manager diagram (s17): portal, PowerShell, CLI and REST clients all go through ARM (with authentication) to the resources.

## Not yet tested

All six scenarios done. Touched only lightly (MCQ options): Policy-as-Code, GitOps, self-healing IaC, protecting credentials. Not tested: learning curve, code complexity, number of tools (s35-36): plain recall.
