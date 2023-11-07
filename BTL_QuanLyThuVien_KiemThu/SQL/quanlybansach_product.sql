-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: quanlybansach
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `price` float DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `category_id` int NOT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Lập trình ngôn ngữ C++','Đây là quyển sách mà tác giả chính là cha đẻ của ngôn ngữ lập trình C++ nổi tiếng Bjarne Stroustrup biên soạn nội dung, do đó nó rất phù hợp cho những bạn mới muốn học lập trình hoặc những bạn sinh viên, cá nhân đã có kinh nghiệm về lập trình cũng có thể tham khảo và học hỏi được từ cuốn sách này. Bạn sẽ nắm được những khái niệm cơ bản và phương pháp lập trình truyền thống, tác giả đi sâu vào phân tích rất cụ thể về các trường hợp và vấn đề cần lưu ý giúp bạn có. ',100000,'https://1.bp.blogspot.com/-s-gP-ukIBbM/XT1BeFwSzAI/AAAAAAAAVGI/pL23OUjM28I1LxVHS24K2suD_M0ykiscgCLcBGAs/s1600/1_34_5027-1.png',1,117,1,'2022-12-22 00:00:00'),(2,'Cóc kiện trời','For train code ',100000,'https://tse4.mm.bing.net/th?id=OIP.7BN7WjZuMkHr8jz1QA4shQHaK8&pid=Api&P=0',1,122,2,'2022-12-22 00:00:00'),(3,'Batman','For train code ',100000,'https://tse3.mm.bing.net/th?id=OIP.9qGNjHHj5MWOvnR6XfmgPAAAAA&pid=Api&P=0',1,123,3,'2022-12-22 00:00:00'),(4,'Ngôn ngữ cơ thể','For Language',120000,'https://sachhoc.com/image/cache/catalog/Chuyennganh/Ky-nang/Cuon-sach-hoan-hao-ve-ngon-ngu-co-the-500x554.jpg',1,211,4,'2023-02-16 00:00:00'),(5,'Thông điệp - từ những biểu cảm và ngôn ngữ cơ thể','For Language',150000,'https://product.hstatic.net/1000237375/product/bia_truoc-01_fd368628e14347129c28eb07b8c6f855_master.jpg',1,124,4,'2023-02-16 00:00:00'),(6,'Lập trình ngôn ngữ Java','Lập trình ngôn ngữ Java là cuốn sách về lập trình Java cho người mới bắt đầu học. Sách chỉ dùng một bộ phận nhỏ của ngôn ngữ Java đủ để giúp học viên thực hiện những bài tập lớn mà không bị sa đà vào những tiểu tiết của ngôn ngữ lập trình.',89000,'https://www.devpro.edu.vn/uploads/studies/1530765360.jpg',1,231,1,'2023-02-21 00:00:00'),(15,'Tớ Học Lập Trình','Nếu bạn là một beginner, thì cuốn sách “Tớ Học Lập Trình” là một sự lựa chọn hoàn hảo.',121000,'https://ironhackvietnam.edu.vn/wp-content/uploads/2021/03/sach-hoc-lap-trinh.jpg',1,121,1,'2023-02-21 00:00:00'),(16,'Lập Trình Và Cuộc Sống','“Lập Trình Và Cuộc Sống” của Jeff Atwood chú trọng vào yếu tố con người. Bởi Jeff Atwood cho rằng “để lập trình hiệu quả, viết code thôi là chưa đủ, con người mới là nhân tố quan trọng nhất”.',211000,'https://ironhackvietnam.edu.vn/wp-content/uploads/2021/03/sach-day-lap-trinh-co-ban-800x800.jpg',1,211,1,'2023-02-21 00:00:00'),(17,'Code Dạo Kí Sự ','Dù bạn là một beginner hay người đã từng học qua lập trình thì website “toidicodedao” không còn là cái tên xa lạ đối với bạn.',211000,'https://ironhackvietnam.edu.vn/wp-content/uploads/2021/03/sach-lap-trinh-666x1024.jpg',1,211,1,'2023-02-21 00:00:00');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-28 23:43:24
