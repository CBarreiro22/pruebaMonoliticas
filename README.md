# pruebaMonoliticas

Para la ejecucion de este repositorio , puede probarlo por medio de gitpod, instalando la extension de chrome Gitpod


<a href="https://chromewebstore.google.com/detail/gitpod/dodmmooeoklaejobgleioelladacbeki?hl=es"> GitpodChrome</a>


![image](https://github.com/CBarreiro22/pruebaMonoliticas/assets/111206402/ab581705-0430-4f66-bb49-9d123356ab6b)

Y en el mismo repo debe aparecer la opcion para la redireccion de gitpod

![image](https://github.com/CBarreiro22/pruebaMonoliticas/assets/111206402/616e4848-8cc8-4f92-a2de-ab5e567e5229)

### Ejecutar Aplicación

Ahora para probar el POC primero se procede levantando el pulsar

### Correr docker-compose usando profiles

Correr Servicio de Base de datos
```bash
docker-compose --profile postgresPropiedades up
```

Correr Servicio Pulsar
```bash
docker-compose --profile pulsar up
```



Luego se procede a ejecutar la aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/propiedadDeLosAlpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/propiedadDeLosAlpes/api --debug run
```

BFF: Web

Desde el directorio src ejecute el siguiente comando

```bash
uvicorn bff_web.main:app --host localhost --port 8003 --reload
```

```sql
select * from propiedades;
select * from agentes;

-- delete from propiedades;
-- delete from agentes;
```

```json
{
"nombre_propietario": "Camilo",
"direccion": "",
"pais": "",
"tipo_propiedad": "Apartamento",
"ubicacion": "Torres del Bosque",
"id_empresa": 12345,
"superficie": 80.5,
"precio": 230000000
}```