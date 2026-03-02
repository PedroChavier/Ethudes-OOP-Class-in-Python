# Counter_Lib

> **Projeto de estudos** — Introdução à Programação Orientada a Objetos com Python.

---

## Sobre o Projeto

Counter_Lib é um documento/módulo criado com fins fundamentalmente educacionais, voltado ao aprendizado e prática de conceitos de **Programação Orientada a Objetos (POO)** utilizando Python como linguagem base.

O projeto implementa uma classe `Counter` — um contador configurável com suporte a limites numéricos, polaridade de incremento e validação de intervalos matemáticos (abertos, fechados e semi-abertos).

---

## Conceitos de POO Abordados

- Definição de classes e instâncias
- Uso de `__init__`, `__repr__` e `__call__` (métodos especiais/dunder)
- Encapsulamento de estado via atributos de instância
- Tipagem com `typing` e `Enum`
- Uso de `match/case` (Python 3.10+)

---

## Estrutura

### `PolarPosition` (Enum)
Define a direção do incremento do contador:

| Valor | Nome | Comportamento |
|-------|------|---------------|
| `0` | `Upper` | Incrementa positivamente |
| `1` | `Lower` | Incrementa negativamente |
| `2` | `PolarInvers` | Inverte a polaridade atual |

---

### `Counter` (Classe Principal)

#### Parâmetros de inicialização

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `increment` | `float` | Passo de incremento base |
| `limit` | `LimitType` | Tupla com limite inferior e superior (opcional) |
| `register` | `float` | Valor inicial do contador (opcional) |
| `analog` | `bool` | Modalidade analógica — *em desenvolvimento* |
| `polar` | `bool` | Define a polaridade padrão (`True` = positivo) |
| `operant` | `bool` | Habilita/desabilita o funcionamento do contador |

#### Tipo `LimitType`

Os limites são expressos como tuplas `(valor, incluído)`, onde o segundo elemento é um `bool` que define se o limite é **fechado** (`True`, inclui o valor) ou **aberto** (`False`, exclui o valor). Qualquer lado pode ser `None` para representar infinito.

```python
# Exemplo: intervalo [0, 10)
limite = ((0, True), (10, False))
c = Counter(increment=1, limit=limite)
```

#### Métodos

| Método | Descrição |
|--------|-----------|
| `__call__(polar_pass, increment_pass)` | Avança o contador. Retorna o novo valor ou o atual se o limite for atingido |
| `SetPlace(Vall)` | Move o registro para um valor específico dentro dos limites |
| `SetOrigem()` | Redefine o registro para o ponto de origem (`init_point`) |
| `Config()` | *Em desenvolvimento* |

---

## Status de Desenvolvimento

| Funcionalidade | Status |
|----------------|--------|
| Lógica de limites (intervalos matemáticos) | ✅ Implementado e testado |
| Incremento com polaridade | ✅ Implementado e testado |
| `SetPlace` / `SetOrigem` | ✅ Implementado |
| `Config(*args)` | 🔧 Em desenvolvimento |
| Argumento `analog` | 🔧 Em desenvolvimento |
| `commit()` / `charge()` | 🔧 Planejado |

---

## Requisitos

- Python 3.10+
- [`sympy`](https://www.sympy.org/) — utilizado para representar infinito (`oo`)

```bash
pip install sympy
```

---

## Exemplo de Uso

```python
from Counter_Lib import Counter, PolarPosition

# Contador de 0 a 10 (fechado), passo 2
c = Counter(increment=2, limit=((0, True), (10, True)), register=0)

c()           # 2
c()           # 4
c(PolarPosition.Lower)  # 2 (decrementa)

print(c)      # 2
```

---

## Observações

- O projeto está em **versão 1.0.0** e em desenvolvimento ativo.
- Há anotações internas no código indicando correções e implementações pendentes.
- O foco atual é na solidez da lógica matemática dos limites e do mecanismo de incremento.

---

*Projeto pessoal de estudos — Counter_Lib v1.0.0*