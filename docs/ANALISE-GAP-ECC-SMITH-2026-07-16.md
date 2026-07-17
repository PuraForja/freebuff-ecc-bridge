# 🚨 ANÁLISE CRÍTICA — Gap ECC vs Smith

> **Data:** 16/07/2026
> **Descoberta:** 99% do conteúdo dos agents ECC NÃO foi transferido para o Smith

---

## 📊 Resumo da Descoberta

| Agent | ECC (original) | Smith (cópia) | Conteúdo transferido |
|-------|---------------:|:-------------:|:--------------------:|
| code-reviewer | ~400 linhas | ~400 linhas | ✅ **100%** |
| planner | ~200 linhas | **1 linha** | ❌ **~0.5%** |
| tdd-guide | ~150 linhas | **1 linha** | ❌ **~0.7%** |
| security-reviewer | ~250 linhas | **1 linha** | ❌ **~0.4%** |
| architect | ~200 linhas | **1 linha** | ❌ **~0.5%** |

**Conclusão: Apenas 1 dos 5 agents analisados tem o conteúdo completo.**

---

## 🔍 Detalhe da Comparação

### 1. code-reviewer — ✅ ÚNICO COM CONTEÚDO COMPLETO

**ECC (`agents/code-reviewer.md`):**
- Prompt Defense Baseline (regras de segurança)
- Review Process (5 passos detalhados)
- Confidence-Based Filtering (regras de filtragem)
- Pre-Report Gate (4 perguntas obrigatórias)
- Common False Positives (12+ padrões para ignorar)
- Review Checklist completo (Security, Code Quality, React, Node.js, Performance, Best Practices)
- Review Output Format com exemplos
- Summary Format
- Approval Criteria
- v1.8 AI-Generated Code Review Addendum
- **~400 linhas de instruções**

**Smith (`agents/code-reviewer.ts`):**
- instructionsPrompt: array com TODO o conteúdo do ECC
- **~400 linhas** — **TRANSFERIDO COMPLETO** ✅

---

### 2. planner — ❌ QUASE VAZIO

**ECC (`agents/planner.md`):**
- Prompt Defense Baseline
- Your Role (4 responsabilidades)
- Planning Process (4 fases detalhadas)
- Plan Format (template completo com markdown)
- Best Practices (7 regras)
- Worked Example: Stripe Subscriptions (exemplo real com ~80 linhas)
- When Planning Refactors
- Sizing and Phasing
- Red Flags to Check
- **~200 linhas de instruções**

**Smith (`agents/planner.ts`):**
```typescript
instructionsPrompt: `--- name: planner description: Expert planning specialist for complex features and refactoring. Use PROACTIVELY when users request feature implementation, architectural changes, or complex refactoring. Automatically activated for planning tasks.`
```
- **APENAS 1 LINHA** — descrição YAML
- **TODO o conteúdo perdido** ❌

---

### 3. tdd-guide — ❌ QUASE VAZIO

**ECC (`agents/tdd-guide.md`):**
- Prompt Defense Baseline
- Your Role (5 responsabilidades)
- TDD Workflow (6 passos)
- Test Types Required (tabela)
- Edge Cases You MUST Test (8 tipos)
- Test Anti-Patterns
- Quality Checklist (9 itens)
- v1.8 Eval-Driven TDD Addendum
- **~150 linhas de instruções**

**Smith (`agents/tdd-guide.ts`):**
```typescript
instructionsPrompt: `--- name: tdd-guide description: Test-Driven Development specialist enforcing write-tests-first methodology. Use PROACTIVELY when writing new features, fixing bugs, or refactoring code. Ensures 80%+ test coverage.`
```
- **APENAS 1 LINHA** ❌

---

### 4. security-reviewer — ❌ QUASE VAZIO

**ECC (`agents/security-reviewer.md`):**
- Prompt Defense Baseline
- Core Responsibilities (6 áreas)
- Analysis Commands
- Review Workflow (3 fases)
- OWASP Top 10 Check (10 itens detalhados)
- Code Pattern Review (tabela com 9 padrões)
- Key Principles (5 princípios)
- Common False Positives
- Emergency Response
- When to Run
- Success Metrics
- **~250 linhas de instruções**

**Smith (`agents/security-reviewer.ts`):**
```typescript
instructionsPrompt: `--- name: security-reviewer description: Security vulnerability detection and remediation specialist. Use PROACTIVELY after writing code that handles user input, authentication, API endpoints, or sensitive data. Flags secrets, SSRF, injection, unsafe crypto, and OWASP Top 10 vulnerabilities.`
```
- **APENAS 1 LINHA** ❌

---

### 5. architect — ❌ QUASE VAZIO

**ECC (`agents/architect.md`):**
- Prompt Defense Baseline
- Your Role (6 responsabilidades)
- Architecture Review Process (4 fases)
- Architectural Principles (5 princípios)
- Common Patterns (Frontend, Backend, Data)
- Architecture Decision Records (template)
- System Design Checklist
- Red Flags
- Project-Specific Architecture (exemplo)
- Scalability Plan (4 níveis)
- **~200 linhas de instruções**

**Smith (`agents/architect.ts`):**
```typescript
instructionsPrompt: `--- name: architect description: Software architecture specialist for system design, scalability, and technical decision-making. Use PROACTIVELY when planning new features, refactoring large systems, or making architectural decisions.`
```
- **APENAS 1 LINHA** ❌

---

## 📈 Estimativa de Perda Total

### Agents analisados (5 de 68)
| Agent | Linhas ECC | Linhas Smith | Perda |
|-------|:----------:|:------------:|:-----:|
| code-reviewer | ~400 | ~400 | 0% |
| planner | ~200 | 1 | **99.5%** |
| tdd-guide | ~150 | 1 | **99.3%** |
| security-reviewer | ~250 | 1 | **99.6%** |
| architect | ~200 | 1 | **99.5%** |
| **TOTAL** | **~1200** | **~404** | **~66%** |

### Projeção para 68 agents
Se o padrão se mantiver (apenas code-reviewer tem conteúdo completo):
- **67 agents** com apenas 1 linha de descrição
- **1 agent** com conteúdo completo
- **Perda estimada: ~98% do conhecimento**

---

## 🎯 O que foi perdido

Para CADA agent perdido, falta:

1. **Prompt Defense Baseline** — Regras de segurança anti-jailbreak
2. **Processo detalhado** — Passos de execução
3. **Checklists** — O que verificar
4. **Exemplos reais** — Código de exemplo
5. **Padrões de output** — Formato de resposta
6. **False Positives** — O que NÃO reportar
7. **Worked Examples** — Casos de uso completos
8. **Addendums** — Melhorias de versão

**Isso significa que 67 dos 68 agents do Smith são PRÁTICAMENTE INÚTEIS** — eles só têm uma descrição de 1 linha e nenhuma instrução real de como executar.

---

## 🔧 Causa Provável

O script de conversão (provavelmente `ecc-install.sh` ou `sync-ecc.sh`) provavelmente:
1. Leu o **frontmatter YAML** (name + description) de cada `.md`
2. Criou o arquivo `.ts` com essa descrição
3. **NÃO extraiu o corpo do markdown** (após o frontmatter)
4. Apenas o `code-reviewer.md` pode ter sido copiado manualmente

---

## ✅ Ação Necessária

**URGENTE:** Reescrever os `instructionsPrompt` de TODOS os 68 agents com o conteúdo completo do ECC.

### Prioridade:
1. 🔴 **Crítico:** agents de segurança (security-reviewer, healthcare-reviewer)
2. 🔴 **Crítico:** agents principais (planner, architect, tdd-guide)
3. 🟡 **Alto:** reviewers de linguagem (20+ agents)
4. 🟡 **Alto:** build resolvers (11 agents)
5. 🟢 **Médio:** agents especializados (restante)

---

*Análise gerada em 16/07/2026 — URGENTE: reescrever agents*
