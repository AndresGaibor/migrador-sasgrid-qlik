"""Parsea todo el corpus y muestra estadísticas de reconocimiento. Uso: uv run python .claude/scripts/corpus_stats.py [kw ...]"""

import collections
import sys
from pathlib import Path

from sas_grid_migrator.sas_parser.parser import parse_program

root = Path("tests/fixtures/sas")
show = set(sys.argv[1:])
tot = un = fr = 0
top = collections.Counter()
shown = collections.Counter()
for p in sorted(root.rglob("*.sas")):
    r = parse_program(p.read_text(errors="replace"), str(p.relative_to(root)))
    tot += r.stats.statements
    un += r.stats.unrecognized
    fr += r.stats.fragments
    for f in r.findings:
        if f.code == "unrecognized_statement":
            k = (f.message.split() or [""])[0].lower()
            top[k] += 1
            if k in show and shown[k] < 3:
                shown[k] += 1
                print(
                    k, "|", f.evidence.file, f.evidence.line, "|", " ".join(f.message.split())[:90]
                )
print(f"statements={tot} unrecognized_top_level={un} macro_fragments={fr}")
print(top.most_common(20))
