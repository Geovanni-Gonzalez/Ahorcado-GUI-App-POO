# PROGRAMACIÓN II

**Semestre:** I Semestre, 2026

**Estudiante:** Geovan

**Estatus de la entrega:** Excelente

## Descripción del Proyecto

Implementación del juego del Ahorcado (Hangman) utilizando Python y las librerías gráficas Tkinter. El proyecto sigue el paradigma de Programación Orientada a Objetos (POO) y cumple con todos los requerimientos funcionales y administrativos solicitados.

## Estructura de Clases

El proyecto se organiza en módulos claros:

- `app.py`: Clase principal `App` (Hereda de `tk.Tk`) que gestiona la navegación entre frames.
- `admin.py`: Clases `AdminFrame` y `MgmtFrame` para la gestión administrativa.
- `player.py`: Clases `NewGameFrame` y `GameFrame` para la lógica de juego del usuario.
- `logic.py`: Módulo auxiliar para lógica de negocio y persistencia.
- `utils.py`: Constantes, configuraciones y utilidades de sistema.

## Funcionalidades

1. **Administración**:
    - Control de acceso seguro mediante contraseña en `Acceso.txt`.
    - Gestión completa (CRUD) de Palabras y Frases.
    - Validación de duplicados y uso.
2. **Juego**:
    - Modos Principiante (Palabras) y Avanzado (Frases).
    - Sistema de puntuación y pistas.
    - Interfaz gráfica amigable.
3. **Innovaciones**:
    - **Blitz Mode**: Juego con temporizador de 60 segundos.
    - **PvP Mode**: Modo duelo local.
    - **Efectos**: Sonido y partículas.

## Ejecución

Para iniciar el programa, ejecute el siguiente comando desde la carpeta raíz del proyecto:

```bash
python programa/main.py
```

Asegúrese de tener instaladas las librerías estándar de Python. No se requieren instalaciones externas (pip).
