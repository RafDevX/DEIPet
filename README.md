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

## Escolhas de Implementação

-   Ao contrário do que é usual, a API Petstore disponibilizada não expõe nenhuma forma de determinar _quantos_ animais de estimação existem no total. Assim, implementando paginação na lista de animais, a única maneira de mostrar ao utilizador quantas páginas há ao todo a seria obter todos e contá-los ­— o que claramente é contra o propósito da própria Petstore fazer paginação e não seria escalável. Assim, foi tomada a decisão de mostrar apenas botões de navegação, _sem_ a informação da quantidade total.

-   Pela mesma razão, não foi implementada uma funcionalidade de pesquisa nem de ordenação, pois tais operações apenas poderiam ser feitas por página em vez de no geral, o que seria pouco útil (ou até enganador) para o utilizador.

-   De notar que alguns animais podem aparecer repetidos em páginas diferentes pelo que APARENTA<sup id="a2">[2](#fn2)</sup> ser um lapso na implementação da Petstore: o parâmetro `offset` afeta os IDs e não o número real de animais existentes, não contemplando que alguns IDs podem ter sido apagados. Por exemplo, havendo animais com IDs `[0 1 2 3 50]` (tendo os animais `4-49` sendo apagados), o `#50` é listado tanto com `(limit=20, offset=0)` (primeira página) como com `(limit=20, offset=20)` (segunda página).

---

<b id="fn1"><sup>1</sup></b> Visto esta ser a única aplicação, para efeitos de conveniência, foi tomada a liberdade de criar um _redirect_, pelo que basta aceder ao endereço [http://127.0.0.1:8000]() sem qualquer _path_. [↩](#a1)
<b id="fn2"><sup>2</sup></b> Pouco tempo foi gasto a testar esta teoria; no entanto, é pouco provável tratar-se de um erro na presente implementação devido à sua simplicidade. [↩](#a2)
