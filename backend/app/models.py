# This file defines the structure of the database tables using SQLAlchemy ORM models.

from sqlalchemy import Column, Integer, String, Numeric, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# 1. PROVIDERS TABLE
class Provider(Base):

    __tablename__ = "providers"

    provider_id = Column(Integer, primary_key=True, index=True)

    provider_name = Column(String, nullable=False)

    # Relationships
    regions = relationship("Region", back_populates="provider")

    services = relationship("Service", back_populates="provider")


# 2. REGIONS TABLE
class Region(Base):

    __tablename__ = "regions"

    region_id = Column(Integer, primary_key=True, index=True)

    provider_id = Column(Integer, ForeignKey("providers.provider_id"), nullable=False)

    region_name = Column(String, nullable=False)

    region_code = Column(String, nullable=False)

    # Relationships
    provider = relationship("Provider", back_populates="regions")

    pricing = relationship("Pricing", back_populates="region")


# 3. SERVICES TABLE
class Service(Base):

    __tablename__ = "services"

    service_id = Column(Integer, primary_key=True, index=True)

    provider_id = Column(Integer, ForeignKey("providers.provider_id"), nullable=False)

    service_name = Column(String, nullable=False)

    # Relationships
    provider = relationship("Provider", back_populates="services")

    resource_types = relationship("ResourceType", back_populates="service")


# 4. RESOURCE TYPES TABLE
class ResourceType(Base):

    __tablename__ = "resource_types"

    resource_type_id = Column(Integer, primary_key=True, index=True)

    service_id = Column(Integer, ForeignKey("services.service_id"), nullable=False)

    resource_name = Column(String, nullable=False)

    vcpu = Column(Integer)

    ram_gb = Column(Numeric)

    storage_gb = Column(Numeric)

    operating_system = Column(String)

    # Relationships
    service = relationship("Service", back_populates="resource_types")

    pricing = relationship("Pricing", back_populates="resource_type")


# 5. PRICING TABLE
class Pricing(Base):

    __tablename__ = "pricing"

    pricing_id = Column(Integer, primary_key=True, index=True)

    resource_type_id = Column(
        Integer, ForeignKey("resource_types.resource_type_id"), nullable=False
    )

    region_id = Column(Integer, ForeignKey("regions.region_id"), nullable=False)

    pricing_model = Column(String, nullable=False)

    price = Column(Numeric, nullable=False)

    currency = Column(String, nullable=False)

    billing_unit = Column(String, nullable=False)

    effective_from = Column(Date)

    effective_to = Column(Date)

    source_url = Column(Text)

    last_verified = Column(Date)

    # Relationships
    resource_type = relationship("ResourceType", back_populates="pricing")

    region = relationship("Region", back_populates="pricing")
