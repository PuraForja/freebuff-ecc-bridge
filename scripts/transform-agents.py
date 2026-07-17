#!/usr/bin/env python3
"""
Transforma agentes para usar módulo compartilhado de Prompt Defense.

Extrai o bloco exato de Prompt Defense de cada agente e substitui
por import + concatenação com o módulo compartilhado em .agents/types/prompt-defense.ts

Uso: python3 scripts/transform-agents.py
"""

import os
import re
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS_DIR = os.path.join(PROJECT_DIR, ".agents")

def transform_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pular se já transformado
    if "from '../types/prompt-defense'" in content:
        return False
    
    # Encontrar o instructionsPrompt
    idx = content.find("  instructionsPrompt: `")
    if idx == -1:
        return False
    
    # O bloco defense termina com "session boundaries."
    marker = "detect repeated abuse and preserve session boundaries."
    marker_pos = content.find(marker, idx)
    if marker_pos == -1:
        return False
    
    # Pular o marker + newlines para chegar ao conteúdo específico
    after_marker = marker_pos + len(marker)
    rest = content[after_marker:]
    stripped = rest.lstrip('\n')
    newlines = len(rest) - len(stripped)
    agent_start = after_marker + newlines
    
    # Encontrar o fechamento da template literal
    closing = content.find("`,\n  spawnerPrompt:", agent_start)
    if closing == -1:
        # Tentar sem newline
        closing = content.find("`,\nspawnerPrompt:", agent_start)
    if closing == -1:
        return False
    
    agent_specific = content[agent_start:closing]
    
    # Construir novo conteúdo usando slicing (evita f-string que corrompe escapes)
    prefix = content[:idx]
    suffix = content[closing + 1:]  # após a vírgula
    new_instructions = '  instructionsPrompt: PROMPT_DEFENSE + `\n\n' + agent_specific + '`,'
    new_content = prefix + new_instructions + suffix
    
    # Adicionar import
    import_line = "import type { AgentDefinition } from '../types/agent-definition'"
    shared_import = "import { PROMPT_DEFENSE } from '../types/prompt-defense'"
    if import_line in new_content and shared_import not in new_content:
        new_content = new_content.replace(import_line, import_line + '\n' + shared_import)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def main():
    print("=" * 60)
    print("🔄 Transform Agents — Extraindo Prompt Defense")
    print("=" * 60)
    
    total = ok = skip = 0
    
    for root, dirs, files in os.walk(AGENTS_DIR):
        for fname in sorted(files):
            if not fname.endswith('.ts') or fname == 'index.ts' or 'types' in root:
                continue
            if fname.startswith('.'):
                continue
            total += 1
            filepath = os.path.join(root, fname)
            try:
                if transform_file(filepath):
                    ok += 1
                    print(f"  ✅ {fname}")
                else:
                    skip += 1
            except Exception as e:
                print(f"  ❌ {fname}: {e}")
    
    print()
    print(f"📊 Total: {total} | Transformados: {ok} | Pulados: {skip}")
    print("=" * 60)


if __name__ == '__main__':
    main()
