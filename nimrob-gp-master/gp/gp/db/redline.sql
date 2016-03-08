-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: redline
-- ------------------------------------------------------
-- Server version	5.1.73-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dayag`
--

DROP TABLE IF EXISTS `dayag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dayag` (
  `DM` varchar(10) DEFAULT NULL,
  `JYRQ` datetime NOT NULL,
  `KP` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `SP` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `MA5` float DEFAULT NULL,
  `MA10` float DEFAULT NULL,
  `MA20` float DEFAULT NULL,
  `MA60` float DEFAULT NULL,
  `MACD_DIF` float DEFAULT NULL,
  `MACD_DEA` float DEFAULT NULL,
  `VOL_TDX_VOLUME` float DEFAULT NULL,
  `VOL_TDX_MAVOL1` float DEFAULT NULL,
  `VOL_TDX_MAVOL2` float DEFAULT NULL,
  `WR1` float DEFAULT NULL,
  `WR2` float DEFAULT NULL,
  `BOLL` float DEFAULT NULL,
  `BOLL_UB` float DEFAULT NULL,
  `BOLL_LB` float DEFAULT NULL,
  `DMI_PDI` float DEFAULT NULL,
  `DMI_MDI` float DEFAULT NULL,
  `DMI_ADX` float DEFAULT NULL,
  `DMI_ADXR` float DEFAULT NULL,
  `DMA_DIF` float DEFAULT NULL,
  `DMA_DIFMA` float DEFAULT NULL,
  `FSL_SWL` float DEFAULT NULL,
  `FSL_SWS` float DEFAULT NULL,
  `TRIX` float DEFAULT NULL,
  `MATRIX` float DEFAULT NULL,
  `BR` float DEFAULT NULL,
  `AR` float DEFAULT NULL,
  `CR` float DEFAULT NULL,
  `CR_MA1` float DEFAULT NULL,
  `CR_MA2` float DEFAULT NULL,
  `CR_MA3` float DEFAULT NULL,
  `CR_MA4` float DEFAULT NULL,
  `VR` float DEFAULT NULL,
  `MAVR` float DEFAULT NULL,
  `OBV` float DEFAULT NULL,
  `MAOBV` float DEFAULT NULL,
  `ASI` float DEFAULT NULL,
  `MAASI` float DEFAULT NULL,
  `EMV` float DEFAULT NULL,
  `MAEMV` float DEFAULT NULL,
  `RSI1` float DEFAULT NULL,
  `RSI2` float DEFAULT NULL,
  `RSI3` float DEFAULT NULL,
  `K` float DEFAULT NULL,
  `D` float DEFAULT NULL,
  `J` float DEFAULT NULL,
  `CCI` float DEFAULT NULL,
  `ROC` float DEFAULT NULL,
  `MAROC` float DEFAULT NULL,
  `MTM` float DEFAULT NULL,
  `MAMTM` float DEFAULT NULL,
  `PSY` float DEFAULT NULL,
  `MAPSY` float DEFAULT NULL,
  `WY1` float DEFAULT NULL,
  `WY2` float DEFAULT NULL,
  `WY3` float DEFAULT NULL,
  `WY4` float DEFAULT NULL,
  `WY5` float DEFAULT NULL,
  `WY6` float DEFAULT NULL,
  `WY7` float DEFAULT NULL,
  `WY8` float DEFAULT NULL,
  `WY9` float DEFAULT NULL,
  `WY10` float DEFAULT NULL,
  `WY11` float DEFAULT NULL,
  `WY12` float DEFAULT NULL,
  `WY13` float DEFAULT NULL,
  `WY14` float DEFAULT NULL,
  `WY15` float DEFAULT NULL,
  `WY16` float DEFAULT NULL,
  `WY17` float DEFAULT NULL,
  `WY18` float DEFAULT NULL,
  `SW1` float DEFAULT NULL,
  `SW2` float DEFAULT NULL,
  `SW3` float DEFAULT NULL,
  `SW4` float DEFAULT NULL,
  `SW5` float DEFAULT NULL,
  `SW6` float DEFAULT NULL,
  `SW7` float DEFAULT NULL,
  `SW8` float DEFAULT NULL,
  `SW9` float DEFAULT NULL,
  `SW10` float DEFAULT NULL,
  `JBM1` float DEFAULT NULL,
  `JBM2` float DEFAULT NULL,
  `JBM3` float DEFAULT NULL,
  `JBM4` float DEFAULT NULL,
  `JBM5` float DEFAULT NULL,
  `JBM6` float DEFAULT NULL,
  `JBM7` float DEFAULT NULL,
  `JBM8` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dayzs`
--

DROP TABLE IF EXISTS `dayzs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dayzs` (
  `DM` varchar(10) DEFAULT NULL,
  `JYRQ` datetime NOT NULL,
  `KP` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `SP` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `MA5` float DEFAULT NULL,
  `MA10` float DEFAULT NULL,
  `MA20` float DEFAULT NULL,
  `MA60` float DEFAULT NULL,
  `MACD_DIF` float DEFAULT NULL,
  `MACD_DEA` float DEFAULT NULL,
  `VOL_TDX_VOLUME` float DEFAULT NULL,
  `VOL_TDX_MAVOL1` float DEFAULT NULL,
  `VOL_TDX_MAVOL2` float DEFAULT NULL,
  `WR1` float DEFAULT NULL,
  `WR2` float DEFAULT NULL,
  `BOLL` float DEFAULT NULL,
  `BOLL_UB` float DEFAULT NULL,
  `BOLL_LB` float DEFAULT NULL,
  `DMI_PDI` float DEFAULT NULL,
  `DMI_MDI` float DEFAULT NULL,
  `DMI_ADX` float DEFAULT NULL,
  `DMI_ADXR` float DEFAULT NULL,
  `DMA_DIF` float DEFAULT NULL,
  `DMA_DIFMA` float DEFAULT NULL,
  `FSL_SWL` float DEFAULT NULL,
  `FSL_SWS` float DEFAULT NULL,
  `TRIX` float DEFAULT NULL,
  `MATRIX` float DEFAULT NULL,
  `BR` float DEFAULT NULL,
  `AR` float DEFAULT NULL,
  `CR` float DEFAULT NULL,
  `CR_MA1` float DEFAULT NULL,
  `CR_MA2` float DEFAULT NULL,
  `CR_MA3` float DEFAULT NULL,
  `CR_MA4` float DEFAULT NULL,
  `VR` float DEFAULT NULL,
  `MAVR` float DEFAULT NULL,
  `OBV` float DEFAULT NULL,
  `MAOBV` float DEFAULT NULL,
  `ASI` float DEFAULT NULL,
  `MAASI` float DEFAULT NULL,
  `EMV` float DEFAULT NULL,
  `MAEMV` float DEFAULT NULL,
  `RSI1` float DEFAULT NULL,
  `RSI2` float DEFAULT NULL,
  `RSI3` float DEFAULT NULL,
  `K` float DEFAULT NULL,
  `D` float DEFAULT NULL,
  `J` float DEFAULT NULL,
  `CCI` float DEFAULT NULL,
  `ROC` float DEFAULT NULL,
  `MAROC` float DEFAULT NULL,
  `MTM` float DEFAULT NULL,
  `MAMTM` float DEFAULT NULL,
  `PSY` float DEFAULT NULL,
  `MAPSY` float DEFAULT NULL,
  `WY1` float DEFAULT NULL,
  `WY2` float DEFAULT NULL,
  `WY3` float DEFAULT NULL,
  `WY4` float DEFAULT NULL,
  `WY5` float DEFAULT NULL,
  `WY6` float DEFAULT NULL,
  `WY7` float DEFAULT NULL,
  `WY8` float DEFAULT NULL,
  `WY9` float DEFAULT NULL,
  `WY10` float DEFAULT NULL,
  `WY11` float DEFAULT NULL,
  `WY12` float DEFAULT NULL,
  `WY13` float DEFAULT NULL,
  `WY14` float DEFAULT NULL,
  `WY15` float DEFAULT NULL,
  `WY16` float DEFAULT NULL,
  `WY17` float DEFAULT NULL,
  `WY18` float DEFAULT NULL,
  `SW1` float DEFAULT NULL,
  `SW2` float DEFAULT NULL,
  `SW3` float DEFAULT NULL,
  `SW4` float DEFAULT NULL,
  `SW5` float DEFAULT NULL,
  `SW6` float DEFAULT NULL,
  `SW7` float DEFAULT NULL,
  `SW8` float DEFAULT NULL,
  `SW9` float DEFAULT NULL,
  `SW10` float DEFAULT NULL,
  `JBM1` float DEFAULT NULL,
  `JBM2` float DEFAULT NULL,
  `JBM3` float DEFAULT NULL,
  `JBM4` float DEFAULT NULL,
  `JBM5` float DEFAULT NULL,
  `JBM6` float DEFAULT NULL,
  `JBM7` float DEFAULT NULL,
  `JBM8` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dp_fx`
--

DROP TABLE IF EXISTS `dp_fx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dp_fx` (
  `JYRQ` date NOT NULL,
  `PJJBZ` float DEFAULT NULL,
  `PJLBZ` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `NB` float DEFAULT NULL,
  `HSL` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dq`
--

DROP TABLE IF EXISTS `dq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dq` (
  `DM` varchar(10) NOT NULL,
  `MC` varchar(32) NOT NULL,
  `DQ` varchar(32) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fscjmxhz`
--

DROP TABLE IF EXISTS `fscjmxhz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fscjmxhz` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `BZE` float DEFAULT NULL,
  `BZL` float DEFAULT NULL,
  `SZE` float DEFAULT NULL,
  `SZL` float DEFAULT NULL,
  `PJBJ` float DEFAULT NULL,
  `PJSJ` float DEFAULT NULL,
  `PJJBZ` float DEFAULT NULL,
  `PJJCZ` float DEFAULT NULL,
  `PJBL` float DEFAULT NULL,
  `PJSL` float DEFAULT NULL,
  `PJLBZ` float DEFAULT NULL,
  `PJLCZ` float DEFAULT NULL,
  `ZXPL` float DEFAULT NULL,
  `ZXPBZ` float DEFAULT NULL,
  `FZXPBZ` float DEFAULT NULL,
  `ZXPE` float DEFAULT NULL,
  `ZXPEBZ` float DEFAULT NULL,
  `H` float DEFAULT NULL,
  `M` float DEFAULT NULL,
  `GJBDE` float DEFAULT NULL,
  `GJBDJ` float DEFAULT NULL,
  `GJBDL` float DEFAULT NULL,
  `GJBDFS` float DEFAULT NULL,
  `GJBDEBZ` float DEFAULT NULL,
  `GJBDLBZ` float DEFAULT NULL,
  `GJBDFSBZ` float DEFAULT NULL,
  `GJSDE` float DEFAULT NULL,
  `GJSDJ` float DEFAULT NULL,
  `GJSDL` float DEFAULT NULL,
  `GJSDFS` float DEFAULT NULL,
  `GJSDEBZ` float DEFAULT NULL,
  `GJSDLBZ` float DEFAULT NULL,
  `GJSDFSBZ` float DEFAULT NULL,
  `ZJBDE` float DEFAULT NULL,
  `ZJBDJ` float DEFAULT NULL,
  `ZJBDL` float DEFAULT NULL,
  `ZJBDFS` float DEFAULT NULL,
  `ZJBDEBZ` float DEFAULT NULL,
  `ZJBDLBZ` float DEFAULT NULL,
  `ZJBDFSBZ` float DEFAULT NULL,
  `ZJSDE` float DEFAULT NULL,
  `ZJSDJ` float DEFAULT NULL,
  `ZJSDL` float DEFAULT NULL,
  `ZJSDFS` float DEFAULT NULL,
  `ZJSDEBZ` float DEFAULT NULL,
  `ZJSDLBZ` float DEFAULT NULL,
  `ZJSDFSBZ` float DEFAULT NULL,
  `DJBDE` float DEFAULT NULL,
  `DJBDJ` float DEFAULT NULL,
  `DJBDL` float DEFAULT NULL,
  `DJBDFS` float DEFAULT NULL,
  `DJBDEBZ` float DEFAULT NULL,
  `DJBDLBZ` float DEFAULT NULL,
  `DJBDFSBZ` float DEFAULT NULL,
  `DJSDE` float DEFAULT NULL,
  `DJSDJ` float DEFAULT NULL,
  `DJSDL` float DEFAULT NULL,
  `DJSDFS` float DEFAULT NULL,
  `DJSDEBZ` float DEFAULT NULL,
  `DJSDLBZ` float DEFAULT NULL,
  `DJSDFSBZ` float DEFAULT NULL,
  `LH` float DEFAULT NULL,
  `LM` float DEFAULT NULL,
  `GLBDE` float DEFAULT NULL,
  `GLBDJ` float DEFAULT NULL,
  `GLBDL` float DEFAULT NULL,
  `GLBDFS` float DEFAULT NULL,
  `GLBDEBZ` float DEFAULT NULL,
  `GLBDLBZ` float DEFAULT NULL,
  `GLBDFSBZ` float DEFAULT NULL,
  `GLSDE` float DEFAULT NULL,
  `GLSDJ` float DEFAULT NULL,
  `GLSDL` float DEFAULT NULL,
  `GLSDFS` float DEFAULT NULL,
  `GLSDEBZ` float DEFAULT NULL,
  `GLSDLBZ` float DEFAULT NULL,
  `GLSDFSBZ` float DEFAULT NULL,
  `ZLBDE` float DEFAULT NULL,
  `ZLBDJ` float DEFAULT NULL,
  `ZLBDL` float DEFAULT NULL,
  `ZLBDFS` float DEFAULT NULL,
  `ZLBDEBZ` float DEFAULT NULL,
  `ZLBDLBZ` float DEFAULT NULL,
  `ZLBDFSBZ` float DEFAULT NULL,
  `ZLSDE` float DEFAULT NULL,
  `ZLSDJ` float DEFAULT NULL,
  `ZLSDL` float DEFAULT NULL,
  `ZLSDFS` float DEFAULT NULL,
  `ZLSDEBZ` float DEFAULT NULL,
  `ZLSDLBZ` float DEFAULT NULL,
  `ZLSDFSBZ` float DEFAULT NULL,
  `DLBDE` float DEFAULT NULL,
  `DLBDJ` float DEFAULT NULL,
  `DLBDL` float DEFAULT NULL,
  `DLBDFS` float DEFAULT NULL,
  `DLBDEBZ` float DEFAULT NULL,
  `DLBDLBZ` float DEFAULT NULL,
  `DLBDFSBZ` float DEFAULT NULL,
  `DLSDE` float DEFAULT NULL,
  `DLSDJ` float DEFAULT NULL,
  `DLSDL` float DEFAULT NULL,
  `DLSDFS` float DEFAULT NULL,
  `DLSDEBZ` float DEFAULT NULL,
  `DLSDLBZ` float DEFAULT NULL,
  `DLSDFSBZ` float DEFAULT NULL,
  `ZS` float DEFAULT NULL,
  `JK` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `JS` float DEFAULT NULL,
  `ZF` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `UPE` float DEFAULT NULL,
  `UPL` float DEFAULT NULL,
  `UPED` float DEFAULT NULL,
  `UPTD` float DEFAULT NULL,
  `UPEPJ` float DEFAULT NULL,
  `UPLPJ` float DEFAULT NULL,
  `UPTPJ` float DEFAULT NULL,
  `DOWNE` float DEFAULT NULL,
  `DOWNL` float DEFAULT NULL,
  `DOWNED` float DEFAULT NULL,
  `DOWNTD` float DEFAULT NULL,
  `DOWNEPJ` float DEFAULT NULL,
  `DOWNLPJ` float DEFAULT NULL,
  `DOWNTPJ` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `MCJL` float DEFAULT NULL,
  `MCJE` float DEFAULT NULL,
  `MBS` float DEFAULT NULL,
  `MSS` float DEFAULT NULL,
  `MUPS` float DEFAULT NULL,
  `MDOWNS` float DEFAULT NULL,
  `NB` float DEFAULT NULL,
  `HSL` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fscjmxhz_backup`
--

DROP TABLE IF EXISTS `fscjmxhz_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fscjmxhz_backup` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `BZE` float DEFAULT NULL,
  `BZL` float DEFAULT NULL,
  `SZE` float DEFAULT NULL,
  `SZL` float DEFAULT NULL,
  `PJBJ` float DEFAULT NULL,
  `PJSJ` float DEFAULT NULL,
  `PJJBZ` float DEFAULT NULL,
  `PJJCZ` float DEFAULT NULL,
  `PJBL` float DEFAULT NULL,
  `PJSL` float DEFAULT NULL,
  `PJLBZ` float DEFAULT NULL,
  `PJLCZ` float DEFAULT NULL,
  `ZXPL` float DEFAULT NULL,
  `ZXPBZ` float DEFAULT NULL,
  `FZXPBZ` float DEFAULT NULL,
  `ZXPE` float DEFAULT NULL,
  `ZXPEBZ` float DEFAULT NULL,
  `H` float DEFAULT NULL,
  `M` float DEFAULT NULL,
  `GJBDE` float DEFAULT NULL,
  `GJBDJ` float DEFAULT NULL,
  `GJBDL` float DEFAULT NULL,
  `GJBDFS` float DEFAULT NULL,
  `GJBDEBZ` float DEFAULT NULL,
  `GJBDLBZ` float DEFAULT NULL,
  `GJBDFSBZ` float DEFAULT NULL,
  `GJSDE` float DEFAULT NULL,
  `GJSDJ` float DEFAULT NULL,
  `GJSDL` float DEFAULT NULL,
  `GJSDFS` float DEFAULT NULL,
  `GJSDEBZ` float DEFAULT NULL,
  `GJSDLBZ` float DEFAULT NULL,
  `GJSDFSBZ` float DEFAULT NULL,
  `ZJBDE` float DEFAULT NULL,
  `ZJBDJ` float DEFAULT NULL,
  `ZJBDL` float DEFAULT NULL,
  `ZJBDFS` float DEFAULT NULL,
  `ZJBDEBZ` float DEFAULT NULL,
  `ZJBDLBZ` float DEFAULT NULL,
  `ZJBDFSBZ` float DEFAULT NULL,
  `ZJSDE` float DEFAULT NULL,
  `ZJSDJ` float DEFAULT NULL,
  `ZJSDL` float DEFAULT NULL,
  `ZJSDFS` float DEFAULT NULL,
  `ZJSDEBZ` float DEFAULT NULL,
  `ZJSDLBZ` float DEFAULT NULL,
  `ZJSDFSBZ` float DEFAULT NULL,
  `DJBDE` float DEFAULT NULL,
  `DJBDJ` float DEFAULT NULL,
  `DJBDL` float DEFAULT NULL,
  `DJBDFS` float DEFAULT NULL,
  `DJBDEBZ` float DEFAULT NULL,
  `DJBDLBZ` float DEFAULT NULL,
  `DJBDFSBZ` float DEFAULT NULL,
  `DJSDE` float DEFAULT NULL,
  `DJSDJ` float DEFAULT NULL,
  `DJSDL` float DEFAULT NULL,
  `DJSDFS` float DEFAULT NULL,
  `DJSDEBZ` float DEFAULT NULL,
  `DJSDLBZ` float DEFAULT NULL,
  `DJSDFSBZ` float DEFAULT NULL,
  `LH` float DEFAULT NULL,
  `LM` float DEFAULT NULL,
  `GLBDE` float DEFAULT NULL,
  `GLBDJ` float DEFAULT NULL,
  `GLBDL` float DEFAULT NULL,
  `GLBDFS` float DEFAULT NULL,
  `GLBDEBZ` float DEFAULT NULL,
  `GLBDLBZ` float DEFAULT NULL,
  `GLBDFSBZ` float DEFAULT NULL,
  `GLSDE` float DEFAULT NULL,
  `GLSDJ` float DEFAULT NULL,
  `GLSDL` float DEFAULT NULL,
  `GLSDFS` float DEFAULT NULL,
  `GLSDEBZ` float DEFAULT NULL,
  `GLSDLBZ` float DEFAULT NULL,
  `GLSDFSBZ` float DEFAULT NULL,
  `ZLBDE` float DEFAULT NULL,
  `ZLBDJ` float DEFAULT NULL,
  `ZLBDL` float DEFAULT NULL,
  `ZLBDFS` float DEFAULT NULL,
  `ZLBDEBZ` float DEFAULT NULL,
  `ZLBDLBZ` float DEFAULT NULL,
  `ZLBDFSBZ` float DEFAULT NULL,
  `ZLSDE` float DEFAULT NULL,
  `ZLSDJ` float DEFAULT NULL,
  `ZLSDL` float DEFAULT NULL,
  `ZLSDFS` float DEFAULT NULL,
  `ZLSDEBZ` float DEFAULT NULL,
  `ZLSDLBZ` float DEFAULT NULL,
  `ZLSDFSBZ` float DEFAULT NULL,
  `DLBDE` float DEFAULT NULL,
  `DLBDJ` float DEFAULT NULL,
  `DLBDL` float DEFAULT NULL,
  `DLBDFS` float DEFAULT NULL,
  `DLBDEBZ` float DEFAULT NULL,
  `DLBDLBZ` float DEFAULT NULL,
  `DLBDFSBZ` float DEFAULT NULL,
  `DLSDE` float DEFAULT NULL,
  `DLSDJ` float DEFAULT NULL,
  `DLSDL` float DEFAULT NULL,
  `DLSDFS` float DEFAULT NULL,
  `DLSDEBZ` float DEFAULT NULL,
  `DLSDLBZ` float DEFAULT NULL,
  `DLSDFSBZ` float DEFAULT NULL,
  `ZS` float DEFAULT NULL,
  `JK` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `JS` float DEFAULT NULL,
  `ZF` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `UPE` float DEFAULT NULL,
  `UPL` float DEFAULT NULL,
  `UPED` float DEFAULT NULL,
  `UPTD` float DEFAULT NULL,
  `UPEPJ` float DEFAULT NULL,
  `UPLPJ` float DEFAULT NULL,
  `UPTPJ` float DEFAULT NULL,
  `DOWNE` float DEFAULT NULL,
  `DOWNL` float DEFAULT NULL,
  `DOWNED` float DEFAULT NULL,
  `DOWNTD` float DEFAULT NULL,
  `DOWNEPJ` float DEFAULT NULL,
  `DOWNLPJ` float DEFAULT NULL,
  `DOWNTPJ` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `MCJL` float DEFAULT NULL,
  `MCJE` float DEFAULT NULL,
  `MBS` float DEFAULT NULL,
  `MSS` float DEFAULT NULL,
  `MUPS` float DEFAULT NULL,
  `MDOWNS` float DEFAULT NULL,
  `NB` float DEFAULT NULL,
  `HSL` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fscjmxhz_mem`
--

DROP TABLE IF EXISTS `fscjmxhz_mem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fscjmxhz_mem` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `BZE` float DEFAULT NULL,
  `BZL` float DEFAULT NULL,
  `SZE` float DEFAULT NULL,
  `SZL` float DEFAULT NULL,
  `PJBJ` float DEFAULT NULL,
  `PJSJ` float DEFAULT NULL,
  `PJJBZ` float DEFAULT NULL,
  `PJJCZ` float DEFAULT NULL,
  `PJBL` float DEFAULT NULL,
  `PJSL` float DEFAULT NULL,
  `PJLBZ` float DEFAULT NULL,
  `PJLCZ` float DEFAULT NULL,
  `ZXPL` float DEFAULT NULL,
  `ZXPBZ` float DEFAULT NULL,
  `FZXPBZ` float DEFAULT NULL,
  `ZXPE` float DEFAULT NULL,
  `ZXPEBZ` float DEFAULT NULL,
  `H` float DEFAULT NULL,
  `M` float DEFAULT NULL,
  `GJBDE` float DEFAULT NULL,
  `GJBDJ` float DEFAULT NULL,
  `GJBDL` float DEFAULT NULL,
  `GJBDFS` float DEFAULT NULL,
  `GJBDEBZ` float DEFAULT NULL,
  `GJBDLBZ` float DEFAULT NULL,
  `GJBDFSBZ` float DEFAULT NULL,
  `GJSDE` float DEFAULT NULL,
  `GJSDJ` float DEFAULT NULL,
  `GJSDL` float DEFAULT NULL,
  `GJSDFS` float DEFAULT NULL,
  `GJSDEBZ` float DEFAULT NULL,
  `GJSDLBZ` float DEFAULT NULL,
  `GJSDFSBZ` float DEFAULT NULL,
  `ZJBDE` float DEFAULT NULL,
  `ZJBDJ` float DEFAULT NULL,
  `ZJBDL` float DEFAULT NULL,
  `ZJBDFS` float DEFAULT NULL,
  `ZJBDEBZ` float DEFAULT NULL,
  `ZJBDLBZ` float DEFAULT NULL,
  `ZJBDFSBZ` float DEFAULT NULL,
  `ZJSDE` float DEFAULT NULL,
  `ZJSDJ` float DEFAULT NULL,
  `ZJSDL` float DEFAULT NULL,
  `ZJSDFS` float DEFAULT NULL,
  `ZJSDEBZ` float DEFAULT NULL,
  `ZJSDLBZ` float DEFAULT NULL,
  `ZJSDFSBZ` float DEFAULT NULL,
  `DJBDE` float DEFAULT NULL,
  `DJBDJ` float DEFAULT NULL,
  `DJBDL` float DEFAULT NULL,
  `DJBDFS` float DEFAULT NULL,
  `DJBDEBZ` float DEFAULT NULL,
  `DJBDLBZ` float DEFAULT NULL,
  `DJBDFSBZ` float DEFAULT NULL,
  `DJSDE` float DEFAULT NULL,
  `DJSDJ` float DEFAULT NULL,
  `DJSDL` float DEFAULT NULL,
  `DJSDFS` float DEFAULT NULL,
  `DJSDEBZ` float DEFAULT NULL,
  `DJSDLBZ` float DEFAULT NULL,
  `DJSDFSBZ` float DEFAULT NULL,
  `LH` float DEFAULT NULL,
  `LM` float DEFAULT NULL,
  `GLBDE` float DEFAULT NULL,
  `GLBDJ` float DEFAULT NULL,
  `GLBDL` float DEFAULT NULL,
  `GLBDFS` float DEFAULT NULL,
  `GLBDEBZ` float DEFAULT NULL,
  `GLBDLBZ` float DEFAULT NULL,
  `GLBDFSBZ` float DEFAULT NULL,
  `GLSDE` float DEFAULT NULL,
  `GLSDJ` float DEFAULT NULL,
  `GLSDL` float DEFAULT NULL,
  `GLSDFS` float DEFAULT NULL,
  `GLSDEBZ` float DEFAULT NULL,
  `GLSDLBZ` float DEFAULT NULL,
  `GLSDFSBZ` float DEFAULT NULL,
  `ZLBDE` float DEFAULT NULL,
  `ZLBDJ` float DEFAULT NULL,
  `ZLBDL` float DEFAULT NULL,
  `ZLBDFS` float DEFAULT NULL,
  `ZLBDEBZ` float DEFAULT NULL,
  `ZLBDLBZ` float DEFAULT NULL,
  `ZLBDFSBZ` float DEFAULT NULL,
  `ZLSDE` float DEFAULT NULL,
  `ZLSDJ` float DEFAULT NULL,
  `ZLSDL` float DEFAULT NULL,
  `ZLSDFS` float DEFAULT NULL,
  `ZLSDEBZ` float DEFAULT NULL,
  `ZLSDLBZ` float DEFAULT NULL,
  `ZLSDFSBZ` float DEFAULT NULL,
  `DLBDE` float DEFAULT NULL,
  `DLBDJ` float DEFAULT NULL,
  `DLBDL` float DEFAULT NULL,
  `DLBDFS` float DEFAULT NULL,
  `DLBDEBZ` float DEFAULT NULL,
  `DLBDLBZ` float DEFAULT NULL,
  `DLBDFSBZ` float DEFAULT NULL,
  `DLSDE` float DEFAULT NULL,
  `DLSDJ` float DEFAULT NULL,
  `DLSDL` float DEFAULT NULL,
  `DLSDFS` float DEFAULT NULL,
  `DLSDEBZ` float DEFAULT NULL,
  `DLSDLBZ` float DEFAULT NULL,
  `DLSDFSBZ` float DEFAULT NULL,
  `ZS` float DEFAULT NULL,
  `JK` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `JS` float DEFAULT NULL,
  `ZF` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `UPE` float DEFAULT NULL,
  `UPL` float DEFAULT NULL,
  `UPED` float DEFAULT NULL,
  `UPTD` float DEFAULT NULL,
  `UPEPJ` float DEFAULT NULL,
  `UPLPJ` float DEFAULT NULL,
  `UPTPJ` float DEFAULT NULL,
  `DOWNE` float DEFAULT NULL,
  `DOWNL` float DEFAULT NULL,
  `DOWNED` float DEFAULT NULL,
  `DOWNTD` float DEFAULT NULL,
  `DOWNEPJ` float DEFAULT NULL,
  `DOWNLPJ` float DEFAULT NULL,
  `DOWNTPJ` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `MCJL` float DEFAULT NULL,
  `MCJE` float DEFAULT NULL,
  `MBS` float DEFAULT NULL,
  `MSS` float DEFAULT NULL,
  `MUPS` float DEFAULT NULL,
  `MDOWNS` float DEFAULT NULL,
  `NB` float DEFAULT NULL,
  `HSL` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8 MAX_ROWS=100000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gl`
--

DROP TABLE IF EXISTS `gl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gl` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `P00` float DEFAULT NULL,
  `P01` float DEFAULT NULL,
  `P02` float DEFAULT NULL,
  `P03` float DEFAULT NULL,
  `P04` float DEFAULT NULL,
  `P05` float DEFAULT NULL,
  `P06` float DEFAULT NULL,
  `P07` float DEFAULT NULL,
  `P08` float DEFAULT NULL,
  `P09` float DEFAULT NULL,
  `P010` float DEFAULT NULL,
  `P10` float DEFAULT NULL,
  `P20` float DEFAULT NULL,
  `P30` float DEFAULT NULL,
  `P40` float DEFAULT NULL,
  `P50` float DEFAULT NULL,
  `P60` float DEFAULT NULL,
  `P70` float DEFAULT NULL,
  `P80` float DEFAULT NULL,
  `P90` float DEFAULT NULL,
  `P100` float DEFAULT NULL,
  `MB` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gl_backup`
--

DROP TABLE IF EXISTS `gl_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gl_backup` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `P00` float DEFAULT NULL,
  `P01` float DEFAULT NULL,
  `P02` float DEFAULT NULL,
  `P03` float DEFAULT NULL,
  `P04` float DEFAULT NULL,
  `P05` float DEFAULT NULL,
  `P06` float DEFAULT NULL,
  `P07` float DEFAULT NULL,
  `P08` float DEFAULT NULL,
  `P09` float DEFAULT NULL,
  `P010` float DEFAULT NULL,
  `P10` float DEFAULT NULL,
  `P20` float DEFAULT NULL,
  `P30` float DEFAULT NULL,
  `P40` float DEFAULT NULL,
  `P50` float DEFAULT NULL,
  `P60` float DEFAULT NULL,
  `P70` float DEFAULT NULL,
  `P80` float DEFAULT NULL,
  `P90` float DEFAULT NULL,
  `P100` float DEFAULT NULL,
  `MB` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gl_eval`
--

DROP TABLE IF EXISTS `gl_eval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gl_eval` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `MB` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gl_eval_backup`
--

DROP TABLE IF EXISTS `gl_eval_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gl_eval_backup` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `MB` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gl_mem`
--

DROP TABLE IF EXISTS `gl_mem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gl_mem` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `P00` float DEFAULT NULL,
  `P01` float DEFAULT NULL,
  `P02` float DEFAULT NULL,
  `P03` float DEFAULT NULL,
  `P04` float DEFAULT NULL,
  `P05` float DEFAULT NULL,
  `P06` float DEFAULT NULL,
  `P07` float DEFAULT NULL,
  `P08` float DEFAULT NULL,
  `P09` float DEFAULT NULL,
  `P010` float DEFAULT NULL,
  `P10` float DEFAULT NULL,
  `P20` float DEFAULT NULL,
  `P30` float DEFAULT NULL,
  `P40` float DEFAULT NULL,
  `P50` float DEFAULT NULL,
  `P60` float DEFAULT NULL,
  `P70` float DEFAULT NULL,
  `P80` float DEFAULT NULL,
  `P90` float DEFAULT NULL,
  `P100` float DEFAULT NULL,
  `MB` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `NZFZ` float DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8 MAX_ROWS=100000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hsag`
--

DROP TABLE IF EXISTS `hsag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hsag` (
  `DM` char(10) NOT NULL,
  `MC` char(128) NOT NULL,
  `JYRQ` date NOT NULL,
  `ZF` float DEFAULT NULL,
  `XJ` float DEFAULT NULL,
  `JD` float DEFAULT NULL,
  `BJ` float DEFAULT NULL,
  `SJ` float DEFAULT NULL,
  `ZL` float DEFAULT NULL,
  `XL` float DEFAULT NULL,
  `ZS` float DEFAULT NULL,
  `HS` float DEFAULT NULL,
  `JK` float DEFAULT NULL,
  `ZG` float DEFAULT NULL,
  `ZD` float DEFAULT NULL,
  `ZTS` float DEFAULT NULL,
  `SYD` float DEFAULT NULL,
  `ZJE` float DEFAULT NULL,
  `LB` float DEFAULT NULL,
  `XFHY` char(64) DEFAULT NULL,
  `DQ` char(32) DEFAULT NULL,
  `ZFL` float DEFAULT NULL,
  `JJ` float DEFAULT NULL,
  `NP` float DEFAULT NULL,
  `WP` float DEFAULT NULL,
  `NWB` float DEFAULT NULL,
  `MRL` float DEFAULT NULL,
  `MCL` float DEFAULT NULL,
  `WPPL` float DEFAULT NULL,
  `LTGB` float DEFAULT NULL,
  `LTSJ` float DEFAULT NULL,
  `ABGZSJ` float DEFAULT NULL,
  `QYD` float DEFAULT NULL,
  `HYD` float DEFAULT NULL,
  `MBJL` float DEFAULT NULL,
  `MBHS` float DEFAULT NULL,
  `CWGX` varchar(50) DEFAULT NULL,
  `SSRQ` varchar(50) DEFAULT NULL,
  `ZGB` float DEFAULT NULL,
  `BG` float DEFAULT NULL,
  `HG` float DEFAULT NULL,
  `ZZC` float DEFAULT NULL,
  `JZC` float DEFAULT NULL,
  `XSGQ` float DEFAULT NULL,
  `ZCHZL` float DEFAULT NULL,
  `LDZC` float DEFAULT NULL,
  `GDZC` float DEFAULT NULL,
  `WXZC` float DEFAULT NULL,
  `LDHZ` float DEFAULT NULL,
  `GJJ` float DEFAULT NULL,
  `CH` float DEFAULT NULL,
  `YSZK` float DEFAULT NULL,
  `YYSR` float DEFAULT NULL,
  `YYCB` float DEFAULT NULL,
  `YYLR` float DEFAULT NULL,
  `TZSY` float DEFAULT NULL,
  `LRZE` float DEFAULT NULL,
  `SHLR` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `WFLR` float DEFAULT NULL,
  `JYXJL` float DEFAULT NULL,
  `ZXJL` float DEFAULT NULL,
  `GDRS` float DEFAULT NULL,
  `RJCG` float DEFAULT NULL,
  `RJSJ` float DEFAULT NULL,
  `LRTB` float DEFAULT NULL,
  `SRTB` float DEFAULT NULL,
  `SZL` float DEFAULT NULL,
  `SXL` float DEFAULT NULL,
  `SXLT` float DEFAULT NULL,
  `MGSY` float DEFAULT NULL,
  `MGJZ` float DEFAULT NULL,
  `TZHJZ` float DEFAULT NULL,
  `MGGJ` float DEFAULT NULL,
  `MGWFP` float DEFAULT NULL,
  `QYB` float DEFAULT NULL,
  `ZYL` float DEFAULT NULL,
  `ZYLJD` char(10) DEFAULT NULL,
  `SSMLL` float DEFAULT NULL,
  `YYLRL` float DEFAULT NULL,
  `JLRL` float DEFAULT NULL,
  `JYDM` char(10) DEFAULT NULL,
  `LASTDATE` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hy`
--

DROP TABLE IF EXISTS `hy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hy` (
  `DM` varchar(10) NOT NULL,
  `MC` varchar(32) NOT NULL,
  `HY` varchar(32) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hy_fx`
--

DROP TABLE IF EXISTS `hy_fx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hy_fx` (
  `HY` varchar(64) NOT NULL,
  `JYRQ` date NOT NULL,
  `PJJBZ` float DEFAULT NULL,
  `PJLBZ` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `NB` float DEFAULT NULL,
  `HSL` float DEFAULT NULL,
  `JLR` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lsday`
--

DROP TABLE IF EXISTS `lsday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lsday` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `M2` float DEFAULT NULL,
  `M3` float DEFAULT NULL,
  `M4` float DEFAULT NULL,
  `M5` float DEFAULT NULL,
  `M6` float DEFAULT NULL,
  `M7` float DEFAULT NULL,
  `M8` float DEFAULT NULL,
  `M9` float DEFAULT NULL,
  `M10` float DEFAULT NULL,
  `M11` float DEFAULT NULL,
  `M12` float DEFAULT NULL,
  `M13` float DEFAULT NULL,
  `M14` float DEFAULT NULL,
  `M15` float DEFAULT NULL,
  `M16` float DEFAULT NULL,
  `M17` float DEFAULT NULL,
  `M18` float DEFAULT NULL,
  `M19` float DEFAULT NULL,
  `M20` float DEFAULT NULL,
  `M21` float DEFAULT NULL,
  `M22` float DEFAULT NULL,
  `M23` float DEFAULT NULL,
  `M24` float DEFAULT NULL,
  `M25` float DEFAULT NULL,
  `M26` float DEFAULT NULL,
  `M27` float DEFAULT NULL,
  `M28` float DEFAULT NULL,
  `M29` float DEFAULT NULL,
  `M30` float DEFAULT NULL,
  `M31` float DEFAULT NULL,
  `M32` float DEFAULT NULL,
  `M33` float DEFAULT NULL,
  `M34` float DEFAULT NULL,
  `M35` float DEFAULT NULL,
  `M36` float DEFAULT NULL,
  `M37` float DEFAULT NULL,
  `M38` float DEFAULT NULL,
  `M39` float DEFAULT NULL,
  `M40` float DEFAULT NULL,
  `M41` float DEFAULT NULL,
  `M42` float DEFAULT NULL,
  `M43` float DEFAULT NULL,
  `M44` float DEFAULT NULL,
  `M45` float DEFAULT NULL,
  `M46` float DEFAULT NULL,
  `M47` float DEFAULT NULL,
  `M48` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `ZFZA` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lsday_mem`
--

DROP TABLE IF EXISTS `lsday_mem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lsday_mem` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `M2` float DEFAULT NULL,
  `M3` float DEFAULT NULL,
  `M4` float DEFAULT NULL,
  `M5` float DEFAULT NULL,
  `M6` float DEFAULT NULL,
  `M7` float DEFAULT NULL,
  `M8` float DEFAULT NULL,
  `M9` float DEFAULT NULL,
  `M10` float DEFAULT NULL,
  `M11` float DEFAULT NULL,
  `M12` float DEFAULT NULL,
  `M13` float DEFAULT NULL,
  `M14` float DEFAULT NULL,
  `M15` float DEFAULT NULL,
  `M16` float DEFAULT NULL,
  `M17` float DEFAULT NULL,
  `M18` float DEFAULT NULL,
  `M19` float DEFAULT NULL,
  `M20` float DEFAULT NULL,
  `M21` float DEFAULT NULL,
  `M22` float DEFAULT NULL,
  `M23` float DEFAULT NULL,
  `M24` float DEFAULT NULL,
  `M25` float DEFAULT NULL,
  `M26` float DEFAULT NULL,
  `M27` float DEFAULT NULL,
  `M28` float DEFAULT NULL,
  `M29` float DEFAULT NULL,
  `M30` float DEFAULT NULL,
  `M31` float DEFAULT NULL,
  `M32` float DEFAULT NULL,
  `M33` float DEFAULT NULL,
  `M34` float DEFAULT NULL,
  `M35` float DEFAULT NULL,
  `M36` float DEFAULT NULL,
  `M37` float DEFAULT NULL,
  `M38` float DEFAULT NULL,
  `M39` float DEFAULT NULL,
  `M40` float DEFAULT NULL,
  `M41` float DEFAULT NULL,
  `M42` float DEFAULT NULL,
  `M43` float DEFAULT NULL,
  `M44` float DEFAULT NULL,
  `M45` float DEFAULT NULL,
  `M46` float DEFAULT NULL,
  `M47` float DEFAULT NULL,
  `M48` float DEFAULT NULL,
  `ZFZ` float DEFAULT NULL,
  `ZFZA` float DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8 MAX_ROWS=100000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lsgl`
--

DROP TABLE IF EXISTS `lsgl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lsgl` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `P00` float DEFAULT NULL,
  `P01` float DEFAULT NULL,
  `P02` float DEFAULT NULL,
  `P03` float DEFAULT NULL,
  `P04` float DEFAULT NULL,
  `P05` float DEFAULT NULL,
  `P06` float DEFAULT NULL,
  `P07` float DEFAULT NULL,
  `P08` float DEFAULT NULL,
  `P09` float DEFAULT NULL,
  `P010` float DEFAULT NULL,
  `P10` float DEFAULT NULL,
  `P20` float DEFAULT NULL,
  `P30` float DEFAULT NULL,
  `P40` float DEFAULT NULL,
  `P50` float DEFAULT NULL,
  `P60` float DEFAULT NULL,
  `P70` float DEFAULT NULL,
  `P80` float DEFAULT NULL,
  `P90` float DEFAULT NULL,
  `P100` float DEFAULT NULL,
  `MB` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lsgl_mem`
--

DROP TABLE IF EXISTS `lsgl_mem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lsgl_mem` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `P00` float DEFAULT NULL,
  `P01` float DEFAULT NULL,
  `P02` float DEFAULT NULL,
  `P03` float DEFAULT NULL,
  `P04` float DEFAULT NULL,
  `P05` float DEFAULT NULL,
  `P06` float DEFAULT NULL,
  `P07` float DEFAULT NULL,
  `P08` float DEFAULT NULL,
  `P09` float DEFAULT NULL,
  `P010` float DEFAULT NULL,
  `P10` float DEFAULT NULL,
  `P20` float DEFAULT NULL,
  `P30` float DEFAULT NULL,
  `P40` float DEFAULT NULL,
  `P50` float DEFAULT NULL,
  `P60` float DEFAULT NULL,
  `P70` float DEFAULT NULL,
  `P80` float DEFAULT NULL,
  `P90` float DEFAULT NULL,
  `P100` float DEFAULT NULL,
  `MB` float DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8 MAX_ROWS=100000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nextjyrq`
--

DROP TABLE IF EXISTS `nextjyrq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nextjyrq` (
  `JYRQ` date NOT NULL,
  `NEXTJYRQ` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sdqs`
--

DROP TABLE IF EXISTS `sdqs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sdqs` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `MNUM` int(11) NOT NULL,
  `MBL` float DEFAULT NULL,
  `MBS` float DEFAULT NULL,
  `MSL` float DEFAULT NULL,
  `MSS` float DEFAULT NULL,
  `MH` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `BL` float DEFAULT NULL,
  `SL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `BE` float DEFAULT NULL,
  `SE` float DEFAULT NULL,
  `BH` float DEFAULT NULL,
  `PMBL` float DEFAULT NULL,
  `PMBS` float DEFAULT NULL,
  `PMSL` float DEFAULT NULL,
  `PMSS` float DEFAULT NULL,
  `PMH` float DEFAULT NULL,
  `PCJL` float DEFAULT NULL,
  `PBL` float DEFAULT NULL,
  `PSL` float DEFAULT NULL,
  `PCJE` float DEFAULT NULL,
  `PBE` float DEFAULT NULL,
  `PSE` float DEFAULT NULL,
  `PBH` float DEFAULT NULL,
  `SP` float DEFAULT NULL,
  KEY `DMJYRQMNUM` (`DM`,`JYRQ`,`MNUM`) USING HASH,
  KEY `DM` (`DM`),
  KEY `JYRQ` (`JYRQ`),
  KEY `MNUM` (`MNUM`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sdqs_mem`
--

DROP TABLE IF EXISTS `sdqs_mem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sdqs_mem` (
  `DM` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `MNUM` int(11) NOT NULL,
  `MBL` float DEFAULT NULL,
  `MBS` float DEFAULT NULL,
  `MSL` float DEFAULT NULL,
  `MSS` float DEFAULT NULL,
  `MH` float DEFAULT NULL,
  `CJL` float DEFAULT NULL,
  `BL` float DEFAULT NULL,
  `SL` float DEFAULT NULL,
  `CJE` float DEFAULT NULL,
  `BE` float DEFAULT NULL,
  `SE` float DEFAULT NULL,
  `BH` float DEFAULT NULL,
  `PMBL` float DEFAULT NULL,
  `PMBS` float DEFAULT NULL,
  `PMSL` float DEFAULT NULL,
  `PMSS` float DEFAULT NULL,
  `PMH` float DEFAULT NULL,
  `PCJL` float DEFAULT NULL,
  `PBL` float DEFAULT NULL,
  `PSL` float DEFAULT NULL,
  `PCJE` float DEFAULT NULL,
  `PBE` float DEFAULT NULL,
  `PSE` float DEFAULT NULL,
  `PBH` float DEFAULT NULL,
  `SP` float DEFAULT NULL,
  KEY `DMJYRQMNUM` (`DM`,`JYRQ`,`MNUM`) USING HASH,
  KEY `DM` (`DM`),
  KEY `JYRQ` (`JYRQ`),
  KEY `MNUM` (`MNUM`)
) ENGINE=MEMORY DEFAULT CHARSET=utf8 MAX_ROWS=100000000;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `week_fx_jg`
--

DROP TABLE IF EXISTS `week_fx_jg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `week_fx_jg` (
  `DM` varchar(12) NOT NULL,
  `MB` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zt_fx`
--

DROP TABLE IF EXISTS `zt_fx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zt_fx` (
  `HY` varchar(12) NOT NULL,
  `JYRQ` date NOT NULL,
  `KNN` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-18 13:52:33
