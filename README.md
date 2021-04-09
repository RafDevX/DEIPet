# Exercício de Candidatura à Bolsa de Iniciação à Investigação do DEI (BL38/2021)

Ver o [enunciado](/enunciado.md) para a especificação.

### Instalar Dependências

Antes de correr o código, é imperativo que o sistema esteja equipado com Python (^3.9.3) e os respetivos _modules_:

-   requests (^2.22.0)
-   django (^3.2)

### Correr Servidor de Desenvolvimento

1. Na diretoria de topo do repositório (onde está este ficheiro), correr:

> `python manage.py runserver`

2. Aceder ao endereço [http://127.0.0.1:8000/deipet/]() através de qualquer _browser_<sup id="a1">[1](#fn1)</sup>;

3. Ctrl-C para terminar a execução.

_Não está apto para produção, por motivos evidentes._

---

<b id="fn1"><sup>1</sup></b> Visto esta ser a única aplicação, para efeitos de conveniência, foi tomada a liberdade de criar um _redirect_, pelo que basta aceder ao endereço [http://127.0.0.1:8000]() sem qualquer _path_. [↩](#a1)
