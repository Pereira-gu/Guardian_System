# Guardian System

Este projeto implementa um sistema de monitoramento/exportação de dados utilizando banco de dados SQLite.

## Estrutura

- `src/` - código-fonte principal (ex: `exporter.py`)
- `dashboard/` - artefatos de dashboard
- `data/` - dados brutos e processados
- `logs/` - arquivos de log
- `tests/` - testes automatizados

## Instalação

1. Crie um ambiente virtual (opcional mas recomendado):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Copie o arquivo `.env.example` ou crie um `.env` com as variáveis de ambiente necessárias.

### Exemplo `.env`
```
DATABASE_URL=sqlite:///data/guardian.db
LOG_LEVEL=INFO
```

## Uso

Executar o script principal:
```
python src\exporter.py
```

## Contribuição

Sinta-se à vontade para abrir issues e pull requests.
