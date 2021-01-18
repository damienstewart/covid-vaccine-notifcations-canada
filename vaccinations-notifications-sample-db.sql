-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 18, 2021 at 03:52 AM
-- Server version: 10.2.36-MariaDB-log
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nec90e5_vaccinations`
--

-- --------------------------------------------------------

--
-- Table structure for table `benchmark`
--

CREATE TABLE `benchmark` (
  `id` int(11) NOT NULL,
  `curr_bm` float NOT NULL,
  `date` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `benchmark`
--

INSERT INTO `benchmark` (`id`, `curr_bm`, `date`) VALUES
(1, 1, 'January 18, 2021');

-- --------------------------------------------------------

--
-- Table structure for table `vacc`
--

CREATE TABLE `vacc` (
  `id` int(11) NOT NULL,
  `percent_vaccinated` text NOT NULL,
  `people_vaccinated` text NOT NULL,
  `date` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vacc`
--

INSERT INTO `vacc` (`id`, `percent_vaccinated`, `people_vaccinated`, `date`) VALUES
(1, '1.420%', '539581', 'January 18, 2021');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `benchmark`
--
ALTER TABLE `benchmark`
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `idn` (`id`);

--
-- Indexes for table `vacc`
--
ALTER TABLE `vacc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `benchmark`
--
ALTER TABLE `benchmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `vacc`
--
ALTER TABLE `vacc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
