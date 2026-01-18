# Continuity Claim Layer

VCDesign is not a function that directly controls the system.
This layer is a protocol for defining the **Status** where the system can claim that "Value is Continuous (Value Continuous)".

## The Final Guard

> **This structure never improves value.**
> **It only prevents claiming continuity when value has already drifted.**

You must not bring any expectations of "productivity improvement" or "efficiency" into this layer.
This defines when the signboard (Claim) that the system is VCDesign compliant should be revoked.

## The Claim

The system can claim to be "VCDesign compliant" only while all three of the following elements are functioning:

1.  **The Core (Logic to Protect)**
    * In-design value (Constitution, BOA, Closure of Responsibility) is protected.
2.  **The Sensor (Context Drift Sensor)**
    * Sensors that detect changes in premises or context drift (Drift) are operating and are not being ignored.
3.  **The Loop (Judgment Return Cycle)**
    * A cycle that stops the system or returns it to design upon detection is functioning.

When even one of these is missing, the system may continue to move, but the assertion of **"Continuity" immediately becomes void (INVALID)**.

## The Mechanism (Judgment Logic)

This layer monitors the following signal transitions and determines the status.

| Sensor State | Loop Action | **Claim Status** | Description |
| :--- | :--- | :--- | :--- |
| Normal | (Monitoring) | **VALID** | Operating normally. |
| **Drift Detected** | **No Action / Ignored** | **INVALID** | Warning was ignored. No longer VCDesign. |
| **Drift Detected** | **Returned / Stopped** | **VALID (Maintaining)** | Because it stopped/returned to protect value, the VCDesign status is maintained. |

"Stopping" is not a failure.
Only "running out of control without stopping" means the loss of Claim.
