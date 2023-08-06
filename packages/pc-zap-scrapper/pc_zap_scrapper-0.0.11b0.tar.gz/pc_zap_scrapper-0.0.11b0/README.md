# Zap Scrapper - Imoveis em Poços de Caldas

Scrapper para obter dados de imóveis na cidade de Poços de Caldas, MG. O aplicativo roda o scrapper, formata os dados e faz o load numa base de dados privada do PostgreSQL.

## 1. Instalação
A instalação é dada através do `pip`:
```bash
$ pip install pc_zap_scrapper 
```

## 2. Configurando a conexão com o banco
Na etapa de load do banco de dados, é necessário fornecer as credenciais do banco de dados. Serão necessárias as informações:
* `DB_USERNAME`
* `DB_PASSWORD`
* `DB_NAME`
* `DB_HOST`
* `DB_PORT`

Esses dados podem ser passados manualmente ou através de arquivo `.env`

### 2.a Configuração manual das credenciais
Basta rodar:

```bash
$ zapscrap configure -p path/to/.env
```
e fornecer cada uma das informações requeridas.

### 2.b Configuração através do arquivo `.env`
alternativamente, pode-se definir o `.env` com as informações necessárias.
```bash
# Arquivo .env para conexão com banco de dados PostgreSQL
DB_USERNAME=nome_do_usuario
DB_PASSWORD=admin123
DB_NAME=nome_da_base
DB_HOST=esse_e_meu.host
DB_PORT=0000
```
Salve esse arquivo em qualquer lugar; por exemplo, em `path/to/.env`. Depois, rode o comando

```bash
$ zapscrap configure -p path/to/.env
```

## 3.