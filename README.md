# _Redis_ Open Microservice

> This is a redis service

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org) [![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices) [![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md) [![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from within this project's root directory:

#### Actions

##### set

> Sets 'key' to hold 'value'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run set \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### rpush

> Insert 'value' at the end of list stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run rpush \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### lpush

> Insert 'value' at the head of list stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run lpush \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### lpop

> Removes and returns the first element of the list stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run lpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### rpop

> Removes and returns the last element of the list stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run rpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### blpop

> Removes and returns the first element of the list stored at 'key'.
> When there are no element in the list, the command will not return
> until an element got added.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run blpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### brpop

> Removes and returns the last element of the list stored at 'key'.
> When there are no element in the list, the command will not return
> until an elements got added.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run brpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### delete

> Removes 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run delete \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### get

> Returns the value of 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run get \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### mget

> Returns the values of multiple 'keys'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| keys           | `list`   | `false`  | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run mget \
    -a keys='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### increment

> Increments a number stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| by             | `int`    | `false`  | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run increment \
    -a key='*****' \
    -a by='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### decrement

> Decrements a number stored at 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| by             | `int`    | `false`  | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run decrement \
    -a key='*****' \
    -a by='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### append

> Appends 'value' to a 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run append \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### getSet

> Returns the current value of 'key' and overwrites it with 'value'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run getSet \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### setnx

> Set a 'key' to 'value' only if the key does not exist yet.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| value          | `any`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run setnx \
    -a key='*****' \
    -a value='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### mset

> Sets multiple 'key'/'value' pairs simultaneously.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| pairs          | `map`    | `false`  | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run mset \
    -a pairs='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### msetnx

> Sets multiple 'key'/'value' pairs simultaneously.
> Only non-existing keys will be set.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| pairs          | `map`    | `false`  | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run msetnx \
    -a pairs='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### expire

> Set a timeout on a 'key'.

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | No description provided. |
| seconds        | `int`    | `true`   | None    | No description provided. |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms run expire \
    -a key='*****' \
    -a seconds='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### rpop

> RPOP a key constantly, and emit the values as events

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | The key to RPOP          |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms subscribe rpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

##### lpop

> LPOP a key constantly, and emit the values as events

##### Action Arguments

| Argument Name  | Type     | Required | Default | Description              |
| :------------- | :------- | :------- | :------ | :----------------------- |
| key            | `string` | `true`   | None    | The key to LPOP          |
| REDIS_HOST     | `string` | `false`  | None    | No description provided. |
| REDIS_PORT     | `int`    | `false`  | None    | No description provided. |
| REDIS_DB       | `string` | `false`  | None    | No description provided. |
| REDIS_PASSWORD | `string` | `false`  | None    | No description provided. |

```shell
oms subscribe lpop \
    -a key='*****' \
    -e REDIS_HOST=$REDIS_HOST \
    -e REDIS_PORT=$REDIS_PORT \
    -e REDIS_DB=$REDIS_DB \
    -e REDIS_PASSWORD=$REDIS_PASSWORD
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit redis on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/redis)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md). Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

- [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build microservices.
- [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of languages.
- [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node, Python, Scala, Java, Clojure.
- [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
- [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
