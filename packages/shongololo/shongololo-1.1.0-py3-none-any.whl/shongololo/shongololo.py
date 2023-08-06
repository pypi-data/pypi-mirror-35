# shongololo.py
""" Collect data from CO2 meters on Pi3 USB ports via serial to FTDI cables
Configuration is down using simple-settings.  Run with a local settings file run_settings.py otherwise defaults will be used:
python shongololo.py --settings=run_settings
"""
import time
import sys
import logging
import shongololo.sys_admin as SA
import shongololo.start_up as SU
from simple_settings import settings

# Configure setup according to settings file if supplied otherwise adopt local defaults
try:
    DATA_DIR = settings.DATA_DIR
    LOG_FILE = settings.LOG_FILE
    DATA_FILE = settings.DATA_FILE
    PERIOD = settings.PERIOD
    IMET_HEADINGS = settings.IMET_HEADINGS
    K30_HEADINGS = settings.K30_HEADINGS

except RuntimeError as e:
    print(e)
    print('No settings file found, using defaults')
    DATA_DIR = './'
    LOG_FILE = 'shongololo_log.log'
    DATA_FILE = 'data.csv'
    PERIOD = 0.5
    IMET_HEADINGS = ', IMET_ID, Pressure, Temperature, Humidity, Date, Time, Latitude x 1000000, Longitude x 1000000, Altitude x 1000, Sat Count'
    K30_HEADINGS = ',K30_ID, CO2 ppm'

if __name__ == "__main__":

    # Start up services
    SU.start_logging(LOG_FILE, None, 0)
    sho_logger = logging.getLogger("shongololo_log_file")
    SA.if_mk_dir(DATA_DIR)
    i_socks, k_socks, device_dict = SU.start_up()
    if SU.test_sensors(i_socks, k_socks) == 1:
        sho_logger.info("No sensors present, quitting")
        SA.close_sensors(i_socks + k_socks)
        sys.exit()

    # Start data file
    status, new_data_dir = SA.mk_numbered_nd(DATA_DIR)
    if status != 0:
        sho_logger.error("Failed to create directory for data logging, data will not be saved to file, try restarting "
                         "the application")
        sys.exit()

    else:
        header = ""
        for c in range(len(device_dict["k30s"])):
            header = header + str(K30_HEADINGS)
        for i in range(len(device_dict["imets"])):
            header = header + str(IMET_HEADINGS)
        fd = SA.ini_datafile(str(new_data_dir) + DATA_FILE, header)

        # PRIMARY LOOP
        while 1:
            pack = []
            data_line = ""
            try:
                latest_imet_data, latest_k30_data = SA.read_data(i_socks, k_socks)

                # Pack data
                for count, k in zip(range(len(device_dict["k30s"])), device_dict["k30s"]):
                    pack.append(k[1] + "," + latest_k30_data[count])

                for count, i in zip(range(len(device_dict["imets"])), device_dict["imets"]):
                    pack.append(i[1] + "," + latest_imet_data[count])

                for x in pack:
                    data_line = data_line + "," + x

                fd.write("\n" + data_line)
                sho_logger.info(data_line)

                time.sleep(PERIOD)

            except KeyboardInterrupt as e:
                SA.close_sensors(i_socks + k_socks)
                SA.stop_file(fd, "\nKeyboard Interrupt: System stopped, closing down and saving data")
                sys.exit()
