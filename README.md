### Análisis de la Regla de $n > 30$ y la Convergencia

La regla de que **$n > 30$** es una muestra "suficientemente grande" es una regla empírica (heurística) generalizada, pero no es una verdad matemática absoluta ni depende exclusivamente del **$\alpha = 5\%$**.

En realidad, la validez de esta regla depende de dos factores que el código ilustra muy bien:

#### 1. No es por el $\alpha$, es por la forma de la distribución
La distribución **$t$-Student** tiene "colas" más pesadas que la Normal. A medida que $n$ aumenta, los grados de libertad ($gl = n - 1$) crecen y la forma de la curva $t$ se vuelve indistinguible de la Normal $Z$.
* Para la mayoría de los propósitos prácticos (ingeniería, ciencias sociales), a partir de **$n = 30$**, la diferencia en la densidad de probabilidad central es mínima.
* Sin embargo, el valor crítico ($t_{crit}$) sigue siendo distinto al de $Z$ incluso para **$n = 30$**.

#### 2. El efecto del $\alpha$ en la convergencia
El valor de $\alpha$ determina qué tan lejos en las "colas" de la distribución estamos mirando. Aquí es donde la regla de 30 puede fallar:
* **Con $\alpha = 5\%$:** El $z_{crit}$ es $\pm 1.96$. Para $n = 30$ ($gl = 29$), el $t_{crit}$ es $\pm 2.045$. La diferencia es pequeña ($\approx 0.08$).
* **Con $\alpha = 1\%$:** El $z_{crit}$ es $\pm 2.576$. Para $n = 30$, el $t_{crit}$ es $\pm 2.756$. La diferencia es mayor ($\approx 0.18$).
* **Con $\alpha$ muy pequeños (ej. $0.1\%$):** Las colas de la $t$-Student tardan mucho más en "adelgazar" hasta alcanzar a la Normal. Aquí podrías necesitar un $n > 100$ para que la aproximación sea buena.

#### 3. El factor más importante: La población original
La regla de **$n > 30$** nace principalmente del **Teorema del Límite Central (TLC)**.
* Si la población de donde se saca la muestra **ya es normal**, se puede usar la distribución Normal incluso con $n = 2$ (si se conoce $\sigma$).
* Si la población es **muy asimétrica** (tiene sesgo) o tiene valores atípicos extremos, un $n = 30$ no será suficiente para que la distribución de la media sea normal; se podría necesitar $n = 50$ o $n = 100$.

---

### Resumen Técnico
La regla de 30 se usa porque para un $\alpha$ estándar (0.05) y una población con asimetría moderada, el error que se comete al usar $Z$ en lugar de $t$ suele ser menor al **5% relativo**, lo cual es aceptable en la práctica manual. Pero con el poder computacional actual (como el script), siempre es mejor usar la distribución **$t$ exacta** sin importar el tamaño de $n$.

**✅ Conclusión:**
No es exclusivo de $\alpha = 5\%$, pero la aproximación es más exacta en niveles de confianza comunes. A niveles de alfa muy exigentes (muy pequeños), la diferencia entre $t$ y $Z$ se nota mucho más, y la regla de "30" se queda corta.
