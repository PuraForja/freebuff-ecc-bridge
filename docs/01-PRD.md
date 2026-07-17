# PRD — Freebuff Agent Smith v3.0

> **Product Requirements Document**
> Versão: 3.0 · Data: 16/07/2026 · Autor: Rolim + Buffy (IA)
>
> 📌 **Propósito deste documento:** Alinhar o time sobre O QUE será construído e POR QUÊ.
> Ele é a "constituição" do projeto — toda decisão deve ser validada contra ele.

---

## 1. Objetivo

> **Por que o Smith existe?**

O Freebuff Agent Smith é um **auto-engenheiro de agentes AI** inspirado no Agent Smith do Matrix. Assim como o vilão copiava a si mesmo, modificava outros programas e criou uma comunidade inteira, o Smith:

- **Descobre** agents em repositórios (GitHub, ECC, CrewAI, Hermes, LangGraph)
- **Analisa** e extrai conhecimento (CONCEITOS, não código)
- **Clona e adapta** agents para o formato Freebuff
- **Instala** e gerencia um ecossistema crescente de agents
- **Observa** o ecossistema e sugere melhorias automáticas

### Frase Definitiva

> **"O Smith não coleciona código. Ele coleciona conhecimento de engenharia."**

### Como funciona na prática

1. 🔍 Usuário pede: "Quero um agente de pesquisa"
2. 🧠 Smith pesquisa local + GitHub, encontra soluções existentes
3. 📊 Compara, apresenta opções ao usuário
4. 🧬 Extrai o CONHECIMENTO (padrões, princípios), não o código
5. 🔧 Adapta e cria o agente no formato Freebuff
6. 📦 Instala, registra linhagem, mantém rastreabilidade
7. 👁️ Monitora o ecossistema continuamente

---

## 2. Problema

> **Qual dor o Smith resolve?**

| Problema | Impacto |
|----------|---------|
| Ecossistemas de agents estão fragmentados (ECC, CrewAI, Hermes, LangGraph) | Não dá para reaproveitar conhecimento entre frameworks |
| Criar agents do zero é demorado e propenso a erros | Horas/dias para cada novo agent |
| Não existe rastreabilidade de onde um agent veio | Impossível saber origem, versão, patches aplicados |
| Atualizações de frameworks quebram agents personalizados | Retrabalho constante |
| Não existe "gerenciador de pacotes" para agents | Impossível atualizar, versionar ou contribuir de volta |
| Agents viram "bagunça" conforme crescem | Código duplicado, padrões inconsistentes |

**Solução:** Uma plataforma que aprende CONHECIMENTO de engenharia (não copia código), mantém linhagem completa, e evolui o ecossistema com segurança.

---

## 3. Público-Alvo

| Perfil | Descrição | Contexto de uso |
|--------|-----------|-----------------|
| **Desenvolvedor AI** | Cria e gerencia agents para Freebuff/Codebuff | Projeto pessoal ou profissional |
| **Equipe de AI** | Múltiplos devs criando agents em paralelo | Colaboração, revisão, versionamento |
| **Explorador** | Quer descobrir e instalar agents prontos | GitHub, ECC, outros repositórios |
| **Contribuidor** | Quer contribuir de volta para projetos originais | Criar PRs automaticamente |

---

## 4. User Stories

### US-01 — Criar Agente
**Como** desenvolvedor AI,
**quero** pedir ao Smith para criar um agente de pesquisa
**para** ter um agente funcional em minutos, não horas.

### US-02 — Descobrir Agents
**Como** explorador,
**quero** que o Smith pesquise GitHub e encontre agents relevantes
**para** não precisar buscar manualmente em dezenas de repositórios.

### US-03 — Gerenciar Patches
**Como** desenvolvedor AI,
**quero** que o Smith detecte quando uma atualização do ECC quebra meus patches
**para** corrigir problemas antes que afetem meu trabalho.

### US-04 — Contribuir de Volta
**Como** contribuidor,
**quero** que o Smith gere automaticamente um PR quando minha melhoria for significativa
**para** contribuir para o ecossistema sem trabalho manual.

### US-05 — Observar Ecossistema
**Como** gerente de agents,
**quero** que o Smith detecte código duplicado e sugira consolidação
**para** manter o ecossistema limpo e eficiente.

### US-06 — Atualizar com Segurança
**Como** desenvolvedor AI,
**quero** que o Smith me avise quando uma atualização do ECC torna meu patch obsoleto
**para** remover patches desnecessários e manter tudo atualizado.

### US-07 — Rastrear Linhagem
**Como** desenvolvedor AI,
**quero** saber a origem completa de cada agent (projeto, versão, patches, autor)
**para** ter rastreabilidade total do conhecimento.

---

## 5. Requisitos Não-Funcionais

| Requisito | Critério |
|-----------|----------|
| **Performance** | Destilação de repos < 5min, criação de agent < 1min |
| **Segurança** | Nunca modificar originais sem autorização explícita |
| **Rastreabilidade** | Todo artefato tem linhagem completa (origem, transformação, destino) |
| **Compatibilidade** | Funciona com ECC, CrewAI, Hermes, LangGraph, projetos GitHub |
| **Extensibilidade** | Novos frameworks podem ser adicionados como fontes |
| **Ética** | Smith recomenda, nunca impõe. Usuário sempre decide |

---

## 6. Fora do Escopo

- ❌ Smith não executa código de terceiros diretamente
- ❌ Smith não modifica repositórios originais sem autorização
- ❌ Smith não substitui o desenvolvedor — apenas assessoria
- ❌ Smith não garante qualidade de agents de terceiros — apenas avalia
- ❌ Smith não é um framework de agents — é uma PLATAFORMA de conhecimento

---

## 7. Métricas de Sucesso

| Métrica | Meta |
|---------|------|
| Tempo para criar um agent funcional | < 5 minutos |
| Precisão da recomendação de agents | > 85% |
| Patches detectados como incompatíveis | 100% antes de quebra |
| PRs gerados automaticamente que são aceitos | > 50% |
| Padrões de engenharia extraídos | > 100 após analisar 500 repos |
| Cobertura de linhagem | 100% dos artefatos rastreados |

---

## 8. Cronograma Estimado

| Fase | Duração | Dependências |
|------|---------|--------------|
| Fase 1: Fundação (Artefatos + Linhagem) | 2 semanas | — |
| Fase 2: Destilador de Conhecimento | 2 semanas | Fase 1 |
| Fase 3: Patches + Smith Update | 2 semanas | Fase 1 |
| Fase 4: Observador + Assimilação | 2 semanas | Fase 2 |
| Fase 5: Contribuição Automática | 1 semana | Fase 3 |
| Fase 6: Biblioteca de Padrões | 1 semana | Fase 2 |

---

## 9. Visão de Arquitetura (Alto Nível)

```
┌─────────────────────────────────────────────────────────┐
│                    FREEBUFF AGENT SMITH                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  DESTILADOR  │  │  OBSERVADOR  │  │  GERENCIADOR │  │
│  │  de          │  │  de          │  │  de          │  │
│  │  Conhecimento│  │  Ecossistema │  │  Patches     │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                 │            │
│         └────────┬────────┘                 │            │
│                  │                          │            │
│         ┌────────▼────────────────────────▼───────┐     │
│         │         BIBLIOTECA SMITH                │     │
│         │    (Conhecimento + Linhagem + DNA)      │     │
│         └─────────────────┬───────────────────────┘     │
│                           │                              │
│         ┌─────────────────▼───────────────────────┐     │
│         │         WORKSPACE                       │     │
│         │    (Artefatos temporários)              │     │
│         └─────────────────┬───────────────────────┘     │
│                           │                              │
│         ┌─────────────────▼───────────────────────┐     │
│         │         RESULTADO                       │     │
│         │    (Agents, Skills, Patches, PRs)       │     │
│         └─────────────────────────────────────────┘     │
│                                                          │
└─────────────────────────────────────────────────────────┘
         ▲                    ▲                    ▲
         │                    │                    │
    ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
    │  ECC    │         │ GitHub  │         │ CrewAI  │
    │ Hermes  │         │ Repos   │         │ LangGraph│
    └─────────┘         └─────────┘         └─────────┘
```

---

*Documento mantido por: Rolim + Buffy*
*Próxima revisão: Após aprovação do GATE 1*
