import {
  ArrowRight,
  BarChart3,
  BookOpen,
  CheckCircle2,
  ChevronRight,
  CircleHelp,
  Clock,
  Download,
  ExternalLink,
  FileText,
  Folder,
  GitFork,
  Info,
  House,
  LayoutGrid,
  List,
  Play,
  Plus,
  Search,
  Settings,
  TriangleAlert,
  Upload,
  X,
  type LucideIcon,
} from "lucide-react";

const icons = {
  grid: LayoutGrid,
  folder: Folder,
  flow: GitFork,
  book: BookOpen,
  settings: Settings,
  help: CircleHelp,
  plus: Plus,
  search: Search,
  arrow: ArrowRight,
  chevron: ChevronRight,
  upload: Upload,
  chart: BarChart3,
  file: FileText,
  check: CheckCircle2,
  warning: TriangleAlert,
  info: Info,
  close: X,
  download: Download,
  play: Play,
  list: List,
  clock: Clock,
  external: ExternalLink,
  home: House,
} satisfies Record<string, LucideIcon>;

export type IconName = keyof typeof icons;
export function Icon({ name, size = 20, className = "" }: { name: IconName; size?: number; className?: string }) {
  const IconComponent = icons[name];
  return <IconComponent className={`icon ${className}`} size={size} strokeWidth={1.6} aria-hidden="true" focusable="false" />;
}
