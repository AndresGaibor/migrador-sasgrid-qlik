import { Component, type ErrorInfo, type ReactNode } from "react";
import { Icon } from "./Icon";

type Props = { children: ReactNode };
type State = { error?: Error };

export class ErrorBoundary extends Component<Props, State> {
  state: State = {};

  static getDerivedStateFromError(error: Error): State {
    return { error };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error("Error al mostrar una sección de la aplicación", error, info.componentStack);
  }

  render() {
    if (!this.state.error) return this.props.children;
    return (
      <section className="panel error-boundary" role="alert">
        <Icon name="warning" size={28} />
        <div>
          <h1>Esta sección tuvo un problema</h1>
          <p>Los datos guardados no se han modificado. Vuelve a cargar la sección; si el problema continúa, regresa a tus proyectos.</p>
          <div className="next-actions">
            <button onClick={() => this.setState({ error: undefined })}>Volver a intentarlo</button>
            <a className="button secondary" href="#/">Ir a mis proyectos</a>
          </div>
        </div>
      </section>
    );
  }
}
