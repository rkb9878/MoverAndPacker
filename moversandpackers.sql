-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 16, 2020 at 11:07 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moversandpackers`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `email` varchar(30) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `mobile` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`email`, `password`, `type`, `mobile`) VALUES
('anmol@gmail.com', '123', 'admin', '9592231891'),
('ayushi.dhir95@gmail.com', '111', 'admin', '7989767699'),
('b@gmail.com', '123', 'subadmin', '9779319197');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bookingid` int(11) NOT NULL,
  `bookername` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `pickupstate` varchar(45) DEFAULT NULL,
  `pickupcity` varchar(45) DEFAULT NULL,
  `pickupaddress` text DEFAULT NULL,
  `droppingstate` varchar(45) DEFAULT NULL,
  `droppingcity` varchar(45) DEFAULT NULL,
  `droppingaddress` text DEFAULT NULL,
  `packagename` varchar(45) DEFAULT NULL,
  `dateofbooking` date DEFAULT NULL,
  `dateofpickup` date DEFAULT NULL,
  `dateofdropping` date DEFAULT NULL,
  `paymentmode` varchar(45) DEFAULT NULL,
  `amountreceived` float DEFAULT NULL,
  `paymentstatus` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `dispatchstatus` varchar(45) DEFAULT NULL,
  `emailstatus` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `booking_track`
--

CREATE TABLE `booking_track` (
  `trackingid` int(11) NOT NULL,
  `bookingid` varchar(45) DEFAULT NULL,
  `remarks` text DEFAULT NULL,
  `dateofupdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `newsid` int(11) NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `dateofnews` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`newsid`, `title`, `description`, `dateofnews`) VALUES
(8, 'new servives', 'new Services have been added for customers', '2019-10-22'),
(9, 'modifications', 'new packages have been availed', '2019-10-28'),
(12, 'modifications of services', 'qqqqqqqqcc', '2019-10-31'),
(13, 'new services for customers!1', 'alert!!!!1', '2019-10-31');

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `packagename` varchar(60) NOT NULL,
  `description` varchar(450) DEFAULT NULL,
  `sourcestate` varchar(45) DEFAULT NULL,
  `sourcecity` varchar(45) DEFAULT NULL,
  `destinationstate` varchar(45) DEFAULT NULL,
  `destinationcity` varchar(45) DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`packagename`, `description`, `sourcestate`, `sourcecity`, `destinationstate`, `destinationcity`, `price`) VALUES
('Gold 101', 'upto 2000 Kg extra @200 per kg', 'Punjab', 'Amritsar', 'Punjab', 'Tarn-Taran', 9000),
('Gold 102', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Bathinda', 14000),
('Gold 103', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Jalandhar', 20000),
('Gold 104', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Pathankot', 28000),
('Gold 105', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Ludhiana', 26000),
('Gold 106', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Gurdaspur', 'Delhi', 'Firozabad', 70000),
('Gold 107', 'upto 2000 Kg extra @200 per Kg ', 'Delhi', 'Shajahnabad', 'Punjab', 'Faridkot', 55000),
('Gold 108', 'upto 2000 Kg extra @200 per Kg ', 'Delhi', 'Mehrauli', 'Haryana', 'Panipat', 45000),
('Gold 109', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Ajnala', 'Punjab', 'Moga', 25000),
('Gold 110', 'upto 2000 Kg extra @200 per Kg ', 'Punjab', 'Attari', 'Jammu and Kashmir', 'Leh', 43000),
('Gold 111', 'upto 2000 Kg extra @200 per Kg ', 'Maharashtra', 'Mumbai', 'Haryana', 'Rohtak', 37000),
('Gold 112', 'upto 2000 Kg extra @200 per Kg ', 'Tamil Nadu', 'Pondicherry', 'Haryana', 'Sirsa', 70000),
('Gold 113', 'upto 2000 Kg extra @200 per Kg ', 'Karnataka', 'Manglore', 'West Bengal', 'Kolkata', 55000),
('Gold 114', 'upto 2000 Kg extra @200 per Kg', 'Delhi', 'Shergarh', 'Uttar Pradesh', 'Kanpur', 50000),
('Gold 115', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Maharashtra', 'Mumbai', 80000),
('Gold 116', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ferozpur', 35000),
('Gold 117', 'upto 2000 Kg extra @200 per Kg', 'Uttar Pradesh', 'Ayodhya', 'Tamil Nadu', 'Ranipet', 85000),
('Gold 118', 'upto 2000 Kg extra @200 per Kg', 'West Bengal', 'Durgapur', 'Punjab', 'Pathankot', 78000),
('Gold 119', 'upto 2000 Kg extra @200 per Kg', 'Kerala', 'Kochi', 'Jammu and Kashmir', 'Srinagar', 90000),
('Gold 120', 'upto 2000 Kg extra @200 per Kg', 'Delhi', 'Firozabad', 'West Bengal', 'Shantipur', 92000),
('Gold 121', 'upto 2000 Kg extra @200 per Kg', 'Maharashtra', 'Ahmednagar', 'Maharashtra', 'Ahmednagar', 18000),
('Gold 122', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Amritsar', 15000),
('Gold 123', 'upto 2000 Kg extra @200 per Kg', 'Jammu and Kashmir', 'Srinagar', 'Jammu and Kashmir', 'Srinagar', 17500),
('Gold 124', 'upto 2000 Kg extra @200 per Kg', 'Haryana', 'Ambala', 'Haryana', 'Gurugram', 32000),
('Gold 125', 'upto 2000 Kg extra @200 per Kg', 'Uttar Pradesh', 'Kanpur', 'Uttar Pradesh', 'Lucknow', 21000),
('Gold 126', 'upto 2000 Kg extra @200 per Kg', 'Karnataka', 'Hampi', 'Karnataka', 'Badami', 20000),
('Gold 127', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ajnala', 13000),
('Gold 128', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Abhor', 30000),
('Gold 129', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Attari', 10000),
('Gold 130', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Faridkot', 12500),
('Gold 131', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Gurdaspur', 12000),
('Gold 132', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Moga', 15000),
('Gold 133', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Tarn-Taran', 'Punjab', 'Tarn-Taran', 12000),
('Gold 134', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Abhor', 'Punjab', 'Abhor', 10000),
('Gold 135', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Ajnala', 'Punjab', 'Ajnala', 12000),
('Gold 136', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Bathinda', 'Punjab', 'Bathinda', 12000),
('Gold 137', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Faridkot', 'Punjab', 'Faridkot', 13000),
('Gold 138', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Attari', 'Punjab', 'Attari', 7500),
('Gold 139', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Ferozpur', 'Punjab', 'Ferozpur', 12000),
('Gold 140', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Gurdaspur', 'Punjab', 'Gurdaspur', 9800),
('Gold 141', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Jalandhar', 'Punjab', 'Jalandhar', 8900),
('Gold 142', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Ludhiana', 'Punjab', 'Ludhiana', 9000),
('Gold 143', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Moga', 'Punjab', 'Moga', 9000),
('Gold 144', 'upto 2000 Kg extra @200 per Kg', 'Punjab', 'Pathankot', 'Punjab', 'Pathankot', 12000),
('Premium 101', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Tarn-Taran', 4500),
('Premium 102', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Bathinda', 7000),
('Premium 103', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Jalandhar', 12000),
('Premium 104', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Pathankot', 15000),
('Premium 105', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Ludhiana', 13000),
('Premium 106', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Gurdaspur', 'Delhi', 'Firozabad', 40000),
('Premium 107', 'upto 1000 Kg extra @200 per Kg ', 'Delhi', 'Shajahnabad', 'Punjab', 'Faridkot', 30000),
('Premium 108', 'upto 1000 Kg extra @200 per Kg ', 'Delhi', 'Mehrauli', 'Haryana', 'Panipat', 28000),
('Premium 109', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Ajnala', 'Punjab', 'Moga', 15000),
('Premium 110', 'upto 1000 Kg extra @200 per Kg ', 'Punjab', 'Attari', 'Jammu and Kashmir', 'Leh', 22000),
('Premium 111', 'upto 1000 Kg extra @200 per Kg ', 'Maharashtra', 'Mumbai', 'Haryana', 'Rohtak', 28000),
('Premium 112', 'upto 1000 Kg extra @200 per Kg ', 'Tamil Nadu', 'Pondicherry', 'Haryana', 'Sirsa', 40000),
('Premium 113', 'upto 1000 Kg extra @200 per Kg ', 'Karnataka', 'Manglore', 'West Bengal', 'Kolkata', 30000),
('Premium 114', 'upto 1000 Kg extra@200 per Kg', 'Delhi', 'Shergarh', 'Uttar Pradesh', 'Kanpur', 30000),
('Premium 115', 'upto 1000 Kg extra @200 per Kg  ', 'Punjab', 'Amritsar', 'Maharashtra', 'Mumbai', 50000),
('Premium 116', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ferozpur', 18000),
('Premium 117', 'upto 1000 Kg extra @200 per Kg', 'Uttar Pradesh', 'Ayodhya', 'Tamil Nadu', 'Ranipet', 50000),
('Premium 118', 'upto 1000 Kg extra @200 per Kg', 'West Bengal', 'Durgapur', 'Punjab', 'Pathankot', 56000),
('Premium 119', 'upto 1000 Kg extra @200 per Kg', 'Kerala', 'Kochi', 'Jammu and Kashmir', 'Srinagar', 58000),
('Premium 120', 'upto 1000 Kg extra @200 per Kg', 'Delhi', 'Firozabad', 'West Bengal', 'Shantipur', 56000),
('Premium 121', 'upto 1000 Kg extra @200 per Kg', 'Maharashtra', 'Ahmednagar', 'Maharashtra', 'Ahmednagar', 12000),
('Premium 122', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Amritsar', 7200),
('Premium 123', 'upto 1000 Kg extra @200 per Kg', 'Jammu and Kashmir', 'Srinagar', 'Jammu and Kashmir', 'Srinagar', 7800),
('Premium 124', 'upto 1000 Kg extra @200 per Kg', 'Haryana', 'Ambala', 'Haryana', 'Gurugram', 20000),
('Premium 125', 'upto 1000 Kg extra @200 per Kg', 'Uttar Pradesh', 'Kanpur', 'Uttar Pradesh', 'Lucknow', 13000),
('Premium 126', 'upto 1000 Kg extra @200 per Kg', 'Karnataka', 'Hampi', 'Karnataka', 'Badami', 12000),
('Premium 127', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ajnala', 5600),
('Premium 128', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Abhor', 20000),
('Premium 129', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Attari', 5000),
('Premium 130', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Faridkot', 6700),
('Premium 131', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Gurdaspur', 5600),
('Premium 132', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Moga', 7000),
('Premium 133', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Tarn-Taran', 'Punjab', 'Tarn-Taran', 4500),
('Premium 134', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Abhor', 'Punjab', 'Abhor', 5000),
('Premium 135', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Ajnala', 'Punjab', 'Ajnala', 4500),
('Premium 136', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Bathinda', 'Punjab', 'Bathinda', 5600),
('Premium 137', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Faridkot', 'Punjab', 'Faridkot', 6700),
('Premium 140', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Gurdaspur', 'Punjab', 'Gurdaspur', 4500),
('Premium 142', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Ludhiana', 'Punjab', 'Ludhiana', 4600),
('Premium 143', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Moga', 'Punjab', 'Moga', 5800),
('Premium 144', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Pathankot', 'Punjab', 'Pathankot', 4500),
('Silver 101', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Tarn-Taran', 7500),
('Silver 102', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Bathinda', 12000),
('Silver 103', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Jalandhar', 17000),
('Silver 104', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Amritsar', 'Punjab', 'Pathankot', 22000),
('Silver 105', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Ludhiana', 'Punjab', 'Ludhiana', 20000),
('Silver 106', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Gurdaspur', 'Delhi', 'Firozabad', 58000),
('Silver 107', 'upto 1500 Kg extra @200 per Kg ', 'Delhi', 'Firozabad', 'Punjab', 'Faridkot', 42000),
('Silver 108', 'upto 1500 Kg extra @200 per Kg ', 'Delhi', 'Mehrauli', 'Haryana', 'Panipat', 40000),
('Silver 109', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Ajnala', 'Punjab', 'Moga', 20000),
('Silver 110', 'upto 1500 Kg extra @200 per Kg ', 'Punjab', 'Attari', 'Jammu and Kashmir', 'Leh', 35000),
('Silver 111', 'upto 1500 Kg extra @200 per Kg ', 'Maharashtra', 'Mumbai', 'Haryana', 'Rohtak', 45000),
('Silver 112', 'upto 1500 Kg extra @200 per Kg ', 'Tamil Nadu', 'Pondicherry', 'Haryana', 'Sirsa', 58000),
('Silver 113', 'upto 1500 Kg extra @200 per Kg ', 'Karnataka', 'Manglore', 'West Bengal', 'Kolkata', 59000),
('Silver 114', 'upto 1500 Kg extra @200 per Kg', 'Delhi', 'Shergarh', 'Uttar Pradesh', 'Kanpur', 40000),
('Silver 115', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Maharashtra', 'Mumbai', 65000),
('Silver 116', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ferozpur', 26000),
('Silver 117', 'upto 1500 Kg extra @200 per Kg', 'Uttar Pradesh', 'Ayodhya', 'Tamil Nadu', 'Ranipet', 66000),
('Silver 118', 'upto 1500 Kg extra @200 per Kg', 'West Bengal', 'Durgapur', 'Punjab', 'Pathankot', 62000),
('Silver 119', 'upto 1500 Kg extra @200 per Kg', 'Kerala', 'Kochi', 'Jammu and Kashmir', 'Srinagar', 70000),
('Silver 120', 'upto 1500 Kg extra @200 per Kg', 'Delhi', 'Firozabad', 'West Bengal', 'Shantipur', 75000),
('Silver 121', 'upto 1500 Kg extra @200 per Kg', 'Maharashtra', 'Ahmednagar', 'Maharashtra', 'Ahmednagar', 15000),
('Silver 122', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Amritsar', 11000),
('Silver 123', 'upto 1500 Kg extra @200 per Kg', 'Jammu and Kashmir', 'Srinagar', 'Jammu and Kashmir', 'Srinagar', 13500),
('Silver 124', 'upto 1500 Kg extra @200 per Kg', 'Haryana', 'Ambala', 'Haryana', 'Gurugram', 26000),
('Silver 125', 'upto 1500 Kg extra @200 per Kg', 'Uttar Pradesh', 'Kanpur', 'Uttar Pradesh', 'Lucknow', 15500),
('Silver 126', 'upto 1500 Kg extra @200 per Kg', 'Karnataka', 'Hampi', 'Karnataka', 'Badami', 16500),
('Silver 127', 'upto 1500 Kg extra @ 200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Ajnala', 9000),
('Silver 128', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Abhor', 25000),
('Silver 129', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Attari', 7600),
('Silver 130', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Faridkot', 8900),
('Silver 131', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Gurdaspur', 8000),
('Silver 132', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Amritsar', 'Punjab', 'Moga', 10000),
('Silver 138', 'upto 1500 Kg extra @200 per Kg', 'Punjab', 'Attari', 'Punjab', 'Attari', 5800),
('Silver 139', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Ferozpur', 'Punjab', 'Ferozpur', 4500),
('Silver 141', 'upto 1000 Kg extra @200 per Kg', 'Punjab', 'Jalandhar', 'Punjab', 'Jalandhar', 4500);

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `reviewid` int(11) NOT NULL,
  `bookingid` int(11) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `review` text DEFAULT NULL,
  `dateofsubmission` date DEFAULT NULL,
  `bookername` varchar(45) DEFAULT NULL,
  `photo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `servicingstations`
--

CREATE TABLE `servicingstations` (
  `service_city_name` varchar(60) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `state` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `servicingstations`
--

INSERT INTO `servicingstations` (`service_city_name`, `description`, `state`) VALUES
('Abhor', 'Abhor,Punjab', 'Punjab'),
('Ahmednagar', 'Ahmednagar,Maharashtra', 'Maharashtra'),
('Ajnala', 'Ajnala,Punjab', 'Punjab'),
('Akhnoor', 'Akhnoor,Jammu and Kashmir', 'Jammu and Kashmir'),
('Aligarh', 'Aligarh,Uttar Pradesh', 'Uttar Pradesh'),
('Ambala', 'Ambala,Haryana', 'Haryana'),
('Amritsar', 'Amritsar,Punjab\n', 'Punjab'),
('Anantnag', 'Anantnag,Jammu and Kashmir', 'Jammu and Kashmir'),
('Attari', 'Attari,Punjab', 'Punjab'),
('Ayodhya', 'Ayodhya,Uttar Pradesh', 'Uttar Pradesh'),
('Badami', 'Badami,Karnataka', 'Karnataka'),
('Ballari', 'Ballari,Karnataka', 'Karnataka'),
('Bareilly', 'Bareilly,Uttar Pradesh', 'Uttar Pradesh'),
('Bathinda', 'Bathinda,Punjab', 'Punjab'),
('Bekal', 'Bekal,Kerala', 'Kerala'),
('Bengaluru', 'Bengaluru,Karnataka', 'Karnataka'),
('Beypore', 'Beypore,Kerala', 'Kerala'),
('Bhopal', 'Bhopal,Madhya Pradesh', 'Madhya Pradesh'),
('Chennai', 'Chennai,Tamil Nadu', 'Tamil Nadu'),
('Dewas', 'Dewas,Madhya Pradesh', 'Madhya Pradesh'),
('Doda', 'Doda,Jammu and Kashmir', 'Jammu and Kashmir'),
('Durgapur', 'Durgapur,West Bengal', 'West Bengal'),
('Faridkot', 'Faridkot,Punjab', 'Punjab'),
('Ferozpur', 'Ferozpur,Punjab', 'Punjab'),
('Firozabad', 'Firozabad,Delhi', 'Delhi'),
('Gunna', 'Gunna,Madhya Pradesh', 'Madhya Pradesh'),
('Gurdaspur', 'Gurdaspur,Punjab', 'Punjab'),
('Gurugram', 'Gurugram,Haryana', 'Haryana'),
('Gwalior', 'Gwalior,Madhya Pradesh', 'Madhya Pradesh'),
('Habra', 'Habra,West Bengal', 'West Bengal'),
('Hampi', 'Hampi,Karnataka', 'Karnataka'),
('Hubli', 'Hubli,Karnataka', 'Karnataka'),
('Indore', 'Indore,Madhya Pradesh', 'Madhya Pradesh'),
('Jabalpur', 'Jabalpur,Madhya Pradesh', 'Madhya Pradesh'),
('Jalandhar', 'Jalandhar,Punjab', 'Punjab'),
('Jangipur', 'Jangipur,West Bengal', 'West Bengal'),
('Kannur', 'Kannur,Kerala', 'Kerala'),
('Kanpur', 'Kanpur,Uttar Pradesh', 'Uttar Pradesh'),
('Kochi', 'Kochi,Kerala', 'Kerala'),
('Kohlapur', 'Kohlapur,Maharashtra', 'Maharashtra'),
('Kolkata', 'Kolkata,West Bengal', 'West Bengal'),
('Kollam', 'Kollam,Kerala', 'Kerala'),
('Latur', 'Latur,Maharashtra', 'Maharashtra'),
('Leh', 'Leh,Jammu and Kashmir\n', 'Jammu and Kashmir'),
('Lucknow', 'Lucknow,Uttar Pradesh', 'Uttar Pradesh'),
('Ludhiana', 'Ludhiana,Punjab', 'Punjab'),
('Madurai', 'Madurai,Tamil Nadu', 'Tamil Nadu'),
('Manglore', 'Manglore,Karnataka', 'Karnataka'),
('Mannur', 'Mannur,Kerala', 'Kerala'),
('Meerut', 'Meerut,Uttar Pradesh', 'Uttar Pradesh'),
('Mehrauli', 'Mehrauli,Delhi', 'Delhi'),
('Moga', 'Moga,Punjab', 'Punjab'),
('Mumbai', 'Mumbai,Maharashtra', 'Maharashtra'),
('Nagpur', 'Nagpur,Maharashtra', 'Maharashtra'),
('Panipat', 'Panipat,Haryana', 'Haryana'),
('Panna', 'Panna,Madhya Pradesh', 'Madhya Pradesh'),
('Pathankot', 'Pathankot,Punjab', 'Punjab'),
('Pondicherry', 'Pondicherry,Tamil Nadu', 'Tamil Nadu'),
('Pune', 'Pune,Maharashtra', 'Maharashtra'),
('Rajauri', 'Rajauri,Jammu and Kashmir', 'Jammu and Kashmir'),
('Ranipet', 'Ranipet,Tamil Nadu', 'Tamil Nadu'),
('Rohtak', 'Rohtak,Haryana', 'Haryana'),
('Sagar', 'Sagar,Madhya Pradesh', 'Madhya Pradesh'),
('Sangli', 'Sangli,Maharashtra', 'Maharashtra'),
('Satna', 'Satna,Madhya Pradesh', 'Madhya Pradesh'),
('Shajahnabad', 'Shajahnabad,Delhi', 'Delhi'),
('Shantipur', 'Shantipur,West Bengal', 'West Bengal'),
('Shergarh', 'Shergarh,Delhi', 'Delhi'),
('Shoranur', 'Shoranur,Kerala', 'Kerala'),
('Sirsa', 'Sirsa,Haryana', 'Haryana'),
('Solapur', 'Solapur,Maharashtra', 'Maharashtra'),
('Srinagar', 'Srinagar,Jammu and Kashmir', 'Jammu and Kashmir'),
('Tarn-Taran', 'Tarn-Taran,Punjab', 'Punjab'),
('Tenkasi', 'Tenkasi,Tamil Nadu', 'Tamil Nadu'),
('Varanasi', 'Varanasi,Uttar Pradesh', 'Uttar Pradesh'),
('Vayala', 'Vayala,Kerala', 'Kerala'),
('Yamuna Nagar', 'Yamuna Nagar,Haryana', 'Haryana');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(30) NOT NULL,
  `mobile` varchar(10) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `photo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `mobile`, `password`, `name`, `address`, `photo`) VALUES
('aaa@gmail.com', '9592231891', '123', 'komal', 'tarn-taran', 'userphotos/76574a111.jpg'),
('abd@gmail.com', '9592231891', '111', 'gitika', 'amritsar', 'userphotos/76421del.png'),
('anmol@yahoo.com', '9592231891', '234', 'ayushi', 'amritsar', 'userphotos/26950del.png'),
('ayushi.dhir95@gmail.com', '8427543923', '123', 'ayushi', 'amritsar', 'userphotos/90862edit.png'),
('harwant@gmail.com', '9465346609', '1234', 'harwant', 'tarn-taran', 'userphotos/86473edit.png'),
('hundal.anmol96@gmail.com', '9592231891', '111', 'anmol', 'tarn-taran', 'userphotos/52086del.png'),
('komal111@gmail.com', '9465346609', '333', 'komal', 'tarn-taran', 'userphotos/10452edit.png'),
('tarsem@gmail.com', '9872553470', '456', 'Tarsem Singh', 'tarn-taran', 'userphotos/4246edit.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookingid`);

--
-- Indexes for table `booking_track`
--
ALTER TABLE `booking_track`
  ADD PRIMARY KEY (`trackingid`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`newsid`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`packagename`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`reviewid`);

--
-- Indexes for table `servicingstations`
--
ALTER TABLE `servicingstations`
  ADD PRIMARY KEY (`service_city_name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bookingid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `booking_track`
--
ALTER TABLE `booking_track`
  MODIFY `trackingid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `newsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `reviewid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
