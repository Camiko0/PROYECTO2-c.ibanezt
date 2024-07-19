-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: tablasheladeria
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingrediente`
--

DROP TABLE IF EXISTS `ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingrediente` (
  `id` int NOT NULL,
  `precio` float NOT NULL,
  `calorias` int NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `inventario` float NOT NULL,
  `es_vegetariano` tinyint NOT NULL,
  `tipo_ingrediente` varchar(50) NOT NULL,
  `sabor` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingrediente`
--

LOCK TABLES `ingrediente` WRITE;
/*!40000 ALTER TABLE `ingrediente` DISABLE KEYS */;
INSERT INTO `ingrediente` VALUES (1,2000,100,'Crema',8.6,0,'Base','Dulce'),(2,800,120,'Leche',8.6,0,'Base','Dulce'),(3,3000,100,'Leche de almendra',6.2,1,'Base','Neutro'),(4,2000,100,'Yemas de huevo',18,0,'Base','Amargo'),(5,500,120,'Azúcar',8.4,0,'Base','Dulce'),(6,2500,30,'Jugo de maracuyá',8.4,0,'Base','Amargo'),(7,3000,18,'Aceite de coco',4.2,0,'Base','Neutro'),(8,2200,100,'Vainilla',10,0,'Complemento',NULL),(9,2500,150,'Chocolate',10,0,'Complemento',NULL),(10,1500,70,'Cacao en polvo',0,0,'Complemento',NULL),(11,3000,30,'Fresas',20,0,'Complemento',NULL),(12,2000,50,'Coco rallado',0,0,'Complemento',NULL),(13,1800,80,'Galletas oreo',12,0,'Complemento',NULL),(14,4000,30,'Almendra',12,1,'Complemento',NULL);
/*!40000 ALTER TABLE `ingrediente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-18 22:30:39
