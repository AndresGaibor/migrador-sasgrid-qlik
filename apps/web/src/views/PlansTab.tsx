import { PlanDetail } from "./plans/PlanDetail";
import { PlanList } from "./plans/PlanList";

export function PlansTab({ id, file }: { id: string; file?: string }) {
  return file ? <PlanDetail key={`${id}:${decodeURI(file)}`} id={id} file={decodeURI(file)} /> : <PlanList id={id} />;
}
