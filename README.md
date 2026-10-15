# Gerador de Quina Equilibrada

Um exercício de lógica, probabilidade e Python: o script gera uma aposta da Quina respeitando filtros de equilíbrio entre números pares/ímpares e baixos/altos.

> **Aviso importante:** a Quina é um sorteio aleatório. Nenhum filtro aumenta a chance de ganhar: toda combinação de 5 números tem exatamente a mesma probabilidade (1 em 24.040.016). Este é um projeto de estudo, não uma estratégia de apostas. Jogue com responsabilidade; apostas são proibidas para menores de 18 anos.

## Sobre o projeto

A ideia parte de uma pergunta simples: o que seria uma aposta "equilibrada"? O projeto transforma essa pergunta em regras claras e em código que roda.

**Transparência:** a ideia e as regras são minhas. O código foi escrito com apoio de IA e adaptado por mim em etapas, como parte do meu aprendizado em Ciência da Computação.

## Como funciona

O script sorteia 5 números entre 1 e 80 e repete o sorteio até que a combinação respeite os dois filtros abaixo:

| Filtro | Regra |
|---|---|
| Pares e ímpares | de 2 a 3 números pares |
| Quentes e frios | de 2 a 3 números baixos (1 a 40); os demais são altos (41 a 80) |
| Final igual | 2 números com finais iguais |

Ao final, ele imprime a aposta gerada e um pequeno diagnóstico (quantidade de pares, ímpares, números quentes e frios), além de números com finais iguais, pois é um padrão dos sorteios.

**Sobre o histórico:** o script lê e valida o arquivo `quina_historico.txt` (e calcula a frequência de cada dezena), mas, nesta primeira versão, esses dados **não influenciam** a aposta gerada. Eles servem como base para as próximas etapas (veja o roteiro abaixo).

## Requisitos

- Python 3 (usa apenas a biblioteca padrão, não há nada para instalar)

## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/fredfiuza10-cyber/gerador-quina-equilibrada.git
   cd gerador-quina-equilibrada
   ```

2. Crie o arquivo `quina_historico.txt` na mesma pasta do script, com **um sorteio por linha**, no formato de lista Python. Os resultados oficiais estão no site das Loterias Caixa. Exemplo do formato (números ilustrativos):

   ```text
   [08, 54, 12, 33, 71]
   [02, 19, 45, 60, 77]
   ```

   Linhas vazias ou mal formatadas são ignoradas.

3. Execute:

   ```bash
   python gerador_quina.py
   ```

### Exemplo de saída (ilustrativo)

```text
JOGO GERADO: [7, 23, 44, 61, 78]

Diagnóstico do jogo:
Pares: 2
Ímpares: 3
Baixos (1–40): 2
Altos (41–80): 3
```

## Estrutura do repositório

```text
gerador-quina-equilibrada/
├── gerador_quina.py      # script principal
├── quina_historico.txt   # histórico de sorteios (você cria; não vem no repositório)
├── .gitignore
└── README.md
```

## Decisões de projeto

- **Leitura robusta:** o histórico é lido com `ast.literal_eval`, e linhas inválidas são descartadas em vez de interromper o programa.
- **Validação:** só entram no histórico listas com exatamente 5 números inteiros; se nenhum sorteio válido for encontrado, o script avisa com um erro claro.
- **Código organizado em funções:** leitura, análise e geração são separadas, o que facilita testar e evoluir cada parte.

## Limitações e próximos passos

- [ ] Usar o histórico de fato: exibir as dezenas mais e menos sorteadas e comparar a aposta gerada com sorteios passados.
- [ ] Verificar se a combinação gerada já foi sorteada alguma vez.
- [ ] Permitir escolher a quantidade de apostas e os filtros por linha de comando.
- [ ] Adicionar testes automatizados para os filtros de equilíbrio.
- [ ] Incluir um arquivo de histórico de exemplo para o projeto rodar logo após o clone.

## Autor

**Frederico Fiuza** · [GitHub](https://github.com/fredfiuza10-cyber)

Feedbacks e sugestões são bem-vindos, abra uma *issue* ou fale comigo.
