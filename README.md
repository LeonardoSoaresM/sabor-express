Documento de Implementação: Testes Unitários - Sabor Express

# 1. Introdução

Este documento detalha a implementação e o resultado final dos testes unitários para o projeto Sabor Express, conforme solicitado na atividade.

O processo de implementação foi iterativo (feito de "tentativa e erro"), onde os testes foram usados para descobrir o comportamento real do código-fonte. O plano inicial foi adaptado para corresponder à arquitetura da aplicação.

O resultado final é um "Build Verde" (Green Build), onde todos os 8 testes da suíte (os 5 testes da tarefa + 3 testes pré-existentes) passam com sucesso.
```bash
========================= 8 passed in 0.09s =========================
```

# 2. Análise e Testes Implementados

Abaixo está a documentação final dos testes que foram implementados com sucesso.


## 2.1. Classe ItemCardapio (Teste Não Implementado)

Durante a análise, eu percebi que ItemCardapio é uma classe abstrata. Ou seja não é possível criar uma instância direta dela.


## 2.2. Classe AvaliacaoRestaurante (test_avaliacao.py)

| Componente Testado | Teste Criado | Mocks (Fixtures) Necessários | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| `AvaliacaoRestaurante.__init__` | `test_init_avaliacao_restaurante_vazio` | Um dicionário de dados vazio (`{'average': 0, ...}`) | O objeto é criado corretamente, com `media == 0` e `avaliacoes_individuais == []`. |
| `AvaliacaoRestaurante.__init__` | `test_init_avaliacao_restaurante_com_dados` | Um dicionário com dados reais (ex: 2 notas) | O objeto é criado corretamente, com a média e a lista de avaliações correspondentes. |


## 2.3. Classe Restaurante (test_restaurante.py)

Os testes desta classe foram os mais complexos, pois exigiram a correção dos nomes dos métodos e da forma como o objeto é criado.

| Componente Testado | Teste Criado | Mocks (Fixtures) Necessários | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| `_avaliacoes.media` (Propriedade) | `test_media_avaliacoes_sem_avaliacoes` | `restaurante_vazio` (Fixture que passa `avaliacoes={...}`) | Garante que a média de um restaurante novo (sem avaliações) é `0`. |
| `adicionar_no_cardapio()` (Método) | `test_adicionar_no_cardapio` | `restaurante_vazio`, `item_sobremesa` (fixtures) | O item é adicionado à lista `_cardapio`. O teste verifica o `len()` da lista e o `_nome` do item. |
| `calcular_media_avaliacoes()` (Método) | `test_calcular_media_avaliacoes` | `restaurante_com_avaliacoes` (Fixture) | O método recalcula a média com base nas notas. O teste verifica se a `media` é atualizada de `0` para `4.0`. |

O método recalcula a média com base nas notas. O teste verifica se a media é atualizada de 0 para 4.0.


# 3. Como Executar os Testes

Para garantir que o ambiente esteja configurado corretamente para a execução:


## 1. Ambiente Virtual e Dependências

É crucial usar um ambiente virtual (venv) e instalar o pytest.

### Ativar o ambiente (Exemplo no PowerShell)
```bash
.\venv\Scripts\Activate


####(Caso tenha problemas com a execução dos scripts como eu tive, execute nesta sequência)
    >>> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

    >>> .\venv\Scripts\Activate
```
### Instalar o pytest (caso ainda não esteja)

```bash
pip install pytest
```

## 2. Execução

Com o venv ativo e o pytest.ini no lugar, basta executar o comando na raiz do projeto:
```bash
pytest
```