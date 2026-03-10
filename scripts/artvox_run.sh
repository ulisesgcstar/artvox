#!/bin/bash

# 1. Iniciar una sesión de tmux llamada 'artvox'
tmux new-session -d -s artvox

# 2. Panel superior: Ejecutar tu Dashboard de Python
tmux send-keys -t artvox "python3 ~/artvox/scripts/dashboard.py" Enter

# 3. Dividir la pantalla horizontalmente (el panel de abajo tendrá el 40% del espacio)
tmux split-window -v -p 40 -t artvox

# 4. Panel inferior: Ejecutar el visualizador CAVA con tu configuración
tmux send-keys -t artvox "cava -p ~/artvox/config/cava_config" Enter

# 5. Conectarse a la sesión para mostrarla en la pantalla de la Pi
tmux attach-session -t artvox