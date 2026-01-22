<div align="center">

<!-- Dynamic Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=87ceeb&height=250&section=header&text=PyDb-Engine&fontSize=80&animation=fadeIn&fontAlignY=38&desc=Build%20.%20Index%20.%20Query&descAlignY=58&descAlign=50&fontColor=36454f" width="100%" />

<!-- Badges Section -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Architecture-B--Tree-ff9f1c?style=for-the-badge&logo=structure&logoColor=white" alt="Data Structure" />
  <img src="https://img.shields.io/badge/Type-In--Memory-7c3aed?style=for-the-badge&logo=memory&logoColor=white" alt="In-Memory" />
  <img src="https://img.shields.io/badge/License-MIT-94a3b8?style=for-the-badge&logo=open-source-initiative&logoColor=white" alt="License" />
</p>

<!-- Tagline -->
<h3>⚡ A high-performance, in-memory relational database engine built from scratch.</h3>
<p><i>No SQLite wrappers. Pure Python implementation of database internals.</i></p>

<!-- Action Buttons -->
[Report Bug](https://github.com/your-username/PyDb-Engine/issues) · [Request Feature](https://github.com/your-username/PyDb-Engine/issues)

</div>

<br />

---

## 📖 Overview

**PyDb-Engine** exists to demystify the "magic" of databases. It is a fully functional SQL engine that implements **lexical analysis**, **query planning**, and **B-Tree indexing** entirely in memory.

> [!IMPORTANT]
> **Why In-Memory?**
> This project focuses on the *logic* of database management systems (DBMS)—specifically how to parse SQL into executable plans and how to structure data for **$O(\log n)$** retrieval—without the overhead of disk I/O management.

---

## ⚙️ Architecture

The engine utilizes a tiered architecture, strictly separating the Query Processor from the Storage Engine.

```mermaid
graph TD
    subgraph Query Processor
    User[User Input] -->|SQL String| Lexer[Lexer / Tokenizer]
    Lexer -->|Tokens| Parser[Parser / Planner]
    Parser -->|Query Plan| Optimizer[Query Optimizer]
    Optimizer -->|Execution Plan| Executor
    end

    subgraph Storage Engine
    Executor -->|Seek/Scan| BTree[B-Tree Index]
    BTree -- "O(log n) Pointer" --> Heap["Heap Storage (__slots__)"]
    Executor -->|Linear Scan| Heap
    end
    
    style BTree fill:#f9f,stroke:#333,stroke-width:2px,color:#000
    style Heap fill:#bbf,stroke:#333,stroke-width:2px,color:#000
    style Optimizer fill:#ff9f1c,stroke:#333,stroke-width:2px,color:#000
