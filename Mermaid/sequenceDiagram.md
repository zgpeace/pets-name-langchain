```mermaid
sequenceDiagram
    participant Client
    participant Server
    Client->>Server: Register user
    activate Server
    Server-->>Client: User already exists.
    deactivate Server

```