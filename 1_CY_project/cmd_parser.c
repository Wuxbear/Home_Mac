#include "include/cmd.h"


void cmd_paser(struct ooxx *p)
{
    switch (p->cmd) {
        case CMD_POWER_OFF:
            //function pointer
            break;
        case CMD_POWER_ON_TIME:
            break;
        case CMD_POWER_ON_ALARM:
            break;
        case CMD_POWER_OFF_TIME:
            break;
        case CMD_MCU_RESET:
            break;
        case CMD_MCU_SET_DATA_ADDR:
            break;
        case CMD_MCU_SET_EXT_MENU:
            break;
        case CMD_MCU_SPI_FLASH_ERASE:
            break;
        case CMD_MCU_SPI_FLASH_WRITE:
            break;
        case CMD_DATA_CHECK:
            break;
        case CMD_OLED_CLEAN:
            break;
        case CMD_OLED_TEXT_OUT:
            break;
        case CMD_OLED_IMAGE_OUT:
            break;
        case CMD_OLED_RESET:
            break;
        case CMD_RTC_SETUP:
            break;
        case CMD_GPIO_DIRECTION_SETUP:
            break;
        case CMD_GPIO_VALUE_SETUP:
            break;
        case CMD_MCU_XPORT:
            break;
        case CMD_I2C_MASTER_SEND:
            break;
        case CMD_MCU_STATUS_CHANGE:
            break;
        case CMD_MCU_EXT_MENU:
            break;
        case CMD_BOOT_ARGUMENT:
            break;
        case CMD_MCU_SELF_TEST:
            break;
        case CMD_OLED_SELF_TEST:
            break;
        default:
            //!! fail
    }
}

