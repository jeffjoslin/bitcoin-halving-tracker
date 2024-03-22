#Bitcoin Halving Tracker

import streamlit as st
import requests
import time
from datetime import datetime, timezone, timedelta
import pytz

def get_block_count():
    response = requests.get('https://blockchain.info/q/getblockcount')
    return int(response.text)

def main():
    st.title("Bitcoin Halving Tracker")

    m1, m2, m3 = st.columns((1,1,1))
    halving_block_count = m1.metric(label = 'Halving Block Count', value = '840,000')
    current_block_count = m2.metric(label = 'Current Block Count', value = '')
    remaining_blocks = m3.metric(label = 'Remaining Blocks', value = '')

    m4 = st.columns((1,))
    estimated_halving_date_metric = m4[0].metric(label = 'Estimated Halving Date and Time', value = '')

    while True:
        block_count = get_block_count()
        countdown = 840000 - block_count

        # Get current time in PST
        pst = pytz.timezone('America/Los_Angeles')
        time_pst = datetime.now(pst).strftime('%Y-%m-%d %H:%M:%S')

        # Calculate estimated halving date and time
        estimated_halving_date = datetime.now(pst) + timedelta(minutes=countdown*10)
        estimated_halving_date = estimated_halving_date.strftime('%B %d, %Y, %I:%M %p')

        # Update the metrics
        current_block_count.metric(label = 'Current Block Count', value = f"{block_count:,}")
        remaining_blocks.metric(label = 'Remaining Blocks', value = f"{countdown:,}")
        estimated_halving_date_metric.metric(label = 'Estimated Halving Date and Time', value = estimated_halving_date)

        # Refresh every 10 minutes
        time.sleep(600)

if __name__ == "__main__":
    main()
