#!/usr/bin/env bash

HCI_DEV="${1}"

# OGF and OCF will be automatically transformed 
# to little-endian by hcitool.Other fields use 
# little-endian directly. And parameter length will 
# automatically generated bt hcitool
# 连接成功后，由于 read by group req 失败，
# 将导致断开连接，断开来接后将不再 adv。

DEV_NAME_STR="ETKmv2-884AFejoker!"
#DEV_NAME_STR="ETKmv2-884AEA230DFF"

CMD_1_OGF="0x08"
CMD_1_OCF="0x0006"
CMD_1_PARAM_LEN=""
ADV_INTERVAL_MIN="0x00 0x08"
ADV_INTERVAL_MAX="0x00 0x80"
ADV_TYPE="0x00"
OWN_ADDR_TYPE="0x00"
PEER_ADDR_TYPE="0X00"
PEER_ADDR="0x00 0x00 0x00 0x00 0x00 0x00"
ADV_CHANNEL_MAP="0X07"
ADV_FILTER_POLICY="0X00"
HCI_CMD_1="${CMD_1_OGF} ${CMD_1_OCF} ${CMD_1_PARAM_LEN} \
           ${ADV_INTERVAL_MIN} ${ADV_INTERVAL_MAX} ${ADV_TYPE} \
           ${OWN_ADDR_TYPE} ${PEER_ADDR_TYPE} ${PEER_ADDR} \
           ${ADV_CHANNEL_MAP} ${ADV_FILTER_POLICY}"

# To figure out the structure of the ADV_DATA, see packet 1509 
# in Fejoker/assets/btsnoop_hci-normal-start-to-end.log
CMD_2_OGF="0x08"
CMD_2_OCF="0x0008"
CMD_2_PARAM_LEN=""
ADV_DATA_LEN="0x07"
ADV_DATA="0x02 \
          0x01 \
          0x06 \
          0x03 \
          0x02 \
          0xf0 0xff \
          0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
          0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
HCI_CMD_2="${CMD_2_OGF} ${CMD_2_OCF} ${CMD_2_PARAM_LEN} \
           ${ADV_DATA_LEN} ${ADV_DATA}"

# To figure out the structure of the SCAN_RSP_DATA, see packet 1510 
# in Fejoker/assets/btsnoop_hci-normal-start-to-end.log
CMD_3_OGF="0x08"
CMD_3_OCF="0x0009"
CMD_3_PARAM_LEN=""
SCAN_RSP_DATA_LEN="0x1E"
# DEV_NAME="0x45 0x54 0x4b 0x6d 0x76 0x32 \
#           0x2d \
#           0x38 0x38 0x34 0x41 \
#           0x45 0x41 0x32 0x33 0x30 0x44 0x30 0x39" # EA230D09
DEV_NAME="0x45 0x54 0x4b 0x6d 0x76 0x32 \
          0x2d \
          0x38 0x38 0x34 0x41 \
          0x46 0x65 0x6a 0x6f 0x6b 0x65 0x72 0x21" # Fejoker!
# DEV_NAME="0x45 0x54 0x4b 0x6d 0x76 0x32 \
#           0x2d \
#           0x38 0x38 0x34 0x41 \
#           0x45 0x41 0x32 0x33 0x30 0x44 0x46 0x21" # EA230DF!
SCAN_RSP_DATA="0x14 \
               0x09 \
               ${DEV_NAME} \
               0x05 \
               0x12 \
               0x50 0x00 \
               0xa0 0x00 \
               0x02 0x0a 0x00 \
               0x00"
HCI_CMD_3="${CMD_3_OGF} ${CMD_3_OCF} ${CMD_3_PARAM_LEN} \
           ${SCAN_RSP_DATA_LEN} ${SCAN_RSP_DATA}"

#hciconfig ${HCI_DEV} name ${DEV_NAME_STR}
# hciconfig ${HCI_DEV} down
# hciconfig ${HCI_DEV} up


hcitool -i ${HCI_DEV} cmd ${HCI_CMD_1}
hcitool -i ${HCI_DEV} cmd ${HCI_CMD_2}
hcitool -i ${HCI_DEV} cmd ${HCI_CMD_3}
hciconfig ${HCI_DEV} leadv
