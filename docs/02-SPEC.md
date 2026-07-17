# SPEC — Freebuff Agent Smith v3.0

> **Especificação Técnica**
> Versão: 3.0 · Data: 16/07/2026 · Autor: Rolim + Buffy (IA)
>
> 📌 **Propósito:** Especificar COMO o Smith será implementado — arquitetura, decisões técnicas, componentes.
> Assume que você leu o `01-PRD.md` (O QUÊ e POR QUÊ).

---

## 1. Visão Geral da Arquitetura

### 1.1 Diagrama de Fluxo

```
┌─────────────────────────────────────────────────────────────┐
│                      FONTES (Read Only)                      │
│  ┌─────┐  ┌───────┐  ┌────────┐  ┌──────────┐  ┌───────┐  │
│  │ ECC │  │ GitHub│  │ CrewAI │  │LangGraph │  │Hermes │  │
│  └──┬──┘  └───┬───┘  └───┬────┘  └────┬─────┘  └───┬───┘  │
│     └─────────┴──────────┴────────────┴─────────────┘      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │  DESTILADOR │  ← Extrai CONHECIMENTO
                    │  de         │    (conceitos, padrões,
                    │  Conhecimento│    princípios)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ BIBLIOTECA  │  ← Armazena DNA
                    │ SMITH       │    (conhecimento reutilizável)
                    │             │    + Linhagem completa
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼────────┐ ┌─▼───────────┐
       │  CRIADOR    │ │OBSERVADOR │ │ GERENCIADOR │
       │  de Agents  │ │ de        │ │ de Patches  │
       │             │ │Ecossistema│ │             │
       └──────┬──────┘ └──┬────────┘ └─┬───────────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼──────┐
                    │  WORKSPACE  │  ← Artefatos temporários
                    │  (temp)     │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  RESULTADO  │  ← Agents, Skills, Patches, PRs
                    │  Final      │
                    └─────────────┘
```

### 1.2 Stack Técnica

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| **Agent Principal** | TypeScript (.agents/*.ts) | Padrão Freebuff |
| **Modelo LLM** | mimo/mimo-v2.5 | Análise profunda |
| **Modelo Rápido** | deepseek/deepseek-v4-flash | Tarefas leves |
| **Banco de Conhecimento** | JSON + Markdown | Simples, versionável |
| **GitHub API** | REST + GraphQL | Descoberta de repos |
| **Workspace** | Diretório temporário | Isolamento de experimentos |
| **Ferramentas** | spawn_agents, read_files, code_search, web_search | Tools existentes |

---

## 2. Decisões Técnicas (ADRs)

### ADR-001: Conhecimento, não Código

| Campo | Detalhe |
|-------|---------|
| **Contexto** | Precisamos reaproveitar conhecimento entre frameworks sem copiar código |
| **Opção A** | Copiar código e adaptar (como fazemos hoje) |
| **Opção B** | Extrair conceitos e princípios abstratos |
| **Decisão** | **Opção B** — Extrair CONHECIMENTO reutilizável |
| **Motivo** | Código fica obsoleto em meses. Princípios duram décadas |
| **Consequência** | Mais complexo de implementar, mas muito mais poderoso |

### ADR-002: Nunca Modificar Originais

| Campo | Detalhe |
|-------|---------|
| **Contexto** | Precisamos manter rastreabilidade e compatibilidade |
| **Opção A** | Modificar repositórios originais diretamente |
| **Opção B** | Camada Read Only + Patches separados |
| **Decisão** | **Opção B** — Originais são intocáveis |
| **Motivo** | Preserva compatibilidade, facilita atualizações, permite contribuição de volta |
| **Consequência** | Necessidade de sistema de patches |

### ADR-003: Artefatos, não Arquivos

| Campo | Detalhe |
|-------|---------|
| **Contexto** | Agentes são compostos de múltiplos elementos (prompts, tools, configs) |
| **Opção A** | Tratar como arquivos (.ts, .md) |
| **Opção B** | Abstrair como "artefatos" tipados |
| **Decisão** | **Opção B** — Tudo é um artefato |
| **Motivo** | Permite operações uniformes (cliclar, adaptar, versionar) |
| **Consequência** | Camada de abstração adicional |

### ADR-004: Linhagem Obrigatória

| Campo | Detalhe |
|-------|---------|
| **Contexto** | Precisamos saber de onde veio cada componente |
| **Opção A** | Metadados opcionais |
| **Opção B** | Linhagem obrigatória em todo artefato |
| **Decisão** | **Opção B** — Toda transformação é rastreada |
| **Motivo** | Permite atualizações seguras, contribuição de volta, auditoria |
| **Consequência** | Overhead mínimo na criação |

---

## 3. Estrutura do Projeto

```
freebuff-agent-smith/
├── .agents/
│   ├── agent-smith.ts              ← Agente principal (v3.0)
│   ├── types/
│   │   ├── agent-definition.ts     ← Tipos de agent
│   │   ├── artifact.ts             ← NOVO: Tipos de artefato
│   │   ├── lineage.ts              ← NOVO: Tipos de linhagem
│   │   ├── patch.ts                ← NOVO: Tipos de patch
│   │   └── knowledge.ts            ← NOVO: Tipos de conhecimento
│   └── *.ts                        ← Agents existentes
├── skills/                         ← 278 skills existentes
├── knowledge/                      ← NOVO: Banco de conhecimento
│   ├── patterns/                   ← Padrões extraídos
│   ├── principles/                 ← Princípios de engenharia
│   ├── lineage/                    ← Linhagem dos artefatos
│   └── index.json                  ← Índice de tudo
├── patches/                        ← NOVO: Patches aplicados
│   ├── ecc/                        ← Patches no ECC
│   ├── github/                     ← Patches em repos GitHub
│   └── index.json                  ← Registro de patches
├── workspace/                      ← NOVO: Workspace temporário
│   └── (criado dinamicamente)
├── docs/
│   ├── 01-PRD.md                   ← Requisitos
│   ├── 02-SPEC.md                  ← Este arquivo
│   ├── 03-PLAN.md                  ← Plano de implementação
│   ├── 04-TASKS.md                 ← Tarefas
│   ├── 05-REVIEW.md                ← Revisão
│   └── COLETANEA-IDÉIAS-SMITH.md   ← Referência bruta
├── scripts/
│   ├── ecc-install.sh
│   └── sync-ecc.sh
├── .ecc-config.json
├── knowledge.md
├── CATALOGO.md
└── SESSAO.md
```

---

## 4. Componentes

### 4.1 Destilador de Conhecimento

**Responsabilidade:** Extrair CONHECIMENTO (conceitos, padrões, princípios) de repositórios, NÃO código.

**Fluxo:**
```
1. Receber URL/nome do repositório
2. Listar agents e skills do repo
3. Para cada agente:
   a. Ler instructionsPrompt
   b. Identificar padrões (antes de fazer X, sempre faz Y)
   c. Generalizar o conceito (sem depender de linguagem)
   d. Classificar qualidade (1-10)
   e. Extrair "DNA" reutilizável
4. Salvar na Biblioteca Smith
5. Atualizar linhagem
```

**Exemplo de DNA extraído:**
```json
{
  "concept": "Planner before Execute",
  "description": "Antes de qualquer execução, criar um plano estruturado",
  "origin": "ECC/planner + CrewAI/planner",
  "quality": 9.2,
  "applicableTo": ["any-language", "any-framework"],
  "pattern": "planejar → aprovar → executar → revisar"
}
```

### 4.2 Observador de Ecossistema

**Responsabilidade:** Monitorar o ecossistema local e sugerir melhorias.

**Capacidades:**
1. **Detecção de duplicação:** Encontra padrões repetidos em múltiplos agents
2. **Consolidação:** Sugere extrair código comum para Skill compartilhada
3. **Padronização:** Detecta implementações inconsistentes do mesmo conceito
4. **Qualidade:** Avalia agents e sugere melhorias
5. **Saúde:** Monitora tamanho, complexidade, dependências

**Exemplo de mensagem:**
```
👁️ Observador detectou:
- 12 agents usam a mesma lógica de "Research First"
- Possível consolidar em uma Skill compartilhada
- Economia estimada: 430 linhas
Deseja analisar?
```

### 4.3 Gerenciador de Patches

**Responsabilidade:** Gerenciar personalizações aplicadas a repositórios de terceiros.

**Operações:**
1. **Criar patch:** Registrar modificação feita em artefato de terceiros
2. **Listar patches:** Mostrar todos os patches aplicados
3. **Verificar compatibilidade:** Detectar quando atualização quebra patches
4. **Remover patch:** Quando upstream implementou oficialmente
5. **Gerar PR:** Preparar Pull Request para contribuição

**Estrutura de Patch:**
```json
{
  "id": "patch-001",
  "target": "ECC/skills/pdf-reader",
  "targetVersion": "2.1",
  "description": "Adicionar suporte a UTF-8",
  "createdAt": "2026-07-16",
  "status": "active",
  "linesChanged": 12,
  "tokenReduction": "28%"
}
```

### 4.4 Biblioteca de Padrões

**Responsabilidade:** Armazenar padrões de engenharia extraídos de múltiplos projetos.

**Padrões iniciais:**
| Padrão | Descrição | Origem |
|--------|-----------|--------|
| Planner before Execute | Planejar antes de executar | ECC, CrewAI |
| Research First | Pesquisar antes de criar | ECC |
| Self Review | Autoavaliação obrigatória | ECC |
| Least Artifact | Menor artefato capaz | Conceitual |
| Read Only Source | Nunca modificar originais | Git, Conceitual |
| Lineage Tracking | Rastrear origem sempre | Git |
| Patch System | Personalizar sem modificar | apt, npm |
| Knowledge over Code | Extrair conceitos | Conceitual |

---

## 5. Configuração

### 5.1 Variáveis de Ambiente

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SMITH_KNOWLEDGE_DIR` | Diretório da biblioteca | `./knowledge/` |
| `SMITH_PATCHES_DIR` | Diretório de patches | `./patches/` |
| `SMITH_WORKSPACE_DIR` | Diretório temporário | `./workspace/` |
| `GITHUB_TOKEN` | Token para API GitHub | `ghp_xxx` |

### 5.2 Dependências

| Pacote | Versão | Finalidade |
|--------|--------|------------|
| @octokit/rest | latest | API GitHub |
| typescript | ^5.0 | Tipagem |
| (ferramentas existentes) | — | spawn_agents, read_files, etc. |

---

## 6. Fluxos Principais

### 6.1 Criar Agent

```
Usuário: "Quero um agente de pesquisa"
    ↓
Smith: "Pesquisando local + GitHub..."
    ↓
Smith: "Encontrei 3 opções:
  1. ECC/search (qualidade 9.2)
  2. CrewAI/researcher (qualidade 8.5)
  3. Criar do zero"
    ↓
Usuário: "Opção 1"
    ↓
Smith: "Extraindo conhecimento do ECC/search..."
    ↓
Smith: "DNA extraído: Research First + Source Validation"
    ↓
Smith: "Criando workspace temporário..."
    ↓
Smith: "Adaptando para formato Freebuff..."
    ↓
Smith: "Agent criado! Linhagem registrada."
    ↓
Usuário: "Salvar como novo agent"
    ↓
Smith: "Salvo em .agents/research-agent.ts"
    ↓
Smith: "Linhagem: ECC/search v2.1 → Smith v3.0 → MeuProjeto"
```

### 6.2 Detectar Incompatibilidade

```
Smith (verificação semanal):
    ↓
"ECC recebeu atualização v2.2"
    ↓
"Verificando 5 patches aplicados..."
    ↓
"4 patches compatíveis ✅"
    ↓
"1 patch incompatível ⚠️"
    ↓
"Patch: pdf-reader-utf8
 Target: ECC/skills/pdf-reader
 Motivo: ECC v2.2 adicionou suporte UTF-8 oficialmente"
    ↓
"Deseja:
  1. Remover patch (já implementado upstream)
  2. Manter patch (customizações adicionais)
  3. Revisar diff"
```

---

## 7. Considerações de Performance

| Gargalo | Impacto | Mitigação |
|---------|---------|-----------|
| Destilação de repo grande | Alto | Cache de conhecimento, processamento incremental |
| Muitos patches | Médio | Índices JSON, verificação lazy |
| Workspace temporário | Baixo | Limpeza automática após uso |

---

## 8. Limitações Conhecidas

| Limitação | Detalhe | Impacto |
|-----------|---------|---------|
| API GitHub rate limit | 5000 req/hora | Limitar destilações simultâneas |
| LLM não entende tudo | Conceitos abstratos podem ser mal extraídos | Validação humana recomendada |
| Patches complexos | Múltiplas modificações no mesmo arquivo | Limitar a 1 patch por arquivo |
| Frameworks novos | Nem todos têm estrutura analisável | Fallback para análise manual |

---

*Documento mantido por: Rolim + Buffy*
*Próxima revisão: Após aprovação do GATE 1*
