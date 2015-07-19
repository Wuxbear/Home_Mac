
#include <stdio.h>

#include "../include/cmd.h"
#include "../include/daemon.h"

//typedef int (*fp[])(void *data);

int cmd_paser(struct cmd_meta_data *p)
{
    fp_t fp;
    switch (p->cmd_id) {
        case CMD_POWER_OFF:
            printf("CMD_POWER_OFF\n");
            break;
        case CMD_POWER_ON_TIME:
            printf("CMD_POWER_ON_TIME\n");
            break;
        case CMD_POWER_ON_ALARM:
            printf("CMD_POWER_ON_ALARM\n");
            break;
        case CMD_POWER_OFF_TIME:
            printf("CMD_POWER_OFF_TIME\n");
            break;
        case CMD_MCU_RESET:
            printf("CMD_MCU_RESET\n");
            break;
        case CMD_MCU_SET_DATA_ADDR:
            printf("CMD_MCU_SET_DATA_ADDR\n");
            break;
        case CMD_MCU_SET_EXT_MENU:
            printf("CMD_MCU_SET_EXT_MENU\n");
            break;
        case CMD_MCU_SPI_FLASH_ERASE:
            printf("CMD_MCU_SPI_FLASH_ERASE\n");
            break;
        case CMD_MCU_SPI_FLASH_WRITE:
            printf("CMD_MCU_SPI_FLASH_WRITE\n");
            break;
        case CMD_DATA_CHECK:
            printf("CMD_DATA_CHECK\n");
            break;
        case CMD_OLED_CLEAN:
            printf("CMD_OLED_CLEAN\n");
            break;
        case CMD_OLED_TEXT_OUT:
            printf("CMD_OLED_TEXT_OUT\n");
            break;
        case CMD_OLED_IMAGE_OUT:
            printf("CMD_OLED_IMAGE_OUT\n");
            break;
        case CMD_OLED_RESET:
            printf("CMD_OLED_RESET\n");
            break;
        case CMD_RTC_SETUP:
            printf("CMD_RTC_SETUP\n");
            break;
        case CMD_GPIO_DIRECTION_SETUP:
            printf("CMD_GPIO_DIRECTION_SETUP\n");
            break;
        case CMD_GPIO_VALUE_SETUP:
            printf("CMD_GPIO_VALUE_SETUP\n");
            break;
        case CMD_MCU_XPORT:
            printf("CMD_MCU_XPORT\n");
            break;
        case CMD_I2C_MASTER_SEND:
            printf("CMD_I2C_MASTER_SEND\n");
            break;
        case CMD_MCU_STATUS_CHANGE:
            printf("CMD_MCU_STATUS_CHANGE\n");
            break;
        case CMD_MCU_EXT_MENU:
            printf("CMD_MCU_EXT_MENU\n");
            break;
        case CMD_BOOT_ARGUMENT:
            printf("CMD_BOOT_ARGUMENT\n");
            break;
        case CMD_MCU_SELF_TEST:
            printf("CMD_MCU_SELF_TEST\n");
            break;
        case CMD_OLED_SELF_TEST:
            printf("CMD_OLED_SELF_TEST\n");
            break;
        default:
            //!! fail
            printf("!!\n");
            break;
    }
    //fp = dlsymbol(ooxx)
    //return (*fp)(ooxx->data);
    return 0;
}

