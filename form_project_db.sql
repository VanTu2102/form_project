-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2023 at 04:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `form_project_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `id` int(11) NOT NULL,
  `answer` text NOT NULL,
  `question_id` int(11) NOT NULL,
  `value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `answer`, `question_id`, `value`) VALUES
(1, 'Family support', 1, 1),
(2, 'Employed', 1, 2),
(3, 'Employed and receive assistance from family as well', 1, 3),
(4, 'Yes I have a well-defined plan for budget allocation', 2, 1),
(5, 'I am still working on developing a strategy for budget allocation', 2, 2),
(6, 'No, I currently don’t have a specific plan for budget allocation', 2, 3),
(7, 'Essential needs like foods, rent, utilities …', 3, 1),
(8, 'Entertainment and leisure activities', 3, 2),
(9, 'Saving for the future', 3, 3),
(10, 'I’m not sure', 3, 4),
(11, 'Immediate needs', 4, 1),
(12, 'Peer influence', 4, 2),
(13, 'Long-term goals', 4, 3),
(15, 'Random or impulsive purchases', 4, 4),
(16, 'Very comfortable', 5, 1),
(17, 'Somewhat comfortable', 5, 2),
(18, 'Not very comfortable', 5, 3),
(19, 'I struggle with this concept', 5, 4),
(20, 'I consistently save a portion of my income', 6, 1),
(21, 'I save occasionally when I have extra money', 6, 2),
(22, 'I rarely save as I spend most of my income', 6, 3),
(23, 'I don’t save at all', 6, 4),
(24, '20% or more', 7, 1),
(25, '10 – 20%', 7, 2),
(26, 'Less than 10%', 7, 3),
(27, 'I don’t allocate my income for savings', 7, 4),
(28, 'Lack of income', 8, 1),
(29, 'Impulse spending', 8, 2),
(30, 'Lack of knowledge about saving options', 8, 3),
(31, 'I don’t face any challenge', 8, 4),
(32, 'Bank accounts', 9, 1),
(33, 'E-wallet', 9, 2),
(34, 'I keep my saving with me or hidden away', 9, 3),
(35, 'Others (Specify)', 9, 4),
(36, 'Yes I have a dedicated emergency fund', 10, 1),
(37, 'I rely on credit cards or loan for emergencies', 10, 2),
(38, 'I rely on family support to handle emergencies', 10, 3),
(39, 'I don’t have a plan', 10, 4),
(40, 'Extremely important', 11, 1),
(41, 'Somewhat important', 11, 2),
(42, 'Not very important', 11, 3),
(43, 'I don’t see the relevance of financial	 education', 11, 4),
(44, 'First year', 12, 1),
(45, 'Second year', 12, 2),
(46, 'Third year', 12, 3),
(47, 'Fourth year+', 12, 4);

-- --------------------------------------------------------

--
-- Table structure for table `forms`
--

CREATE TABLE `forms` (
  `session_id` text NOT NULL,
  `answer_id` int(11) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `forms`
--

INSERT INTO `forms` (`session_id`, `answer_id`, `last_updated`) VALUES
('72e35acf-a2cb-4d64-8ba2-a079427e036f', 8, '2023-12-18 02:50:07'),
('72e35acf-a2cb-4d64-8ba2-a079427e036f', 42, '2023-12-18 02:50:07'),
('c47d4a86-0ff5-41ee-9783-149b9fda0c19', 7, '2023-12-18 02:50:15'),
('c47d4a86-0ff5-41ee-9783-149b9fda0c19', 44, '2023-12-18 02:50:15'),
('e0161d31-bc14-4bc4-bdd1-3b984c5bdae9', 9, '2023-12-18 02:51:26'),
('e0161d31-bc14-4bc4-bdd1-3b984c5bdae9', 46, '2023-12-18 02:51:26'),
('0896119d-80b5-4f55-80b5-7d31b787a78a', 9, '2023-12-18 02:51:27'),
('0896119d-80b5-4f55-80b5-7d31b787a78a', 46, '2023-12-18 02:51:27'),
('6388fd4a-a924-4bc2-93ed-e8a0bdfe96ff', 7, '2023-12-18 02:51:34'),
('6388fd4a-a924-4bc2-93ed-e8a0bdfe96ff', 47, '2023-12-18 02:51:34'),
('28488c8b-5e88-47ed-a58b-9de958a9c1ea', 8, '2023-12-18 03:21:46'),
('28488c8b-5e88-47ed-a58b-9de958a9c1ea', 45, '2023-12-18 03:21:46'),
('887fd295-b0ce-42a9-89ed-74591688dbdb', 8, '2023-12-18 03:21:59'),
('887fd295-b0ce-42a9-89ed-74591688dbdb', 46, '2023-12-18 03:21:59'),
('633e7fcf-4ccb-4d3e-b99e-6559401b4a78', 10, '2023-12-18 03:22:12'),
('633e7fcf-4ccb-4d3e-b99e-6559401b4a78', 44, '2023-12-18 03:22:12'),
('7c66362a-d33b-4c9a-9659-82887e6a65c0', 9, '2023-12-18 03:54:43'),
('7c66362a-d33b-4c9a-9659-82887e6a65c0', 46, '2023-12-18 03:54:43'),
('d0b9d437-cb83-4b67-807a-ea83c6c83327', 8, '2023-12-18 03:55:00'),
('d0b9d437-cb83-4b67-807a-ea83c6c83327', 47, '2023-12-18 03:55:00'),
('d0b9d437-cb83-4b67-807a-ea83c6c83327', 46, '2023-12-18 03:55:00'),
('e2dac48d-e31b-42b8-bc70-097d28936f66', 24, '2023-12-18 04:33:45'),
('e2dac48d-e31b-42b8-bc70-097d28936f66', 45, '2023-12-18 04:33:45'),
('e30f0ffe-aa83-4d14-85bc-74616e9a8496', 27, '2023-12-18 04:46:30'),
('e30f0ffe-aa83-4d14-85bc-74616e9a8496', 47, '2023-12-18 04:46:30'),
('827da74b-320e-492f-8f6f-b2d080493f12', 3, '2023-12-18 05:57:37'),
('827da74b-320e-492f-8f6f-b2d080493f12', 4, '2023-12-18 05:57:37'),
('827da74b-320e-492f-8f6f-b2d080493f12', 10, '2023-12-18 05:57:37'),
('827da74b-320e-492f-8f6f-b2d080493f12', 24, '2023-12-18 05:57:37'),
('827da74b-320e-492f-8f6f-b2d080493f12', 44, '2023-12-18 05:57:37'),
('008639a7-4fc3-456f-9303-31dac8ae4f35', 26, '2023-12-18 05:57:54'),
('008639a7-4fc3-456f-9303-31dac8ae4f35', 45, '2023-12-18 05:57:54'),
('4053847d-3040-4945-9989-082e342499ed', 2, '2023-12-18 07:36:59'),
('4053847d-3040-4945-9989-082e342499ed', 47, '2023-12-18 07:36:59'),
('f3e0edd5-a0e6-4679-987e-75dde1ef4778', 3, '2023-12-18 07:37:04'),
('f3e0edd5-a0e6-4679-987e-75dde1ef4778', 46, '2023-12-18 07:37:04'),
('84907b98-3f86-4626-8e84-5205a7d2dd1d', 1, '2023-12-18 07:37:09'),
('84907b98-3f86-4626-8e84-5205a7d2dd1d', 44, '2023-12-18 07:37:09'),
('3f061748-a1c1-4f31-8ff7-bf029736b412', 2, '2023-12-18 07:37:14'),
('3f061748-a1c1-4f31-8ff7-bf029736b412', 47, '2023-12-18 07:37:14'),
('3548a494-f5a7-4505-b1b7-ef74febbf535', 1, '2023-12-18 07:41:57'),
('3548a494-f5a7-4505-b1b7-ef74febbf535', 45, '2023-12-18 07:41:57'),
('45d72e23-aa02-4097-a47b-1850eb152dc5', 1, '2023-12-18 10:56:47'),
('45d72e23-aa02-4097-a47b-1850eb152dc5', 45, '2023-12-18 10:56:47'),
('6c5c81a9-0e22-4793-b39b-a1b585e7dc14', 3, '2023-12-18 10:57:02'),
('6c5c81a9-0e22-4793-b39b-a1b585e7dc14', 46, '2023-12-18 10:57:02'),
('6c5c81a9-0e22-4793-b39b-a1b585e7dc14', 47, '2023-12-18 10:57:02'),
('8d29e6db-4594-408f-be8c-0194f1b6f5ec', 1, '2023-12-18 10:57:16'),
('8d29e6db-4594-408f-be8c-0194f1b6f5ec', 47, '2023-12-18 10:57:16'),
('11ec4b3f-d676-4542-a168-f4059283ac45', 3, '2023-12-18 11:00:33'),
('11ec4b3f-d676-4542-a168-f4059283ac45', 2, '2023-12-18 11:00:33'),
('11ec4b3f-d676-4542-a168-f4059283ac45', 47, '2023-12-18 11:00:33'),
('a180bab0-7dc7-4de7-8fde-f6c6ff746c50', 25, '2023-12-18 11:36:44'),
('a180bab0-7dc7-4de7-8fde-f6c6ff746c50', 44, '2023-12-18 11:36:44'),
('9d4d297a-e06a-499a-9bf4-fce2e58acc10', 25, '2023-12-18 11:37:02'),
('9d4d297a-e06a-499a-9bf4-fce2e58acc10', 46, '2023-12-18 11:37:02'),
('63e73dc5-5fb4-4c8f-ba71-906c9dc52692', 25, '2023-12-18 12:57:21'),
('63e73dc5-5fb4-4c8f-ba71-906c9dc52692', 47, '2023-12-18 12:57:21'),
('f13e2500-74fb-4161-8cbc-6afa2178d8ec', 27, '2023-12-18 12:57:28'),
('f13e2500-74fb-4161-8cbc-6afa2178d8ec', 44, '2023-12-18 12:57:28'),
('bc00eb55-1f87-4de3-a396-a7c8b95e2c83', 26, '2023-12-18 12:57:34'),
('bc00eb55-1f87-4de3-a396-a7c8b95e2c83', 45, '2023-12-18 12:57:34'),
('e3d71b3e-2857-46a1-8607-2f9ae0fe8bec', 17, '2023-12-18 12:57:49'),
('e3d71b3e-2857-46a1-8607-2f9ae0fe8bec', 24, '2023-12-18 12:57:49'),
('e3d71b3e-2857-46a1-8607-2f9ae0fe8bec', 44, '2023-12-18 12:57:49'),
('0c40983f-d65f-4cc3-b397-358cf752e285', 24, '2023-12-18 12:58:35'),
('0c40983f-d65f-4cc3-b397-358cf752e285', 46, '2023-12-18 12:58:35'),
('6b6fdbe4-f8ff-484e-adfe-7b618d83437b', 44, '2023-12-18 12:58:42'),
('6b6fdbe4-f8ff-484e-adfe-7b618d83437b', 26, '2023-12-18 12:58:42'),
('f79a1382-ba35-4d0a-8867-3f20c19346b6', 24, '2023-12-18 12:58:55'),
('f79a1382-ba35-4d0a-8867-3f20c19346b6', 44, '2023-12-18 12:58:55'),
('c4723604-5d72-4b51-ba14-17966f2bb8a4', 26, '2023-12-18 12:59:01'),
('c4723604-5d72-4b51-ba14-17966f2bb8a4', 47, '2023-12-18 12:59:01'),
('2ecbf7cf-fb83-4ea5-ba86-826c4541b841', 27, '2023-12-18 12:59:06'),
('2ecbf7cf-fb83-4ea5-ba86-826c4541b841', 46, '2023-12-18 12:59:06'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 2, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 5, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 8, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 12, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 18, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 21, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 26, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 29, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 33, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 36, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 41, '2023-12-18 14:30:29'),
('8dbaefa0-cb5f-49e5-b943-660ce2a5a043', 44, '2023-12-18 14:30:29'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 3, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 6, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 7, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 11, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 16, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 22, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 24, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 30, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 33, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 36, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 42, '2023-12-18 14:30:45'),
('ae688954-cecc-4e94-a285-e7ef9aba384f', 45, '2023-12-18 14:30:45'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 3, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 5, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 8, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 12, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 16, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 20, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 24, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 28, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 32, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 36, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 41, '2023-12-18 14:31:03'),
('679542fa-5bc9-4795-9c50-bfa7c7a72659', 46, '2023-12-18 14:31:03'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 6, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 2, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 8, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 13, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 16, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 20, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 26, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 29, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 32, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 36, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 40, '2023-12-18 14:31:18'),
('a3df9725-4b5f-417d-b3be-c0e4631a675f', 47, '2023-12-18 14:31:18'),
('d222f471-2b06-4a1f-a0be-c32ab7257898', 3, '2023-12-18 15:01:09'),
('d222f471-2b06-4a1f-a0be-c32ab7257898', 44, '2023-12-18 15:01:09'),
('72e35acf-a2cb-4d64-8ba2-a079427e036f', 1, '2021-12-18 15:36:59'),
('72e35acf-a2cb-4d64-8b2-a079s27e036b', 8, '2021-12-18 16:05:42'),
('72e35acf-a2cb-4d64-8b2-a079s27e036b', 44, '2021-12-18 16:09:29'),
('84907b98-3f86-4626-8e84-5205a7dadd', 5, '2023-12-01 03:45:53'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 2, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 4, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 8, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 11, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 17, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 31, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 23, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 24, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 34, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 37, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 42, '2023-12-19 15:21:27'),
('bce591ab-599a-43cf-b52e-fbc9b7117661', 46, '2023-12-19 15:21:27'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 1, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 4, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 7, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 11, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 17, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 23, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 24, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 30, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 32, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 36, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 40, '2023-12-11 15:22:14'),
('0db4a89b-ca8e-4609-a93d-f04190ec40df', 44, '2023-12-11 15:22:14');

-- --------------------------------------------------------

--
-- Table structure for table `parts`
--

CREATE TABLE `parts` (
  `id` int(11) NOT NULL,
  `part` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parts`
--

INSERT INTO `parts` (`id`, `part`) VALUES
(1, 'Income Sources'),
(2, 'Budget Allocation - Spending'),
(3, 'Savings – Tech – Crisis handling'),
(4, 'Final question');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL,
  `part_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `question`, `part_id`) VALUES
(1, 'From where do you derive your income', 1),
(2, 'Which of the following best describes your approach to budget allocation', 2),
(3, 'How do you prioritize spending your money', 2),
(4, 'What factors influence your budget decisions the most?', 2),
(5, 'How comfortable are you with differentiating between “wants” and “needs” in your budget?', 2),
(6, 'How do you describe your current saving habits?', 3),
(7, 'What percentage of your income do you typically allocate for your savings?', 3),
(8, 'What challenge do you face when it comes to saving money?', 3),
(9, 'Where do you usually keep your savings', 3),
(10, 'Do you have an emergency fund in place for unexpected expenses?', 3),
(11, 'How do you perceive the role of financial education in preparing for financial crises?', 3),
(12, 'Which year are you in?', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexes for table `forms`
--
ALTER TABLE `forms`
  ADD KEY `answer_id` (`answer_id`);

--
-- Indexes for table `parts`
--
ALTER TABLE `parts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `part_id` (`part_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `parts`
--
ALTER TABLE `parts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`);

--
-- Constraints for table `forms`
--
ALTER TABLE `forms`
  ADD CONSTRAINT `forms_ibfk_1` FOREIGN KEY (`answer_id`) REFERENCES `answers` (`id`);

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`part_id`) REFERENCES `parts` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
