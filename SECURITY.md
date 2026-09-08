# Security policy

## Reporting

Do not post vulnerability details, real credentials or personal data in public issues. Use GitHub private vulnerability reporting if it is available for this repository. If unavailable, open an issue asking the maintainer to arrange a private reporting channel, without including the vulnerability details.

## Scope

Fixes target the current main branch. These are educational local/reference implementations, not hardened production services. There is no deployment-level authentication, authorization, rate limiting or durable distributed infrastructure.

AI input screening is heuristic and can miss secrets. Never send sensitive source or personal data to an untrusted model provider. Payment compensation only restores local inventory; it does not undo or establish the outcome of an external payment.

The current tests and examples require no secrets. Keep environment files, private keys, user data, databases and generated artifacts out of commits. A clean scan is useful evidence, not a guarantee of every possible secret format.
