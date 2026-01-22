<div align="center">

# 🗄️ PyDb-Engine

**A high-performance, in-memory relational database engine optimized for $O(\log n)$ retrieval.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Data Structure](https://img.shields.io/badge/Data_Structure-B--Tree-orange?style=for-the-badge)
![Optimization](https://img.shields.io/badge/Optimization-Memory_Efficient-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

</div>

---

## 📖 Overview

**PyDb-Engine** is a custom database implementation designed to bridge the gap between abstract database theory and low-level system optimization. Unlike wrapper libraries, this engine implements its own **lexical analysis**, **query planning**, and **self-balancing B-Tree indexing** from scratch.

The core philosophy is **Memory Efficiency**: By leveraging Python's `__slots__`, the engine drastically reduces memory overhead per record, mimicking C-style struct management while maintaining strict ACID-like transaction isolation in memory.

## ⚙️ Architecture

The engine utilizes a classic tiered architecture to separate parsing logic from data storage:

```mermaid
graph TD
    User[User Input / CLI] -->|SQL String| Lexer[Lexer]
    Lexer -->|Tokens| Parser[Parser & Planner]
    Parser -->|Query Plan| Executor[Executor]
    Executor -->|Seek/Scan| BTree[B-Tree Index]
    BTree -->|Read/Write| Storage[Tuple Storage (__slots__)]
