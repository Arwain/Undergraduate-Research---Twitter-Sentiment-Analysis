import time as tm
import extract_data_ks
import extract_data_sy
import extract_data_btc

while True:
    extract_data_ks.main()
    # Wait 6 hours
    tm.sleep(21600)
    extract_data_btc.main()
    # Wait 6 hours
    tm.sleep(21600)
    extract_data_ks.main()
     # Wait 4 hours
    tm.sleep(14400)
    extract_data_sy.main()
      # Wait 4 hours
    tm.sleep(14400)
    extract_data_btc.main()
    # Wait 4 hours
    tm.sleep(14400)
    extract_data_sy.main()
    