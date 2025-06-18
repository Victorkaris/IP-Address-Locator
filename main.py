import requests
import streamlit as st
import pandas as pd

st.title("🌐 IP Address Locator")

st.markdown("Enter an IPv4 address like <span style='color:green'><strong>8.8.8.8</strong></span> to get location details.", unsafe_allow_html=True)


# Get user input ip address
ip = st.text_input("Enter IP Address", value="")


if ip:
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data['status'] == 'success':
            st.subheader("📍 Location Details")
            st.write(f"Country: {data['country']}")
            st.write(f"Region: {data['regionName']}")
            st.write(f"City: {data['city']}")
            st.write(f"ZIP: {data['zip']}")
            st.write(f"ISP: {data['isp']}")
            st.write(f"Coordinates: {data['lat']}, {data['lon']}")

            # ✅ Display map
            location_df = pd.DataFrame({'lat': [data['lat']], 'lon': [data['lon']]})
            st.subheader("🗺️ Map")
            st.map(location_df, zoom=15)
        else:
            st.error(f"❌ Error: {data.get('message', 'Invalid IP')}")
    else:
        st.error("❌ Failed to retrieve data. Please try again.")
