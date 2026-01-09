# Portfolio Management Module

Sistema de gestión de portafolios de inversión construido siguiendo los principios de **Domain-Driven Design (DDD)**.

## 📋 Tabla de Contenidos
- [Problema](#Problema)
- [Descripción](#descripción)
- [Arquitectura DDD](#arquitectura-ddd)
- [Modelado del Negocio](#modelado-del-negocio)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Testing](#testing)


## ⚠️  Problem
> You’re building a portfolio management module, part of a personal investments and trading app

> Construct a simple Portfolio class that has a collection of Stocks. Assume each Stock has a “Current Price” 
method that receives the last available price. Also, the Portfolio class has a collection of “allocated” Stocks 
that represents the distribution of the Stocks the Portfolio is aiming (i.e. 40% META, 60% APPL)

> Provide a portfolio rebalance method to know which Stocks should be sold and which ones should be bought to 
have a balanced Portfolio based on the portfolio’s allocation.

> Add documentation/comments to understand your thinking process and solution
> Important: If you use LLMs that’s ok, but you must share the conversations.

Dado este planteamiento nos disponemos a desarrollar una solución en python.


## 📖 Descripción

Este módulo permite gestionar portafolios de inversión, incluyendo:
- Gestión de colecciones de stocks (acciones)
- Asignación porcentual de activos
- Rebalanceo automático de portafolios basado en objetivos de distribución
- Cálculo de qué stocks comprar o vender para mantener el balance deseado

## 🏗️ Arquitectura DDD

El proyecto está estructurado siguiendo **Domain-Driven Design**, separando claramente las responsabilidades en tres capas principales:

### 1. **Domain Layer** (`/domain`)
Contiene la **lógica de negocio pura** y las entidades del dominio. Esta capa es independiente de la infraestructura y frameworks externos.

**Responsabilidades:**
- Definir las entidades del negocio (Portfolio, Stock)
- Implementar la lógica de negocio (rebalanceo, cálculos)
- Definir interfaces de repositorios (contratos)
- Value Objects y reglas de negocio

**Principio clave:** El dominio no conoce detalles de persistencia ni infraestructura.

### 2. **Application Layer** (`/application`)
Orquesta los casos de uso de la aplicación, coordinando las operaciones del dominio.

**Responsabilidades:**
- Servicios de aplicación que coordinan operaciones del dominio
- Punto de entrada de la aplicación (`entrypoint/main.py`)
- DTOs (Data Transfer Objects) si es necesario
- Casos de uso del sistema

### 3. **Infrastructure Layer** (`/infrastructure`)
Implementa los detalles técnicos y la persistencia de datos.

**Responsabilidades:**
- Implementaciones concretas de repositorios
- Acceso a bases de datos o APIs externas
- Configuración de frameworks
- Adaptadores de infraestructura

## 📁 Estructura del Proyecto

```
fintual_test/
│
├── domain/                           # Capa de Dominio
│   ├── portfolio.py                 
│   ├── stock.py                     
│   ├── price.py                     
│   ├── operation_type.py                     
│   ├── operation.py                     
│   ├── currency.py                     
│   ├── allocation_stock.py                     
│   └── repositoriy/
│       ├── istock_repository.py      # Interfaces de los repositorios
│       └── iportfolio_repository.py  # Interfaces de los repositorios
│
├── application/                      # Capa de Aplicación
│   ├── dto/                          # Data object tranfers
│   │   ├── portfolio_dto.py             
│   │   └── stock_dto.py                 
│   ├── services/
│   │   ├── portfolio_service.py      # Servicio de aplicación
│   │   ├── portfolio_service_test.py # Test Servicio de aplicación
│   │   └── stock_service.py          # Servicio de aplicación
│   └── entrypoint/
│       └── main.py                   # Punto de entrada ⭐
│
└── infrastructure/                   # Capa de Infraestructura
    └── persistence/                  # Implementación de persistencias
         └── memory/
             ├── memory_portfolio_repository.py  
             └── memory_stock_repository.py      

```

## 🔧 Servicios y Repositorios

### Servicios de Aplicación

Los **servicios de aplicación** (`application/services/`) orquestran las operaciones del dominio y coordinan con la capa de infraestructura:

**Ventajas:**
- ✅ **Abstracción de persistencia**: El dominio no conoce de dónde vienen los datos
- ✅ **Testabilidad**: Fácil crear mocks del repositorio
- ✅ **Flexibilidad**: Cambiar la fuente de datos sin afectar la lógica de negocio
- ✅ **Separación de responsabilidades**: Lógica de negocio vs. acceso a datos

### Repositorios

Los **repositorios** abstraen la persistencia y obtención de datos:

**Interface (Domain):**
`domain/repository/iportfolio_repository.py`
```python
class IPortfolioRepository:
    @abc.abstractmethod
    def create(self, portfolio: Portfolio) -> str:
        ...

    @abc.abstractmethod
    def get_all(self) -> list[Portfolio]:
        ...

    @abc.abstractmethod
    def get_by_id(self, id: str) -> Portfolio:
        ...

```

**Implementación (Infrastructure):**
`infrastructure/persistence/memory/memory_portfolio_repository.py`
```python
class MemoryPortfolioRepository(IPortfolioRepository):
    portfolios: dict[str, Portfolio]

    def __init__(self, portfolios: list[Portfolio] = None):
        self.portfolios = {}

        if portfolios is not None:
            for portfolio in portfolios:
                self.portfolios.setdefault(portfolio.id, portfolio)

    def create(self, portfolio: Portfolio) -> str:
        self.portfolios.setdefault(portfolio.id, portfolio)
        return portfolio.id

    def get_by_id(self, id: str) -> Portfolio:
        return self.portfolios.get(id)

    def get_all(self) -> list[Portfolio]:
        return list(self.portfolios.values())

```

Esto permite cambiar la implementación sin modificar el dominio (Principio de Inversión de Dependencias).

## 🚀 Instalación

### Requisitos

- Python 3.8+

### Pasos

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Nitri0/fintual_test.git
cd fintual_test
```

2. **Crear entorno virtual (opcional pero recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## 💻 Uso

### Ejecutar la Aplicación

Para ejecutar el proyecto, corre el archivo principal ubicado en:

```bash
python application/entrypoint/main.py
```

O desde la raíz del proyecto:

```bash
python -m application.entrypoint.main
```

### Ejemplo de Uso

Tomando como base de modificación el archivo `application/entrypoint/main.py`

### Agregar tipos de stocks

Pueden agregar tipos de stocks siguiendo el formato, esto toma la funcion de repositorio de tipos de stocks

`application/entrypoint/main.py`
```python
    ...    

    stocks_type: dict[str, StockType] = {
        "APPLE": StockType(
            id="1",
            name="APPLE",
            symbol="APPLE",
            price=Price(
                value=2.0,
                currency=Currency("USD")
            ),
        ),
        "META": StockType(
            id="2",
            name="META",
            symbol="META",
            price=Price(
                value=1.0,
                currency=Currency("USD")
            ),
        )
    }
    
    ...
```

### Modificar los stocks del portafolio

Puede modificar tanto los tipos de stock como la cantidad que estan incluidos en el portafolio agregandolos. Lo pueden agregar aquí:

`application/entrypoint/main.py`
```python
    ...    

    stocks: list[Stock] = [
        Stock(
            id="id",
            type=stocks_type.get("APPLE"),
            quantity=10000,
        ),
        Stock(
            id="id",
            type=stocks_type.get("META"),
            quantity=500,
        ),
    ]
    
    ...
```


### Modificar distribución esperado

Pueden modificar la distribucion esperada agregando tipos de stock o modificando los porcentajes asignados a cada tipo:

`application/entrypoint/main.py`
```python
    ...    

    allocated_stocks: list[AllocatedStock] = [
        AllocatedStock(
            stock_type=stocks_type.get("APPLE"),
            percent=0.25
        ),
        AllocatedStock(
            stock_type=stocks_type.get("META"),
            percent=0.75
        )
    ]
    
    ...
```

### Modificar tolerancia

Tambien pueden condigurar la tolerancia soportada para realizar una operación

`application/entrypoint/main.py`
```python
    ...    

    portfolio = Portfolio(
        id="1",
        name="Default Portfolio",
        stocks=stocks,
        allocated_stocks=allocated_stocks,
        tolerance=0.01
    )
    
    ...
```

## 🧪 Testing

El proyecto incluye tests para capa de servicio.

### Ejecutar Test

```bash
python -m unittest application/services/portfolio_service_test.py
```


## 📚 Conceptos Clave de DDD Aplicados

1. **Entities**: `Portfolio` y `Stock` son entidades con identidad propia
2. **Value Objects**: `RebalanceResult` representa un valor calculado
3. **Repositories**: Abstracción para acceso a datos
4. **Services**: Operaciones que no pertenecen naturalmente a una entidad
5. **Separation of Concerns**: Cada capa tiene responsabilidades claras
6. **Dependency Inversion**: El dominio define interfaces, la infraestructura las implementa


## Logs IA

Siguiendo los requisitos adjunto [chat utilizado](https://claude.ai/share/a69b6d11-3262-4692-8f87-5c3ed00f2781) para llegar a la solución actual


Cabe destacar que tanto la documentación generada como el código fueron evaluados y 
reescritos directamente por mi persona 


>**Muchas gracias** por tu tiempo si llegaste hasta aquí.

 > Quedo abierto a cualquier feedback por correo **hsh283@gmail.com** ✅
