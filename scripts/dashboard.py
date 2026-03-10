import os
import socket
from datetime import datetime
import time
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

console = Console()

def get_cpu_temp():
    """Obtiene la temperatura y define el color según el estado"""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_raw = f.read()
            temp_c = float(temp_raw) / 1000.0
            
            # Lógica de colores: Verde seguro, Rojo advertencia
            if temp_c < 70.0:
                color = "bold green"
            else:
                color = "bold red"
                
            return f"[{color}]CPU TEMP: {temp_c:.1f}°C[/{color}]"
    except:
        return "[white]CPU TEMP: N/A[/white]"

def generate_layout():
    """Genera la interfaz con Colores Neon y Reloj Cyan Limpio"""
    hora = datetime.now().strftime("%H:%M:%S")
    fecha = datetime.now().strftime("%d / %m / %Y")
    temp_info = get_cpu_temp()
    user_name = os.getlogin().upper()
    
    # Tabla principal configurada para centrar todo el contenido
    table = Table(show_header=False, border_style="cyan", expand=True, box=None)
    table.add_column(justify="center") 
    
    # 1. Nombre en Verde Fosforescente
    table.add_row(f"[bold bright_green]ARTVOX BY.{user_name}[/bold bright_green]")
    
    # 2. Fecha en Blanco
    table.add_row(f"[white]{fecha}[/white]")
    
    # 3. Temperatura Dinámica
    table.add_row(temp_info)
    
    table.add_row("") # Espacio estético

    # 4. Reloj en Color Cyan (Solo los números, sin fondo)
    table.add_row(f"[bold cyan]{hora}[/bold cyan]")
    
    table.add_row("") # Espacio estético
    table.add_row("[italic white]Esperando Spotify Connect...[/italic white]")
    
    return Panel(
        table, 
        title="[bold white]Control Panel[/bold white]", 
        border_style="blue",
        padding=(1, 1)
    )

if __name__ == "__main__":
    try:
        # Live permite que la terminal se actualice sin parpadeos molestos
        with Live(generate_layout(), refresh_per_second=1, screen=True) as live:
            while True:
                live.update(generate_layout())
                time.sleep(1)
    except KeyboardInterrupt:
        # Permite salir con Ctrl+C sin mostrar errores de Python
        pass