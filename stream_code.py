import streamlit as st
 
metro_stations = {}


def add_station(metro_dict, station, shop, category, distance, rating):
   
    if station not in metro_dict:
        metro_dict[station] = {}  
    
    metro_dict[station][shop] = {
        "category": category,
        "distance": int(distance),  
        "rating": rating
    }






add_station(metro_stations, "King Saud University", "Maliha", "Cafe", 13, 4.3)
add_station(metro_stations, "King Saud University", "Bo Burger", "Restaurant", 14, 4.7)
add_station(metro_stations, "King Saud University", "BRNX Pizza", "Restaurant", 12, 4.2)
add_station(metro_stations, "King Saud University", "The Coffee Address", "Cafe", 19, 4.3)

add_station(metro_stations, "King Salman Oasis", "Shots", "Cafe", 46, 3.9)
add_station(metro_stations, "King Salman Oasis", "Subway", "Restaurant", 7, 3.9)
add_station(metro_stations, "King Salman Oasis", "Burger Castle", "Restaurant", 8, 4.1)
add_station(metro_stations, "King Salman Oasis", "Social Cafe & Roastery", "Cafe", 41, 3.8)

add_station(metro_stations, "KACST", "Masami Sushi", "Restaurant", 5, 3.9)
add_station(metro_stations, "KACST", "Grill It", "Restaurant", 6, 3.8)
add_station(metro_stations, "KACST", "Starbucks", "Cafe", 3, 4.4)
add_station(metro_stations, "KACST", "Beanery Cafe", "Cafe", 7, 4.7)

add_station(metro_stations, "At Takhassousi", "Mama Nourah", "Restaurant", 4, 4.2)
add_station(metro_stations, "At Takhassousi", "Makani", "Restaurant", 5, 3.3)
add_station(metro_stations, "At Takhassousi", "House of Matcha", "Cafe", 3, 4.4)
add_station(metro_stations, "At Takhassousi", "Sultan Coffee", "Cafe", 5, 3.9)

add_station(metro_stations, "Alwurud", "La Pizza", "Restaurant", 11, 4.0)
add_station(metro_stations, "Alwurud", "Ramli Cafe", "Cafe", 14, 4.5)
add_station(metro_stations, "Alwurud", "Albahsaly Palace Restaurant", "Restaurant", 10, 3.5)
add_station(metro_stations, "Alwurud", "Camfy", "Cafe", 12, 4.6)

add_station(metro_stations, "King Abdulaziz Road", "Half Million", "Cafe", 6, 4.1)
add_station(metro_stations, "King Abdulaziz Road", "Chick N Bun", "Restaurant", 7, 3.7)
add_station(metro_stations, "King Abdulaziz Road", "Cafe NAI", "Cafe", 11, 3.9)
add_station(metro_stations, "King Abdulaziz Road", "Naughty Bird", "Restaurant", 7, 3.0)

add_station(metro_stations, "King Fahad Stadium", "RED Food Street", "Restaurant", 26, 4.4)
add_station(metro_stations, "King Fahad Stadium", "Najed Restaurant", "Restaurant", 16, 4.2)
add_station(metro_stations, "King Fahad Stadium", "Bid Coffee", "Cafe", 12, 4.5)
add_station(metro_stations, "King Fahad Stadium", "Archi", "Cafe", 38, 3.9)

add_station(metro_stations, "City Center Ishbiliyah", "Subway", "Restaurant", 21, 4.0)
add_station(metro_stations, "City Center Ishbiliyah", "Casapasta", "Restaurant", 42, 4.3)
add_station(metro_stations, "City Center Ishbiliyah", "Costa Coffee", "Cafe", 39, 4.1)
add_station(metro_stations, "City Center Ishbiliyah", "Dunkin", "Cafe", 10, 4.1)

add_station(metro_stations, "Al Khaleej Metro Station", "Diet Coach", "Restaurant", 5, 4.7)
add_station(metro_stations, "Al Khaleej Metro Station", "Herfy", "Restaurant", 7, 3.8)
add_station(metro_stations, "Al Khaleej Metro Station", "Midnight Coffee", "Cafe", 13, 3.7)
add_station(metro_stations, "Al Khaleej Metro Station", "The Coffee Address", "Cafe", 13, 4.1)

add_station(metro_stations, "Khalid Bin Akwakeed Road", "TGI Friday's", "Restaurant", 3, 4.1)
add_station(metro_stations, "Khalid Bin Akwakeed Road", "Fed n Full", "Restaurant", 4, 4.2)
add_station(metro_stations, "Khalid Bin Akwakeed Road", "Mind Break", "Cafe", 7, 4.4)
add_station(metro_stations, "Khalid Bin Akwakeed Road", "Starbucks", "Cafe", 5, 4.1)

add_station(metro_stations, "Riyadh Exhibition Center", "Al Diriyah Restaurant", "Restaurant", 4, 4.6)
add_station(metro_stations, "Riyadh Exhibition Center", "Piatto Restaurant", "Restaurant", 9, 4.2)
add_station(metro_stations, "Riyadh Exhibition Center", "TUXEDO Coffee", "Cafe", 9, 4.3)
add_station(metro_stations, "Riyadh Exhibition Center", "COVO Artisan Coffee", "Cafe", 19, 4.7)

add_station(metro_stations, "AlNuzha Metro", "Najd Village", "Restaurant", 18, 4.0)
add_station(metro_stations, "AlNuzha Metro", "Yerivian Restaurant", "Restaurant", 913, 4.2)
add_station(metro_stations, "AlNuzha Metro", "Knoll Coffee Roasters", "Cafe", 24, 4.5)
add_station(metro_stations, "AlNuzha Metro", "Locale Coffee", "Cafe", 27, 3.8)

add_station(metro_stations, "Ministry of Education", "Al Tazaj", "Restaurant", 19, 4.9)
add_station(metro_stations, "Ministry of Education", "Swiss Butter", "Restaurant", 18, 4.6)
add_station(metro_stations, "Ministry of Education", "FELT", "Cafe", 24, 4.4)
add_station(metro_stations, "Ministry of Education", "Bean Here", "Cafe", 10, 4.5)

add_station(metro_stations, "Al Hamra", "Bayaz", "Restaurant", 5, 3.9)
add_station(metro_stations, "Al Hamra", "Sbarro Hamra Mall", "Restaurant", 5, 3.3)
add_station(metro_stations, "Al Hamra", "Rimthan Coffee", "Cafe", 1, 4.9)
add_station(metro_stations, "Al Hamra", "Elixir Bunn Coffee", "Cafe", 6, 4.1)



def show_nearby_options(name_of_station, sort_method, category_filter):
    if name_of_station in metro_stations:
        places = list(metro_stations[name_of_station].items())

        # Apply Category Filter if not "All"
        if category_filter != "All":
            places = [item for item in places if item[1]["category"] == category_filter]

        # Apply Sorting if not "None"
        if sort_method == "By Rating":
            places.sort(key=lambda x: x[1]["rating"], reverse=True)
        elif sort_method == "By Distance":
            places.sort(key=lambda x: x[1]["distance"])

        # Show Results
        if places:
            st.subheader(f"🚇 Nearby Options at {name_of_station}:")
            for res, details in places:
                st.markdown(f"""
                **📍 {res}**
                - 📏 **Distance:** {details['distance']} min  
                - ⭐ **Rating:** {details['rating']}/5  
                - 🍽️ **Category:** {details['category']}  
                ---""")  # Separator for readability
        else:
            st.warning("⚠️ No results found for the selected filters.")
    else:
        st.error("❌ The station name is wrong. Please check again.")


def show_nearby_stations(name_of_restorcafe):
    for sta,place in metro_stations.items():
        for res,details in place.items():
            if res.lower() == name_of_restorcafe.lower():
                st.markdown(f"""
                **📍 {res}**
                - 📏 **Distance:** {details['distance']} min  
                - ⭐ **Rating:** {details['rating']}/5  
                - 🍽️ **Category:** {details['category']}  
                ---""")  # Separator for readabilit
                return sta
    return None  



sort_by_rate=lambda station: sorted(metro_stations[station].items(),key=lambda x:x[1]["rating"],reverse=True)
sort_by_distance=lambda station: sorted(metro_stations[station].items(),key=lambda x:x[1]["distance"])

def filter_by_category(station, category):
    options = metro_stations.get(station,{})

    if not options :
        return {"error": "Station not found"}

    if not any(info['category'] == category for info in options.values()):
        return {"error": "Category not found in this station"}

    filtered_items = filter(lambda item: item[1]["category"] == category, options.items())

    return {name: info for name, info in filtered_items}

     
# Streamlit UI
st.title("🚆 Riyadh Metro Nearby Places")
st.image("https://www.riyadhbus.sa/o/rcrc-theme/images/rcrc/main-slider-f0493a.svg")
# Tabs for different searches
tab1, tab2 = st.tabs(["📍 Search by Metro Station", "🔍 Search by Restaurant Name"])

with tab1:
    st.subheader("Find Nearby Restaurants & Coffee Shops by Metro Station")

    # Dropdown for selecting a metro station
    station_choice = st.selectbox("Select a Metro Station:", list(metro_stations.keys()))

    # OPTIONAL: Sorting method
    sort_method = st.selectbox("Sort by (Optional):", ["None", "By Rating", "By Distance"])

    # OPTIONAL: Category Filter
    category_choice = st.selectbox("Filter by Category (Optional):", ["All"] + ["Cafe", "Restaurant"])

    if st.button("Find Places"):
        show_nearby_options(station_choice, sort_method, category_choice)

with tab2:
    st.subheader("Find the Metro Station for a Restaurant or Coffee Shop")
    restaurant_search = st.text_input("Enter Restaurant or Coffee Shop Name")
    restaurant_search = restaurant_search.rstrip()
    if st.button("Find Metro Station"):
        station_name = show_nearby_stations(restaurant_search)
        if station_name:
            st.success(f"✅ The restaurant **'{restaurant_search}'** is located at 🚆 **{station_name}**")
        else:
            st.error(f"❌ The restaurant **'{restaurant_search}'** was not found in any station.")

