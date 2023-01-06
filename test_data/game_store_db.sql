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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `likes` int DEFAULT NULL,
  `dislikes` int DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contracts` (
  `contract_number` int NOT NULL AUTO_INCREMENT,
  `amount` DECIMAL DEFAULT NULL,
  PRIMARY KEY (`contract_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contracts`
--

LOCK TABLES `contracts` WRITE;
/*!40000 ALTER TABLE `contracts` DISABLE KEYS */;
/*!40000 ALTER TABLE `contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phonenumber` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deals`
--

DROP TABLE IF EXISTS `deals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deals` (
  `contract_number` int NOT NULL,
  `company_id` int NOT NULL,
  `deal_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`deal_id`),
  KEY `contract_number` (`contract_number`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `deal_ibfk_1` FOREIGN KEY (`contract_number`) REFERENCES `contracts` (`contract_number`),
  CONSTRAINT `deal_ibfk_2` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deals`
--

LOCK TABLES `deals` WRITE;
/*!40000 ALTER TABLE `deals` DISABLE KEYS */;
/*!40000 ALTER TABLE `deals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `deptid` int NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discounts`
--

DROP TABLE IF EXISTS `discounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discounts` (
  `discount_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `start_date` DATE DEFAULT NULL,
  `end_date` DATE DEFAULT NULL,
  `active` Varchar(10) DEFAULT 'NO',
  `percentage` int NOT NULL,
  PRIMARY KEY (`discount_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `discount_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discounts`
--

LOCK TABLES `discounts` WRITE;
/*!40000 ALTER TABLE `discounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `discounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `degree_of_education` varchar(50) DEFAULT NULL,
  `has_insurance` int DEFAULT NULL,
  `superviser_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`superviser_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fulltime_employees`
--

DROP TABLE IF EXISTS `fulltime_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fulltime_employees` (
  `emp_id` int NOT NULL,
  `salary` DECIMAL DEFAULT NULL,
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `employee_fulltime_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fulltime_employees`
--

LOCK TABLES `fulltime_employees` WRITE;
/*!40000 ALTER TABLE `fulltime_employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `fulltime_employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parttime_employees`
--

DROP TABLE IF EXISTS `parttime_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parttime_employees` (
  `emp_id` int NOT NULL,
  `salary` DECIMAL DEFAULT NULL,
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `employee_parttime_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parttime_employees`
--

LOCK TABLES `parttime_employees` WRITE;
/*!40000 ALTER TABLE `parttime_employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `parttime_employees` ENABLE KEYS */;
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
  CONSTRAINT `employee_works_for_official_branch_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `employee_works_for_official_branch_ibfk_2` FOREIGN KEY (`official_branch_branchid`) REFERENCES `official_branches` (`branch_id`)
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
  CONSTRAINT `employee_works_for_sales_branch_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `employee_works_for_sales_branch_ibfk_2` FOREIGN KEY (`sales_branch_branchid`) REFERENCES `sales_branches` (`branch_id`)
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
-- Table structure for table `given_comments`
--

DROP TABLE IF EXISTS `given_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `given_comments` (
  `comment_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `isbuyer` int DEFAULT NULL,
  KEY `comment_id` (`comment_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `given_comment_ibfk_1` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`comment_id`),
  CONSTRAINT `given_comment_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `given_comments`
--

LOCK TABLES `given_comments` WRITE;
/*!40000 ALTER TABLE `given_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `given_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `official_branches`
--

DROP TABLE IF EXISTS `official_branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `official_branches` (
  `branch_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phonenumber` varchar(50) DEFAULT NULL,
  `date_Of_establishment` DATE DEFAULT NULL,
  `deptid` int NOT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `manager_id` (`manager_id`),
  KEY `deptid` (`deptid`),
  CONSTRAINT `official_branch_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `official_branch_ibfk_2` FOREIGN KEY (`deptid`) REFERENCES `departments` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `official_branches`
--

LOCK TABLES `official_branches` WRITE;
/*!40000 ALTER TABLE `official_branches` DISABLE KEYS */;
/*!40000 ALTER TABLE `official_branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `official_departments`
--

DROP TABLE IF EXISTS `official_departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `official_departments` (
  `deptid` int NOT NULL,
  KEY `deptid` (`deptid`),
  CONSTRAINT `official_department_ibfk_1` FOREIGN KEY (`deptid`) REFERENCES `departments` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `official_departments`
--

LOCK TABLES `official_departments` WRITE;
/*!40000 ALTER TABLE `official_departments` DISABLE KEYS */;
/*!40000 ALTER TABLE `official_departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_code` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `buy_price` decimal DEFAULT NULL,
  `sell_price` decimal DEFAULT NULL,
  `product_type` varchar(100) DEFAULT NULL,
  `game_type` varchar(100) DEFAULT NULL,
  `receipt_id` int,
  `in_stock` varchar(10) DEFAULT 'NO',
  `provider_name` varchar(100) DEFAULT NULL,
  `sold_date` DATE DEFAULT NULL,
  PRIMARY KEY (`product_code`),
  FOREIGN KEY (`receipt_id`) REFERENCES `receipts` (`receipt_id`)
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
-- Table structure for table `products_deals`
--

DROP TABLE IF EXISTS `products_deals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_deals` (
  `deal_id` int NOT NULL,
  `product_code` int NOT NULL,
  `amount` decimal DEFAULT NULL,
  KEY `deal_id` (`deal_id`),
  KEY `product_code` (`product_code`),
  CONSTRAINT `products_deal_ibfk_1` FOREIGN KEY (`deal_id`) REFERENCES `deals` (`deal_id`),
  CONSTRAINT `products_deal_ibfk_2` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_deals`
--

LOCK TABLES `products_deals` WRITE;
/*!40000 ALTER TABLE `products_deals` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_deals` ENABLE KEYS */;
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
  CONSTRAINT `products_has_comment_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`comment_id`)
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
-- Table structure for table `receipts`
--

DROP TABLE IF EXISTS `receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipts` (
  `receipt_id` int NOT NULL AUTO_INCREMENT,
  `total_price` decimal DEFAULT NULL,
  `customer_id` int NOT NULL,
  `data` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`receipt_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `receipt_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipts`
--

LOCK TABLES `receipts` WRITE;
/*!40000 ALTER TABLE `receipts` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_branches`
--

DROP TABLE IF EXISTS `sales_branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_branches` (
  `branch_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phonenumber` varchar(50) DEFAULT NULL,
  `date_Of_establishment` DATE DEFAULT NULL,
  `deptid` int NOT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `manager_id` (`manager_id`),
  KEY `deptid` (`deptid`),
  CONSTRAINT `sales_branch_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `sales_branch_ibfk_2` FOREIGN KEY (`deptid`) REFERENCES `sales_departments` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_branches`
--

LOCK TABLES `sales_branches` WRITE;
/*!40000 ALTER TABLE `sales_branches` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales_branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_departments`
--

DROP TABLE IF EXISTS `sales_departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_departments` (
  `deptid` int NOT NULL,
  KEY `deptid` (`deptid`),
  CONSTRAINT `sales_department_ibfk_1` FOREIGN KEY (`deptid`) REFERENCES `departments` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_departments`
--

LOCK TABLES `sales_departments` WRITE;
/*!40000 ALTER TABLE `sales_departments` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales_departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouses`
--

DROP TABLE IF EXISTS `warehouses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `capacity` varchar(50) DEFAULT NULL,
  `manager_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `warehouse_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouses`
--

LOCK TABLES `warehouses` WRITE;
/*!40000 ALTER TABLE `warehouses` DISABLE KEYS */;
/*!40000 ALTER TABLE `warehouses` ENABLE KEYS */;
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
  `amount` decimal DEFAULT NULL,
  KEY `warehouse_id` (`warehouse_id`),
  KEY `product_code` (`product_code`),
  CONSTRAINT `warehouse_has_products_ibfk_1` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouses` (`id`),
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
-- Table structure for table `warranties`
--

DROP TABLE IF EXISTS `warranties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warranties` (
  `product_id` int NOT NULL,
  `end_date` DATE DEFAULT NULL,
  KEY `product_id` (`product_id`),
  CONSTRAINT `warranty_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warranties`
--

LOCK TABLES `warranties` WRITE;
/*!40000 ALTER TABLE `warranties` DISABLE KEYS */;
/*!40000 ALTER TABLE `warranties` ENABLE KEYS */;
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
