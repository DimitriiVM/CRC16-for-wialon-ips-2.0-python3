def crc16(data, offset, length):
    if data is None or offset < 0 or offset > len(data) - 1 and offset+length > len(data):
        return 0
    crc = 0x0000
    for i in (range(0, length)):
        crc ^= data[i]
        for j in range(0, 8):
            if (crc & 0x0001) > 0:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = crc >> 1
    return crc

#data: массив данных, для которых вы хотите вычислить CRC.
#offset: с какого смещения вы хотите начать расчет CRC
#length: для какого смещения вы хотите вычислить CRC
