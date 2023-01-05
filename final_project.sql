-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: final_project
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `comment_id` int NOT NULL,
  `likes` int DEFAULT NULL,
  `dislikes` int DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract`
--

DROP TABLE IF EXISTS `contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contract` (
  `contract_number` int NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`contract_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract`
--

LOCK TABLES `contract` WRITE;
/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phonenumber` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deal`
--

DROP TABLE IF EXISTS `deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deal` (
  `contract_number` int NOT NULL,
  `company_id` int NOT NULL,
  `deal_id` int NOT NULL,
  PRIMARY KEY (`deal_id`),
  KEY `contract_number` (`contract_number`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `deal_ibfk_1` FOREIGN KEY (`contract_number`) REFERENCES `contract` (`contract_number`),
  CONSTRAINT `deal_ibfk_2` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deal`
--

LOCK TABLES `deal` WRITE;
/*!40000 ALTER TABLE `deal` DISABLE KEYS */;
/*!40000 ALTER TABLE `deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `deptid` int NOT NULL,
  `dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount` (
  `discount_id` int NOT NULL,
  `product_id` int NOT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `percentage` int NOT NULL,
  PRIMARY KEY (`discount_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `discount_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount`
--

LOCK TABLES `discount` WRITE;
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `degree_of_education` varchar(50) DEFAULT NULL,
  `has_insurance` int DEFAULT NULL,
  `superviser_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `superviser_id` (`superviser_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`superviser_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_fulltime`
--

DROP TABLE IF EXISTS `employee_fulltime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_fulltime` (
  `emp_id` int NOT NULL,
  `salary` int DEFAULT NULL,
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `employee_fulltime_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_fulltime`
--

LOCK TABLES `employee_fulltime` WRITE;
/*!40000 ALTER TABLE `employee_fulltime` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_fulltime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_parttime`
--

DROP TABLE IF EXISTS `employee_parttime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_parttime` (
  `emp_id` int NOT NULL,
  `salary` int DEFAULT NULL,
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `employee_parttime_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_parttime`
--

LOCK TABLES `employee_parttime` WRITE;
/*!40000 ALTER TABLE `employee_parttime` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_parttime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_works_for_official_branch`
--

DROP TABLE IF EXISTS `employee_works_for_official_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_works_for_official_branch` (
  `employee_id` int NOT NULL,
  `official_branch_branchid` int NOT NULL,
  KEY `employee_id` (`employee_id`),
  KEY `official_branch_branchid` (`official_branch_branchid`),
  CONSTRAINT `employee_works_for_official_branch_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `employee_works_for_official_branch_ibfk_2` FOREIGN KEY (`official_branch_branchid`) REFERENCES `official_branch` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_works_for_official_branch`
--

LOCK TABLES `employee_works_for_official_branch` WRITE;
/*!40000 ALTER TABLE `employee_works_for_official_branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_works_for_official_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_works_for_sales_branch`
--

DROP TABLE IF EXISTS `employee_works_for_sales_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_works_for_sales_branch` (
  `employee_id` int NOT NULL,
  `sales_branch_branchid` int NOT NULL,
  KEY `employee_id` (`employee_id`),
  KEY `sales_branch_branchid` (`sales_branch_branchid`),
  CONSTRAINT `employee_works_for_sales_branch_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `employee_works_for_sales_branch_ibfk_2` FOREIGN KEY (`sales_branch_branchid`) REFERENCES `sales_branch` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_works_for_sales_branch`
--

LOCK TABLES `employee_works_for_sales_branch` WRITE;
/*!40000 ALTER TABLE `employee_works_for_sales_branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_works_for_sales_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `given_comment`
--

DROP TABLE IF EXISTS `given_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `given_comment` (
  `comment_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `isbuyer` int DEFAULT NULL,
  KEY `comment_id` (`comment_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `given_comment_ibfk_1` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`comment_id`),
  CONSTRAINT `given_comment_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `given_comment`
--

LOCK TABLES `given_comment` WRITE;
/*!40000 ALTER TABLE `given_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `given_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `official_branch`
--

DROP TABLE IF EXISTS `official_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `official_branch` (
  `branch_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phonenumber` varchar(50) DEFAULT NULL,
  `data_Of_creation` varchar(50) DEFAULT NULL,
  `deptid` int NOT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `manager_id` (`manager_id`),
  KEY `deptid` (`deptid`),
  CONSTRAINT `official_branch_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `official_branch_ibfk_2` FOREIGN KEY (`deptid`) REFERENCES `department` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `official_branch`
--

LOCK TABLES `official_branch` WRITE;
/*!40000 ALTER TABLE `official_branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `official_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `official_department`
--

DROP TABLE IF EXISTS `official_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `official_department` (
  `deptid` int NOT NULL,
  KEY `deptid` (`deptid`),
  CONSTRAINT `official_department_ibfk_1` FOREIGN KEY (`deptid`) REFERENCES `department` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `official_department`
--

LOCK TABLES `official_department` WRITE;
/*!40000 ALTER TABLE `official_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `official_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_code` int NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `buy_price` int DEFAULT NULL,
  `sell_price` int DEFAULT NULL,
  `total_amount` int DEFAULT NULL,
  `availible_amount` int DEFAULT NULL,
  `game_type` varchar(100) DEFAULT NULL,
  `receipt_id` int NOT NULL,
  `isSold` int DEFAULT NULL,
  `provider_name` varchar(100) DEFAULT NULL,
  `sold_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_code`),
  KEY `receipt_id` (`receipt_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`receipt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_deal`
--

DROP TABLE IF EXISTS `products_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_deal` (
  `deal_id` int NOT NULL,
  `product_code` int NOT NULL,
  `amount` int DEFAULT NULL,
  KEY `deal_id` (`deal_id`),
  KEY `product_code` (`product_code`),
  CONSTRAINT `products_deal_ibfk_1` FOREIGN KEY (`deal_id`) REFERENCES `deal` (`deal_id`),
  CONSTRAINT `products_deal_ibfk_2` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_deal`
--

LOCK TABLES `products_deal` WRITE;
/*!40000 ALTER TABLE `products_deal` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_has_comment`
--

DROP TABLE IF EXISTS `products_has_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_has_comment` (
  `product_code` int NOT NULL,
  `comment_id` int NOT NULL,
  `score` int DEFAULT NULL,
  KEY `product_code` (`product_code`),
  KEY `comment_id` (`comment_id`),
  CONSTRAINT `products_has_comment_ibfk_1` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`),
  CONSTRAINT `products_has_comment_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_has_comment`
--

LOCK TABLES `products_has_comment` WRITE;
/*!40000 ALTER TABLE `products_has_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_has_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `receipt_id` int NOT NULL,
  `total_price` int DEFAULT NULL,
  `customer_id` int NOT NULL,
  `data` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`receipt_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `receipt_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_branch`
--

DROP TABLE IF EXISTS `sales_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_branch` (
  `branch_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phonenumber` varchar(50) DEFAULT NULL,
  `data_Of_creation` varchar(50) DEFAULT NULL,
  `deptid` int NOT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `manager_id` (`manager_id`),
  KEY `deptid` (`deptid`),
  CONSTRAINT `sales_branch_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `sales_branch_ibfk_2` FOREIGN KEY (`deptid`) REFERENCES `sales_department` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_branch`
--

LOCK TABLES `sales_branch` WRITE;
/*!40000 ALTER TABLE `sales_branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_department`
--

DROP TABLE IF EXISTS `sales_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_department` (
  `deptid` int NOT NULL,
  KEY `deptid` (`deptid`),
  CONSTRAINT `sales_department_ibfk_1` FOREIGN KEY (`deptid`) REFERENCES `department` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_department`
--

LOCK TABLES `sales_department` WRITE;
/*!40000 ALTER TABLE `sales_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `capacity` varchar(50) DEFAULT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `warehouse_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse_has_products`
--

DROP TABLE IF EXISTS `warehouse_has_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse_has_products` (
  `warehouse_id` int NOT NULL,
  `product_code` int NOT NULL,
  `amount` int DEFAULT NULL,
  KEY `warehouse_id` (`warehouse_id`),
  KEY `product_code` (`product_code`),
  CONSTRAINT `warehouse_has_products_ibfk_1` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`id`),
  CONSTRAINT `warehouse_has_products_ibfk_2` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse_has_products`
--

LOCK TABLES `warehouse_has_products` WRITE;
/*!40000 ALTER TABLE `warehouse_has_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouse_has_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warranty`
--

DROP TABLE IF EXISTS `warranty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warranty` (
  `product_id` int NOT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  KEY `product_id` (`product_id`),
  CONSTRAINT `warranty_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranty`
--

LOCK TABLES `warranty` WRITE;
/*!40000 ALTER TABLE `warranty` DISABLE KEYS */;
/*!40000 ALTER TABLE `warranty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-03 17:05:27
