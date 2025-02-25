# Análise de Desempenho dos Servidores HTTP

## Visão Geral
Esta análise compara o desempenho entre um servidor HTTP básico e um servidor HTTP com threads sob diferentes cargas de clientes simultâneos.

## Configuração do Teste
- Servidor: Servidor HTTP Local (Python)
- Porta: 8000
- Casos de Teste: 1, 2, 5 e 10 clientes simultâneos
- Métrica: Tempo de resposta em segundos

## Resultados

### Comparação de Desempenho

| Clientes Simultâneos | Servidor Básico (s) | Servidor com Thread (s) | Melhoria |
|---------------------|---------------------|----------------------|-----------|
| 1                   | 0,0040             | 0,0038              | 5%        |
| 2                   | 0,0062             | 0,0054              | 13%       |
| 5                   | 0,0112             | 0,0088              | 21%       |
| 10                  | 0,0238             | 0,0157              | 34%       |

## Principais Descobertas

1. **Processamento Sequencial vs Paralelo**
   - Servidor básico processa requisições sequencialmente
   - Servidor com thread processa múltiplas requisições simultaneamente

2. **Impacto no Desempenho**
   - A diferença de desempenho aumenta com a carga simultânea
   - Servidor com thread mostra melhoria significativa com 10+ clientes
   - Requisições únicas mostram diferença mínima

3. **Escalabilidade**
   - Servidor com thread escala melhor com aumento de carga
   - Tempo de resposta do servidor básico cresce linearmente com número de clientes

## Conclusão
O servidor com thread demonstra desempenho superior sob carga simultânea, tornando-o mais adequado para aplicações com múltiplos usuários. A melhoria torna-se mais pronunciada conforme aumentam as conexões simultâneas.