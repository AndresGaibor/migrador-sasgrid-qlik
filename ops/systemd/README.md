# Despliegue con systemd + Tailscale Serve

```bash
cd apps/web && bun install && bun run build && cd ../..   # UI compilada (la sirve la API)
uv sync
sudo systemctl link $PWD/ops/systemd/sgm-api.service $PWD/ops/systemd/sgm-tailscale-serve.service
sudo install -d -o ubuntu -g ubuntu -m 0700 /var/lib/sgm/imports
sudo systemctl enable --now sgm-api.service sgm-tailscale-serve.service
```

URL: `https://<host>.<tailnet>.ts.net:3900` (solo tailnet; sin autenticación propia: el límite de acceso es la tailnet).
Tras actualizar código o UI: `sudo systemctl restart sgm-api`.
Logs: `journalctl -u sgm-api -f`. Datos: `/var/lib/sgm`.
