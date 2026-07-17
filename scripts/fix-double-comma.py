#!/usr/bin/env python3
"""
Fix: Remove double comma in transformed agents.
Searches for: ` , , newline spaces spawnerPrompt  →  ` , newline spaces spawnerPrompt
"""

import os

AGENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".agents")

fixed = 0
for root, dirs, files in os.walk(AGENTS_DIR):
    for fname in files:
        if not fname.endswith('.ts') or fname == 'index.ts':
            continue
        path = os.path.join(root, fname)
        with open(path, 'r') as fh:
            content = fh.read()
        # Pattern: backtick, comma, comma, newline
        # We need to find backtick+comma+comma and change to backtick+comma
        # The actual text is: ...project?"`,   ,\n  spawnerPrompt:...
        #                                     ^backtick ^comma1 ^comma2
        old = "`,\n  spawnerPrompt:"
        idx = content.find(old)
        if idx > 0 and content[idx-1] == ',':
            # Found: comma, backtick? No, we have: ...`,  ,\n...
            # Actually the pattern is: backtick, comma, comma, newline
            # So at `idx` we find: `, \n  spawnerPrompt:
            # And content[idx-1] is a comma
            # Wait, let me think again:
            # The file has: ...\"`,,\n  spawnerPrompt:...
            # That's: backtick at pos X, comma at X+1, comma at X+2, newline at X+3
            # So content[idx] where idx = content.find("`,\n  spawnerPrompt:")
            # This finds: ` at some pos, , at next, \n at next...
            # So idx points to the backtick
            # content[idx-1] would be " before the backtick
            # I need to check content[idx+1] and content[idx+2] for double comma
            
            # Let me try a different approach - find the exact double-comma pattern
            pass
        
        # Simpler approach: find text ending with comma+backtick+comma+newline+spawnerPrompt
        # Or just: grep for `, then \n  spawnerPrompt: and see if there are 2 commas
        
        # Let me search for the raw bytes
        lines = content.split('\n')
        changed = False
        new_lines = []
        for line in lines:
            # Check if line ends with double comma (before the spawnerPrompt line)
            if line.rstrip().endswith(',,') and 'spawnerPrompt' not in line:
                line = line.rstrip()[:-1]  # Remove last comma
                changed = True
            new_lines.append(line)
        
        if changed:
            content = '\n'.join(new_lines)
            with open(path, 'w') as fh:
                fh.write(content)
            fixed += 1
            print(f"  ✅ {fname}")

print(f"\nFixed: {fixed} files")
