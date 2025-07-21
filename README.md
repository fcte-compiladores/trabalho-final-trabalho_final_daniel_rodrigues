# Colorizador de Código com Lexer e Interface Gráfica

## Integrantes
- Daniel Rodrigues Nascimento — Matrícula: 231037665 — Turma: 16:00-18:00

## Introdução
Este projeto implementa um analisador léxico simples (**lexer**) que reconhece tokens de uma linguagem do estilo C e gera um arquivo HTML com **destaque de sintaxe colorido**.

A análise léxica é feita com expressões regulares (regex) e permite identificar diferentes tipos de tokens no código. A interface gráfica em **Tkinter** facilita a entrada do código e a geração do HTML.

A linguagem reconhecida é um subconjunto de linguagens como C/C++/Java. A sintaxe esperada inclui:

- **Palavras-chave:** `int`, `float`, `if`, `else`, `while`, `return`, etc.
- **Números:** inteiros e decimais (`42`, `3.14`)
- **Strings:** `"texto"` ou `"""multilinha"""`
- **Caracteres:** `'a'`, `'\n'`
- **Booleanos:** `true`, `false`
- **Operadores:** `+`, `-`, `*`, `/`, `==`, `!=`, `>=`, etc.
- **Comentários:** `// comentário de linha`
- **Identificadores:** nomes de variáveis, funções, etc.
- **Pontuação:** `{`, `}`, `(`, `)`, `[`, `]`, `;`, `,`

### Exemplo de código reconhecido:

int main() {
    // Exemplo de programa
    float pi = 3.14;
    if (pi > 0) {
        printf("Valor positivo");
    }
    return 0;
}

## Instalação

Requisitos

Python 3.7 ou superior

Instruções

Clone ou baixe este repositório.

Execute o arquivo da interface com:

    python3 gui.py

Uma janela gráfica será aberta. Digite ou cole seu código na área de texto e clique em “Gerar HTML Colorido” para salvar o arquivo resultante.

Execute:

    xdg-open nome_que_salvou.html

## Referências

Crafting Interpreters — livro que inspirou a organização do lexer

Documentação oficial do Python (re, tkinter)

Artigos e exemplos de syntax highlighting em HTML

StackOverflow (resolução de regex e expressões edge cases)

## Bugs, Limitações e Melhorias Futuras

O lexer não trata erros léxicos como strings malformadas ou comentários aninhados.

Não há parsing nem análise semântica.

Reconhecimento limitado à sintaxe básica estilo C.

HTML gerado não possui preview embutido (precisa ser aberto no navegador).

Interface simples — pode ser expandida com suporte a temas, salvamento automático, múltiplos arquivos ou live preview.
