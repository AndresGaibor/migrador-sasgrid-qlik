export type OrderedStep = { order: number; id?: string };
export function orderSteps<T extends OrderedStep>(steps: T[]): T[] {
  return steps.map((step, index) => ({ step, index })).sort((a, b) => a.step.order - b.step.order || a.index - b.index).map(({ step }) => step);
}

export type SourceNode = {
  type?: string;
  loc?: { line?: number; end_line?: number };
  line?: number;
  text?: string;
  statements?: { line?: number; text?: string }[];
  queries?: { text?: string; loc?: { line?: number; end_line?: number } }[];
  body?: SourceNode[];
};
export type SourceExcerpt = { line: number; text: string };

export function sourceLines(nodes: SourceNode[]): SourceExcerpt[] {
  const lines: SourceExcerpt[] = [];
  const add = (line: number | undefined, text: string | undefined) => {
    if (typeof line === "number" && text?.trim()) lines.push({ line, text: text.trim() });
  };
  const visit = (node: SourceNode) => {
    add(node.line ?? node.loc?.line, node.text);
    for (const statement of node.statements ?? []) add(statement.line, statement.text);
    for (const query of node.queries ?? []) add(query.loc?.line, query.text);
    for (const child of node.body ?? []) visit(child);
  };
  for (const node of nodes) visit(node);
  const unique = new Map<string, SourceExcerpt>();
  for (const line of lines) unique.set(`${line.line}\0${line.text}`, line);
  return [...unique.values()].sort((a, b) => a.line - b.line);
}

export function sourceEvidence(nodes: SourceNode[], line: number): SourceExcerpt | null {
  const lines = sourceLines(nodes);
  return lines.find((item) => item.line === line) ?? lines.find((item) => item.line < line && item.line + 1 > line) ?? null;
}
