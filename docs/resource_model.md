| Field            | Purpose                              |  
| ---------------- | ------------------------------------ |
| Provider         | Identifies AWS, Azure, or GCP        |
| Service          | Identifies compute, storage, etc.    |
| Region           | Identifies the deployment region     |
| Resource Name    | Original provider-specific name      |
| vCPU             | CPU capacity                         |
| RAM              | Memory capacity                      |
| Storage          | Storage capacity, where applicable   |
| Operating System | OS associated with the price         |
| Pricing Model    | On-demand, Spot, or commitment-based |
| Price            | Cost of the resource                 |
| Billing Unit     | Unit to which the price applies      |
| Currency         | Currency of the price                |


DATABASE SCHEMA

| Table            | Purpose                        | Example information                  |
| ---------------- | ------------------------------ | ------------------------------------ |
|    providers     | Stores cloud provider details  | AWS, Azure, GCP                      |
|    regions       | Stores available cloud regions | Mumbai, Singapore                    |
|    services      | Stores cloud services          | Compute, Storage                     |
|  resource_types  | Stores resource specifications | Instance type, vCPU, RAM             |
|  pricing         | Stores resource pricing        | Hourly price, currency, billing unit |


CONCEPTUAL DIAGRAM

PROVIDERS
    |
    ├──────── REGIONS
    |
    └──────── SERVICES
                  |
                  v
             RESOURCE_TYPES
                  |
                  v
                PRICING