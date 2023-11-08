-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 08 Lis 2023, 12:11
-- Wersja serwera: 10.4.25-MariaDB
-- Wersja PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `tlumacz`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pytania`
--

CREATE TABLE `pytania` (
  `Nr` int(11) NOT NULL,
  `slowo` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `pytania`
--

INSERT INTO `pytania` (`Nr`, `slowo`) VALUES
(1, 'jabłko'),
(2, 'samochód'),
(3, 'rower'),
(4, 'pomarancza'),
(5, 'drzwi'),
(6, 'mieć'),
(7, 'banan'),
(8, 'potrafić'),
(9, 'okno'),
(10, 'pytanie'),
(11, 'pies'),
(12, 'kot'),
(13, 'jeść'),
(14, 'nowy'),
(15, 'stary'),
(16, 'tekst'),
(17, 'nauka'),
(18, 'temat'),
(19, 'lekcja'),
(20, 'język'),
(21, 'tablet'),
(22, 'klawiatura'),
(23, 'samolot'),
(24, 'hulajnoga'),
(25, 'kabel'),
(26, 'zasilać'),
(27, 'kanapka'),
(28, 'kodować'),
(29, 'rysunek '),
(30, 'pięć'),
(31, 'nowoczesny'),
(32, 'morze'),
(33, 'woda'),
(34, 'ocean'),
(35, 'oko'),
(36, 'ręka'),
(37, 'plecak'),
(38, 'bluza'),
(39, 'kurtka'),
(40, 'papier '),
(41, 'duch'),
(42, 'żaba'),
(43, 'koza'),
(44, 'wybuch'),
(45, 'warzywa');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pytania`
--
ALTER TABLE `pytania`
  ADD PRIMARY KEY (`Nr`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `pytania`
--
ALTER TABLE `pytania`
  MODIFY `Nr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
