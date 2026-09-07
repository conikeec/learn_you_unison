---
name: unison-services
description: Build and operate Unison HTTP or typed services, external integrations, concurrent programs, and deployments. Use when a Unison task crosses a process, network, storage, or Cloud boundary.
---

# Choose the execution boundary first

Distinguish a local CLI, an ordinary HTTP service, and a Unison Cloud program.
Unison programs can run outside Unison Cloud; Cloud APIs belong to libraries and a deployment platform.
Read [service decisions](references/services.md) before selecting dependencies or packaging.

## Implement the boundary with explicit failures

1. Inspect the installed HTTP, JSON, IO, concurrency, or Cloud definitions relevant to the task.
2. Define the external contract: input validation, result type, expected failures, and remaining effects.
3. Keep domain logic pure or behind a narrow ability where that supports testing.
4. Implement a thin interpreter or transport boundary. Inspect parsing and encoding behavior instead of concatenating payload strings.
5. Test malformed input, external failure, timeout/cancellation, and cleanup where relevant.
6. Package or deploy through the selected runtime, then exercise its real entrypoint.

## Separate implementation from deployment evidence

Typechecked deployment code has not deployed a service.
After authorized deployment, record the exact environment, returned service reference or artifact, and a real request result.
For mutable service names, record which service hash the name resolves to.
Do not treat a successful HTTP connection as evidence that its response satisfies the application's schema.

Native Unison service calls can preserve typed interfaces across the network.
They still require operational failure handling and compatible deployed types.
See [native services](https://www.unison.cloud/learn/native-services/) for the platform's model.
