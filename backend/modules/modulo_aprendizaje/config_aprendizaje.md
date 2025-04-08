# Configuración de Aprendizaje del Clon

Este módulo define cómo se entrena la personalidad del clon GENIA CEO a partir de los datos proporcionados por el usuario.

## Instrucciones

- El archivo `aprendizaje_personalidad.py` contiene la función `generar_prompt_personalidad`.
- Esta función se encarga de construir un prompt personalizado usando la información subida por el usuario.
- El prompt luego es usado por la API de OpenAI para crear respuestas con el tono, estilo y rol del experto.

## Datos esperados

- nombre
- rol
- estilo_comunicacion
- valores
- frases_tipicas
- forma_ensenar
- historia
- publico_objetivo

El sistema debe validar que al menos el `nombre`, `rol` y `estilo_comunicacion` estén presentes antes de generar respuestas.

## Formato de salida

Texto tipo string que representa el prompt base para construir respuestas coherentes con la personalidad entrenada.
