#ifndef __CMD_H__
#define __CMD_H__

// Support command list

#define CMD_POWER_OFF   0x00
#define CMD_POWER_ON_TIME   0x01
#define CMD_POWER_ON_ALARM  0x02
#define CMD_POWER_OFF_TIME  0x03
#define CMD_MCU_RESET   0x04

#define CMD_MCU_SET_DATA_ADDR   0x10
#define CMD_MCU_SET_EXT_MENU    0x11

#define CMD_MCU_SPI_FLASH_ERASE 0x20
#define CMD_MCU_SPI_FLASH_WRITE 0x21
#define CMD_DATA_CHECK  0x22

#define CMD_OLED_CLEAN  0x30
#define CMD_OLED_TEXT_OUT   0x31
#define CMD_OLED_IMAGE_OUT  0x32
#define CMD_OLED_RESET  0x32

#define CMD_RTC_SETUP   0x40

#define CMD_GPIO_DIRECTION_SETUP    0x50
#define CMD_GPIO_VALUE_SETUP    0x51

#define CMD_MCU_XPORT   0x60

#define CMD_I2C_MASTER_SEND 0x70

#define CMD_MCU_STATUS_CHANGE   0xC0
#define CMD_MCU_EXT_MENU    0xC1
#define CMD_BOOT_ARGUMENT   0xC2

#define CMD_MCU_SELF_TEST   0xE0
#define CMD_OLED_SELF_TEST  0xE1


#endif

